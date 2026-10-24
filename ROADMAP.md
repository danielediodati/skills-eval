# Roadmap

The order the measurements get made in. [CONTEXT.md](CONTEXT.md) holds the vocabulary and the practice; the plugin's map ([skills](https://github.com/danielediodati/skills/blob/main/docs/work/map-drift-protection/map.md)) holds what is still to measure on the way to drift protection that holds. What the plugin does, and its own milestones, are in [skills](https://github.com/danielediodati/skills/blob/main/ROADMAP.md).

Milestones, features and tickets, and how they are written and numbered: [docs/agents/issue-tracker.md](docs/agents/issue-tracker.md). Here a feature is one measurement: its spec is its protocol, committed before any paid call, and it ends with a result that can be read. A closed milestone becomes one row under *Done*, and its tag keeps the details. A change to the plugin and its measurement are two features, one per repository: the change first, in `skills`, then the measurement here, against the change's commit. The plugin's version ships only once the measurement holds (`skills`'s `AGENTS.md`).

## Done

One row per plugin milestone this repository measured for, by the plugin's number and tag, which this repository shares. Rows 1 to 7 were made in `skills`, before the trials had a repository of their own; until milestones, each was a session, a feature and a tag at once.

| plugin milestone | tag | measured |
| --- | --- | --- |
| 1 | `v0.1.0` | A table, per request, of where each decision ended up with and without the seam charter, judged blind |
| 2 | `v0.2.0` | A real edd run on `triage_ticket`: budget agreed first, core set before extended, verdict against the target |
| 3 | `v0.3.0` | The silent drift rate with the rule alone, beside neither and both |
| 4 | `v0.4.0` | 24 charters drafted from the code by Sonnet and Haiku, read line by line against the user's |
| 5 | `v0.5.0` | Sonnet's silent drift rate, with no charter and with an unread one it wrote, with intervals |
| 6 | `v0.6.0` | Haiku's rate beside Sonnet's, each with its intervals |
| 7 | `v0.9.0` | REPS's drift replayed by the model that made it: 3 of 15 episodes drift with a charter against 10 of 15, and 4 of 6 asked moves are held back against 0 of 6 |
| 11 | `v0.11.0` | The move the user names, on the rule of 0.11.0: made in 6 of 6 runs against 0.10.0's 2 of 6, and 2 of 15 episode runs drift against 3 of 15 ([results](trials/results-asked-move.md)) |

## Milestone 12 - `1.0.0` - Drift protection that holds

**Shows**: the measurement the plugin's milestone 12 ships on: Sonnet's and Haiku's silent drift rate on the final text, each beside 0.10.0's.

### Feature 12.1 - The silent drift rate on the final text

Spec: `trials/protocol-silent-drift-4.md`, written by its first ticket.

Sonnet's and Haiku's silent drift rate with the charter on the final text the plugin's map settles, beside 0.10.0's 2 and 1 of 48 and `without`'s 32 and 33, with intervals.

1. **The protocol for `drafted` again, on the final text.** Sixteen requests, two models, 96 runs - [ticket](docs/work/12.1-drafted-again/issues/01-protocol.md)
2. **`drafted` on the final text, run and read.** Each model's rate beside 0.10.0's - [ticket](docs/work/12.1-drafted-again/issues/02-runs-and-results.md)

## Parked

Nothing yet.
