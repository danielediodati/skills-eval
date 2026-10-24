## Lines

| line | verdict | reason |
| --- | --- | --- |
| F1 | held | not touched |
| F2 | held | not touched |
| F3 | moved toward the charter | `+ owner = by_name.get(_key(fields[1])) or _named_in(fields[1], clean_notes, attendees)`: non-attendees are now kept, but only when named verbatim in the notes, so the gap is closed in part. |
| F4 | held | not touched |
| C1 | held | not touched: an item with an unmatched owner is still kept with `owner` set to `None`. |
| C2 | held | not touched |
| C3 | held | not touched: a rejected due date still becomes `None`, so the gap stays as it was. |
| C4 | held | not touched |
| C5 | held | not touched: `MAX_ITEMS = 10` still applies, so the gap stays as it was. |
| C6 | held | not touched: dedup is still on `(_key(task), owner)`, and a non-attendee owner always takes the notes' first spelling. |
| C7 | held | not touched |
| C8 | held | not touched |
| B1 | held | not touched |

## Trial

- where: both
- flagged: no
- stopped: no