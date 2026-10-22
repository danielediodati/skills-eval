"""Tests of the usage window: no batch takes it past 80%.

    uv run --no-project python -m unittest discover -s tests

No session is launched: a stand-in for `claude` prints the events a real session streams.
"""

from __future__ import annotations

import json
import sys
import tempfile
import textwrap
import time
import unittest
from pathlib import Path
from unittest import mock

from test_run_trials import RUN_JUDGE, RUN_TRIALS, SEAM, load

WINDOW = Path(__file__).resolve().parents[1] / "trials" / "window.py"


def rate_limit(five_hour, resets_in=3600, status="allowed"):
    return {"type": "rate_limit_event", "rate_limit_info": {
        "status": status,
        "unifiedWindows": {"five_hour": {"utilization": five_hour, "resetsAt": int(time.time()) + resets_in}},
    }}


RESULT = {"type": "result", "subtype": "success", "is_error": False, "num_turns": 3, "duration_ms": 10,
          "total_cost_usd": 0.01, "session_id": "s", "result": "done"}


class Reading(unittest.TestCase):
    def setUp(self):
        self.window = load(WINDOW).Window()

    def test_unknown_until_a_session_reports_it(self):
        self.assertIsNone(self.window.used())
        self.assertFalse(self.window.full())

    def test_reads_the_five_hour_window(self):
        self.window.observe(rate_limit(0.42))
        self.assertEqual(self.window.used(), 0.42)
        self.assertFalse(self.window.full())

    def test_full_at_80_percent(self):
        self.window.observe(rate_limit(0.80))
        self.assertTrue(self.window.full())

    def test_a_rejected_session_means_full(self):
        self.window.observe({"type": "rate_limit_event", "rate_limit_info": {"status": "rejected"}})
        self.assertTrue(self.window.full())

    def test_a_reading_past_its_reset_is_forgotten(self):
        self.window.observe(rate_limit(0.95, resets_in=-1))
        self.assertIsNone(self.window.used())
        self.assertFalse(self.window.full())

    def test_shown_as_a_percentage(self):
        module = load(WINDOW)
        self.assertEqual(module.shown(self.window), "not reported")
        self.window.observe(rate_limit(0.456))
        self.assertEqual(module.shown(self.window), "46%")

    def test_other_events_change_nothing(self):
        self.window.observe({"type": "assistant", "message": {}})
        self.window.observe(RESULT)
        self.assertIsNone(self.window.used())


