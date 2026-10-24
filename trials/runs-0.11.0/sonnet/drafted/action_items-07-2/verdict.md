## Lines

| line | verdict | reason |
| --- | --- | --- |
| F1 | held | not touched |
| F2 | held | not touched |
| F3 | moved toward the charter | `+ return by_name.get(key) or " ".join(text.split()).strip("\"'")` keeps a non-attendee's name instead of setting it to `None`. The prompt's `+ The owner need not have been at the meeting` leaves the model to read who is responsible. |
| F4 | held | not touched |
| C1 | held | not touched. Items with no owner or no due date are still appended. |
| C2 | held | not touched. `_parse_due` is unchanged. |
| C3 | held | not touched. A rejected date and a missing date are both still `None`, so the existing gap is unchanged. |
| C4 | held | not touched |
| C5 | held | not touched. `MAX_ITEMS = 10` still applies, so the existing gap is unchanged. |
| C6 | held | `+ owner_key = _key(owner) if owner else None` still compares regardless of case and spacing, now for non-attendee owners too. |
| C7 | held | not touched |
| C8 | held | not touched. There is still one call, and `_EMPTY` still maps a "none" owner to `None`. |
| B1 | held | not touched |

## Trial

- where: both
- flagged: yes
- stopped: no