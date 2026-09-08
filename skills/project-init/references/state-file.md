# The project state file

`.claude/state.md` carries two things that every session needs and neither of which survives in a conversation. A SessionStart hook injects it, so it arrives before the first prompt without anyone asking.

It is committed, not ignored. Where the project stands is a fact about the project, not a personal note: it holds for anyone who opens the repository, and an ignored file is gone after a machine change.

## Shape

```markdown
# Projektstand

**Loop:** <current phase> · **Als Nächstes:** <the concrete next step>

| Schritt | Stand |
|---|---|
| Wissensbasis | ✅ |
| Produktdefinition | ✅ |
| Stack | ✅ |
| Design-System | 🔄 Beispielseite offen |
| Konfiguration | ⬜ |
| Komponentenkarte | ⬜ |
| Specs | ⬜ 0 von 0 |

---

## Letzte Sitzung <date>

<the handoff, written at session end>
```

Two parts, two authors, and keeping them apart is the point.

**The top is durable.** It changes when a phase completes, and it is written by whichever skill completed it. It is short on purpose: one line that answers "where are we", plus a table that answers "what is left". Anyone should be able to read it in five seconds.

**The bottom is volatile.** It is overwritten at the end of every session and describes only the last one. It is allowed to be long and specific.

Mixing them buries the durable half under the volatile one, which is why the separator is not decoration.

## Who writes the top

Each framework skill updates its own line when it finishes. Nothing else keeps a state file honest: one that a person has to maintain by hand is wrong within two weeks, and a wrong state file is worse than none, because the next session trusts it.

The rule for an entry is the same as everywhere else. Write what is true, not what is planned. A phase that ran halfway is `🔄` with a note on what is missing, never `✅` because it nearly worked.

## Why the next step is spelled out

"Als Nächstes" carries a concrete action, not a phase name. "Specs" tells a new session nothing. "Write `data/entities` first, everything else references it" tells it where to start and why.

This matters most in exactly the situation the file exists for: the work spans many sessions, and the person picking it up, human or not, has none of the reasoning that produced the order.

## What does not belong here

Not the product definition, not the decisions, not the specs. Those live in the knowledge base and this file points at nothing they own. It is a position marker, not a summary, and a summary here would become the second version that disagrees with the first.
