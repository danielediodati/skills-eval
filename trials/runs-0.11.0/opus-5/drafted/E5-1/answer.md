Ticket scritto: `docs/work/09-the-report-in-the-chat/issues/06-the-contract-not-the-reading.md`.

## Cosa dice

Le quattro cause del passaggio, verificate nel codice una per una, e tre di esse sono sistemabili senza toccare nulla di discutibile:

1. **Lo scorer confronta il documento emesso**, mentre `_produced`, due righe sotto, costa il volume su `log.to_performed`. Stessa run, due oggetti diversi, e quello usato per il documento non è quello che finisce in SQLite. Si risolvono entrambi i lati attraverso `to_performed`; `workout_id`, `report` e `proposed_exclusion` restano sul documento emesso perché non sopravvivono alla risoluzione — e `report` parola per parola è l'unica cosa nella suite che misura le parole dell'utente.
2. **Il prompt vieta `assumed`, la forma obbliga a scrivere un valore e il set lo vuole `assumed`.** U2 si aspetta `"amount": 10, "amount_source": "assumed"`, e `log.validate` lo accetta già: rifiuta solo la contraddizione. Il prompt è l'unico file che dissente, e dissente con sé stesso — riga 128 contro riga 133. Si cancella la riga 128.
3. **Il vocabolario delle esclusioni non è nel contesto.** `classify` risolve contro dodici pattern e sette articolazioni lette dai dati; il modello ne vede due, come esempi. Un valore fuori vocabolario torna come `LogRejected`, cioè come rifiuto: è l'unica leva sui rifiuti disponibile senza spostare una linea del charter.

## Cosa ho lasciato dov'era

**Il rifiuto che chiude la run.** Il charter lo dice a parole fra i vincoli — *«A refusal ends the run. There is no repair turn»* — e la richiesta non nomina quello spostamento, quindi resta. Costa 4 run su 54; la causa 3 toglie uno dei due modi in cui un documento si guadagna un rifiuto, e il re-run dirà quanto resta. Nessuna riga del charter è toccata dal ticket: le cause 1 e 3 sono codice, la 2 riporta il prompt a quello che charter e validator già dicono.

**Il set resta intatto.** Scritto alla cieca; una riga difficile è un risultato, non una riga da ammorbidire.

## Una cosa su cui puoi dirmi che sbaglio

Il set dice che *un documento che riscrive le parti invariate è sbagliato*. Punteggiando sul documento risolto, smette di pagarlo. Nel ticket ho scelto di **riportarlo senza addebitarlo** — una nota sulla riga, e la run tiene — perché ciò che arriva all'utente è identico nei due casi. Se preferisci che resti un fallimento, è un solo ramo nello scorer.

Il re-run è locale e gratuito su `gpt-oss:20b`. Su Groq servirebbe concordare prima un budget, e il ticket lo scrive.

Il ticket 05 resta aperto e si chiude su questo re-run; fonderli in uno solo è una tua decisione.