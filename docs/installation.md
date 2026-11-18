# Local Installation and Use

## Status

This is a local development candidate. There is no universal installer because each platform has different Skill packaging and tool interfaces. The Codex adapter documents current directory-based installation; it has not yet been invocation-tested. Other platform adapters remain unverified.

## Use the core rules manually

1. For Codex, copy the complete `AI-Startup-Planner` directory into `.agents/skills/` under the target project, or into `~/.agents/skills/` for user-wide availability. Start a new Codex session and invoke `$ai-startup-planner` to check discovery. Current official docs describe Skills as a directory centered on `SKILL.md` with optional references, scripts, and assets. See the [Codex Skill guide](https://developers.openai.com/codex/skills) and [installation paths](https://developers.openai.com/api/reference/cli).
2. For other environments, use the platform's supported custom-instruction or Skill mechanism and follow its adapter documentation.
3. Provide only the relevant References for the current task; use `manifest/module-registry.yaml` and `references/_registry/` to select them.
4. Tell the assistant which project workspace to use. Keep it outside this Skill source directory.
5. Confirm which tools are available in that session. If file persistence or research is unavailable, use the documented fallback and do not claim the action was performed.

## Create or resume project data

Use `references/core/project-initialization.md` and `references/core/state-management.md`. Validate JSON records against `schemas/` before relying on them. Keep each venture isolated in its own workspace and follow the schemas for IDs, evidence, decisions, assumptions, and history.

## Validate the bundled synthetic example

From the repository root:

```text
python -m pip install -r requirements-dev.txt
python scripts/validate_examples.py
```

The bundled fixture is fictional. It demonstrates data shape only and must not be copied as real project evidence.

## Update the Skill

Review the changelog and version. Back up or commit local work before replacing an installed copy. Re-read any platform-specific adapter instructions because its package format may differ from this source repository.

## Uninstall

Remove the installed Skill using the target platform's documented process. This does not remove separate project workspaces; handle project data independently and only at the user's request.
