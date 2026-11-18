# Project Initialization and Recovery

## Purpose

Create a minimal, recoverable project workspace or resume an existing one without mixing venture data into the reusable Skill source.

## Initialization workflow

1. Confirm project name and an available authorized workspace location. If no location is selected, propose one before writing.
2. Assign a stable project ID and create an isolated project directory.
3. Create `project-profile.json` and `project-state.json` from their schemas. Keep unknowns null or explicitly unknown; do not infer user facts.
4. Create registry files for decisions, evidence, assumptions, dependencies, deliverables, and version history using the supplied schemas.
5. Record initial status, current gate, open tasks, and next action. Do not mark a gate passed without evidence.
6. Validate files and report the directory, created files, missing information, and first suggested action.

## Recovery workflow

1. Read the project index, profile, state, and relevant registries when access is authorized.
2. Check that project IDs match and identify malformed, stale, or missing files.
3. Summarize current status, latest confirmed decisions, relevant evidence, active assumptions, blockers, unfinished deliverables, and next actions.
4. Verify the most important input records rather than relying solely on a free-text summary.
5. If records conflict, preserve them and follow `references/_registry/conflict-resolution.md`; do not silently repair authoritative data.
6. Ask the user only for information needed to continue safely or make a material decision.

## Minimal workspace layout

```text
project-id/
├── project-profile.json
├── project-state.json
├── registries/
│   ├── decision-log.json
│   ├── evidence-registry.json
│   ├── assumption-registry.json
│   ├── dependency-graph.json
│   ├── deliverable-registry.json
│   └── version-history.json
├── research/
├── strategy/
├── financial/
├── product-operations/
├── business-plan/
├── assets/
└── snapshots/
```

Create subdirectories as needed; do not create empty scaffolding unless it helps the user. Keep this workspace outside the Skill source repository.