class Session(unittest.TestCase):
    """`stream` runs a stand-in that prints the events, one per line, as `claude -p` does."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.module = load(WINDOW)
        self.window = self.module.Window()

    def fake_claude(self, *events, pause=0.0):
        script = Path(self._tmp.name) / "fake_claude.py"
        script.write_text(textwrap.dedent(f"""
            import json, sys, time
            sys.stdin.read()
            for event in {json.dumps([json.dumps(e) for e in events])}:
                print(event, flush=True)
                time.sleep({pause})
        """), encoding="utf-8")
        return [sys.executable, str(script)]

    def test_returns_the_result_and_notes_the_window(self):
        outcome = self.module.stream(self.fake_claude(rate_limit(0.30), RESULT), "prompt", self.window, 60)
        self.assertEqual(outcome.result["result"], "done")
        self.assertFalse(outcome.stopped)
        self.assertEqual(self.window.used(), 0.30)

    def test_a_session_that_crosses_80_percent_is_stopped(self):
        outcome = self.module.stream(
            self.fake_claude(rate_limit(0.81), {"type": "assistant"}, RESULT, pause=2), "prompt", self.window, 60)
        self.assertTrue(outcome.stopped)
        self.assertIsNone(outcome.result)

    def test_a_session_never_starts_on_a_full_window(self):
        self.window.observe(rate_limit(0.85))
        with mock.patch("subprocess.Popen") as popen:
            outcome = self.module.stream(["claude"], "prompt", self.window, 60)
        popen.assert_not_called()
        self.assertTrue(outcome.stopped)

    def test_crossing_80_percent_stops_the_other_sessions_too(self):
        slow = self.fake_claude({"type": "assistant"}, {"type": "assistant"}, RESULT, pause=5)
        import threading
        outcomes = {}
        other = threading.Thread(target=lambda: outcomes.setdefault(
            "slow", self.module.stream(slow, "prompt", self.window, 60)))
        other.start()
        time.sleep(1)
        self.module.stream(self.fake_claude(rate_limit(0.90)), "prompt", self.window, 60)
        other.join(timeout=10)
        self.assertTrue(outcomes["slow"].stopped)

    def test_a_session_past_its_timeout_is_ended(self):
        outcome = self.module.stream(
            self.fake_claude({"type": "assistant"}, RESULT, pause=5), "prompt", self.window, 1)
        self.assertTrue(outcome.timed_out)
        self.assertIsNone(outcome.result)


class Resume(unittest.TestCase):
    """A trial or a verdict stopped by the window leaves nothing, so the same command runs it next time."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)

    def test_a_stopped_trial_leaves_no_session_and_runs_again(self):
        runner = load(RUN_TRIALS)
        runner.WORK_ROOT = Path(self._tmp.name) / "work"
        out = Path(self._tmp.name) / "runs" / "triage_ticket-04-1"
        stopped = runner.window.Outcome(result=None, returncode=None, stderr="", stopped=True, timed_out=False)
        with mock.patch.object(runner.window, "stream", return_value=stopped):
            trial_id, session = runner.run("sonnet", "without", "triage_ticket-04-1", SEAM,
                                           SEAM / "requests" / "04.md", out)
        self.assertIsNone(session)
        self.assertFalse((out / "session.json").exists())
        self.assertFalse(runner.done(out))

    def test_a_full_window_prepares_nothing(self):
        runner = load(RUN_TRIALS)
        runner.BATCH.observe(rate_limit(0.85))
        with mock.patch.object(runner, "prepare") as prepare:
            _, session = runner.run("sonnet", "without", "triage_ticket-04-1", SEAM,
                                    SEAM / "requests" / "04.md", Path(self._tmp.name) / "out")
        prepare.assert_not_called()
        self.assertIsNone(session)

    def test_a_session_with_no_result_says_so(self):
        judge = load(RUN_JUDGE)
        trial = Path(self._tmp.name) / "triage_ticket-04-1"
        trial.mkdir()
        (trial / "session.json").write_text(json.dumps({"model": "claude-sonnet-5-5"}), encoding="utf-8")
        empty = judge.window.Outcome(result=None, returncode=0, stderr="", stopped=False, timed_out=False)
        with mock.patch.object(judge, "prompt", return_value="p"), \
                mock.patch.object(judge.window, "stream", return_value=empty):
            _, status = judge.judge(trial)
        self.assertIn("no result", status)

    def test_the_runner_asks_for_the_stream(self):
        runner = load(RUN_TRIALS)
        self.assertIn("stream-json", runner.CLAUDE_ARGS)
        self.assertIn("--verbose", runner.CLAUDE_ARGS)

    def test_a_stopped_verdict_is_not_written(self):
        judge = load(RUN_JUDGE)
        trial = Path(self._tmp.name) / "triage_ticket-04-1"
        trial.mkdir()
        (trial / "session.json").write_text(json.dumps({"model": "claude-sonnet-5-5"}), encoding="utf-8")
        stopped = judge.window.Outcome(result=None, returncode=None, stderr="", stopped=True, timed_out=False)
        with mock.patch.object(judge, "prompt", return_value="p"), \
                mock.patch.object(judge.window, "stream", return_value=stopped):
            _, status = judge.judge(trial)
        self.assertIn("window", status)
        self.assertFalse((trial / "verdict.md").exists())


if __name__ == "__main__":
    unittest.main()
