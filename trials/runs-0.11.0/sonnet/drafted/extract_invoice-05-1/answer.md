Invoices whose lines plus VAT equal the amount due now come back `ok` and go to the ledger. BP-2291 is covered by a new unit test: lines 309.00 + VAT 61.80 = 370.80. I ran the unit tests and all 17 pass. I didn't make any paid model calls, so I haven't tried it against a real model.

**What changed**
- The model now also reports `tax`, the VAT or tax amount printed on the invoice. It reports 0 if the invoice shows none.
- Status is `ok` only when `lines_total + tax == total` exactly, with no tolerance. The code does the sum and doesn't derive or correct the tax.
- A wrong quantity or a mistyped total still lands in the review pile. The tests cover a total of 307.80 and a total of 309.00 (VAT left out) against 61.80 of VAT.
- `tax` is now a field in the result. Because the code rejects a missing number rather than defaulting it, an answer without `tax` is an `InvoiceError` ("tax is missing").
- I updated `seam.py`, `test.py`, `README.md` and the charter.

**Charter line that moved:** the Status line in `evals/extract_invoice/charter.md`. The old rule was `lines_total == total`. I recorded your reason there. I also added `tax` to the Output line, since it is now a returned field.

**Limitation:** the check trusts the tax figure the model reads. It doesn't test that the tax is 20% of the lines. A wrong total that the printed VAT happens to explain would pass, but that would mean the printed figures are consistent, which is what you asked for.