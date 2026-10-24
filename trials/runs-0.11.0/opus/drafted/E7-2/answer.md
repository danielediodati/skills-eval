Ho aggiunto OpenRouter come terzo provider, accanto a Ollama e Groq. L'ho provato solo in locale: nessuna chiamata a pagamento, nessuna rete. Quindi non so ancora se una pianificazione vera su OpenRouter va a buon fine.

**Come si usa:**

| Variabile | Effetto |
|---|---|
| `LLM_BACKEND=openrouter` | planner e logger passano da OpenRouter |
| `ENTRANCE_BACKEND=openrouter` | anche l'entrance (vale anche da sola) |
| `OPENROUTER_API_KEY` | obbligatoria |
| `OPENROUTER_MODEL` | se vuota usa `qwen/qwen3.8-27b`, lo stesso di Groq: così cambia solo il provider |

**Cosa ho cambiato**
- **Codice:** tutto il lavoro sta in `src/trainer/coach/models.py`, come prevedeva `docs/research/paid-llm-provider.md`. È servita una nuova dipendenza, `langchain-openai`, che passa dall'endpoint di OpenRouter compatibile con OpenAI.
- **Output strutturato strict:** `ChatOpenAI` di suo manda lo schema con `strict: false`, e così l'enum degli esercizi ammessi diventerebbe solo un suggerimento. La classe `StrictOpenRouter` lo forza a strict. In più ogni richiesta porta `require_parameters: true`, così OpenRouter la manda solo a provider che rispettano davvero schema e ragionamento.
- **Ragionamento:** planner e logger ragionano a `low` (`REASONING`), l'entrance non ragiona, come già succede su Ollama.
- **Controlli prima della run:** `ready()` controlla che ci sia la chiave, che OpenRouter elenchi il modello e che almeno un suo provider supporti quello che serve (`structured_outputs`, `reasoning`, `tools`). Se manca qualcosa lo segnala come stato, indicando la variabile da cambiare.
- **Quota finita:** credito esaurito (402) e limite giornaliero dei modelli gratuiti diventano `QuotaSpent`, quindi la run si ferma subito invece di ritentare.
- **Documenti:** ho aggiornato `.env.example` e la tabella dei provider nel README.

**Charter:** non ho spostato nessuna linea. Il charter del planner richiede schema strict e `REASONING = "low"` su ogni modello che pianifica, e il codice li fa valere anche su OpenRouter.

**Verifiche**
- I test dei modelli passano tutti, 47 (16 sono nuovi).
- mypy è pulito.
- Con la chiave, il modello costruito ha questo body di richiesta: `{'provider': {'require_parameters': True}, 'reasoning': {'effort': 'low'}}`. Senza chiave si ferma con `no OpenRouter credentials: set OPENROUTER_API_KEY in .env ...`.
- La suite completa dà 1577 passati e **3 falliti**, tutti in `test_bot.py` sulle esclusioni. Non dipendono da questa modifica: `proposing()` in `tests/test_logger.py:519` ha la data `retest="2026-10-15"` scritta a mano, oggi è già passata e il validator la rifiuta. Non l'ho toccata perché è fuori da questa richiesta; si sistema con una data relativa a oggi.

**Da sapere**
- Non so ancora se un provider di `qwen/qwen3.8-27b` su OpenRouter supporta insieme `structured_outputs` e `reasoning`. Se nessuno lo fa, `ready()` lo dirà al primo avvio di `trainer bot`. Il modo più economico per scoprirlo è la lista dei modelli, che è gratuita; una run di `trainer plan` invece costa e richiede un budget concordato prima.
- La cartella non è un repository git, quindi non ho fatto commit.
- Alcuni comandi di sola lettura sono stati bloccati dai permessi, ma ho letto gli stessi file con gli altri strumenti, quindi non manca nulla.