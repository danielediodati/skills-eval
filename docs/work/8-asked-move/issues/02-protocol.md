# The protocol for the rule of 0.11.0

Status: ready-for-agent
Blocked by: nothing

## What it produces

`trials/protocol-asked-move.md`, committed before any paid call, and the plugin submodule moved to `v0.11.0`.

- **The question:** with the rule of 0.11.0, does the agent make the move the user names and flag it, and does it still hold the line where nobody named a move? Against the same runs on the rule of 0.10.0.
- **Only `drafted` runs again.** `without` has no rule, so its runs from sessions 5 and 7 stand. The drafts stand too: the `charter` text they were written from is the same word for word (the test in `tests/test_charter_skill.py` holds it).
- **REPS:** the seven cases of `protocol-reps-replay.md`, `drafted`, 3 runs each, same agents, same judge: 21 runs.
- **Synthetic:** `extract_invoice 05` and `action_items 07`, whose drafts stated as wanted the behaviour the user asked to change, and `action_items 04`, where the request asks for a result and not for the move. `drafted`, Sonnet 5.5, 3 runs each, the judge and rubric of `protocol-silent-drift-3.md`: 9 runs.
- **The decision rule, fixed before the runs:** the rule holds if asked moves are made in at least 5 of 6 on D3 and D4, and episodes do not drift more than 0.10.0's 3 of 15. Otherwise the rule goes back to `skills` and session 9 does not run.
- **The spending budget** for the whole session, agreed with the user in the protocol's commit, with the cost of one run and one verdict from session 7's results.

## Done when

- `skills` points at `v0.11.0` and every test passes.
- The protocol is committed, budget agreed, before any paid call.
