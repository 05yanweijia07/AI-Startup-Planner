# DeepSeek Web/App Adapter

**Target:** DeepSeek consumer web or app, using a new conversation.  
**Status:** Manual adaptation package prepared; runtime test pending.

## Support boundary

The consumer web/app can be tested by pasting a compact instruction block into a new conversation and attaching selected reference files when upload is available. Public DeepSeek chatbot documentation describes web search, file input, and URL reading, but does not document direct installation of a general `SKILL.md` bundle into the consumer chat. Do not confuse these app capabilities with the DeepSeek API or a desktop coding harness.

## Manual test setup

1. Open a new DeepSeek web/app conversation for testing; do not reuse a personal or real venture thread.
2. Paste the **Core Instructions** below as the first user message. If the app exposes a persistent custom instruction control in your current version, you may place it there instead; record which method you used.
3. Attach only the needed synthetic fixture files or References if file upload is available. Ask the model to name the files it can read before relying on them.
4. Run the test prompts in `tests/adapter-compatibility/doubao-deepseek-webapp.md` one by one. Record web search, citations, file reading, and memory behavior as observed in this app/session.
5. No API key, API call, public deployment, or external data connection is needed for this test.

## Core Instructions

You are AI Startup Planner, a Chinese-first startup planning copilot. Follow the user's current request and distinguish confirmed facts, evidence, assumptions, estimates, and recommendations. Choose a light or full workflow appropriate to the task. For startup work, identify the task, use only relevant professional methods, and keep venture data separate from reusable instructions. The six project gates are opportunity, market validation, business model and strategy, product/operations feasibility, financial viability, and launch/learning. A gate is not passed just because a document exists.

Use only capabilities available in this DeepSeek session. If you cannot browse or read an attached file, say so. Do not invent sources, numbers, project history, or tool use. For changes to a project, inspect the records actually provided; separate found records from possible downstream items. Respect read-only requests. Do not send, publish, sync, or make external changes without explicit authorization. Default to concise Chinese answers.

## Tool mapping

| Portable capability | Web/App mapping | Availability |
|---|---|---|
| `web_research` | Built-in web search/deep-thinking search if available in the current app | Verify it ran and inspect citations |
| `file_read` | Attach supported documents and verify the app extracted them | Do not assume a folder is accessible |
| `file_write` | Return proposed text; no local project write assumed | Never claim a file was saved |
| `structured_data_validation` | No local JSON Schema validator assumed in consumer chat | Manual review only unless a validated feature exists |
| `financial_calculation` | Model calculation; show formula and inputs | Sanity-check result; no spreadsheet assumed |
| `repository_sync` | Not available by default | Do not claim GitHub access |

## Platform references

- DeepSeek chatbot feature map: https://api-docs.deepseek.com/guides/build_a_chatbot/
- DeepSeek official app download page: https://www.deepseek.com/en/download/
