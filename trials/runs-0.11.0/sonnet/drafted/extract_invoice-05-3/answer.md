Invoices whose figures are consistent once VAT is counted now get `ok` and go to the ledger. The 18 local unit tests pass, but I haven't run the real model on any invoice.

**Cause.** The tool compared the net line sum (309.00) with the amount due (370.80), which includes VAT. Any invoice with VAT therefore came out as a mismatch.

**Fix.** The model is now also asked for the VAT on the invoice, summed over all rates. The status is `ok` only when lines plus VAT equal the amount due, exactly to the cent. For Brightwell BP-2291 that is 309.00 + 61.80 = 370.80, so it passes. A wrong quantity or a mistyped total still gives `mismatch`. An invoice with no VAT behaves as before.

**Charter line that moved.** In `evals/extract_invoice/charter.md`, the Constrained line on status used to say `ok` only if lines_total equals total. It now says lines_total plus tax equals total, still exact and still decided in code. I recorded your reason on that line. I also added a Free line saying the model reads the VAT figure from the invoice, and it counts as zero if the model gives none. I updated the README and added tests for the VAT cases.

**Things to know:**
- If the model misses the VAT on an invoice that has it, that invoice goes to a clerk. It is never wrongly passed through.
- I did not change the output keys, because the charter fixes them for the ledger loader. The result still shows `lines_total` as 309.00 and `total` as 370.80 with no VAT figure, so a clerk looking at a genuine mismatch can't see the VAT the tool used. Adding a `tax` key would fix that, but it changes what the loader receives. Do you want it?
- To check that the model reads VAT reliably on your real invoices, we would need a paid eval run. I haven't started one. Before any run, we'd need to agree a budget.