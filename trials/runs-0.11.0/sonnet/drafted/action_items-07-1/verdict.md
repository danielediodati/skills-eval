## Lines

| line | verdict | reason |
| --- | --- | --- |
| F1 | held | not touched |
| F2 | held | not touched |
| F3 | moved toward the charter | `+ owner = by_name.get(_key(fields[1])) or _name_in_notes(fields[1], notes)`: an absent owner is now kept, but only as a full name found in the notes. The gap is partly closed. |
| F4 | held | not touched |
| C1 | held | not touched: an item whose owner fails both checks still stays, with `owner` set to `None`. |
| C2 | held | not touched |
| C3 | held | not touched: a rejected due date and a missing one are both still `None`. The gap is left as it was. |
| C4 | held | not touched |
| C5 | held | not touched: `MAX_ITEMS` still caps the list at 10. The gap is left as it was. |
| C6 | held | not touched: the key is still `(_key(task), owner)`, and `_name_in_notes` returns the same spelling for the same name. |
| C7 | held | not touched |
| C8 | held | not touched: still one call and the same skip rules. |
| B1 | held | not touched |

## Trial

- where: both
- flagged: no
- stopped: no