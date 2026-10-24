# Perché `you-choose` ha fallito 1 volta su 3

Il planner legge il testo libero. Nessuna regola toglie un solo esercizio, e nessuna regola toglie lo squat. Quel «niente squat» letto come «via il back squat» è una scelta del modello del planner, Haiku 4.5.

## Il percorso di «oggi niente squat, proponi tu»

1. **Entrance.** Il modello della chat chiama `adapt_this_workout(said="oggi niente squat, proponi tu")`. `entrance.py:773-776` passa al planner solo `said`. Niente diventa `exclude`, `groups` o `minutes`.
2. **Request.** `plan.adaptation_requested` (`plan.py:523`) parte dall'intero catalogo con le sole esclusioni già attive nel DB. `asked` è vuoto, quindi `named` è vuoto e non c'è nessuna riga «They also named, and the plan keeps to it: no squat». Lo squat resta nell'insieme ammissibile.
3. **Brief.** `planner.adapted` (`coach/planner.py:255`) mette la frase dell'utente in cima («what they said is the first thing it answers to»). Sotto c'è il workout di oggi del mesociclo, con il back squat dentro, e l'indicazione «start from it unless what they said points elsewhere». Il modello è partito da lì e ha sostituito l'esercizio con il suo vicino più ovvio: `Front_Barbell_Squat`.
4. **Validatore.** Per un'adattazione (`plan.py:829-847`) controlla solo che gli id siano ammissibili, che nessun esercizio compaia due volte, le righe `despite` e `counts_as`. Budget e gruppi vengono saltati di proposito («An adaptation answers to what the user said, which no rule reads»). Nessun controllo confronta il piano con le parole dell'utente, quindi il front squat passa.
5. **Eval.** `without_pattern = ["squat"]` boccia il piano perché il `movement_pattern` del front squat nel catalogo è `squat` (`adapt_evaluation.py:333`).

## Cosa dice il charter

`evals/planner/charter.md`, riga 19 (Free): per un'adattazione «the time, the groups, the equipment and which workout to start from, read off what the user said». Capire quanto è ampio «niente squat» spetta al modello. 2 volte su 3 l'ha letto come lo intendevi tu.

## Cosa si può fare

- **Senza spostare linee:** aggiungere in `adapted()` un criterio come «a pattern or a kind of exercise they name is all of it: with «niente squat», no exercise of the squat pattern». È lo stesso tipo di frase che c'è già per «solo kettlebell». Informa il giudizio del modello e non decide al suo posto, quindi il charter lo permette.
- **Spostando una linea:** convertire «niente squat» in un'esclusione nel codice (`asked.exclude`, o un `exclude` sulla chiamata `adapt_this_workout`). Così la decisione passa dalla riga 19 (Free) al campo vincolato. Le esclusioni oggi sono trattate come sicurezza (riga 28), non come preferenza del giorno. Lo farei solo se me lo chiedi tu.

Non ho lanciato niente. Per verificare la prima strada bisogna rifare almeno la riga `you-choose` contro un modello a pagamento, e la stima e il budget te li chiederei prima.