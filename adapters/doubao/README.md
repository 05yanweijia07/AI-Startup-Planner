# Doubao Web/App Adapter

**Target:** Doubao consumer web or app, using a custom agent or a normal conversation.  
**Status:** Manual adaptation package prepared; runtime test pending.

## Support boundary

The portable source folder is not directly installable as a Skill in the consumer Doubao chat based on the public instructions reviewed. Doubao describes custom agents with configurable style, skills, and background. Its separate open-platform Skill workflow accepts ZIP packages and has platform review/deployment requirements; those distribution steps are out of scope for this manual web/app test. Confirm available controls in the user's current app version.

## Manual test setup

1. Create a new, isolated Doubao custom agent if the interface offers it. Name it `AI Startup Planner Test` and keep visibility private. If custom-agent creation is unavailable, start a new chat instead.
2. Paste the **Core Instructions** below into the agent's role/background/instructions field if available. Otherwise paste them as the first message in a new conversation.
3. If the interface supports knowledge/files, upload only `SKILL.md`, `references/_registry/routing-rules.md`, `references/_registry/loading-policy.md`, `references/_registry/conflict-resolution.md`, and the synthetic fixture files needed for a test. Do not upload real venture data for this test.
4. Ask the test prompts in `tests/adapter-compatibility/doubao-deepseek-webapp.md` one by one in the same isolated agent/conversation. Record whether the platform actually reads the uploaded files and whether a new conversation retains any instruction context.
5. Do not publish the agent, submit a Skill package, or connect external tools as part of this test.

## Core Instructions

You are AI Startup Planner, a Chinese-first startup planning copilot. Follow the user’s current request and distinguish confirmed facts, evidence, assumptions, estimates, and recommendations. Choose a light or full workflow appropriate to the task. For startup work, identify the task, use only relevant professional methods, and keep venture data separate from reusable instructions. The six project gates are opportunity, market validation, business model and strategy, product/operations feasibility, financial viability, and launch/learning. A gate is not passed just because a document exists.

Use only capabilities available in this Doubao session. If you cannot browse or read an attached file, say so. Do not invent sources, numbers, project history, or tool use. For changes to a project, inspect the records actually provided; separate found records from possible downstream items. Respect read-only requests. Do not send, publish, sync, or make external changes without explicit authorization. Default to concise Chinese answers.

## Tool mapping

| Portable capability | Web/App mapping | Availability |
|---|---|---|
| `web_research` | Built-in search if shown in this account/session | Check at runtime; don't assume freshness or citations |
| `file_read` | User file attachment or custom-agent knowledge, if available | Check file parsing and whether contents are actually surfaced |
| `file_write` | Usually return proposed text; use any file creation control only when available and authorized | Not assumed |
| `structured_data_validation` | No local Python/JSON Schema validator assumed in chat | Manual review only unless a validated feature exists |
| `financial_calculation` | Model calculation; show formula and inputs | Sanity-check result; no external spreadsheet assumed |
| `repository_sync` | Not available by default | Do not claim GitHub access |

## Platform references

- Doubao consumer feature overview: https://www.doubao.com/legal/feature_intro
- Doubao Open Platform Skill integration guide (separate platform): https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide
- Doubao Open Platform developer docs: https://open.doubao.com/document
