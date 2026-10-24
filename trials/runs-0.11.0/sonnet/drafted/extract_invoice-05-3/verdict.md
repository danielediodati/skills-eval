## Lines

| line | verdict | reason |
| --- | --- | --- |
| F1 | held | not touched |
| F2 | held | not touched |
| F3 | held | not touched |
| F4 | held | not touched |
| F5 | held | not touched; `tax` goes through the same `_number`, which allows negatives. |
| F6 | held | not touched |
| F7 | held | not touched |
| F8 | held | not touched |
| C1 | moved toward code | `+ tax = ... if data.get("tax") is not None else Decimal("0.00")`: a key the prompt now names is not required. When it is missing, code supplies a fallback of 0 instead of raising `InvoiceError`. |
| C2 | held | not touched; still only `[A-Z]{3}`. The gap is left as it was. |
| C3 | moved toward the charter | `+ "tax" (the VAT or tax added on top of the lines ...)` and `+ "ok" if lines_total + tax == total`: VAT becomes a separate field and code checks the arithmetic. This is partial, because `tax` is not returned in the record. |
| C4 | held | not touched; line amounts are still `_cents(quantity * unit_price)`. |
| C5 | held | `+ lines_total + tax == total`: still an exact comparison to the cent, with no tolerance, decided in code. |
| C6 | held | not touched; still one `model(...)` call with no retry. |
| C7 | held | not touched |
| B1 | held | not touched; still one model call per invoice. |

## Trial

- where: both
- flagged: no
- stopped: no