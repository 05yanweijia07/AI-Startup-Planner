# Project State Management

## Authority and record boundaries

- `project-profile.json` stores stable project identity and baseline facts.
- `project-state.json` stores current status, gate results, active tasks, blockers, next actions, and stale deliverables.
- Decision, evidence, and assumption registries preserve their own history and provenance.
- Reports and deliverables are derived explanations, not competing authoritative records.

## Update workflow

1. Identify the exact fact, decision, status, or output that changed and the source of the change.
2. Check whether it is a new fact, estimate, assumption, or user decision. Keep those categories distinct.
3. Update the canonical record only when authorized and supported. Preserve IDs and prior records.
4. Check dependency links and identify affected analyses or deliverables. Update them or mark them stale.
5. Record a meaningful change in version history with a timestamp supplied by the runtime; never invent one.
6. Validate schemas and project IDs after writing. If validation cannot run, say so.
7. Summarize changed files, consequences, unresolved items, and the next action.

## Decision changes

When the user changes a confirmed decision, retain the old record with `superseded` status and add the new choice with a link to the prior decision. Reassess dependencies, gates, forecasts, and deliverables. Do not treat an old decision as immutable when the user explicitly revises it.

## Stale outputs

Mark a deliverable stale if a material input it depends on changes. A stale marker means review is needed; it does not imply the deliverable is necessarily wrong. Recompute only affected outputs where possible.

## Recovery and backups

Keep recoverable snapshots when the environment supports them. A snapshot reference must point to a real file or version. If persistence is unavailable, return a proposed patch or state update without claiming it was saved.
