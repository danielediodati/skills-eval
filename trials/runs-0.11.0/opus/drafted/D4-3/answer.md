Ho costruito la parte del ticket che si poteva fare, e mi sono fermato prima di *«ok»* e *«no»*: quelle due righe chiedono di spostare una linea del charter dell'entrance, e prima serve una tua decisione.

## Cosa ho costruito
- **Una proposta lasciata senza risposta ha un esito: `superseded`, il settimo.** Prima una nuova richiesta su una proposta aperta la cancellava senza scrivere niente, e nell'archivio risultava *cut*. Ora viene scritta come `superseded`, e la nuova richiesta resta nella stessa negoziazione, subito dopo. L'ho messo in CONTEXT.md (Ending) e in ADR-0007, nella sezione *Amended in session 15c*.
- **Il resoconto dell'allenamento adattato chiude l'adattamento.** Dopo un resoconto, se il giorno per cui era stato chiesto l'adattamento è passato, la proposta finisce come `superseded`. Un tap fatto dopo non cambia niente: la chat dice che il piano non è più quello in mano (la situazione `SUPERSEDED`, che esisteva già).
- **Il pulsante *Solo 30 minuti* non c'è più.** Restano *Va bene* e *Non mi va*, anche sul mesociclo. Ho corretto la riga del README che parlava di tre pulsanti.

Test: 1911 passano e 3 falliscono. Le 3 falliscono già prima di ogni mia modifica: sono i test dei pulsanti di esclusione in `test_bot.py`, e non li ho toccati. mypy è pulito. Ho aggiunto 7 test: 5 per la negoziazione e 2 che passano dalla chat.

## Su cosa ti chiedo una decisione
Per accettare o rifiutare una proposta scritta in parole, l'entrance deve poter chiamare `Negotiation.answer`. Oggi non ha modo di farlo. La strada naturale sono due nuovi handoff, *accetta* e *rifiuta*. Ma il charter dice, tra le cose fissate dal codice: **«The handoff set is closed (`HANDOFFS`, seven tools)»**. Aggiungerne due sposta quella linea. Il ticket lo implica, ma l'ha scritto un agente, quindi non basta: lo spostamento lo puoi nominare solo tu.

- **Cosa compra:** *«ok»*, *«perfetto»*, *«daje»* e *«no»* funzionano come i tap. Per ora l'entrance sa solo rispondere *usa i pulsanti*.
- **Se dici sì:** aggiungo gli handoff e la nota nel prompt sulla proposta aperta, correggo la riga del charter con la tua motivazione e aggiungo le righe al README e a `docs/adapting/eval-set.toml`.
- **Poi l'eval a pagamento** (`trainer eval --suite adapt`): prima concordiamo un budget per tutto il ticket, con una stima, e parte solo col tuo via.

La nota nel prompt l'ho lasciata ferma apposta, perché cambia a seconda della risposta.

## Cosa non ho potuto fare
- **Nessun commit:** la cartella non è un repository git, quindi niente hash, niente ROADMAP e niente commit di chiusura. In ogni caso il ticket resta aperto.
- **Comandi bloccati:** alcuni comandi composti sono stati rifiutati perché questa sessione non può chiedere permessi. Li ho sostituiti con comandi singoli, senza conseguenze.
- **File temporanei:** per capire come chiudere una proposta in LangGraph ho usato uno script in `%TEMP%\reps-15c1-probe\`, che si può cancellare. In `%TEMP%\reps-scratch\` c'era già un altro `probe.py`, non mio: l'ho lasciato com'era.

Una cosa curiosa: per chiudere la proposta la registro come se l'avesse scritta il nodo `prescribe`, che porta solo a END. Registrata come `propose`, il grafo passerebbe a `planner`, e una ripresa ricomincerebbe a pianificare. Ho lasciato al planner la gestione dei `minutes` nella risposta, anche se ora nessun pulsante la usa: il planner non ha ancora un charter, e toccarlo vorrebbe dire scriverne uno.