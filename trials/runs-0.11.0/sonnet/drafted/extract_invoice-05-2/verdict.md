## Lines

| line | verdict | reason |
| --- | --- | --- |
| F1 | held | not touched |
| F2 | held | not touched |
| F3 | held | not touched |
| F4 | held | not touched |
| F5 | held | not touched; `_number(raw_tax, "tax")` accepts negative values, so negative amounts stay allowed. |
| F6 | held | not touched |
| F7 | held | not touched |
| F8 | held | not touched |
| C1 | held | Existing keys are still required and checked. The new `tax` is optional: `Decimal("0.00") if raw_tax is None`. A malformed tax raises `InvoiceError` naming `tax`. |
| C2 | held | not touched; the gap (only three capital letters checked) is left as it was. |
| C3 | moved toward the charter | `+ "tax" (the VAT or sales tax amount shown on the invoice...)` and `+ "status": "ok" if lines_total + tax == total`. VAT is now a separate field, checked by code against net and total. |
| C4 | held | not touched; line amounts are still `_cents(quantity * unit_price)`. |
| C5 | held | `lines_total + tax == total` is still an exact comparison in code, with no tolerance; adding the VAT term is the C3 move. |
| C6 | held | not touched; still one `model(...)` call, no retry. |
| C7 | held | not touched |
| B1 | held | not touched; one model call per invoice. |

## Trial

- where: both
- flagged: no
- stopped: no