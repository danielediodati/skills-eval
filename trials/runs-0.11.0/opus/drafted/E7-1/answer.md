Ho aggiunto OpenRouter come terzo provider (`LLM_BACKEND=openrouter`), ma non l'ho ancora provato contro il servizio vero: quella è una chiamata a pagamento, e serve prima il tuo via libera e un budget.

**Come funziona**
- Il backend usa il pacchetto dedicato `langchain-openrouter` 0.2.9, con `OPENROUTER_API_KEY` e `OPENROUTER_MODEL`.
- Il modello predefinito è `qwen/qwen3.8-27b`, lo stesso di Groq, così il primo confronto tiene fermo il modello.
- Anche l'entrance può girarci, con `ENTRANCE_BACKEND=openrouter`.
- Prima del run il programma controlla tre cose: che la chiave ci sia, che OpenRouter elenchi il modello, e che il modello supporti `tools` (e anche `structured_outputs` per i modelli che pianificano). Se una manca, si ferma e dice cosa sistemare.
- Se i crediti finiscono (errore 402), il run si ferma subito invece di riprovare. È lo stesso trattamento della quota giornaliera di Groq.
- Ho aggiornato `.env.example`, che diceva ancora "Not read yet", e il README (intro, tabella dei provider, entrance).

**Charter**: nessuna linea è stata spostata. Il charter del planner vincola l'output strutturato strict. Su OpenRouter questo non sarebbe garantito: il pacchetto non manda `strict`, e il router potrebbe passare la richiesta a un provider che ignora lo schema. In quel caso l'enum degli id ammissibili non vincolerebbe più nulla. Per tenere la linea in `models.py`:
- `StrictOpenRouter` mette `strict=True` sullo schema;
- `provider={"require_parameters": true}` fa usare solo i provider che rispettano tutti i parametri della richiesta.

Un test cattura la richiesta prima che esca e verifica entrambe le cose.

**Test**: 1577 passati, mypy pulito.

**Cose da sapere**
- **Tre test di `test_bot.py` fallivano anche senza questa modifica.** La fixture `proposing()` in `tests/test_logger.py` aveva la data di retest fissa al `2026-10-15`, ormai passata. Il bot usa la data vera e la validazione la rifiutava, giustamente. L'ho spostata al `2099-01-01`.
- **`uv add` ha abbassato pydantic da 2.13.5 a 2.12.5**, per i vincoli del pacchetto `openrouter`. La suite è verde lo stesso.
- **`REASONING = "low"` non si applica su OpenRouter**, come già succede su Groq. Il charter del planner dice che vale "su ogni modello che pianifica". Passarlo insieme a `require_parameters` escluderebbe i modelli che non ragionano. Non l'ho toccato: dimmi tu se vuoi metterlo.
- **Due comandi sono stati bloccati dai permessi della sessione.** Il primo era l'heredoc per aggiungere i test, che ho poi aggiunto con l'editor. Il secondo era il controllo a mano con le variabili d'ambiente (`LLM_BACKEND=openrouter uv run trainer plan`), che quindi non ho fatto. Lo stesso comportamento è coperto dai test.
- La cartella non è un repository git, quindi non c'è nessun commit.

Il passo successivo sarebbe un `trainer plan` vero su OpenRouter. Quanto vuoi spendere per provarlo?