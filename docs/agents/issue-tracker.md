# Issue tracker: files in the repo

Issues for this repo are markdown files, versioned with the code. GitHub Issues is not used.

## Layout

- `ROADMAP.md` lists, in order, the plugin's milestones this repository measures for. This repository has no milestones and no versions of its own: a **milestone** here is the plugin's, `## Milestone <m> - `<version>` - <title>` with the plugin's number and version, its `**Shows**:` line naming the measurement the release waits on, then the features that make it. When the plugin's milestone ships, this repository takes the same tag, on the commit holding the results it shipped on.
- A **feature** is a result someone can watch, described by a spec, numbered inside its milestone in one sequence with the plugin's features of that milestone, each repository listing the other's: `### Feature <m>.<f> - <title>`, a `Spec:` line linking the spec, then a numbered list of its tickets, each linking its file. A feature ships no tag.
- A **ticket** is numbered inside its feature, and named by the three numbers: `12.1.1` is ticket 1 of feature 1 of milestone 12.
- `docs/work/<m>.<f>-<name>/spec.md` is the feature's spec, and `docs/work/<m>.<f>-<name>/issues/<nn>-<slug>.md` one of its tickets; the name after the number is only a label.
- The rows under *Done* are the plugin's milestones this repository measured for; rows 1 to 7 were made in `skills`, as sessions, before this repository existed.
- A ticket, feature or milestone of another repository is named with the repository first: `skills-eval` 12.1.1, `skills` 12.

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
