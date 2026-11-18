# Decision Management

## Record a decision

For each material founder choice, record a stable `decision_id`, topic, exact choice, status, date/time from the runtime, decision owner when known, rationale, supporting/contradicting evidence IDs, and affected records or outputs.

Use `proposed` for a recommendation not yet accepted, `confirmed` for a user-approved choice, `withdrawn` when abandoned, and `superseded` when replaced by a later decision. AI recommendations are not confirmed decisions unless the user adopts them.

## Before recommending

State the decision needed, viable options, evidence and assumptions, key tradeoffs, reversibility, and downstream effects. Keep the recommendation separate from the user's choice.

## Change process

On user-requested change, inspect the available decision log and dependency graph first. Identify actual prior choices and direct dependencies separately from plausible downstream areas that have no record yet. Do not describe hypothetical records as found. Then explain the proposed replacement, changed risks, and outputs to refresh. Record history rather than editing away the old choice. If persistence is unavailable, give the user a clearly labeled proposed log entry.
