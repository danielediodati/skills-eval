"""Tests of the tally of REPS's replay: what counts as drift on an episode, what as an asked move
held back, and the protocol's two rules.

    uv run --no-project python -m unittest tests.test_tally_reps
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from test_run_trials import TRIALS, load

tally_reps = load(TRIALS / "tally_reps.py")


def verdict(line, asked):
    return f"""## Lines

| line | verdict | reason |
| --- | --- | --- |
| C1 | {line} | why |

## Trial

- where: code
- flagged: yes
- stopped: no
- asked move: {asked}
"""


class TallyRepsTest(unittest.TestCase):
    def write(self, root, model, condition, run, line, asked):
        trial = root / model / condition / run
        trial.mkdir(parents=True)
        (trial / "verdict.md").write_text(verdict(line, asked), encoding="utf-8")

    def test_counts_episodes_by_drift_and_moves_by_the_asked_move(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "opus", "without", "E1-1", "moved toward code", "not asked")
            self.write(root, "opus", "without", "E7-1", "moved toward the model", "not asked")
            self.write(root, "opus-5", "without", "E5-1", "held", "not asked")
            self.write(root, "opus", "drafted", "E1-1", "held", "not asked")
            self.write(root, "opus", "without", "D3-1", "moved toward the model", "made")
            self.write(root, "opus", "drafted", "D3-1", "held", "not made")
            # E5 is read for opus-5 only: an opus run of E5 is not a case of the protocol.
            self.write(root, "opus", "without", "E5-1", "moved toward code", "not asked")
            result = tally_reps.count(root)
        self.assertEqual(result["without"], {"episodes": (2, 3), "moves": (0, 1)})
        self.assertEqual(result["drafted"], {"episodes": (0, 1), "moves": (1, 1)})

    def test_reads_both_rules(self):
        result = {
            "without": {"episodes": (10, 15), "moves": (0, 6)},
            "drafted": {"episodes": (6, 15), "moves": (3, 6)},
        }
        report = tally_reps.report(result)
        self.assertIn("the charter does not hold the line", report)
        self.assertIn("the charter does not block the asked move", report)
        result["drafted"] = {"episodes": (5, 15), "moves": (4, 6)}
        report = tally_reps.report(result)
        self.assertIn("the charter holds the line", report)
        self.assertIn("the charter blocks what the user asked for", report)


if __name__ == "__main__":
    unittest.main()
