The list can now name someone who wasn't at the meeting as the owner. The 19 local unit tests pass. I haven't run a real model on your 3 March notes, because that would be a paid call and needs your approval first.

**What changed**
- **Code (`seam.py`):** an owner no longer has to be an attendee. If the model names an attendee, the name comes back spelled as you gave it. Any other name, such as "Marta Olsen", is kept as the model wrote it, with spacing tidied.
- **`None` now means open:** `owner=None` appears only when the notes name nobody. That is the item you need to chase.
- **Prompt:** it now tells the model that the owner can be someone who was absent, and that it should give their full name.
- **Tests and README:** I replaced the test that dropped absent owners with one that keeps them. I added a test for the prompt wording and one for two different absent owners on the same task. I also updated the README line.

**Charter lines that moved**
The charter is `evals/action_items/charter.md`. I changed these in the same edit, for the reason you gave: an unowned line reads as a task nobody took.
- **Constrained, owner check:** the rule that an owner must be an attendee is replaced. Any named person is kept, and `None` means the notes named nobody.
- **Free, who owns an item:** the model now decides ownership for attendees and non-attendees alike.
- **Constrained, deduplication:** the same task given to different absent people used to collapse into one unowned item. It now stays as separate items.

**Cost of the change:** code can no longer check a non-attendee's name, so the model could name the wrong person or invent one. The charter now says this is the accepted cost of showing absent owners.

**Not covered:** the output has no separate marker for "owner was absent". Marta shows as the owner, and that is enough to tell her task apart from an open one. The code can't yet send her the list, because it doesn't know her contact details.

If you want to try it on the 3 March notes, tell me a budget for the real-model run and I'll go from there.