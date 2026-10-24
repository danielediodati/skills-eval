```
## Lines

| line | verdict | reason |
| --- | --- | --- |
| C1 | moved toward the model | `groups=(), allocation=(), adapting=Adapting(..., groups=request.groups)` and the docstring "The slot's groups are not held": the request no longer carries the slot's muscle groups, so the admissible set and `every_group_trained` stop constraining them. The prompt now says "the slot is where you start, not a limit". |

## Trial

- where: both
- flagged: yes
- stopped: no
- asked move: made
```