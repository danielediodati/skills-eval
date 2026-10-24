The list now gives a task to someone who missed the meeting when the notes say it's theirs. For your 3 March notes, "Approve the budget" comes out with owner Marta Olsen and due 10 March. The 20 local unit tests pass. I didn't run the real model, so I haven't seen it write "Marta Olsen" on your actual notes. I made no paid calls.

**The line that moved:** the charter's "Owner must be an attendee" rule. I changed that line and the "Who owns an item" line under Free, and noted your reason in the charter. A task the notes gave to an absent colleague used to lose its owner and look abandoned.

**What the code checks now:**
- **Attendees:** matched as before and returned as you spelled them.
- **Absent people:** accepted only if their full name (two words or more) appears in your notes. It's returned as the notes spell it. A name the model made up still becomes "no owner".
- **Real open tasks:** these still come out with no owner. An item with no owner now means the notes really didn't say who has it. That's how you tell the two kinds apart.

**Prompt:** it now tells the model to write the full name, as the notes give it, when someone absent took the task.

**Limit:** if the model answers with just "Marta" for an absent person, the item loses its owner. That matches how attendees' first names are already handled. A more forgiving match would mean guessing, so I left it strict. Say if you want it looser.

**Not covered:** the tool only returns the list. Sending it to Marta is outside it. Her name is now on the item, so whatever sends the list can address her.

I changed `seam.py`, `test.py`, `README.md` and `evals/action_items/charter.md`.