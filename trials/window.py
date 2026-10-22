"""The usage window: no batch takes it past 80%.

Trials and verdicts run on the user's subscription, in the same five-hour window the user works
in. Each `claude -p` session streams its events (`--output-format stream-json --verbose`); a
`rate_limit_event` carries how much of the window is used. One `Window` per batch keeps the last
reading. At 80% every session still running is ended and none starts: what it was doing leaves
nothing behind, and the same command runs it again in the next window.
"""

from __future__ import annotations

import json
import subprocess
import threading
import time
from typing import NamedTuple

LIMIT = 0.80


class Outcome(NamedTuple):
    result: dict | None  # the session's closing `result` event, as `--output-format json` gives it
    returncode: int | None
    stderr: str
    stopped: bool  # ended, or never started, by the window
    timed_out: bool


class Window:
    def __init__(self, limit=LIMIT):
        self.limit = limit
        self._lock = threading.Lock()
        self._used = None
        self._resets_at = None
        self._sessions = set()

    def used(self):
        """The share of the five-hour window used, 0 to 1, or None when no session has reported it
        since the window last reset."""
        with self._lock:
            if self._resets_at is not None and self._resets_at <= time.time():
                self._used = self._resets_at = None
            return self._used

    def full(self):
        used = self.used()
        return used is not None and used >= self.limit

    def observe(self, event):
        if event.get("type") != "rate_limit_event":
            return
        info = event.get("rate_limit_info") or {}
        five_hour = (info.get("unifiedWindows") or {}).get("five_hour")
        with self._lock:
            if info.get("status") == "rejected":
                self._used, self._resets_at = 1.0, info.get("resetsAt")
            elif five_hour:
                self._used, self._resets_at = five_hour["utilization"], five_hour.get("resetsAt")
            elif info.get("rateLimitType") == "five_hour" and info.get("utilization") is not None:
                self._used, self._resets_at = info["utilization"], info.get("resetsAt")
        if self.full():
            self._end_all()

    def _end_all(self):
        with self._lock:
            sessions = list(self._sessions)
        for process in sessions:
            process.kill()

    def _start(self, process):
        with self._lock:
            self._sessions.add(process)

    def _end(self, process):
        with self._lock:
            self._sessions.discard(process)


def shown(window):
    used = window.used()
    return "not reported" if used is None else f"{used:.0%}"


def stream(args, prompt, window, timeout, **popen):
    """Run one session to its end, unless the window fills or the timeout passes first."""
    if window.full():
        return Outcome(None, None, "", stopped=True, timed_out=False)
    process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, encoding="utf-8", **popen)
    window._start(process)
    expired = threading.Event()

    def expire():
        expired.set()
        process.kill()

    timer = threading.Timer(timeout, expire)
    timer.start()
    stderr = []
    drain = threading.Thread(target=lambda: stderr.append(process.stderr.read()))
    drain.start()
    result = None
    try:
        try:
            process.stdin.write(prompt)
            process.stdin.close()
        except OSError:  # ended before it read its prompt
            pass
        for line in process.stdout:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            window.observe(event)
            if event.get("type") == "result":
                result = event
        process.wait()
    finally:
        timer.cancel()
        window._end(process)
        drain.join()
    stopped = window.full() and result is None
    timed_out = expired.is_set() and result is None and not stopped
    return Outcome(result, process.returncode, "".join(stderr), stopped=stopped, timed_out=timed_out)
