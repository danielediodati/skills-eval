Ho scritto il ticket: `docs/work/09-the-report-in-the-chat/issues/06-the-contract-not-the-reading.md`.

**La diagnosi in una riga**: i quattro guasti sono un contratto incoerente fra la forma, il prompt e lo scorer, e si tengono a coppie.

1. `strict_schema` rende obbligatorio ogni campo del blocco, quindi un numero che l'utente non ha dato **deve** essere copiato dalla prescrizione ed etichettato — esattamente ciò che la Free list del charter dice di lasciare fuori ("A value nobody gave is left out, never filled in"). Il codice qui è in debito verso il charter, non il contrario.
2. Il prompt si contraddice da solo: `logger.py:128` vieta `assumed`, `:133-136` lo chiama l'etichetta onesta. Il validatore e il set stanno con il secondo.
3. Il vocabolario delle esclusioni non è nel contesto, e `classify` vuole un valore del catalogo carattere per carattere (`lumbar spine`). Letto dal catalogo nel brief, mai una costante.
4. `_difference` confronta il documento **emesso**, mentre il volume accanto è già confrontato su quello **risolto** (`_produced`). Le trenta righe non cambiano: cambia quale documento si misura.

**Quello che ho lasciato deliberatamente fuori**, con il perché nella tabella finale del ticket:

- *un documento rifiutato chiude il run* (il planner ri-pianifica, questo no) è una riga `Constrained` del charter. Vale 4 run determinati su 54 — poco, contro il contratto — e si muove solo se lo nomini tu;
- *`assumed` non è mai del modello*: il codice lo ammette da sempre dove il piano tace (U6). Il ticket allinea il prompt al codice e **non** tocca il charter;
- la barra al 100% di `trainer eval`: con un 20b locale su un compito di lettura non è ciò che suggerisce il primo passaggio, ma non è una chiamata di questo ticket.

Lo stato è `needs-triage` e non `ready-for-agent`: i quattro item sono specificati, ma le tre righe sopra aspettano te e il passaggio va approvato con un budget prima della prima chiamata a pagamento.

Nota: il ticket mette i controlli gratuiti prima di qualsiasi provider — in particolare **la riscoratura dei record del primo passaggio** (contengono `performed` e `questions`), che riproduce il 7 → 30 su 50 senza spendere nulla. Non ho potuto verificare se quei record sono ancora in `TRAINER_HOME/eval-runs`: il comando che guardava quella directory richiedeva un'approvazione che qui nessuno può dare, quindi nel ticket il controllo è condizionato alla loro presenza.