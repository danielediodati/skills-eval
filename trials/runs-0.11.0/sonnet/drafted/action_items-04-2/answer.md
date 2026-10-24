I changed the prompt so the model writes an attendee's full name when the notes use a first name or nickname. I haven't run it against a real model, so I don't know yet whether it fixes your 3 March example.

**Cause.** The model was told to give the owner "as written in the list above". For "Tom looks into the venue" it probably answered `Tom`. The code only accepts an exact match to an attendee's full name, so `Tom` was dropped to no owner. The item itself was kept, which is why the venue and badges tasks still appeared.

**Change.**
- **Prompt (`seam.py`).** It now says the notes often use first names or nicknames like "Tom", "Tommy" or "Ana R." When one clearly means someone present, the model must write that person's full name from the list, never the short form. "none" is for when the notes don't make clear who took the task.
- **Test (`test.py`).** I added a check that the prompt carries this instruction. The 18 unit tests pass.

**Charter lines.** None moved. The charter already makes mapping nicknames and first names to attendees the model's job. The code check that the owner must be an attendee is unchanged. I didn't make the code guess "Tom" means Tom Becker, because that would loosen a check the charter keeps in code.

**Next step.** The real test is a paid run: your 3 March notes, plus a nickname case like "Tommy" or "Ana R.", through the actual model. I haven't started one. If you want it, we should first agree a spending budget for it.