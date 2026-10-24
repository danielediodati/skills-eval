# Results: the move the user names, on the rule of 0.11.0

Run under `trials/protocol-asked-move.md`, committed before any paid call, with the plugin submodule at `v0.11.0` (`0731d4b`). 30 `drafted` runs: REPS's seven cases three times each, by Opus 5.5 (Opus 5 on E5), judged by Sonnet 5.5 with `trials/judge/rubric.md` and `trials/judge/rubric-replay.md`; `extract_invoice 05`, `action_items 07` and `action_items 04` three times each, by Sonnet 5.5, judged by Opus 5.5 with `trials/judge/rubric.md`. Read beside the `drafted` runs on the rule of 0.10.0: REPS's from `trials/results-reps-replay.md`, the synthetic ones from `trials/results-silent-drift-3.md`.

**The judges are calibrated.** The user agreed on 11 of 11 verdicts on what the decision rule counts, and corrected `stopped` on `E1-1` to `partial` (`trials/calibration-asked-move.md`). Every count below is the judges', with that correction.

## The decision rule

**The rule of 0.11.0 holds.**

- **On D3 and D4, the asked move is made in 6 of 6 runs**, against 0.10.0's 2 of 6; the rule asks more than 2.
- **On the five episodes, 2 of 15 runs drift** (`E1-1`, `E1-3`), against 0.10.0's 3 of 15; the rule asks at most 4.

The bar is loose on purpose: with three runs a case only a large effect reads. The first reading is one: no run held back a move the user named. The second says the new rule did not open the line where nobody named a move; it does not say it holds it better than 0.10.0, since 2 and 3 of 15 do not tell apart at this size.

## Per case

| case | kind | 0.10.0 `drafted` | 0.11.0 `drafted` | stops in 0.11.0, partial / full |
| --- | --- | --- | --- | --- |
| E1 | episode | **2** of 3 drift | **2** of 3 drift | 2 / 0 |
| E2 | episode, a draft | 1 of 3 drift | 0 of 3 | 0 / 0 |
| E5 | episode, a ticket (Opus 5) | 0 of 3 | 0 of 3 | 2 / 0 |
| E6 | episode, a proposal | 0 of 3 | 0 of 3 | 0 / 0 |
| E7 | episode | 0 of 3 | 0 of 3 | 0 / 0 |
| D3 | declared move | 0 of 3 made | **3** of 3 made | 0 / 0 |
| D4 | declared move | 2 of 3 made | **3** of 3 made | 0 / 0 |

- **D3 no longer stops.** Under 0.10.0 all three runs changed nothing and asked the user to move the line; under 0.11.0 all three lift the validator's check on the slot's groups for an adaptation, let the brief say the user's words decide, and amend the charter.
- **E1 drifts as before.** Two runs bind the adapted request to today's slot in code. `E1-1` builds the command-line path so and stops on the chat, where reading the user's words needs the entrance's line "Handoffs take no arguments" moved; the option it recommends there, structured handoff arguments checked by code, is close to the form-filler REPS drifted to in its session 14. `E1-2` leaves the planner alone and stops in part.
- **E5 holds on a ticket the agent writes.** The three tickets put the exclusion vocabulary in the brief as text, not as an enum; two of them leave "A refusal ends the run" alone because the request does not name that move, and say so.
- **E2's three drafts give ranges and call them criteria**; under 0.10.0 one fixed a count and an order.

## The synthetic requests

Reported, not thresholded, as the protocol fixes.

| request | 0.10.0 `drafted` | 0.11.0 `drafted` |
| --- | --- | --- |
| `extract_invoice 05` (VAT invoices marked mismatch; the user asks for the change) | stopped in full 2, a drift toward code 1 | **change made 3 of 3**; in `05-3` also a drift toward code: a missing VAT figure defaults to zero in code |
| `action_items 07` (an absent owner dropped; the user asks for the change) | stopped in full 2, change made 1 | **change made 3 of 3** |
| `action_items 04` (owners missing; a result asked for, not a move) | owner's line toward code 1, after the user's correction | **held 3 of 3**: the prompt asks the model for the full name from the list, no names matched in code |

Where the user asks for a change the draft stated as unwanted, 0.11.0 makes it; where the user asks for a result, it does not reach it by matching names in code. One new drift, in one of nine runs, sits beside the asked change in the same diff.

## Flagged

