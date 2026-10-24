I changed the prompt so the model should now give "Tom looks into the venue" to Tom Becker and "Priya to order the badges" to Priya Raman. I haven't confirmed that against a real model, because that needs a paid call.

**Cause.** The prompt told the model to write the owner "as written in the list". It never said the notes use first names and nicknames. A model that answered "Tom" or "Priya" failed the code's check that the owner is a listed attendee. The item was kept but the owner became `None`. I'm inferring this from the code, since I have no log of the actual model output.

**Change.** In `seam.py`, the owner instruction now says the notes usually use first names or nicknames ("Tom", "Tommy", "Ana R."). It tells the model to work out which person on the list is meant and write their full name from the list. I added a test in `test.py` that the prompt says this. The 18 tests pass.

**Charter.** No line moved, so `charter.md` is unchanged. Resolving first names and nicknames was already the model's job, and the owner check in code stays strict. I didn't add a first-name lookup in code. That would take over a decision the charter leaves to the model and would loosen the owner check.

**What this doesn't fix.** The model still decides who an item belongs to. If the notes are ambiguous, for example two attendees called Tom, it may answer "none". That is intended, since code never guesses an owner.

**Checking it.** A small run on your 3 March notes would show whether the model now returns all three owners. It would cost one model call per run. Give me a budget for the ticket and the model to use, and I'll run it.