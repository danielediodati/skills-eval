Ho tolto una regola invece di aggiungerne un'altra. In un adattamento, il planner non è più obbligato ad allenare tutti i gruppi della giornata prevista: se l'utente dice «oggi faccio il core ma niente gambe», il piano può essere solo core.

**Dov'era il vicolo cieco.** Nella giornata gambe+core i gruppi li fissa il codice, e il validatore rifiutava ogni piano che lasciava fuori un gruppo, gambe comprese. Il modello aveva quindi due strade: ignorare l'utente o vedersi rifiutare tre tentativi e non proporre niente. `leave_out` accetta solo singoli esercizi, quindi non poteva esprimere «niente gambe».

**Cosa ho cambiato**
- `src/trainer/plan.py`, in `every_group_trained`: se il piano è un adattamento, il controllo sui gruppi non si applica. Per un piano normale e per il mesociclo resta com'è.
- `src/trainer/coach/planner.py`, nel `brief`: in un adattamento i gruppi della giornata sono il punto di partenza, e quali allenare lo decide ciò che l'utente ha detto. Il testo che imponeva «ogni gruppo almeno un esercizio» resta solo per i piani normali.
- `tests/test_plan.py`: un test nuovo con «oggi faccio il core ma niente gambe» su una giornata gambe+core, che ora non viene rifiutato.

**La linea del charter che si è spostata** (`evals/planner/charter.md`): in un adattamento, quali gruppi allenare passa dai vincoli del codice alle decisioni del modello. Ho annotato le tue parole come motivo. La regola sui gruppi resta tra i vincoli, salvo che negli adattamenti.

**Cosa non ho toccato.** Gli esercizi proponibili restano quelli dei gruppi della giornata. «Il core ma niente gambe» ci sta dentro, quindi non serviva allargarli. Una richiesta come «petto invece di gambe» va ancora gestita scegliendo un'altra giornata del ciclo (`workout`).

**Test e verifiche**
- Il type check è pulito.
- Test: 1851 passati, 3 falliti. I tre falliti sono in `tests/test_bot.py`, sui pulsanti di conferma di un'esclusione nel logger. Falliscono anche con la mia modifica disattivata, quindi esistevano già e non li ho introdotti io. Non li ho indagati.
- Non ho fatto girare nulla a pagamento. La verifica vera, cioè la riga in Telegram o `trainer eval --suite adapt`, costa crediti: prima va stimata e la lanci solo se approvi.