For your 3 March notes, the budget approval now comes out as "Approve the budget", owner Marta Olsen, due 2026-03-10. An item with no owner now means nobody took it.

All 20 tests pass, including one built from your 3 March notes. I haven't run a real model on the new prompt, so I haven't seen it write Marta's name on real notes. I didn't run one because that costs money. If you want a paid check, we'd first agree a budget.

- **The cause:** the code accepted an owner only if they were on the attendee list. Marta wasn't, so her name was dropped and the item was kept with no owner.
- **The prompt:** it now tells the model to write the name as the notes do when a task goes to someone who wasn't at the meeting.
- **The check:** a name outside the attendee list is kept only if it appears in the notes as whole words. A name the model made up still becomes "no owner". The name comes back spelled as the notes spell it.
- **First names:** a bare first name or a partial name of an attendee, such as "Tom", is still not accepted as an owner. It becomes "no owner", as before.

**Charter lines moved:**
- Under Free, "Which attendee owns an item" became "Who owns an item, attendee or not".
- Under Constrained, "Owner must be an attendee" became "Owner must be an attendee or be named in the notes".

Both lines carry your reason. The README is updated to match.

If the notes mention Marta only by first name ("Marta will approve…") and never give her full name, the model will probably write "Marta Olsen". The check will then find nothing in the notes to match and drop the owner. I left that as it is, since loosening it would let invented names through. Say so if you'd rather accept it.

I haven't added anything that sends the list to Marta. This change only puts her name on the item, which is what lets you address her.