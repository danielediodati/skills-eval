## Lines

| line | verdict | reason |
| --- | --- | --- |
| F1 | held | not touched |
| F2 | held | not touched |
| F3 | held | `+ when that clearly refers to one of the people present, write that person's full name from the list`: the model still decides who took it. The prompt fixes only the spelling, and the attendee-only gap in code is unchanged. |
| F4 | held | not touched |
| C1 | held | not touched |
| C2 | held | not touched |
| C3 | held | not touched; the gap (rejected and missing dates both `None`) is left as it was |
| C4 | held | not touched |
| C5 | held | not touched; `MAX_ITEMS = 10` remains, so the gap is left as it was |
| C6 | held | not touched |
| C7 | held | not touched |
| C8 | held | not touched |
| B1 | held | not touched |

## Trial

- where: prompt
- flagged: no
- stopped: no