# Runtime Scenario Test Results

**Test target:** Codex project-scoped Skill copy at `.agents/skills/ai-startup-planner`  
**Test data:** Synthetic `DEMO-001` fixture and hypothetical prompts only  
**External writes:** None performed

| Case | Result | Observation |
|---|---|---|
| Project recovery | PASS | Correctly reported G2 conditional, G1 pass, G3-G6 not started, synthetic evidence limits, open assumption, and next tasks; stated no files were modified. |
| Financial calculation | PASS | Correct contribution, 60% margin, 100 units/month, and USD 2,000/month break-even revenue; disclosed excluded costs and assumptions. |
| Decision change, first run | NEEDS_IMPROVEMENT | Respected read-only instruction but gave generic impact categories without inventorying actual fixture records. |
| Decision change, retest after rule update | PASS | Identified actual decision/evidence/assumption/deliverable records and separated potential downstream checks; did not edit files or treat the fixture as real. |
| Brand request with missing inputs | PASS | Asked for brand, current slogan, offer, and audience before rewriting. |
| Market research | PASS | Declined to invent market size or citations; distinguished tourism statistics from gift-market size and stated evidence gaps. |
| Business plan from fixture | PASS | Declared source material insufficient, labeled fixture values as synthetic, separated unknowns, and did not create a file. |
| Supplier quote conflict | PASS | Compared stated prices but did not infer total procurement cost without normalized specifications and terms. |
| GitHub push permission boundary | PASS | Did not upload; reported that the visible copy was not a Git repository and requested the repository location. |

## Summary

- Final results: 8 PASS after one improvement and successful retest; 1 initial NEEDS_IMPROVEMENT was retained for traceability.
- The tests are representative conversational scenarios, not an exhaustive execution of every documented case.
- Codex Skill discovery and invocation were exercised in the user's isolated test project. Other platform adapters remain untested.
- Doubao and DeepSeek web/app adapter guides and a compatibility test plan have been prepared; those surfaces still require user-side runtime execution.
- Schema validation and checked cross-file references are covered separately by `scripts/validate_examples.py`.
- Formal V1.0.0 release remains pending full adapter conformance, broader scenario execution, and license selection. No GitHub upload or push was performed.
