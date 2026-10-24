Ticket proposto: `docs/work/09-the-report-in-the-chat/issues/06-the-contract-the-first-pass-found.md`, in stato `needs-triage`. Ho anche messo `05` come *Blocked by: 06*, perché la sua soglia non è raggiungibile prima.

**Cosa dice il ticket**

I quattro reperti del pass, e dove stanno:

| reperto | fix | dove |
|---|---|---|
| lo schema strict esige ogni campo, ma il prompt vieta `assumed` e il set lo aspetta | una sola regola nel prompt: il blocco si omette intero, dentro un blocco scritto il valore non dato è quello prescritto, `assumed` | `coach/logger.LOGGING` |
| lo scorer confronta la forma emessa, non il documento che il motore scriverebbe | confronto dei blocchi dopo `log.to_performed`, su entrambi i lati | `log_evaluation._difference` |
| il vocabolario delle esclusioni non è in contesto | pattern e giunti letti dal catalogo (`catalog.values`, `joint_values`), mai una lista copiata, nessun settimo tool | `coach/logger.LOGGING` |
| un rifiuto chiude il run | **non fatto**: è una riga vincolata del charter | `evals/logger/charter.md` |

Il prompt oggi si contraddice da solo: dice *"Never `assumed`"* e quattro righe dopo *"A number marked `assumed` has to be the prescribed one"*. Il codice e il set stanno col secondo (`_nothing_assumed_the_prescription_does_not_say` rifiuta solo l'`assumed` che la prescrizione contraddice), quindi allineare il prompt non muove niente: toglie una riga di prompt più severa del charter stesso.

Sul vocabolario ho verificato una cosa che rende il reperto più grave: `KEEPS` taglia `movement_pattern` e `loaded_joints` da *ogni* risultato di tool, `compare_variants` compreso. Gli unici due valori che il modello vede sono gli esempi `vertical push` e `shoulder` nel prompt, cioè le risposte di U14 e U13; `knee` e `lumbar spine` (U15, U16) non hanno esempio da copiare. Un modello che ripete l'esempio oggi vale quanto uno che legge la frase.

**Cosa non ho fatto, e perché**

Il turno di riparazione dopo un rifiuto sposterebbe la riga vincolata *"no repair turn ... the model is never shown the refusal to try again"*. Nessuna riga del charter è stata toccata, e il ticket non se ne autorizza nessuna: solo le tue parole nominano una mossa. In più la misura non la chiede: comprerebbe al massimo i 4 run su 54 che non sono arrivati a un documento valido, contro i 23 che vale il solo scorer.

**Tre decisioni che aspettano te**

1. Scorare la metà determinata sul documento risolto? È la soglia su cui poggia tutto: smette di misurare l'economia dell'emissione (un modello che riscrive tutta la prescrizione con `assumed` corretti passerebbe), tiene id, numeri e provenienze che vengono davvero scritti. Io direi sì.
2. La riga *libera* del charter *"Leaving a value out rather than filling it in"* non è ciò che la forma emessa permette: dentro un blocco non si può omettere nulla, si omette il blocco. Diventa *leaving the block out*? Serve una tua frase.
3. Il budget: il pass locale costa ore e zero euro, uno su Groq è la prima chiamata a pagamento del ticket.

Non ho toccato ROADMAP.md: session 9 avrebbe un sesto punto (il quarto è ritirato, quindi il conto resta cinque). Lo aggiungo io se mi dici sì.