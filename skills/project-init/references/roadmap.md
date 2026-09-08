# The roadmap

`roadmap.md` in the knowledge base is where the project's current position lives. It answers "where are we and what comes next" for anyone opening the project, and it is the only file that answers it.

It starts as the setup process and grows into the build plan. Those are the same document at two stages of a project's life, not two documents, which is why it is created at the very beginning rather than once building starts.

## Initialised with the process

Created in phase 0, before the product definition exists, holding the steps ahead as unstarted. A project's first session then already knows what the path looks like.

```markdown
# Fahrplan

**Jetzt:** <the current step> · **Als Nächstes:** <the concrete next action>

## Aufbau

| Schritt | Stand | Notiz |
|---|---|---|
| Wissensbasis | ⬜ | |
| Produktdefinition | ⬜ | |
| Stack | ⬜ | |
| Design-System | ⬜ | entfällt ohne Oberfläche |
| Projektkonfiguration | ⬜ | |
| Komponentenkarte | ⬜ | |
| Specs | ⬜ | 0 von 0 |
| Seitenplanung | ⬜ | |
| UI-Specs | ⬜ | 0 von 0 |

## Bauphasen

<Empty until the specs stand. Derived from them, not planned ahead of them.>
```

Status marks: `⬜` open, `🔄` in progress, `✅` done, `❌` deliberately dropped.

Adapt the step names to the project's documentation language. Drop steps that do not apply rather than marking them done: a project without an interface has no design system and no UI specs, and leaving them as permanently open rows makes the file look unfinished forever.

## Kept current

A roadmap that is not updated is worse than none, because the next session believes it. Two rules keep it honest.

**Each skill records its own step.** When a step completes, the skill that completed it writes that in, along with the next action. Nothing that depends on a person remembering survives contact with a busy week.

**"Als Nächstes" is an action, not a phase name.** "Specs" tells a new session nothing. "Write the entity model first, everything else references it" tells it where to begin and why. This matters most exactly here, because the reasoning that produced the order is the part nobody has any more after a few days.

Write what is true, not what is planned. A step that ran halfway is `🔄` with a note on what is missing, never `✅` because it nearly worked.

## Referenced from the configuration

The project's root configuration names this file as the place the current status lives, and states the obligation to keep it current. Without that, a session has no reason to look, and the file quietly becomes a diary nobody reads.

## Where it does not overlap

The roadmap is a position marker, not a summary. It says which step and what next; it does not restate what the other documents own.

The spec index owns which specs exist and their individual status. The roadmap carries at most a count and points at the index. On a disagreement the index wins, because it is closer to the work.

The session handoff in `.claude/state.md` owns what happened in the last session. The roadmap says where the project stands, which is a different question and changes far more slowly.

## Later

Once the specs stand, the build phases follow from them: what gets built in which order, with what gate at the end. That section is derived from finished specs rather than guessed in advance, which is why it stays empty until then.
