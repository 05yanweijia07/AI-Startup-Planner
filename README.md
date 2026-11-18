# AI Startup Planner

**Version:** 1.0.0 (core control file, in progress)  
**Architecture:** Portable Core + Platform Adapters + Separate Project Workspace

**License:** MIT; see [`LICENSE`](LICENSE).

AI Startup Planner is a modular, evidence-led copilot for founders. It helps turn an idea into a validated opportunity, coherent business model, feasible operating plan, transparent financial scenarios, and useful business-plan deliverables.

This public repository contains the reusable planning Skill and development materials. Each venture's private project data belongs in a separate workspace and is excluded from this repository.

## Current status

The portable control file is available: [`SKILL.md`](SKILL.md). Project Intelligence schemas and operating rules cover profiles, state, decisions, evidence, assumptions, dependencies, deliverables, and history. The manifest and capability indexes are in [`manifest/`](manifest/); entries marked `in_progress` or `planned` are not complete engines or connected tools. Shared adapter contracts are in [`adapters/common/`](adapters/common/), routing/loading/conflict rules are in [`references/_registry/`](references/_registry/), core project-state References are in [`references/core/`](references/core/), and professional methods are organized by engine under [`references/`](references/).

This is a V1.0.0 local development candidate. Project Intelligence has schemas, operating rules, a synthetic fixture, and validation scripts. Five engines have initial workflow and method References, and two industry modules have initial guidance. Representative Codex scenarios were exercised in an isolated project; results are in [`tests/RESULTS.md`](tests/RESULTS.md). Manual web/app adapters for Doubao and DeepSeek are prepared, but runtime tests remain; see `tests/adapter-compatibility/` and `docs/release-checklist.md`.

## Architecture

### Portable Core

The platform-neutral rules and business-planning workflows. The core refers to capabilities by function rather than assuming a particular vendor's tools. Professional methods are organized as modular References and loaded only when relevant.

### Platform Adapters

An adapter maps the core's capability contracts and file conventions to an actual environment, such as Codex, ChatGPT, Claude Code, or another agent platform. Platform-specific metadata and integrations belong in the adapter; they must not silently change core logic or venture data.

Portability applies to the core rules and data concepts. It does not mean that a Skill package or tool interface can be installed unchanged on every platform.

### Separate Project Workspace

Each startup's profile, decisions, evidence, assumptions, status, history, and deliverables belong in an independent project workspace. Keep those materials out of this reusable Skill source. A future project workspace may be a separate local directory or repository; it is not created or connected automatically by this repository.

## Core workflow

The Skill recognizes eight task types: ideation, project setup, market research, business strategy, financial analysis, product and operations, business-plan deliverables, and project updates. It chooses among four modes:

- **QUICK** for a focused answer or small edit.
- **GUIDED** for step-by-step project development.
- **RESEARCH** for evidence-seeking questions.
- **BUILD** for substantial plans, workspace changes, or deliverables.

For venture progress, six gates track opportunity, market validation, business model and strategy, product and operational feasibility, financial viability, and launch and learning. Gates are revisitable checkpoints; the founder makes the decision to proceed.

## Using the Skill

1. Open `SKILL.md` and provide it to an AI environment that supports custom instructions or Skills.
2. Use a platform adapter to map required capabilities, such as web research or file access, to tools actually available in that environment.
3. For persistent project work, provide or create a separate project workspace and tell the assistant which project to use.
4. Start with a request in ordinary language, for example: “Help me assess demand for a local food gift box” or “Continue the market validation stage for my project.”

Exact installation steps depend on the target platform and will be documented in the corresponding adapter. Do not assume a tool, Reference, or project file exists unless the environment confirms it.

See [`docs/installation.md`](docs/installation.md) for local use and [`docs/release-checklist.md`](docs/release-checklist.md) for readiness criteria. The project is not yet a published V1.0.0 release.

### Validate the data examples

The fixture under `tests/fixtures/synthetic-project/` is fictional and exists only to demonstrate the schemas. It is not a real venture or market research. From this repository directory, install the development dependency and run:

```text
python -m pip install -r requirements-dev.txt
python scripts/validate_examples.py
python scripts/validate_project.py
```

The example validator checks each fixture against its Draft 2020-12 JSON Schema, date formats, and selected cross-file references. The project validator also checks Skill metadata, YAML manifests, registry paths, schema examples, and required test documentation. These checks do not validate business claims or replace review of project-specific data.

## Data and permission principles

- Separate reusable Skill source from venture-specific information.
- Keep structured project state as the authoritative record; reports should cite or explain it rather than create conflicting facts.
- Distinguish sourced facts, estimates, assumptions, and recommendations.
- Use only capabilities actually available in the current environment.
- Inspect existing files before changing them; preserve provenance and history when supported.
- Do not publish, sync, or push project or Skill data externally without explicit authorization.

## Planned development sequence

The following is the intended sequence, not a statement that these files already exist:

1. **Core foundation:** README, `SKILL.md`, principles, intent and mode rules, initial registries.
2. **Project intelligence:** initial schemas cover the project profile, current state, decision, evidence, assumption, dependency, deliverable, and version-history records; synthetic examples and a local validation script are included. Operational guidance and project-specific review remain.
3. **Routing registries:** an initial module registry and tool capability registry are defined; planned modules still need their References and runtime adapters.
4. **Portable integration rules:** common capability contracts and Reference routing/loading/conflict rules are defined; target-platform mappings remain.
5. **Professional engines:** initial workflow and method References for all five engines; deeper specialization may be added as validation reveals needs.
6. **Testing and optimization:** scenario suite is documented; runtime execution and adapter conformance remain.
7. **Release preparation:** local installation guide, changelog, and release checklist are present; the repository uses the MIT License, while final review and platform packaging remain open.

The repository is published at [github.com/05yanweijia07/AI-Startup-Planner](https://github.com/05yanweijia07/AI-Startup-Planner). Keep venture-specific project data out of this public source repository.

## Versioning

The intended milestones are V0.1.0 for the foundation, V0.2.0 for project intelligence, V0.3.0 for professional engines, V0.4.0 for adapters, V0.5.0 for testing and optimization, and V1.0.0 for a reviewed release. The current `1.0.0` label identifies the target core specification version; it does not imply the complete product has shipped.

## Language

User interaction defaults to Chinese, unless the user requests another language. File names, IDs, and structured data fields use English for portability and consistency.

