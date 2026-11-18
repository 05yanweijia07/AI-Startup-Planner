# Reference Loading Policy

## Progressive levels

| Level | Load | When |
|---|---|---|
| `L0` | `SKILL.md` and core behavior | Always active. |
| `L1` | Relevant core guidance, project schemas, state records, or registry details | Setup, recovery, update, or core process work. |
| `L2` | Task-specific professional or industry References | The task needs that domain. Load selected sections, not every file in the domain. |
| `L3` | Templates and output-specific resources | Only when the requested artifact requires them. |

These are logical levels. A runtime may implement them using file reads, search, retrieval, or manual selection. Do not claim automatic loading unless the platform actually performed it.

## Efficient loading

1. Read the registry or module summary first.
2. Load the narrowest relevant section that addresses the task.
3. Follow only required dependencies and applicable exclusions.
4. Deduplicate shared guidance and project facts.
5. Expand to a full Reference only when its summary is insufficient or the task requires the whole method.
6. Re-select context for each new task; preserve project state, not irrelevant knowledge context.

## Missing or unavailable content

If a registry entry points to a missing file, or a module is marked planned, do not invent its contents. Continue with available core rules and general reasoning when safe; say what was unavailable if that limitation materially affects confidence or completeness. Do not imply that a capability, tool, Reference, or adapter is active just because it is listed.

## Context limits

Prefer concise extracts and source references over copying long material into the answer. Load sufficient evidence to support the requested result, and keep user-provided source material distinguishable from derived analysis.
