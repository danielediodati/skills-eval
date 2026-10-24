Ho tolto una regola, non ne ho aggiunte: quando adatta l'allenamento di oggi, il planner non è più vincolato ai gruppi muscolari previsti dallo slot del mesociclo. Così *«oggi faccio il core ma niente gambe»* nel giorno gambe ora ha un piano valido (prima veniva respinto perché le gambe restavano scoperte).

**Linea del charter spostata** (`evals/planner/charter.md`), come hai chiesto:
- **Ora libero:** in un adattamento i gruppi da allenare li decide il modello, e conta prima quello che l'utente ha detto. I gruppi dello slot arrivano al modello solo come punto di partenza.
- **Vincolato, ma non si applica più agli adattamenti:** il controllo "ogni gruppo richiesto riceve un esercizio" resta per gli allenamenti normali e per i mesocicli.

**Cosa resta vincolato dal codice:** esclusioni, attrezzatura di oggi, minuti ±5, nessun esercizio ripetuto, esercizi richiesti ed esclusi, il formato del piano. Una richiesta su un pattern escluso viene ancora respinta, con la data del re-test.

**Cosa cambia in pratica:**
- In un adattamento il codice non passa più nessun gruppo né ripartizione dei minuti, quindi il set di esercizi ammessi non è più ristretto ai gruppi dello slot.
- Il brief dice al modello: «What they asked for comes first, the groups this workout trains included: the slot is where you start, not a limit», e riporta i gruppi dello slot come informazione.
- La riga 8 del set (trazioni nel giorno gambe) ora parte direttamente invece di essere rimandata con `workout`.
- L'aggiustamento in `_admits` che suggeriva un altro allenamento del ciclo non poteva più scattare, quindi l'ho rimosso.

**Verifica:**
- mypy è pulito.
- Ho aggiornato i test che fissavano il vecchio comportamento e ne ho aggiunto uno per il piano solo core nel giorno gambe.
- Falliscono 3 test in `tests/test_bot.py` (conferma dell'esclusione). Non c'entrano con questa modifica: `proposing` in `tests/test_logger.py:559` usa come data di re-test predefinita `2026-10-15`, che ormai è passata. Non li ho toccati.
- Non sono riuscito a leggere il conteggio totale dei test dall'output, quindi non te lo do.
- Non ho lanciato niente a pagamento. Il set `adapt` andrà rilanciato per misurare l'effetto, e prima ti chiederò un budget.

**Da decidere sul ticket 04:** `workout` ora dice solo quale slot del ciclo questo allenamento conta come fatto. Se l'entrance non lo passa su *«niente gambe»*, il piano rispetta le parole ma viene segnato come fatto lo slot gambe, e la rotazione salta le gambe per questo ciclo. Questo tocca la demo («il ciclo dopo è ancora giusto»). È una scelta dell'entrance, non del planner: l'ho annotata nel ticket 04 e non l'ho cambiata.