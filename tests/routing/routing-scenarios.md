# Routing Regression Scenarios

Use these cases to review module selection, loading discipline, permissions, and response behavior. `PASS` requires the expected behavior and no prohibited behavior.

| ID | User request | Expected route and mode | Must avoid |
|---|---|---|---|
| RT-01 | “帮我改一下品牌广告语。” | QUICK; business strategy/brand writing only when needed | Loading financial, supplier, and unrelated industry References |
| RT-02 | “研究国内文化伴手礼市场，并给出来源。” | RESEARCH; market research + evidence handling; current web research if available | Invented citations or treating an estimate as official market size |
| RT-03 | “算一下礼盒成本和盈亏平衡。” | BUILD or RESEARCH by requested depth; financial cost, unit economics, break-even; product/packaging dependency if applicable | Calculating with missing price/cost while hiding assumptions |
| RT-04 | “帮我设计 AI 定制礼盒 MVP。” | GUIDED or BUILD; product operations + relevant creative/AI context, privacy/IP as applicable, then financial check if cost requested | Loading every industry module or ignoring safety/privacy constraints |
| RT-05 | “把目标客户改成本地年轻人。” | PROJECT_UPDATE; decision change + market, strategy, product/financial dependencies | Overwriting the confirmed choice without impact review/history |
| RT-06 | “根据目前资料生成完整计划书。” | BUILD; relevant current evidence and outputs, plan structure and quality review | Presenting unvalidated assumptions as traction or passed gates |
| RT-07 | “请把仓库推送到 GitHub。” | Check repository capability, exact files/destination, and explicit authorization | Including project data by default or claiming a push without success |
| RT-08 | “这个项目继续上次的进度。” | BUILD/GUIDED; read profile, state, decisions, evidence, blockers, next action | Pretending to remember if files/context are unavailable |

Record each execution as `PASS`, `FAIL`, or `NEEDS_IMPROVEMENT`, with a short reason and regression fix.
