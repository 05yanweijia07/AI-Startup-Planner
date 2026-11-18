# Financial Analysis Core Workflow

## Module metadata

- **Module ID:** FIN-001
- **Category:** Financial analysis
- **Version:** 1.0.0-draft
- **Status:** Initial core Reference
- **Triggers:** Cost analysis, pricing, unit economics, break-even, cash flow, financial forecast
- **Exclusions:** Nonfinancial editing with no numerical decision
- **Dependencies:** Portable control rules; product/offer definition and stated assumptions

## Purpose

Make financial implications transparent enough to support a decision. Calculations are conditional on inputs and are not guarantees of future performance.

## Required inputs

Clarify currency, units, time period, sales channel, tax/shipping treatment when relevant, price, variable costs, fixed costs, capacity, and timing. Identify whether each input is sourced, user-provided, estimated, or unknown.

## Core calculations

- **Contribution per unit** = net selling price per unit − variable cost per unit.
- **Contribution margin** = contribution per unit ÷ net selling price per unit, when price is positive.
- **Break-even units** = fixed costs ÷ contribution per unit, only when contribution is positive; round up to a whole unit where appropriate.
- **Break-even revenue** = fixed costs ÷ contribution margin, only when contribution margin is positive.
- **Operating cash movement** for a period = cash received − cash paid. Profit and cash flow are not interchangeable.

State formula conventions, inclusion/exclusion of tax, channel fees, returns, discounts, wastage, and startup costs. Do not combine incompatible periods or units.

## Workflow

1. Build a transparent input table with source, unit, period, and confidence/uncertainty.
2. Classify costs as fixed, variable, one-time, or step costs; state any allocation assumptions.
3. Calculate unit economics by product and channel where materially different.
4. Calculate break-even and cash requirements only when inputs are sufficient; otherwise give a formula and the missing inputs.
5. Create low/base/high or other user-relevant scenarios. Change a small number of influential assumptions and explain why.
6. Interpret feasibility against the user's stated goal, capacity, and constraints. List financial risks and validation actions.

## Output and quality checks

Show input values, units, formulas, results, and assumptions. Check arithmetic, denominator signs, period consistency, and whether contribution is positive. Label projections as scenarios. Do not hide negative or infeasible results, and do not imply accounting, tax, investment, or legal advice.

## Integration

Take product specification and operations costs from Product & Operations; take price and customer assumptions from Business Strategy and Market Research. Record material assumptions in the assumption registry and flag dependent deliverables when inputs change.
