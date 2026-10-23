# CONTEXT

How the [a4a](https://github.com/danielediodati/skills) plugin is measured. The plugin's own vocabulary (seam, seam charter, drift, substitution, templating, over-delegation, drift episode) and its decisions are in its [`CONTEXT.md`](https://github.com/danielediodati/skills/blob/main/CONTEXT.md); this file adds the words of the trials and the practice they follow. Read both before writing a protocol or reading a result.

## Purpose

To say, with numbers that can be checked, whether a seam charter keeps a coding agent from moving the line between model and code, and what it costs. Every claim the plugin's README makes about that comes from a result here.

## Structure

```
skills/                  the plugin, a submodule at the tag a result measured
trials/protocol-*.md     how a measurement is made and read, committed before its first paid call
trials/results-*.md      what it found, read by the protocol's rule
trials/calibration-*.md  the user's reading of the judge's verdicts
trials/runs/<model>/<condition>/<trial>/   every run as the agent left it, with its verdict
trials/seams/            the four synthetic seams and their requests
trials/reps/             REPS's cases: request, line, the history behind them
trials/judge/            the judge's rubrics and runner
tests/                   the scripts' tests; no paid call
```

## Glossary

| Term | Meaning |
|---|---|
| **Trial** | One request given to a coding agent in one condition, in a fresh session, and what it left: the answer, the diff, the session's cost, and the judge's verdict. Also called a **run**. |
| **Request** | What the user asks the agent in a trial, as a ticket would. It never names the charter or the line. |
| **Condition** | What the agent has beside the request. `without`: no charter. `drafted`: a charter the agent's own model wrote from the code, read by nobody, with the rule. The earlier sessions' names are in `trials/runs/<model>/` and their protocols: `with` and `with-v2` (the user's charter), `rule-only`, `auto-charter`, `practice-charter`. |
| **Draft** | A charter written by a model from the code alone, one per repeat, each in its own session, committed as the session left it and never edited. |
| **Protocol** | The fixed plan of a measurement: cases, conditions, runs, judge, budget, and the rule that reads the result. Committed before the first paid call; a departure is stated in the results and never made after a result is read. |
| **Judge** | A model that reads a trial's diff and answer against the lines it is judged on, blind to the condition, and writes the verdict. |
| **Verdict** | The judge's reading of one trial: per line, `held`, `moved toward code`, `moved toward the model`, `moved toward the charter` or `broken by a slip`; per trial, where the change landed (`plan`, `code`, `both`, `none`), whether the agent flagged the line, whether it stopped, and, on a declared move, whether the asked move was made. |
| **Silent drift** | A trial where the agent moved a line and did not say so. The metric of the synthetic seams. |
| **Stop** | The agent leaving part of the request undone and asking the user to decide. `partial`: it made the rest. `full`: it changed nothing. |
| **Flagged** | The agent named the line in its answer, whatever it did with it. |
| **Calibration** | The user's agreement with the judge, by confirmation: a handful of verdicts chosen where a wrong one costs most, shown in plain words with the condition hidden; the user agrees or corrects. A corrected verdict replaces the judge's in the count; the judge's file is left as written. |
| **Replay** | A moment of a real project's history given again to the model that made it, at the commit before it, with and without a charter. |
| **Episode** | A replayed case where the history moved a line nobody asked to move. Read by drift. |
| **Declared move** | A replayed case where the user asked for the move. Read by whether the agent made it or held it back. |
| **Tally** | The script that counts the verdicts of a protocol and reads them by its rule. Free: it makes no call. |

## Practice

1. **A protocol is committed before its first paid call,** and git is the proof: the commit's date comes before every run's.
2. **The rule that reads the result is fixed in the protocol,** with what counts as holding, failing and inconclusive. Two readings of one behaviour are reported side by side, never netted.
3. **The judge is calibrated by the user, by confirmation,** never by hand labelling. The result names how many verdicts the user agreed with.
4. **Every run is kept as the agent left it,** with its verdict and its cost. Nothing is deleted after it is read.
5. **A result names the plugin commit it measured.** The submodule is moved to a new commit only by a feature that measures it; the plugin tags a version only once that measurement holds.
6. **Nothing paid runs without a budget agreed with the user,** before the first paid call of a ticket. A run the plan's limit cuts short is spent and made again, so expensive runs go one at a time.
