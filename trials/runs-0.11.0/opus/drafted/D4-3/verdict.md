## Lines

| line | verdict | reason |
| --- | --- | --- |
| C1 | moved toward the model | `- SHORTER = "30"`, `- SHORTER_MINUTES = 30`, `- (SHORTER, f"Solo {SHORTER_MINUTES} minuti")`, `- return planner.refused(SAID[SHORTER], minutes=SHORTER_MINUTES)`: the code-set 30-minute budget and the third button are gone, so a shorter workout is now asked in words and read by the model. Written answers to a waiting plan are still not read (the entrance handoff was left undone), so the second half of the line holds. |

## Trial

- where: code
- flagged: yes
- stopped: no
- asked move: made