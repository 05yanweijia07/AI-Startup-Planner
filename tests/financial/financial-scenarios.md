# Financial Calculation Scenarios

Use these arithmetic fixtures to check formulas and units in financial outputs.

## F-01: Simple break-even

- Net selling price: USD 20/unit
- Variable cost: USD 8/unit
- Fixed cost: USD 1,200/month
- Contribution: 20 − 8 = USD 12/unit
- Contribution margin: 12 ÷ 20 = 60%
- Break-even: 1,200 ÷ 12 = 100 units/month
- Break-even revenue: 1,200 ÷ 0.60 = USD 2,000/month

Expected result: **PASS** if all quantities retain the monthly basis and the output labels this as a model result, not a sales forecast.

## F-02: Negative contribution

- Net selling price: USD 10/unit
- Variable cost: USD 12/unit
- Fixed cost: USD 1,000/month

Expected result: state contribution is negative and volume alone cannot reach break-even under these inputs. Do not output a positive break-even quantity.

## F-03: Sensitivity

Using F-01 fixed cost, if price falls to USD 18 and variable cost remains USD 8, contribution is USD 10 and break-even is 120 units/month. If price stays USD 20 and variable cost rises to USD 10, the same 120 units/month result applies. Explain the changed assumption.

## F-04: Missing units

If a cost is quoted per case and selling price is per item with no items-per-case information, do not calculate unit contribution. Ask for conversion or show the formula and missing input.
