# V1.0.0 Local Release Checklist

This checklist describes release readiness; completing it does not publish or upload the project.

## Core and documentation

- [x] Portable core control file exists.
- [x] Project data schemas and synthetic examples exist.
- [x] Module and tool registries distinguish planned work from available capability.
- [x] Reference routing, loading, and conflict rules exist.
- [x] Core references for five professional engines exist.
- [x] Common platform adapter contract and local use guide exist.
- [x] Choose and add the MIT License before external distribution.
- [ ] Finalize exact platform packaging and verify each claimed adapter.

## Validation

- [x] Schema fixture validator and documented command are provided.
- [x] Representative routing, state, conflict, financial, and end-to-end scenarios are documented.
- [ ] Re-run validator in an environment with `requirements-dev.txt` installed.
- [x] Execute and record representative Codex runtime scenarios; see `tests/RESULTS.md`.
- [ ] Execute the full scenario matrix and verify adapter conformance for the target platform.
- [ ] Run `tests/adapter-compatibility/doubao-deepseek-webapp.md` in the selected Doubao and DeepSeek web/app surfaces and record results.
- [ ] Review all references and registry paths after remaining edits.

## Distribution

- [x] Keep Skill source and startup project data separate.
- [x] No GitHub upload or push is part of this local development task.
- [ ] Obtain explicit user direction for repository visibility and any upload.

## Release decision

Call a release `V1.0.0` only after all blocking items are complete and at least one target adapter has passed conformance checks. Until then, describe the project as a local development candidate, even if the core manifest uses the target version number.
