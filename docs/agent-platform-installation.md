# Agent Platform Installation

The GitHub repository is the source of the Skill. Publishing the repository does not install the Skill in an agent platform. Use the platform's own Skills or plugin flow, and verify that the Skill appears in that platform's invocation menu before relying on it.

The upload bundle is available at [`packages/AI-Startup-Planner.zip`](../packages/AI-Startup-Planner.zip). It contains `SKILL.md`, its routed References, schemas, registries, and the shared adapter contract. It contains no venture-specific workspace data.

## ChatGPT Skills

ChatGPT Skills are available only to eligible ChatGPT Business, Enterprise, Healthcare, and Edu users, subject to workspace settings and product availability.

1. In ChatGPT, open **Plugins** and select the **Skills** tab.
2. Choose **Create** → **Upload from your computer** and select `AI-Startup-Planner.zip`.
3. Review the uploaded Skill and any scan results. Install it when the platform makes it available.
4. Start a new chat and check the Skills menu or use the platform's offered invocation control to select AI Startup Planner.
5. Confirm it is active with a small test prompt before using it on real project data.

If the Skills tab or upload action is unavailable, the account or workspace does not currently expose Skill installation. A public GitHub URL or a Project file is not a substitute for an installed Skill.

Official guidance: [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

## Doubao Work / iDA Skill Market

This path is for the agent product that exposes the Skill Center or Skill Market. It is separate from the regular consumer Doubao chat page.

1. Open **Skill Center** or **Skill Market** and choose **Create Skill** → **Upload Skill**.
2. Upload `AI-Startup-Planner.zip` (or the same ZIP renamed to `.skill` if the interface requires that extension).
3. Review the parsed name, description, and resource files; complete required scenario and permission settings.
4. Publish or save the Skill according to the product's workflow, then add it to the intended agent if agent authorization is available.
5. In that agent's conversation, select the Skill from the lightning/Skills menu or invoke it with `@` when supported.

The standard consumer Doubao web/app interface may not expose this Skill Center. Doubao Open Platform public-market publishing is a separate process with platform eligibility and review requirements; this bundle alone does not publish or approve it.

Official guidance: [iDA Skill Market](https://docs.volcengine.com/docs/data-agent/skill-market?lang=zh) and [Doubao Open Platform Skill Integration](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide).

## DeepSeek Harness desktop

The regular DeepSeek web/app chat does not document an installable Skill directory. DeepSeek Harness desktop has a local Skill provider that reads a directory bundle with `SKILL.md` at its root.

1. Download the repository ZIP from GitHub and extract it.
2. Create a Skill directory in one of Harness's supported roots, for example `%USERPROFILE%\\.agents\\skills\\ai-startup-planner` or `%USERPROFILE%\\.dsh\\skills\\ai-startup-planner`.
3. Copy the **contents** of the extracted repository into that directory so `SKILL.md` is directly inside `ai-startup-planner`; keep `references`, `manifest`, `schemas`, and `adapters` alongside it.
4. Open or refresh a Harness session and confirm AI Startup Planner appears in the session's Skills list. Select it using the invocation control shown by that Harness version.

Official guidance: [DeepSeek Harness Skills subsystem](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md).

## Current verification boundary

The local schema and project-structure validators passed before publication. They validate the files and examples, not whether a particular hosted platform has installed or invoked this Skill. ChatGPT, Doubao Work/iDA, and DeepSeek Harness runtime invocation still need to be confirmed in the respective user account and app.
