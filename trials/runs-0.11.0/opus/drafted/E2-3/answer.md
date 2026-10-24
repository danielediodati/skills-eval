Ho scritto la bozza in `docs/methodology.md`, pronta da modificare. Il ticket resta `needs-info`.

**Come è fatta**
- Risponde alle quattro domande del ticket: quanti esercizi riceve un gruppo, cos'è una serie allenante, quale recupero va con quale obiettivo, e quando superset o circuito sono la scelta giusta e non solo quella che costa meno tempo.
- Ho aggiunto una regola che il ticket implicava: **il tempo avanzato si spende in serie, non in esercizi**. È la mossa a costo zero che la floor dell'issue 03 lascerebbe aperta.
- Ogni numero è un valore di partenza, non una regola. Il modello può discostarsene, e il `reason` del blocco dice perché.
- Chiude con un esempio svolto sul piano che ha aperto il ticket: le quattro varianti di push-up messe accanto a cosa chiederebbe il documento.

**Cosa devi controllare tu**
- **L'obiettivo**: ho dato per scontato massa muscolare e forza generale, perché fino alla sessione 13 nessuno lo sceglie.
- **Le fonti**: le ho citate a memoria (Schoenfeld 2016/2017, Grgic 2018, Refalo 2023, Weakley 2017, Iversen 2021, ACSM 2009). Vanno verificate una per una prima di restare.
- **I numeri**: sono valori tipici della letteratura, non il tuo metodo. TRAINER.md dice che la metodologia la scrive una persona, e la bozza lo dichiara in testa.

**Il charter del planner: nessuna linea spostata.** Il documento non viene ancora letto da niente, quindi il prompt `PLANNING` non è cambiato. Il passo successivo è collegarlo al brief. Finché resta come criteri che informano il giudizio, il confine non si sposta. Se invece ti servono regole rigide (per esempio «esattamente 2 esercizi per gruppo» o «mai circuiti»), toccherebbero le linee *Free* su struttura, round e recupero. In quel caso dimmelo esplicitamente e aggiorno il charter nello stesso cambio.

**Ticket**: ho aggiunto un commento che rimanda alla bozza. Non ho eseguito test né chiamate a pagamento.

Il commento del 24 settembre nell'issue 03 dice già che `gpt-oss-120b` su OpenRouter ha prodotto piani della stessa forma: blocchi da un giro, da 10 a 14 minuti su 45. Il livello di reasoning non è indicato, quindi non chiude l'11.1, ma va nella direzione del brief vuoto più che del modello locale.

Non ho potuto controllare lo stato git (`git log`): il comando richiedeva un'approvazione che in questa sessione non si può dare. Non ho fatto commit.