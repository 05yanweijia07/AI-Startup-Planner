# Platform Adapter Capability Contracts

## Purpose

An adapter connects the portable core to capabilities that a specific runtime actually exposes. This contract names the work the core may request; it does not imply a tool is installed, authenticated, available in the current session, or authorized for a particular action.

## Adapter responsibilities

For each capability, an adapter should declare:

| Field | Meaning |
|---|---|
| Capability ID | Stable portable name, such as `web_research` |
| Runtime mapping | Actual tool, API, or documented manual workflow |
| Availability | Available, unavailable, or conditional in this session |
| Inputs and outputs | Accepted input shape and returned result shape |
| Permission class | `read_only`, `local_write`, `external_write`, or `destructive` |
| Side effects | Files, remote state, messages, cost, or other consequences |
| Limits | Scope, file size, freshness, rate, or platform restrictions |
| Fallback | Safe alternative when unavailable or unsuccessful |

The core must check availability at runtime. Registry presence alone is never proof of availability.

## Portable capability contracts

### Research: `web_research`

- **Inputs:** research question, geography, time period, and any source constraints.
- **Outputs:** source title and URL, publisher, publication/access date when available, relevant finding, scope, and limitations.
- **Permission:** `read_only`.
- **Quality:** distinguish what the source says from analysis or inference; prefer primary sources where appropriate.
- **Fallback:** state that current research could not be performed; offer a bounded desk analysis or research plan.

### File access: `file_read` and `file_write`

- `file_read` accepts an authorized path and returns content or a clearly labeled extraction; permission is `read_only`.
- `file_write` accepts an authorized target, content, and intended change; permission is `local_write`.
- Before a write, inspect the target if it exists. Preserve unrelated content and report the resulting path.
- **Fallback:** ask the user to provide the excerpt or return proposed content and path without claiming persistence.

### Data: `structured_data_validation`

- **Inputs:** schema and data paths, plus expected cross-file references.
- **Outputs:** syntax/schema result and actionable errors; distinguish schema validation from business-quality review.
- **Permission:** `read_only` unless a separate repair/write step is requested and authorized.
- **Fallback:** perform available syntax checks and identify which validation could not run.

### Financial: `financial_calculation`

- **Inputs:** numeric values, currency, units, time period, and assumptions.
- **Outputs:** formulas, results, scenario comparisons, and limitations.
- **Permission:** `read_only` for calculation.
- **Quality:** show units and assumptions; never convert projections into claims of actual performance.
- **Fallback:** present transparent formulas and calculations from provided inputs.

### Visualization: `visualization`

- **Inputs:** structured content and requested visual format.
- **Outputs:** chart, diagram, or other artifact, with data labels and units where applicable.
- **Permission:** typically `local_write` when saving a file; creation in an external application may require `external_write`.
- **Fallback:** use a text table or Mermaid diagram where suitable.

### Repository integration: `repository_sync`

- **Inputs:** repository identity, selected files, target branch, and intended operation.
- **Outputs:** remote commit/sync outcome and resulting reference.
- **Permission:** `external_write`; inspect the exact file set and destination first.
- **Rule:** explicit user authorization is required for upload, push, or sync. Never include project data in the Skill repository by default.
- **Fallback:** prepare local changes and provide manual instructions.

## Permission handling

1. Confirm the capability is available in this session.
2. Check that the requested action fits the capability's permission class and the user's authorization.
3. Separate read, local-write, and external-write steps; do not let permission for one imply permission for another.
4. For destructive or hard-to-reverse actions, verify the exact target and expected effect before proceeding.
5. Report failure and partial side effects accurately. Do not retry external writes blindly.

## Adapter conformance checklist

- [ ] Every advertised runtime mapping exists and is usable in the target environment.
- [ ] Input/output shapes and failure behavior are documented.
- [ ] Permissions and side effects are visible to the core.
- [ ] Unsupported capabilities have safe fallbacks.
- [ ] Platform-specific install or metadata rules stay in the adapter package.
- [ ] Core behavior and project data formats remain portable.
