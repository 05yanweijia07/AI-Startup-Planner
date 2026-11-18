# Codex Adapter

**Status:** In progress; package layout documented, not installed or runtime-validated.

Codex recognizes a Skill as a directory containing `SKILL.md` and optional `references/`, `scripts/`, and `assets/`. OpenAI's current Codex-facing documentation lists project-scoped Skills under `.agents/skills/` and user-scoped Skills under `~/.agents/skills/`. For a project install, place the complete `AI-Startup-Planner` directory under the target project's `.agents/skills/`; for user-wide use, place it in the user's `.agents/skills/` directory. Start a new Codex session after installation and explicitly invoke `$ai-startup-planner` for a first check. [Build skills](https://developers.openai.com/codex/skills) · [Skill installation paths](https://developers.openai.com/api/reference/cli)

Complete `adapters/common/adapter-template.md` against the actual Codex environment before declaring support. Map file, research, validation, and external integration capabilities to tools actually present in the session.

Keep the reusable Skill source separate from each project workspace. Do not assume Codex has access to a project directory until the user has selected or provided it. Follow the core authorization rule for local writes and external repository changes.

The directory format and installation locations are documented by OpenAI, but this Skill has not yet been installed or invocation-tested in a separate Codex project. Tool availability remains session-dependent.
