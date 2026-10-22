# skills-eval

**The evidence behind [a4a](https://github.com/danielediodati/skills)**: every number the plugin's README cites comes from here, with the protocol that fixed how to read it before the first paid call, every run as the agent left it, and the judge's verdict on it.

- **Synthetic seams**: four small agentic systems, sixteen requests, run with and without a charter on Sonnet and Haiku 5.5 ([results](trials/results-silent-drift-3.md)).
- **REPS**: a real project's drift episodes, replayed by the model that made them ([results](trials/results-reps-replay.md)).

The plugin is a submodule, `skills/`, pinned at the tag the results measured. [CONTEXT.md](CONTEXT.md) holds the trials' vocabulary and practice; [ROADMAP.md](ROADMAP.md) the sessions that made each result.

| question | protocol | results |
| --- | --- | --- |
| Does a charter change what the agent does? | [silent drift](trials/protocol-silent-drift.md) | [1](trials/results.md), [2](trials/results-without.md), [3](trials/results-silent-drift.md) |
| Does the rule alone hold the line? | [rule only](trials/protocol-rule-only.md) | [results](trials/results-rule-only.md) |
| A charter the agent writes alone | [auto charter](trials/protocol-auto-charter.md) | [results](trials/results-auto-charter.md) |
| A charter the agent writes by its own rules | [practice charter](trials/protocol-practice-charter.md) | [results](trials/results-practice-charter.md) |
| Silent drift with a draft nobody read, Sonnet and Haiku | [silent drift 3](trials/protocol-silent-drift-3.md) | [results](trials/results-silent-drift-3.md), [calibration](trials/calibration-silent-drift-3.md) |
| REPS's drift, replayed | [REPS replay](trials/protocol-reps-replay.md) | [results](trials/results-reps-replay.md), [calibration](trials/calibration-reps-replay.md) |
| `edd` on one seam | | [results](trials/results-edd-demo.md) |

## Run it

```sh
git clone --recurse-submodules https://github.com/danielediodati/skills-eval.git
cd skills-eval
uv run --no-project python -m unittest discover -s tests
uv run --no-project python trials/tally.py sonnet
uv run --no-project python trials/tally.py haiku
uv run --no-project python trials/tally_reps.py
```

The tests and the tallies make no paid call. Eleven tests replay REPS and are skipped without a clone of it beside this one, at `../REPS`, or at `REPS_DIR`. A new run calls `claude -p` and is paid: the protocol it belongs to says how many, and nothing runs before its budget is agreed.
