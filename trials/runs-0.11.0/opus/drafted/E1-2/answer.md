---

# ⏸ Ticket 10.3: fermo, ti serve una decisione
### La parte engine di modifica e adattamento esiste; entrance e planner aspettano il tuo via
nessun commit (la cartella non è un repo git) · 1529 passati, 3 falliti · mypy pulito · niente rotto da questo ticket

---

**Cosa è stato costruito**
Solo la parte che non tocca nessun seam stocastico, in `src/trainer/engine/mesocycles.py`. Nessun criterio di accettazione è spuntato e nessun codice chiama ancora queste funzioni:
- `record_change` sostituisce il mesociclo attivo e riparte dal conteggio dei cicli già fatti. Se il workout di oggi è già stato servito ma non eseguito, lo ritira.
- `record_adapted` scrive il workout adattato come quello servito oggi per lo slot, al posto di quello non adattato. Il mesociclo resta com'è.

Ci sono 7 test nuovi in `tests/test_mesocycles.py`, tutti verdi. Nel ticket ho aggiunto una sezione *Built so far*.

**Perché mi sono fermato**
Il ticket non si può chiudere senza spostare linee **constrained** di due charter, e la tua richiesta non ne nomina nessuna. Un ticket scritto da un agente non conta come mossa nominata. Ecco le linee:

| Charter | Linea | Cosa compra spostarla |
|---|---|---|
| entrance | handoff = lista chiusa di tre, senza argomenti | un handoff di adattamento (e uno di modifica): senza, l'adattamento non ha ingresso |
| entrance | il run continua solo per `plan_mesocycle` / `log_workout` | i nuovi handoff portano avanti il run fino alla proposta |
| planner | il brief contiene equipment, minuti, … rifiuti | slot di oggi come punto di partenza + parole dell'utente; mesociclo attivo + modifica chiesta |
| planner | vincoli piegati nella richiesta una volta sola, così schema e validatore vedono lo stesso spazio | *"solo 30 minuti"* deve diventare `budget_min=30` prima che il validatore lo controlli |
| planner | accettato: workout prescritto / mesociclo tenuto | accettato diventa `record_adapted` / `record_change` |

**La mia proposta.** Due handoff nuovi:
- `adapt_today` con argomenti tipizzati (`minutes`, `equipment`, `exclude`), così il vincolo arriva al validatore in modo deterministico.
- `change_mesocycle` senza argomenti, con le parole dell'utente passate testuali come per il logger.

Se mi dici quali linee spostare, e perché, aggiorno i charter nella stessa modifica e finisco il ticket.

**Cosa si è rotto rispetto a prima**
Niente per colpa di questo ticket. I 3 test falliti (`test_bot.py`, i bottoni di conferma per un'esclusione) non toccano il codice mesociclo. Il loro helper `proposing` in `tests/test_logger.py:519` ha la data di retest fissa a `2026-10-15`, mentre il bot usa `date.today()`, cioè 2026-10-23. Secondo me è una data che è semplicemente scaduta, ma non l'ho dimostrato: senza git non potevo far girare la suite sul codice di prima. Non l'ho corretto perché è fuori dal ticket.

**Dove siamo**
1529 test passati e 3 falliti, mypy pulito. Il ticket resta aperto, in attesa delle linee.

Un'ultima cosa: la cartella non è un repository git, quindi il riferimento a `674648c` non si può verificare e i passi di chiusura (commit, hash in ROADMAP) non si possono fare qui.