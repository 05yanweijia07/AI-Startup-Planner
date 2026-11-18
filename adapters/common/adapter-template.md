# Platform Adapter Specification Template

Copy this file into a platform-specific adapter directory and complete every section before claiming that platform is supported.

## Adapter metadata

- Adapter ID:
- Platform and supported version range:
- Adapter version:
- Status: `planned` / `in_progress` / `validated`
- Maintainer:
- Last verified date:

## Skill packaging

Document the platform's required file layout, metadata/frontmatter, installation method, update/uninstall process, and any platform-specific prompt limits. Keep platform packaging separate from Portable Core content where possible.

## Capability mapping

| Portable capability | Runtime tool or workflow | Availability conditions | Permission class | Side effects | Fallback |
|---|---|---|---|---|---|
| `web_research` |  |  | `read_only` |  |  |
| `file_read` |  |  | `read_only` |  |  |
| `file_write` |  |  | `local_write` |  |  |
| `structured_data_validation` |  |  | `read_only` |  |  |
| `financial_calculation` |  |  | `read_only` |  |  |
| `visualization` |  |  | `local_write` or `external_write` |  |  |
| `repository_sync` |  |  | `external_write` |  |  |

## File and workspace behavior

Describe how the adapter reads and writes user-selected paths, detects existing files, preserves project/Skill separation, handles unavailable workspaces, and reports partial failures.

## Permission behavior

Explain how the runtime expresses user consent for local changes and external writes. Confirm how confirmation requirements interact with platform policy. Do not claim that a registry entry itself grants permission.

## Conformance checks

- [ ] Core task types and four modes work as intended.
- [ ] Six startup gates remain user-owned checkpoints.
- [ ] Reference routing and missing-reference fallback work.
- [ ] Project state can be read, updated, validated, and recovered where tools permit.
- [ ] External writes require explicit authorization.
- [ ] Representative routing and end-to-end scenarios pass.
- [ ] Unsupported capabilities are disclosed honestly.

## Known limitations

List unsupported capabilities, prompt/file constraints, platform-specific behavior, and untested workflows. Set `validated` only after the checks above have evidence.
