Il ticket 15c.1 non è chiuso. Ho fatto la parte che non tocca le regole del modello. Le risposte scritte *«ok»* e *«no»* non funzionano ancora: per farle funzionare va spostata una linea della charter dell'entrance, e serve il tuo via.

## Cosa funziona ora

L'ho verificato con modelli finti (nessun modello a pagamento): ogni caso ha un test che passa.

| Tu scrivi, con un piano aperto | Cosa succede |
|---|---|
| una domanda (*«che vuol dire superset?»*) | l'entrance sa che c'è un piano in attesa, risponde e il piano resta aperto |
| una nuova richiesta (*«ho 20 minuti»*) | il piano aperto si chiude come `stopped` e viene salvato. Il nuovo piano lo segue nella stessa negoziazione. Un tap sul vecchio piano non scrive niente e la chat dice che è stato superato |
| il resoconto dell'allenamento che l'adattamento adattava | il resoconto viene scritto e l'adattamento si chiude come `stopped`. Un tap dopo non cambia niente e la chat dice che quell'allenamento è già registrato (nuova situazione `OVERTAKEN`) |

- **Fine di una proposta senza risposta:** ho riusato `stopped` invece di aggiungere un settimo tipo di fine. Così nessuna proposta risulta più *cut*. L'ho scritto in CONTEXT.md (Ending) e in ADR-0007 al punto 7.
- **Pulsante tolto:** *Solo 30 minuti* non c'è più, ora ogni piano ha solo *Va bene* e *Non mi va*.
- **README:** ho aggiunto alla tabella le due righe vere oggi. Non ho scritto che *«ok»* accetta un piano.
- **Mesociclo aperto:** un resoconto non chiude un cambio di mesociclo in attesa. Si chiudono solo gli adattamenti.

**Stato:** mypy pulito. Test: 1911 passati, 3 falliti. I 3 fallivano già prima delle mie modifiche (vedi sotto).

## Dove mi sono fermato: *«ok»* e *«no»* scritti

Per accettare o rifiutare un piano scrivendo, l'entrance ha bisogno di due chiamate nuove. Nella charter (`evals/entrance/charter.md`) toccano due linee:

- **Constrained**, *"The closed tool surface: the seven HANDOFFS…"*: diventerebbero nove.
- **Free**, *"Which handoff a message gets…"*: l'elenco guadagnerebbe "accetta" e "rifiuta".

Il ticket lo chiede, ma per la regola della charter un ticket scritto da un agente non basta: lo spostamento lo devi nominare tu.

**Cosa propongo:** `accept_plan()` e `turn_down_plan()`, senza argomenti.
- Il motivo del rifiuto arriva al planner come testo tuo, parola per parola, come fa già `log_workout`.
- Così la linea *"Handoffs take no arguments"* resta dov'è.
- Entrambe passano da `Negotiation.answer`, come un tap.
- Cosa compra: le prime due righe della tabella del ticket, e lo spot della demo in cui il piano si accetta scrivendo.

Se mi dici di sì:
1. Aggiungo le due chiamate e aggiorno la charter con il motivo che mi dai.
2. Aggiungo all'eval-set dell'adattamento le righe con un piano aperto. Il banco di prova oggi non sa preparare un piano aperto, quindi va esteso.
3. Ti porto una stima di costo per `trainer eval --suite adapt` e fissiamo un budget per tutto il ticket. Non lancio niente a pagamento prima del tuo ok.

Una domanda più piccola: la nuova situazione `OVERTAKEN` non è nell'elenco "Input" della charter. Non l'ho aggiunta io perché la regola dice di cambiare la charter solo per uno spostamento che nomini tu. Vuoi che la aggiunga insieme alle due chiamate?

## Altre cose da sapere

- **I 3 test che falliscono:** sono i test sull'esclusione proposta in `tests/test_bot.py`. La loro data di riprova è fissa al 2026-10-15 (`tests/test_logger.py:559`), ormai passata, e `log.py:763` rifiuta le date non future. Il problema è il test che scade con il calendario, non questo ticket, e non li ho toccati.
- **Niente commit:** la directory non è un repository git, quindi non ho committato. Non ho fatto nemmeno i passi di chiusura (`/code-review`, ROADMAP, cancellazione del ticket): li faccio quando il ticket sarà davvero finito.
- **Vecchi pulsanti già in chat:** un *Solo 30 minuti* inviato prima di questa modifica ora viene ignorato in silenzio, senza messaggio.
- **Due comandi bloccati:** due comandi shell sono stati rifiutati per mancanza di permessi. Ho fatto le stesse modifiche con l'editor, quindi non manca niente.