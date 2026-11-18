# Dependency Management

## Purpose

Track which analyses, gates, and deliverables depend on project facts, decisions, evidence, or assumptions so changes can be reviewed efficiently.

## Link rules

Use stable node IDs and explicit edge relations from the dependency graph schema. A dependency means a change in the source may affect the target; it does not mean the target automatically becomes invalid.

For each material update:

1. Find direct downstream nodes.
2. Review whether each dependent conclusion changes under the new input.
3. Recalculate or revise affected items when feasible.
4. Mark unresolved deliverables stale and explain why.
5. Avoid broad invalidation of unrelated work.

## Graph quality

Do not create dangling endpoints. Keep references resolvable to a record ID or workspace-relative path. Prefer a small useful graph to exhaustive links that nobody can maintain. Preserve contradictory links as such rather than forcing a false dependency.
