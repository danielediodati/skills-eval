OpenRouter è ora il terzo provider: `LLM_BACKEND=openrouter`, oppure `ENTRANCE_BACKEND=openrouter` per la sola entrance. Non l'ho mai provato contro OpenRouter vero: nessuna chiamata a pagamento è partita, e nemmeno il controllo da CLI senza chiave (vedi sotto).

**Test:**
- I 46 test di `tests/test_models.py` passano, 14 dei quali nuovi per OpenRouter.
- mypy è pulito (85 file).
- La suite completa dà 1576 passati e 3 falliti, tutti in `tests/test_bot.py`, e non dipendono da questa modifica. La fixture `proposing` in `tests/test_logger.py:519` propone un'esclusione con `retest_date` fissa al 2026-10-15. Oggi è il 2026-10-23, e `log.py:732` rifiuta una data di retest che non sia dopo oggi. Non l'ho toccata.

**Come funziona:**
- **Variabili:** `OPENROUTER_API_KEY`, `OPENROUTER_MODEL` e `OPENROUTER_MAX_TOKENS`. Senza `OPENROUTER_MAX_TOKENS` vale il limite del modello.
- **Modello di default:** è lo stesso di Groq, `qwen/qwen3.8-27b`. Così cambiare provider lascia fermo il modello e un confronto cambia una cosa sola.
- **Costruzione:** passa da `langchain-openai` con `base_url` impostato su OpenRouter; l'ho aggiunta alle dipendenze.
- **Controllo prima del run:** senza chiave si ferma con lo stato e la correzione. Se OpenRouter non serve il modello, l'errore nomina la variabile da cambiare. Se il modello non ha nessun provider con `structured_outputs` e `tools`, viene rifiutato.
- **Crediti finiti:** un 402 diventa `QuotaSpent`, quindi il planner si ferma subito invece di riprovare.

**Charter:** non ho spostato nessuna linea. Il provider resta configurazione (charter del planner, ADR-0004 item 8). C'era però un rischio da evitare: `ChatOpenAI` manda `strict: false` per gli schemi dict, e così sarebbe saltata in silenzio la decodifica vincolata. Entrambi i charter la mettono tra le cose vincolate, perché è quella che tiene gli id degli esercizi dentro l'enum. Ho fatto due cose:
- l'output strutturato su OpenRouter è sempre `strict`;
- le richieste partono con `provider.require_parameters: true`, così OpenRouter manda la richiesta solo ai provider che rispettano `response_format`.

**Documenti aggiornati:** `.env.example`, la tabella dei provider nel README e il testo di ADR-0004 item 8, che diceva «`ollama` o `groq`».

**Cosa manca:**
- **Controllo da CLI:** volevo lanciare `LLM_BACKEND=openrouter uv run trainer plan` senza chiave, per vedere il messaggio di stato senza rete. Il permesso è stato negato, quindi quel percorso è verificato solo dai test.
- **Prova vera:** serve un run a pagamento, che non parte senza tuo via libera e un budget concordato.
- **Commit:** la cartella non è un repository git.
- **Modelli per nodo:** `PLANNER_MODEL` e `LOGGER_MODEL`, suggeriti nella ricerca, non li ho fatti perché non li avevi chiesti. Ora planner e logger usano lo stesso `OPENROUTER_MODEL`.