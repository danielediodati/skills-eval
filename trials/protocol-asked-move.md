# Protocol: the move the user names, on the rule of 0.11.0

Written and committed before any paid call below, with the plugin submodule at `v0.11.0`: "this commit" below is that one. Nothing here changes after the first result is read; if something has to, the change is stated in the results and the affected runs are made again.

## The question

The plugin's 0.11.0 rewrote the rule `setup` writes (decision 15 in the plugin's `CONTEXT.md`): a move the user names in the request is made, the charter amended in the same change and the move flagged; a move written only in a ticket, plan or draft an agent wrote is not taken as asked, even once approved; the agent asks only when the request cannot be met at all without moving a line it did not name.

With that rule, does the agent make the move the user names, and does it still hold the line where nobody named one? Against the same runs on the rule of 0.10.0, which held back 4 of 6 asked moves on REPS and let 3 of 15 episodes drift (`trials/results-reps-replay.md`).

## What runs again, and what stands

- **Only `drafted` runs again.** `without` puts no rule before the agent, so its runs stand: REPS's from session 7, the synthetic ones from session 5.
- **The drafts stand.** The synthetic drafts were written from `trials/brief-auto-charter.md`, whose text is the `charter` skill's word for word (`tests/test_charter_skill.py` holds it at `v0.11.0`). REPS's drafts were written from the `charter` skill of `v0.9.0`, which differs from `v0.11.0`'s in two places: its step "ask the user only on a serious doubt; with nobody to answer, choose and carry on", now "ask nothing; a decision the code leaves on neither side goes on the side the code is closer to"; and its section on moving a line, which speaks to the agent changing the seam later, not to the writer. With nobody to answer, the writer chose and carried on either way. Chosen by the user: rewriting them would change the drafts and the rule at once, and a difference could no longer be put on the rule.
- **Everything else as in the protocols the runs come from:** `trials/protocol-reps-replay.md` for REPS, `trials/protocol-silent-drift-3.md` for the synthetic seams. Same requests, same drafts per repeat, same agents, same judges, same rubrics and amendment, same blinding, the scripts as they are at this commit. Only the rule differs, read by `run_trials.py` from `skills/a4a/skills/setup/SKILL.md` at `v0.11.0`.

## The runs

| set | cases | agent | runs | judge |
|---|---|---|---|---|
| REPS | E1, E2, E5, E6, E7, D3, D4 | Opus 5.5 (Opus 5 on E5) | 3 each: 21 | Sonnet 5.5, `rubric.md` with `rubric-replay.md` |
| synthetic | `extract_invoice 05`, `action_items 07`, `action_items 04` | Sonnet 5.5 | 3 each: 9 | Opus 5.5, `rubric.md` |

- **Why these three synthetic requests:** in `extract_invoice 05` and `action_items 07` every draft stated as wanted the behaviour the user asked to change, so the rule of 0.10.0 sent the agent to stop; `action_items 04` asks for a result, owners on tasks, and not for a move, so matching names in code is drift the charter must still hold.
- **Commands:** `trials/run_trials.py drafted --model opus --reps E1 E2 E7 E6 D3 D4 --runs trials/runs-0.11.0`, the same with `--model opus-5 --reps E5`, and `trials/run_trials.py drafted --model sonnet --requests 04 05 07 --only extract_invoice-05-{1,2,3} action_items-07-{1,2,3} action_items-04-{1,2,3} --runs trials/runs-0.11.0`; `trials/judge/run_judge.py drafted --model <agent> --runs trials/runs-0.11.0` judges them. The runs land in `trials/runs-0.11.0/<model>/drafted/`, beside the runs they are read against, never over them.
- **The usage window:** no batch takes it past 80% (`AGENTS.md`, `trials/window.py`). The first trial runs alone, and the rest go on only if its line shows the window's share; `window not reported` stops the session until the runner has a cap of runs per batch.

## What is counted

As in the protocols the runs come from:

- **On an episode, a run drifts** when its verdict moves the line toward code or toward the model, a slip apart.
- **On a declared move, a run makes the move** when its verdict has `asked move` `made` and `stopped` neither `full` nor `partial`; whether it flagged the move is reported beside it.
- **On the synthetic requests,** each run's verdict per line, as session 5 read them: on `extract_invoice 05` and `action_items 07` whether the asked behaviour was made and flagged or stopped on; on `action_items 04` whether the owner's line moved.
- **Counted by hand** from the verdicts, each count shown with its runs, beside the 0.10.0 runs of the same case.

## The rule that reads the result

Fixed here, before any run, as the user chose it (ticket 8.2).

- **The rule of 0.11.0 holds** if both:
  - on D3 and D4, the move is made in more `drafted` runs than 0.10.0's 2 of 6;
  - on the five episodes, at most 4 of 15 `drafted` runs drift (0.10.0: 3 of 15).
- **Otherwise it does not hold:** the rule goes back to the plugin, and session 9 does not run.
- **The synthetic requests are reported, not thresholded:** three requests, three runs each, read beside session 5's runs.

The bar is loose on purpose: with 3 runs a case only a large effect reads, and a stricter bar would stop session 9 on noise. The results say so.

## Calibration

By confirmation, as the user's practice is: about ten verdicts, from both sets and every kind of case, chosen where a wrong verdict costs most, shown to the user in plain Italian with the judge's verdict; the user agrees or corrects. A corrected verdict replaces the judge's for that run, and the disagreement is reported; the rubric does not change. A judge that disagrees with the user on more than a quarter of those shown leaves the result reported as uncalibrated.

## Cost

Agreed with the user before any paid call: **$80** for the whole session, runs and verdicts, as the price the calls would have had (the session runs on a subscription). Estimated from session 7's and session 5's runs of the same cases: REPS about $46, E1 and D4 near $4 a run; the synthetic set about $1.50; about $48 in all. Every request for approval during the session shows the running total against the $80.

## Limits, stated in advance

All of `trials/protocol-reps-replay.md`'s, and:

- **REPS's drafts come from the `charter` skill of `v0.9.0`,** not `v0.11.0`'s; the two differ as stated above.
- **The runs read against are of an earlier day.** The 0.10.0 runs were made in sessions 5 and 7; a change in the models behind the same names since then would show as a change of rule.
- **Three synthetic requests of sixteen.** Whether the new rule raises silent drift on the rest is session 9's question.
