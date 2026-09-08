---
name: session-recap
description: "Write the handoff for the next session into the project state file, so the work continues instead of restarting. Covers what was done, what was decided, what comes next and what is still open, compressed to what the next session actually needs. Use it at the end of a working session, when the user says goodbye or signals they are stopping for the day, when a session is being wrapped up, or when someone asks for a handoff or a summary of where things stand. A hook can trigger it on farewell phrases so nobody has to remember."
---

# Session Recap

Every session starts with an empty context window. What the last one learned is gone unless it was written down, and reconstructing it costs more than writing it did.

This writes the handoff. It takes a minute and saves the next session twenty.

## Where it goes

Into the lower half of `.claude/state.md`, below the separator. **Never overwrite the whole file.**

The upper half carries where the project stands in the process, is written by other skills as phases complete, and is durable. The lower half is this handoff, describes only the last session, and is overwritten each time. Replacing the file wholesale destroys the durable half, and nothing will tell you it happened.

If the file does not exist yet, create it with both halves, and fill the upper one from what is actually true rather than leaving it empty.

## Check the top before writing the bottom

The end of a session is the moment the upper half is most likely to be stale, because a phase may have been completed by hand rather than through the skill that would have recorded it.

So read it, compare against what happened, and correct it if it is wrong. This is the cheapest opportunity to catch a state file drifting, and a state file that has drifted is worse than none, because the next session believes it.

## Format

```
## Letzte Sitzung <date> · <branch>

Ziel: <one sentence>

Gemacht:
- <file or area>: <what>
- ...

Entschieden: <only non-obvious decisions, otherwise omit>

Nächstes: <the concrete next action, one sentence>

Offen: <only if it blocks something, otherwise omit>
```

Write it in the project's documentation language, which the project configuration states. The headings above are an example, not a fixed wording.

## Rules

**Facts only, no narrative.** The next session needs what it cannot reconstruct: which branch, which commit range, how many tests passed, which gate is through. Not how the work felt.

**"Nächstes" has to be actionable.** "Continue" is not a next step. Name the file, the document or the command. If the order matters, say why, because the reasoning that produced it is exactly what will be missing.

**Keep it to around fifteen lines.** The limit is the discipline. Beyond that it stops being read, and an unread handoff is the same as none.

**Omit empty sections.** A "Decided: nothing" line costs attention and carries nothing.

**Overwrite the lower half, do not append.** Only the last session is relevant. A growing log buries the current state under history, and history lives in the version control system.

**Where a correction is owed, that is the next step.** Something noticed but not fixed outranks the next new piece of work, otherwise it sinks and resurfaces as a bug.

## Afterwards

Give the user two or three lines in the chat saying what was written. They are ending the session, not starting a review.
