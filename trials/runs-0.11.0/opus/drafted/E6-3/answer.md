## Planner e «niente squat»: legge il testo libero, nessuna regola toglie un solo esercizio

Non c'è nessuna regola che toglie un esercizio, né una che toglie un pattern. Il planner legge la frase così com'è, e la scelta di togliere solo il back squat l'ha fatta il modello. Il codice qui non decide niente.

### Il percorso di «oggi niente squat, proponi tu»

| passo | dove | cosa succede |
|---|---|---|
| 1. Entrance | `src/trainer/coach/entrance.py:70` | `adapt_this_workout(said)` riceve solo la frase. Dalla 14.4 non ci sono più campi (`leave_out`, `exclude`, …). |
| 2. Request | `entrance.py:776` → `plan.py:523` | `adaptation_requested(connection, today, said=said)` riceve un `Asked()` vuoto. Quindi `exclude=()` e `given=[]`: «squat» non diventa mai un'esclusione. L'admissible set è l'intero catalogo, con tutti gli squat e l'attrezzatura di tutto il catalogo. |
| 3. Brief | `src/trainer/coach/planner.py:255` | Al modello arrivano: la frase alla lettera, poi *«an exercise in or out»*, poi *«start from it unless what they said points elsewhere»*, e infine il workout 1 in JSON, il cui primo blocco è `Barbell_Squat`. |
| 4. Validatore | `plan.py:837` | Per un adattamento controlla solo due cose: nessun esercizio doppio e id ammissibili. Il commento lo dice: *«An adaptation answers to what the user said, which no rule reads»*. `Front_Barbell_Squat` è ammissibile, quindi il piano passa. |
| 5. Eval | `src/trainer/adapt_evaluation.py:333` | Solo qui conta il `movement_pattern` del catalogo: `Front_Barbell_Squat` ha pattern `squat` e la riga fallisce. |

### Perché il modello l'ha letto come «uno squat in meno»

Il motivo che ha scritto nel blocco, *«front squat replaces back squat»*, mostra il ragionamento: ha preso «squat» come il nome dell'esercizio in programma, `Barbell_Squat`, e non come la categoria di movimento. Il brief lo spinge in questa direzione in due punti:

- *«an exercise in or out»* inquadra la richiesta come un singolo esercizio da togliere o aggiungere;
- *«start from it»* accanto a un workout che ha un solo squat invita a sostituirlo con un esercizio simile.

Per l'attrezzatura il brief ha un esempio esplicito: *«solo kettlebell»* significa che ogni esercizio deve essere col kettlebell (aggiunto in `1879139`). Per un movimento escluso non c'è un esempio equivalente. È andata così in 1 run su 3: nelle altre 2 il modello l'ha letto giusto, quindi è una lettura instabile, non un bug.

Nella prima passata lo stesso sintomo (`Dumbbell_Squat` tenuto) aveva un'altra causa: `leave_out` accettava solo id. Quel campo non esiste più, quindi oggi la causa è solo la lettura del modello.

### Cosa si può fare, rispetto al charter

Il charter del planner (`evals/planner/charter.md:20`) lascia al modello la lettura della frase e la scelta di cosa entra ed esce, perché *«no validator rule reads the words»* (ADR-0008 item 6).

- **Consiglio: un criterio nel brief**, sullo stampo dell'esempio del kettlebell. Per esempio: *un movimento nominato, come «niente squat», toglie ogni esercizio di quel movimento, non solo quello in programma.* È un criterio che informa il giudizio, quindi il confine del charter resta dov'è.
- **Alternativa: farlo tenere al codice**, con l'entrance che estrae il pattern in `exclude` oppure con il validatore che legge la frase. Questo sposterebbe il confine: torneremmo ai campi tolti nella 14.4, contro ADR-0008 item 6. Va fatto solo se me lo chiedi tu esplicitamente.

Non ho cambiato niente e non ho lanciato niente di pagamento. Nel repo non trovo il log di quella run: il motivo del blocco l'ho preso dal ticket di `4a5af5f`, non dal transcript.