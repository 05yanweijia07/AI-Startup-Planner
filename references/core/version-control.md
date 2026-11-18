# Project Version History

## What constitutes a meaningful change

Record material changes to confirmed decisions, key evidence, assumptions, gate status, financial inputs, project identity, or deliverables. Routine formatting edits need not create a project snapshot unless the user requests it.

## History entry

Use the version-history schema: stable version ID, runtime timestamp, change type, short summary, changed record references, actor when known, and a snapshot reference only if an actual snapshot exists.

## Preserve and restore

History is append-only where possible. Do not rewrite past entries to make the current state appear consistent. To restore an earlier state, inspect the snapshot and subsequent changes, identify the intended scope, and record restoration as a new event. Keep independent Skill-source versioning separate from project-data history.
