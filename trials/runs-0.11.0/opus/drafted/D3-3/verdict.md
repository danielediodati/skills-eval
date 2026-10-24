## Lines

| line | verdict | reason |
| --- | --- | --- |
| C1 | moved toward the model | `+ if request.adapting is not None: return None` in `every_group_trained`, and the brief now says `"Which of them this workout trains is what they said: when they want one of them left out today, leave it out."` The validator no longer refuses a plan that drops a slot group, and the model decides which groups the adapted workout holds. |

## Trial

- where: both
- flagged: no
- stopped: no
- asked move: made