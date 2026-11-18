# Reference and Project Conflict Resolution

## Conflict classes

- **Instruction or rule conflict:** two applicable rules prescribe incompatible actions.
- **Data conflict:** records or sources disagree about a value or fact.
- **Strategic conflict:** methods recommend different business directions.
- **Freshness conflict:** a previously valid analysis depends on changed or stale inputs.

## Priority order

Apply the following order, while preserving each rule's scope:

1. **P0 — Safety, law, and platform constraints.** These cannot be displaced by ordinary business advice.
2. **P1 — The user's current explicit instruction.** It may request a change to an earlier choice but cannot override P0.
3. **P2 — Confirmed project decisions.** Keep them active until the user changes or withdraws them through a recorded update.
4. **P3 — Applicable industry-specific requirements.** Apply only to the activity and jurisdiction in scope; flag uncertainty.
5. **P4 — Task-specific methods.** Use within their stated purpose and limits.
6. **P5 — General methods, examples, or heuristics.** Treat as supporting guidance, not project evidence.

## Data disagreements

Do not silently choose or average conflicting values. Compare source, date, scope, unit, quantity, tax/shipping inclusion, and methodology when relevant. Preserve incompatible records with provenance. If the difference changes the result, show scenarios or ask a focused question.

## User-requested decision change

Treat a request to alter a confirmed choice as a change request, not as a reason to reject the user or silently overwrite history:

1. Identify the old and proposed values.
2. Check direct and downstream dependencies.
3. Explain material consequences and analyses that may become stale.
4. Apply the change if the user has clearly requested it; record the supersession where persistence is available.
5. Update or mark dependent outputs stale. Keep the old record traceable.

## Unresolved conflict

Name the conflict, relevant sources or modules, and practical impact. Separate facts from recommendations. Ask only for a decision needed to proceed; otherwise provide clearly labeled alternatives and state what remains unresolved.
