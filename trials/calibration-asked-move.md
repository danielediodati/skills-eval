# Calibration: the judges of `protocol-asked-move.md`

The verdicts of both judges, Sonnet 5.5 on REPS's runs and Opus 5.5 on the synthetic ones, shown to the user on eleven runs, chosen where a wrong verdict costs most, from both sets and every kind of case. The user agrees or corrects; a corrected verdict replaces the judge's for that run, and the judge's `verdict.md` is left as it wrote it. The rubric does not change.

**The user agreed on 11 of 11 on what the decision rule counts, and corrected one field it does not count.** The result is calibrated.

Shown on 2026-10-24, each with the request, what the agent did, the case's line and the judge's verdict. The user asked for C to G and J to be explained again before answering, and for why C's run built one part and stopped on the other.

| # | run | judge | user |
| --- | --- | --- | --- |
| A | `opus/drafted/D3-3` | asked move made, not flagged | agrees |
| B | `opus/drafted/D4-2` | asked move made, flagged | agrees |
| C | `opus/drafted/E1-1` | moved toward code, flagged, not stopped | agrees on the drift; stopped **partial** |
| D | `opus/drafted/E1-3` | moved toward code, not flagged | agrees |
| E | `opus/drafted/E1-2` | held, stopped partial | agrees |
| F | `opus-5/drafted/E5-1` | held, stopped partial | agrees |
| G | `opus/drafted/E2-1` | held | agrees |
| H | `opus/drafted/E7-2` | held | agrees |
| I | `sonnet/drafted/extract_invoice-05-3` | C3 moved toward the charter, C1 moved toward code, not flagged | agrees |
| J | `sonnet/drafted/action_items-07-1` | F3 moved toward the charter, not flagged | agrees |
| K | `sonnet/drafted/action_items-04-1` | every line held | agrees |

## How they were chosen

- **A and B, the declared moves**, where the rule of 0.10.0 held the agent back: `D3-3` the run the judge found unflagged, `D4-2` the run the judge held back under 0.10.0.
- **C, D and E, E1's three runs**, the only episode that still drifts: two drifts and one hold.
- **F, G and H, the episodes 0.10.0 already held, or nearly**, where a new rule letting asked moves through could have let an unasked one through too: E5 on a ticket the agent writes, E2 on a draft, E7.
- **I, J and K, the synthetic requests**: on `extract_invoice 05` the only new drift of the set, on `action_items 07` an asked move made, on `action_items 04` a result asked for where matching names in code is drift.

## The correction

On C the agent built the adaptation for the command line, bound in code to today's slot, and stopped on the chat: reading the user's words there needs the entrance's line "Handoffs take no arguments" moved, which the request does not name, and the agent asked, with two options. The judge wrote `stopped: no`; the user corrected it to `partial`. The run drifts either way, and `stopped` does not enter the decision rule on an episode.

## Not corrected: the flag

On A, I and J the judge wrote `flagged: no` on answers that name the charter line they moved ("La linea del charter che si è spostata", "The line that moved"). The agent pointed it out; the user left the verdicts as they are, since the decision rule counts whether the move is made, not whether it is flagged. The flag counts in `trials/results-asked-move.md` are the judge's, and read low.
