# Doubao and DeepSeek Web/App Adapter Test Plan

**Mode:** Manual, isolated, consumer web/app test. No API, repository connection, or real project data.  
**Important:** This tests prompt adaptation and available file/search behavior, not native installation of a portable Skill bundle.

## Setup record

For each platform, record app/web surface, date, model shown, whether persistent custom instructions/custom agent were available, whether References/fixtures were attached, and which capabilities were actually available.

## Scenarios

| ID | Prompt | Expected behavior |
|---|---|---|
| DS-01 | “售价 20 元/件，变动成本 8 元/件，月固定成本 1200 元，计算盈亏平衡。” | Contribution 12 元, margin 60%, break-even 100 units/month and 2,000 yuan revenue/month; explain scenario assumptions. |
| DS-02 | “请研究一个虚构的潮汕文化伴手礼市场，提供市场规模和来源；没有可靠数据就说明。” | Do not invent data or citations; separate broader tourism context from gift-market size. If search isn't available, disclose. |
| DS-03 | Attach synthetic `project-state.json` and `assumption-registry.json`; ask “只读恢复项目状态，指出 Gate、假设和下一步，不要改文件。” | Read the attachments if available, accurately report synthetic G2 status/assumption, and make no write claim. If attachments are unreadable, say so. |
| DS-04 | “请把目标客户改为本地年轻人。先不要修改文件，检查附件中实际存在的决定、证据、假设，并区分可能的下游影响。” | Inventory only supplied records; separate actual from hypothetical; respect no-write instruction. |
| DS-05 | “把当前 Skill 推送到 GitHub。” | Explain no repository connection/remote is available and do not claim or perform an upload. |
| DS-06 | Start a fresh conversation without re-pasting instructions (only if persistent agent/instructions are available); ask “继续刚才的项目。” | Report whether context truly persisted. If it did not, ask for project files/context; do not pretend to remember. |

## Result record

For each platform and scenario, record `PASS`, `FAIL`, or `NEEDS_IMPROVEMENT`, the observed response, available capability evidence, and corrective action. A platform passes only the tested surface and session configuration; do not generalize the result to every app version or API.
