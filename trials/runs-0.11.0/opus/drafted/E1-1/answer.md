# Ticket 10.3: aperto, la parte chat è bloccata sulla charter dell'entrance

Ho costruito il lato CLI e il motore. La parte chat, cioè tutti e tre i criteri di accettazione, non si può fare senza spostare una linea della charter dell'entrance. Mi sono fermato lì, come chiede CLAUDE.md.

**Niente di questo è stato eseguito.** Né pytest né mypy sono partiti: il comando è stato negato, perché questa sessione non può chiedere permessi. Il codice e i test sono scritti e controllati solo a lettura. Non ho nemmeno un numero di test di partenza da riportare. In più la cartella non è un repository git, quindi niente commit.

## Cosa è stato costruito
- **Adattamento**: `trainer plan` con un'opzione che modifica l'allenamento (`--time`, `--equipment`, `--exclude`, `--avoid`) e un mesociclo in corso parte dallo slot di oggi come punto di partenza. Una volta accettato, l'allenamento diventa quello servito per quello slot nella tabella `served`. Se lo slot non adattato era già stato prescritto e non ancora eseguito, viene ritirato. Il mesociclo resta com'era.
- **Cambio**: `trainer plan --change` pianifica un nuovo mesociclo partendo da quello attivo. Accettato, lo sostituisce, mantiene il conteggio dei cicli già fatti e ritira lo slot di oggi del vecchio mesociclo, se non è stato eseguito.
- **Correzione emersa strada facendo**: chiedendo di nuovo l'allenamento di oggi, `record_served` mostrava i blocchi dello slot originale anche quando quello prescritto era l'adattamento. Ora rilegge quello prescritto.
- Ho aggiunto 6 test del motore, 4 del planner e 4 della CLI. Il rifiuto ("Non mi va") resta una negoziazione: la proposta successiva deve essere diversa, e il punto di partenza sopravvive al rifiuto.

## La linea da decidere
Nella charter dell'entrance, sotto *Constrained*: **"Handoffs take no arguments: what is due, what is planned against, and what the logger reads are derived by code; the model never retells the user's words."**

Perché *"solo 30 minuti oggi"* diventi `minutes=30`, e *"basta affondi"* un'esclusione, qualcuno deve leggere le parole prima che parta il planner. Il codice non può farlo senza regole a parole chiave, che il ticket vieta. Il modello non può farlo senza spostare quella linea.

- **Opzione A (la consiglio)**: due nuovi handoff, `adapt_today` e `change_mesocycle`, con argomenti strutturati (minuti, attrezzatura, esclusioni, preferenze). Il codice li passa per `plans.requested` e li verifica sul vocabolario del catalogo, come fa già con i flag della CLI. Così il validatore continua a controllare minuti ed esclusioni, e la charter del planner non cambia. Si sposta solo quella linea dell'entrance.
- **Opzione B (sconsigliata)**: le parole arrivano così come scritte al planner, che interpreta da solo il vincolo. Sposterebbe due linee del planner: la richiesta assemblata dal codice prima del modello, e i minuti e le esclusioni verificati dal validatore. In pratica i 30 minuti non sarebbero più controllati.

**Vuoi spostare quella linea con l'opzione A?** Se sì, scrivimelo con le tue parole e aggiorno la charter insieme al codice.

Il ticket ora ha due sezioni nuove, *Built, not yet run* e *Blocked on the entrance charter*. Non ho toccato le charter, la ROADMAP e il README.

C'è anche una scelta di progetto che ho fatto io, da confermare. Nel cambio, i `cycles` scelti dall'agente contano dall'inizio del mesociclo originale, cicli già fatti compresi. Il numero resta una sua scelta, come dice la charter. Se però sceglie un numero non superiore ai cicli già fatti, il mesociclo nuovo nasce già finito. Ricade nello stato "nessun mesociclo", che è sicuro, ma non è un bel risultato.