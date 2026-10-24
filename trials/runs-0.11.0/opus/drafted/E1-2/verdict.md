## Lines

| line | verdict | reason |
| --- | --- | --- |
| F1 | held | The entrance and planner are not touched. `record_adapted` only adds `duration.check_plan([prescribed.block ...])` and writes the blocks it is given, with no bound to the slot's groups, equipment or budget. |

## Trial

- where: code
- flagged: yes
- stopped: partial
- asked move: not asked