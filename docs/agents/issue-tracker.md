# Issue tracker: files in the repo

Issues for this repo are markdown files, versioned with the code. GitHub Issues is not used.

## Layout

- `ROADMAP.md` lists the milestones in order. A **milestone** is a release, declared before it is built: `## Milestone `<version>` - <title>`, its `**Shows**:` line, then its features. Only a milestone ships a version and a tag.
- A **feature** is a result someone can watch, described by a spec: `### Feature `<name>` - <title>` under its milestone, a `Spec:` line linking the spec, then a numbered list of its tickets, each linking its file. A feature ships no tag.
- `docs/work/<feature>/spec.md` is the feature's spec, and `docs/work/<feature>/issues/<nn>-<slug>.md` one of its tickets. `<nn>` is the ticket's number inside the feature; elsewhere a ticket is named `<feature>.<nn>`.
- Milestones closed before features existed were called sessions, one per tag: their rows under *Done* stay as they were.

## A ticket

```md
# <title>

Status: <triage label>
Blocked by: <ticket numbers in the same feature, <feature>.<nn> in another, or "nothing">

## What it produces
## Done when
```

`Status` takes the labels in `docs/agents/triage-labels.md`. A ticket is unblocked when every ticket in its `Blocked by` line is closed.

## Conventions

- **Create a ticket**: write the file, and add its line to the feature in `ROADMAP.md`.
- **Read a ticket**: read the file.
- **List open tickets**: the files under `docs/work/<feature>/issues/`. Every open ticket has a file; a file with no line in `ROADMAP.md` is a mistake.
- **Comment**: add to the ticket file, under a dated heading.
- **Change the label**: edit the `Status` line.
- **Close**: delete the file and remove its line from `ROADMAP.md`, in the commit that finishes the work. What outlives the ticket goes where it belongs first: a decision in `CONTEXT.md` or an ADR, a result in the file the ticket names.

## When a skill says "publish to the issue tracker"

Write a ticket file and add it to `ROADMAP.md`.

## When a skill says "fetch the relevant ticket"

Read the ticket file.
