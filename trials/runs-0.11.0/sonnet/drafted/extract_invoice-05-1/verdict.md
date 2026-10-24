## Lines

| line | verdict | reason |
| --- | --- | --- |
| F1 | held | not touched |
| F2 | held | not touched |
| F3 | held | not touched |
| F4 | held | not touched |
| F5 | held | not touched |
| F6 | held | not touched |
| F7 | held | not touched |
| F8 | held | not touched |
| C1 | held | `+ tax = _cents(_number(data.get("tax"), "tax"))`: the new key is required and a missing one raises `InvoiceError` naming the field, so the shape check still covers every key. |
| C2 | held | not touched |
| C3 | moved toward the charter | `+ "tax" (the VAT or other tax amount printed on the invoice...)` and `+ "status": "ok" if lines_total + tax == total`: VAT becomes a separate field, and code checks the arithmetic between net, VAT and total. |
| C4 | held | not touched |
| C5 | held | `- lines_total == total` became `+ lines_total + tax == total`: the comparison is still exact to the cent, with no tolerance. |
| C6 | held | not touched |
| C7 | held | not touched |
| B1 | held | not touched |

## Trial

- where: both
- flagged: no
- stopped: no