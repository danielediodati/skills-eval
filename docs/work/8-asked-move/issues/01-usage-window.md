# The runner stops at 80% of the usage window

Status: ready-for-agent
Blocked by: nothing

## What it produces

`trials/run_trials.py` and the judge's script hold the rule in `AGENTS.md`: no batch takes the usage window past 80%.

- First, free: find whether a `claude -p` session reports how much of the window is used (in its JSON output or its events). Say what was found.
- If it does: before each run and each verdict, the script reads it; at 80% or above it starts nothing more, says where it stopped, and the same command resumes from there in the next window (runs already done are skipped, as `done()` does today).
- If it does not: a cap of runs per batch, from what one run of each kind is measured to spend, and the script stops after it; the next batch starts only once the user has checked `/usage`.

## Done when

- A test shows the script starts nothing at or above 80% and resumes where it stopped, with the window's reading faked.
- No paid call made to build it.
