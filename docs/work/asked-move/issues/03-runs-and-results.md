# The rule of 0.11.0, run and read

Status: ready-for-agent
Blocked by: 1, 2

## What it produces

The 30 runs of the protocol, judged, and `trials/results-asked-move.md`: per case, 0.10.0 beside 0.11.0, the asked moves made and flagged, the episodes that drift, and the verdict against the decision rule.

- Runs in batches that stop at 80% of the usage window (ticket 1). The window's reading comes from a field the CLI marks internal (`rate_limit_info.unifiedWindows.five_hour`), seen in its schema and never yet in a real session: run the first trial alone (`--parallel 1 --only <one id>`), and go on only if its line shows a percentage. If it says `window not reported`, stop, and the runner falls back to a cap of runs per batch with `/usage` checked by the user in between.
- Calibration by confirmation: 7 to 15 mixed verdicts shown to the user in plain Italian, agreed or corrected.
- The answer to the plugin's map ticket "Measure the rule of 0.11.0" written in `skills` (`docs/work/map-drift-protection/issues/01-measure-0.11.0.md`), pointing to the results file.
- The plugin's `v0.11.0` shipped before this measurement. If the rule holds, it stays; if not, it is withdrawn in `skills`, as the user chose.

## Done when

- Every run has a verdict, the calibration is done, the results file reads the decision rule.
- The total spent is within the budget, and the results file states it.
