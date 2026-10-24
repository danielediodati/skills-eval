Invoices whose figures include VAT now go straight to the ledger. Brightwell BP-2291 (309.00 + 61.80 = 370.80) comes out `ok`. All 19 unit tests pass, including new ones for this. I ran no paid model calls, so I haven't tried it on real invoices.

**The cause:** the tool added up the invoice lines, which are before VAT, and compared that to the amount due, which includes VAT. Any invoice with VAT therefore came out as a mismatch.

**The fix:**
- **VAT figure:** the model now also reads the VAT amount printed on the invoice. It sums them if there are several, and an invoice with none counts as 0.
- **The check:** an invoice is `ok` only if lines plus VAT equals the amount due, to the cent. It is still exact, with no tolerance, and the code still decides it, not the model.
- **Result:** each result now carries a `tax` field. I updated the README to match.

**Charter line that moved:** in `evals/extract_invoice/charter.md`, the Status line under Constrained changed from `lines_total == total` to `lines_total + tax == total`. I recorded your reason there and added `tax` to the output description.

**Still caught as mismatches:**
- A wrong quantity or a mistyped total, even when the invoice shows VAT.
- An invoice with VAT where the model leaves the VAT out. It goes to a clerk, which is the safe direction.

**Not checked:** the code does not test that the VAT is 20% of the lines. A wrong VAT figure that still adds up to the total would pass. Checking it would need a rate rule, which I left out because you didn't ask for it.