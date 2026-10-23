# AGENTS

## Agent skills

### Issue tracker

Issues live in the repo, as markdown files under `docs/work/<feature>/issues/`, listed in `ROADMAP.md` under their feature and milestone. See `docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.

## Usage window

Trials, judges and screenings run on the user's subscription and spend the same usage window the user works in. No batch takes the window past 80%: it stops there and resumes in the next window. A run that would start above 80% does not start. The mistake behind it: in session 3 the judge's calls ran into the account's usage limit and 17 failed at once.
