Ho tolto la regola invece di aggiungerne un'altra. Quando l'utente adatta l'allenamento di oggi, i gruppi muscolari del giorno della rotazione non vincolano più il piano: sono un punto di partenza, e quello che l'utente dice viene prima. Ho verificato tutto solo con test locali; non ho lanciato nessuna chiamata a pagamento.

**Il vicolo cieco.** Un adattamento si costruiva sui gruppi dello slot del giorno (es. gambe + core). Quei gruppi decidevano quali esercizi erano ammessi e imponevano almeno un esercizio per ciascuno. Con «oggi faccio il core ma niente gambe» nessun piano poteva passare: senza gambe veniva rifiutato. E non c'era un'altra strada, perché i gruppi non si potevano nominare.

**Cosa cambia**
- **Codice** (`src/trainer/plan.py`): un adattamento non porta più gruppi né la divisione dei minuti tra i gruppi. Lo slot resta solo per sapere da quale allenamento si parte e quale conta come fatto nel ciclo, quindi il ciclo dopo resta giusto. I suoi gruppi passano nel nuovo campo `Adapting.groups`. Di conseguenza non scattano più né il filtro per gruppi né il controllo che ogni gruppo sia allenato.
- **Istruzioni al planner** (`src/trainer/coach/planner.py`): «Workout N usually trains …» seguito da «What they said comes first: train the groups their words ask for…».
- **Rimosso:** il suggerimento «give its number as `workout`», che dopo la modifica non poteva più scattare. Il CLI ora stampa i gruppi dello slot.

**Cosa non si muove:** esclusioni, attrezzatura, tempo (±5 minuti), insieme degli esercizi ammessi, esercizi chiesti ed esercizi lasciati fuori. Un esercizio chiesto ma sotto esclusione resta rifiutato: la volontà dell'utente non scavalca la sicurezza.

**Righe della charter spostate** (`evals/planner/charter.md`), su tue parole:
- **Free**, riga nuova: quali gruppi allena un adattamento spetta al modello, con la motivazione che hai dato.
- **Constrained**, due righe ristrette: i gruppi non entrano più nella richiesta di un adattamento, e la regola `untrained` non si applica agli adattamenti.

**Test** (solo locali): 1851 passano, 3 falliscono, mypy pulito.
- Ho aggiunto due test, uno con un piano di solo plank e uno con «core ma niente gambe» passato per l'entrance; prima della modifica sarebbero stati rifiutati.
- Ho riscritto tre test che fissavano il vecchio comportamento: le trazioni nel giorno gambe adesso partono invece di essere rifiutate.
- I 3 test di `tests/test_bot.py` che falliscono riguardano le esclusioni proposte dal logger, non questa modifica. `tests/test_logger.py:559` ha come data di re-test `2026-10-15`, che ormai è passata. Non li ho toccati.

**Da fare**
- Ho aggiornato il ticket 04: la riga 8 (trazioni) non ha più bisogno di `workout`.
- La cartella non è un repository git, quindi non c'è nessun commit.
- Vale la pena aggiungere «oggi faccio il core ma niente gambe» come riga di `docs/adapting/eval-set.toml` e misurarla con `trainer eval --suite adapt`. È a pagamento, quindi prima ci accordiamo su un budget per il ticket.