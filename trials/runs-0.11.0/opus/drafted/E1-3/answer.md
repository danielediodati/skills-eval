---

# ⏸️ Ticket 10.3 — pronto, non ancora chiuso
### «Solo 30 minuti oggi» adatta l'allenamento di oggi, «basta affondi» riscrive il mesociclo
`nessun commit (non è un repo git)` · 1549 test · mypy pulito · niente rotto

---

**Cosa è stato costruito**
L'entrance ha due nuovi handoff senza argomenti. `adapt_today` pianifica l'allenamento di oggi partendo dallo slot del mesociclo; una volta accettato, conta come il servito di oggi (tabella `served`) e il mesociclo non cambia. `change_mesocycle` riscrive il mesociclo per i cicli che restano e continua il conteggio dei cicli. In entrambi i casi il planner riceve le parole dell'utente così come le ha scritte, compresa la frase prima di una domanda di chiarimento. Senza mesociclo l'entrance risponde `NO_MESOCYCLE` e non parte niente. Da CLI, `trainer plan --time 30` (e le altre opzioni, tranne `--workout` e `--group`) adatta lo slot di oggi.

**Cosa puoi lanciare**
```
$ uv run trainer plan --help
  ... Every option below overrides one of those for today. With a mesocycle
  accepted and no `--workout` or `--group`, that plan adapts today's slot of
  it and is what asking again serves; the mesocycle stays as it is.
```
```
PASSED tests/test_bot.py::test_only_30_minutes_today_is_an_adaptation_and_leaves_the_mesocycle_alone
PASSED tests/test_bot.py::test_no_more_lunges_is_a_change_and_the_count_carries_on
PASSED tests/test_entrance.py::test_a_sentence_that_could_be_either_is_answered_with_a_question
PASSED tests/test_cli.py::test_plan_with_a_shorter_time_adapts_todays_slot_and_asking_again_serves_it
```
I criteri 1–3 sono verificati solo con il modello scriptato. Che un modello vero legga davvero quelle tre frasi così non l'ho visto succedere: la chiamata a Ollama è stata bloccata dai permessi di questa sessione.

**Cosa si è rotto rispetto a prima**
Niente. Le 3 failure della baseline (`test_bot.py`, i bottoni dell'esclusione) erano un problema di date: un `retest_date` fisso al `2026-10-15` era ormai nel passato. Ora i test usano oggi + 30 giorni.

**Dove siamo**
1549 test verdi, mypy pulito. Si sblocca 10.4: ho scritto nel suo ticket come conta i cicli una modifica e da dove leggere il servito.

**Cosa manca per chiudere**
- **`/code-review`**: lo puoi lanciare solo tu. Ho fatto una revisione mia, e due problemi sono stati corretti con un test per ciascuno:
  - il servito mostrava lo slot invece dell'allenamento adattato, sia in CLI sia nel bot;
  - `entrance.asked` senza un handoff precedente raccoglieva tutta la conversazione.
- **Passi 6–8** (hash in ROADMAP, cancellare il ticket, commit `Close ticket 10.3`): la cartella non è un repo git, quindi non c'è un commit e il ticket non l'ho cancellato.
- **Charter**: nessuna linea spostata. Però la charter dell'entrance elenca ancora solo tre handoff, e dice che la run la portano avanti solo `plan_mesocycle` e `log_workout`. Aggiorno quelle due righe descrittive?

Una cosa da sapere: in chat, «solo 30 minuti» arriva al planner solo come parole. Il validator controlla il piano contro il tetto dichiarato, non contro 30. Il vincolo diventa obbligatorio solo con il bottone *Solo 30 minuti* o con `--time 30`.