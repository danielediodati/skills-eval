# Issue tracker: files in the repo

Issues for this repo are markdown files, versioned with the code. GitHub Issues is not used.

## Layout

- `ROADMAP.md` lists the milestones in order. A **milestone** is a release, declared before it is built, and numbered in order from 1: `## Milestone <m> - `<version>` - <title>`, its `**Shows**:` line, then its features. Only a milestone ships a version and a tag.
- A **feature** is a result someone can watch, described by a spec, numbered inside its milestone: `### Feature <m>.<f> - <title>`, a `Spec:` line linking the spec, then a numbered list of its tickets, each linking its file. A feature ships no tag.
- A **ticket** is numbered inside its feature, and named by the three numbers: `1.2.1` is ticket 1 of feature 2 of milestone 1.
- `docs/work/<m>.<f>-<name>/spec.md` is the feature's spec, and `docs/work/<m>.<f>-<name>/issues/<nn>-<slug>.md` one of its tickets; the name after the number is only a label.
- The rows under *Done* before milestone 1 are the plugin's sessions, made in `skills` before this repository existed; their numbers are the plugin's.
- A ticket, feature or milestone of another repository is named with the repository first: `skills-eval` 1.2.1, `skills` 12.

## A ticket

```md
# <title>

Status: <triage label>
Blocked by: <ticket numbers in the same feature, <m>.<f>.<nn> in another, or "nothing">

## What it produces
## Done when
```

`Status` takes the labels in `docs/agents/triage-labels.md`. A ticket is unblocked when every ticket in its `Blocked by` line is closed.

## Conventions

- **Create a ticket**: write the file, and add its line to the feature in `ROADMAP.md`.
- **Read a ticket**: read the file.
- **List open tickets**: the files under `docs/work/<m>.<f>-<name>/issues/`. Every open ticket has a file; a file with no line in `ROADMAP.md` is a mistake.
- **Comment**: add to the ticket file, under a dated heading.
- **Change the label**: edit the `Status` line.
- **Close**: delete the file and remove its line from `ROADMAP.md`, in the commit that finishes the work. The feature's last ticket keeps its line, marked `**done** `<commit>``, so a finished feature does not read as one not yet cut. What outlives the ticket goes where it belongs first: a decision in `CONTEXT.md` or an ADR, a result in the file the ticket names.

## When a skill says "publish to the issue tracker"

Write a ticket file and add it to `ROADMAP.md`.

## When a skill says "fetch the relevant ticket"

Read the ticket file.
