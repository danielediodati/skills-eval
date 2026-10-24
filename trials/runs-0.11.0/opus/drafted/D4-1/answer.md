# Ticket 15c.1: costruito in parte, poi fermo su una linea del charter

Il ticket non è chiuso. Ho fatto la parte che non tocca il charter dell'entrance. Le risposte *«ok»* e *«no»* sono ferme finché non decidi tu.

## Cosa funziona ora (provato con modelli scriptati)
- **Nuovo ending `superseded`.** Una proposta lasciata senza risposta viene registrata come `superseded`, non più `cut`. Succede in due casi: arriva una nuova richiesta sopra di lei, oppure arriva il report dell'allenamento che adattava. Nel primo caso la nuova richiesta resta nella stessa negoziazione e segue la precedente. Ho aggiornato CONTEXT.md (Ending) e aggiunto un emendamento ad ADR-0007.
- **Il report chiude l'adattamento aperto.** Dopo il report, un tap su *Va bene* non scrive nulla e la chat risponde con la Situation `SUPERSEDED` già esistente.
- ***Solo 30 minuti* tolto.** Ogni piano ha solo *Va bene* e *Non mi va*. Ho corretto la frase sui bottoni nel README.
- **Corretto un bug nel lettore dei run, `runs.negotiations`.** In produzione tutti i grafi usano un solo checkpointer. Lì il thread dell'entrance copriva il run del planner, quindi anche una proposta semplicemente in attesa risultava `cut`. È questa la causa del `cut` visto in 15b.3, più che `Negotiation.open`.

Test: 1909 in totale, 1906 verdi. Gli altri 3 (`test_bot`, i bottoni dell'exclusion) falliscono uguali anche senza le mie modifiche e non li ho indagati. mypy è pulito. Ho tolto due test sul bottone dei 30 minuti e ne ho aggiunti due nuovi: uno sul report che chiude l'adattamento, l'altro su una nuova richiesta sopra una proposta aperta, che finisce `superseded` e non lascia nessun `cut`.

## Dove mi sono fermato
Per le righe *«ok»* → accettato e *«no»* → rifiutato servono due nuovi handoff dell'entrance, che chiamano `Negotiation.answer`. Il charter dice:

> *The handoff set is closed, seven tools in `HANDOFFS`*

- **Cosa compra spostarla:** l'utente risponde a un piano scrivendo, e il modello decide se il messaggio è un sì o un no. Oggi accettare un piano, cioè scrivere un allenamento o un mesociclo, lo decide solo il tap dell'utente. Il modello avrebbe una decisione nuova.
- **Perché chiedo:** il ticket lo chiede, ma il ticket non conta come tua richiesta di spostare la linea. Senza spostarla, queste due righe non si possono fare.

**Vuoi spostarla?** Se sì, aggiungo i due handoff, avviso l'entrance della proposta aperta e aggiorno la linea del charter con il motivo che mi dai. Poi aggiungo le righe all'eval set e lancio le verifiche gratuite. Solo dopo ti chiedo il budget per il passaggio a pagamento di `trainer eval --suite adapt`, con la stima del costo.

## Da sapere
- La cartella non è un repository git: non ho potuto verificare `c2e8e2a` e non ho fatto commit. Le modifiche sono solo nei file.
- Quando un tap arriva su un adattamento chiuso dal report, `SUPERSEDED` dice che scrivendo di nuovo se ne ottiene un altro. In quel caso non è del tutto esatto: si può fare meglio con una Situation dedicata.
- Ho annotato lo stato e il punto bloccato nel file del ticket.