## Lines

| line | verdict | reason |
| --- | --- | --- |
| C1 | moved toward the model | `- (SHORTER, f"Solo {SHORTER_MINUTES} minuti")` and `- SHORTER_MINUTES = 30` remove the code-set 30-minute budget. `+ PROPOSED = "... If this message asks for something else to be planned, or for that plan changed -- other minutes ... call the handoff ... the plan in chat is dropped for it"` and `Negotiation.open` now ends the pending plan, so what the user writes while a plan waits is read against it by the model. |

## Trial

- where: both
- flagged: yes
- stopped: no
- asked move: made