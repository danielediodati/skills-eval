Il planner legge testo libero. Nessuna regola toglie un solo esercizio, e nessuna toglie lo squat: il codice non ha mai saputo che «niente squat» fosse un vincolo.

**Cosa succede con «oggi niente squat, proponi tu»**

| passo | cosa succede | dove |
|---|---|---|
| entrance | chiama `adapt_this_workout` passando solo `said`, cioè la frase dell'utente | `src/trainer/coach/entrance.py:306` |
| request | `requested` costruisce la richiesta con `adaptation_requested(..., said=said)` e un `Asked` vuoto: `exclude` resta `()` | `src/trainer/coach/entrance.py:768-776` |
| esclusioni | `constraining_today` riceve `given=[]`. Nella richiesta finiscono solo le esclusioni salvate (in questa fixture nessuna), e lo squat non c'è | `src/trainer/plan.py:550-555` |
| brief | la frase arriva al modello così com'è, come «the first thing it answers to», insieme a «plan the workout it asks for -- … an exercise in or out» | `src/trainer/coach/planner.py:259-274` |
| validator | per un adattamento tempo e gruppi vengono saltati. Resta solo l'ammissibilità, ma senza esclusioni `Front_Barbell_Squat` è ammissibile e passa | `src/trainer/plan.py:837-847` |
| eval | `without_pattern = ["squat"]` boccia qualsiasi esercizio con `movement_pattern = squat`, e il front squat ce l'ha | `src/trainer/adapt_evaluation.py:333` |

Quindi la scelta di levare tutto lo schema motorio o solo il back squat l'ha fatta Haiku, leggendo la frase. Nel run fallito (1 su 3) l'ha intesa a livello di esercizio, e il brief gli dava uno spunto in quella direzione: «an exercise in or out» parla di esercizi, non di schemi. Negli altri due run l'ha letta bene.

**Dove sta la linea**

- Il charter del planner (`evals/planner/charter.md:7`, `:19`) lascia **libera** la scelta degli esercizi in un adattamento: comandano le parole dell'utente, non il codice.
- Il percorso per escludere davvero uno schema c'è, ma lo raggiunge solo il terminale: `Asked.exclude` accetta schemi motori (`plan.py:413`) e `cli.py:1424` lo passa. La chat non lo valorizza mai.

**Le due correzioni possibili**

- **Senza spostare la linea:** un criterio nel brief, per esempio che «niente squat» indica uno schema motorio e quindi niente front squat, goblet o split squat. Informa il giudizio del modello e non gli toglie la decisione.
- **Spostando la linea:** dare all'entrance un argomento `exclude` da girare ad `Asked.exclude`. Lo squat uscirebbe dall'admissible set e il validator lo garantirebbe al 100%. Però la decisione passerebbe dal planner all'entrance, che dovrebbe tradurre la frase in vocabolario del catalogo, e il punto 19 del charter andrebbe riscritto. Lo faccio solo se me lo chiedi tu.

Non ho lanciato niente, né test né chiamate pagate: ho solo letto il codice.