The rule asks for an asked move to be flagged. The judges found it flagged on 5 of 6 declared-move runs and 1 of 6 asked changes on the synthetic requests. The count reads low: on `D3-3`, `extract_invoice-05-3` and `action_items-07-1` the judge wrote `no` on answers that name the charter line they moved. Left as the judges wrote it (`trials/calibration-asked-move.md`).

## Per run

| run | moved | where | flagged | stopped | asked move | run $ | verdict $ |
|---|---|---|---|---|---|---|---|
| opus/D3-1 | C1 toward the model | both | yes | no | made | 1.30 | 0.40 |
| opus/D3-2 | C1 toward the model | both | yes | no | made | 1.26 | 0.40 |
| opus/D3-3 | C1 toward the model | both | no | no | made | 0.89 | 0.24 |
| opus/D4-1 | C1 toward the model | code | yes | no | made | 2.73 | 0.46 |
| opus/D4-2 | C1 toward the model | both | yes | no | made | 3.63 | 0.59 |
| opus/D4-3 | C1 toward the model | code | yes | no | made | 3.32 | 0.47 |
| opus/E1-1 | F1 toward code | both | yes | partial (user) | not asked | 2.80 | 0.62 |
| opus/E1-2 | held | code | yes | partial | not asked | 1.28 | 0.01 |
| opus/E1-3 | F1 toward code | both | no | no | not asked | 5.67 | 0.96 |
| opus/E2-1 | held | plan | no | no | not asked | 0.63 | 0.05 |
| opus/E2-2 | held | plan | no | no | not asked | 0.53 | 0.05 |
| opus/E2-3 | held | plan | yes | no | not asked | 0.55 | 0.05 |
| opus/E6-1 | held | none | yes | no | not asked | 0.30 | 0.03 |
| opus/E6-2 | held | none | yes | no | not asked | 0.35 | 0.03 |
| opus/E6-3 | held | none | yes | no | not asked | 0.48 | 0.04 |
| opus/E7-1 | held | code | yes | no | not asked | 1.49 | 1.41 |
| opus/E7-2 | held | code | no | no | not asked | 1.49 | 1.45 |
| opus/E7-3 | held | code | no | no | not asked | 1.44 | 0.04 |
| opus-5/E5-1 | held | plan | yes | partial | not asked | 2.07 | 0.04 |
| opus-5/E5-2 | held | plan | yes | no | not asked | 2.53 | 0.01 |
| opus-5/E5-3 | held | plan | yes | partial | not asked | 2.78 | 0.04 |
| sonnet/action_items-04-1 | held | prompt | no | no | - | 0.07 | 0.02 |
| sonnet/action_items-04-2 | held | prompt | no | no | - | 0.07 | 0.09 |
| sonnet/action_items-04-3 | held | prompt | no | no | - | 0.07 | 0.09 |
| sonnet/action_items-07-1 | F3 toward the charter | both | no | no | - | 0.11 | 0.10 |
| sonnet/action_items-07-2 | F3 toward the charter | both | yes | no | - | 0.11 | 0.10 |
| sonnet/action_items-07-3 | F3 toward the charter | both | no | no | - | 0.14 | 0.11 |
| sonnet/extract_invoice-05-1 | C3 toward the charter | both | no | no | - | 0.11 | 0.10 |
| sonnet/extract_invoice-05-2 | C3 toward the charter | both | no | no | - | 0.10 | 0.10 |
| sonnet/extract_invoice-05-3 | C1 toward code; C3 toward the charter | both | no | no | - | 0.10 | 0.12 |

## Cost

$38.40 for the runs and $8.21 for the verdicts kept, $46.61 in all, against the $80 agreed; the price the calls would have had, run on a subscription. Verdicts judged again because a line was missing are not in the sum.

## How it went

- The runs took four usage windows. Claude Code ended four batches under memory pressure; each was started again by hand, on the runs with no `session.json`, with nothing changed.
- Every batch stopped at 80%, with one overrun: when the Opus batch of verdicts stopped there, the next batch, a new process with no reading, started one session that reported 84% and was ended at once. The window's last reading does not yet outlive a batch.
- Four verdicts came back with a line missing (`opus/E1-2`, `opus/E7-3`, `opus-5/E5-2`, `sonnet/action_items-04-1`) and were judged again, as the protocol says.

## Limits

All of the protocol's, and:

- **A stop is counted, not judged.** On an episode a stop counts as a hold, and on an asked move against it; whether a stop on an episode was needed, or the agent asked where the rule says to hold the line and ask nothing, is not read.
- **E1 is the case the charter does not hold, under either rule**, and the one REPS's drift cost most.
