# The session handoff

`.claude/state.md` carries what happened in the last session, and nothing else. A SessionStart hook injects it, so it arrives before the first prompt without anyone asking.

It is committed, not ignored. What was done last session is a fact about the project, not a personal note, and an ignored file is gone after a machine change.

## What it is not

It does not say where the project stands in the process. That is the roadmap's job, and duplicating it here would create the second version that eventually disagrees with the first. See `references/roadmap.md`.

The division is worth stating precisely, because the two look similar:

**The roadmap** answers *where are we and what comes next*. It changes when a step completes, which is rarely, and it lives in the knowledge base with the other durable documents.

**The handoff** answers *what happened last time*. It is overwritten every session and describes only the most recent one.

Mixing them buries the durable answer under the volatile one.

## Shape

```markdown
# Letzte Sitzung <date> · <branch>

Ziel: <one sentence>

Gemacht:
- <file or area>: <what>
- ...

Entschieden: <only non-obvious decisions, otherwise omit>

Nächstes: <the concrete next action, one sentence>

Offen: <only if it blocks something, otherwise omit>
```

Write it in the project's documentation language. The headings are an example, not a fixed wording.

## Rules

**Facts only.** What the next session cannot reconstruct: which branch, which commit range, how many tests passed, which gate is through. Not how the work felt.

**"Nächstes" has to be actionable.** Name the file, the document or the command. "Continue" is not a next step.

**Around fifteen lines.** The limit is the discipline. Beyond it the file stops being read, and an unread handoff is the same as none.

**Overwrite, do not append.** Only the last session is relevant. A growing log buries the present under history, and history is what the version control system is for.

## How it gets written

By `session-recap` at the end of a session, triggered by a hook on farewell phrases so nobody has to remember. See that skill for the details.
