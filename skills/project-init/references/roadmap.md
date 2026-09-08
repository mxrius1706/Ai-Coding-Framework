# The roadmap

`roadmap.md` in the knowledge base is where the project's current position lives. It answers "where are we and what comes next" for anyone opening the project, and it is the only file that answers it.

It starts as the setup process and grows into the build plan. Those are the same document at two stages of a project's life, not two documents, which is why it is created at the very beginning rather than once building starts.

## Shipped filled in

The framework ships the roadmap at `templates/roadmap.md`, already carrying the steps, the skill that performs each one and the rules below. Copy it in during phase 0 and adjust only what is project-specific. Composing it fresh each time invites variation where there is no reason for any.

It is copied in **before the product definition exists**, so a project's very first session already knows what the path looks like.

Status marks: `⬜` open, `🔄` in progress, `✅` done, `❌` deliberately dropped. Drop steps that do not apply rather than marking them done: a project without an interface has no design system and no UI specs, and leaving them permanently open makes the file look unfinished forever.

## Kept current

A roadmap that is not updated is worse than none, because the next session believes it. Two rules keep it honest.

**Each skill records its own step.** When a step completes, the skill that completed it writes that in, along with the next action. Nothing that depends on a person remembering survives contact with a busy week.

**"Als Nächstes" is an action, not a phase name.** "Specs" tells a new session nothing. "Write the entity model first, everything else references it" tells it where to begin and why. This matters most exactly here, because the reasoning that produced the order is the part nobody has any more after a few days.

Write what is true, not what is planned. A step that ran halfway is `🔄` with a note on what is missing, never `✅` because it nearly worked.

## Reaching the session

Two mechanisms, and both are needed.

**The SessionStart hook injects it**, so it is in context before the first prompt without anyone choosing to read it. Its path goes into `.claude/roadmap-path` when the hook is installed, because the knowledge base sits outside the repository and the hook cannot guess.

Once the build phases are in it, the file is too large to inject whole. From then on the hook injects the head plus the one section named by the `**Aktuelle Bauphase:**` line, and truncates neither. That line is therefore load-bearing: pointing it at the wrong phase gives the next session the wrong phase with nothing failing. It is set at every phase change, in the same edit as the current position.

**The root configuration names it** as the place the current status lives, and states the obligation to keep it current. The hook covers the reading; this covers the writing. Without the obligation the file becomes a diary of the first week that everything afterwards quietly contradicts.

## Where it does not overlap

The roadmap is a position marker, not a summary. It says which step and what next; it does not restate what the other documents own.

The spec index owns which specs exist and their individual status. The roadmap carries at most a count and points at the index. On a disagreement the index wins, because it is closer to the work.

The session handoff in `.claude/state.md` owns what happened in the last session. The roadmap says where the project stands, which is a different question and changes far more slowly.

## Later

Once the specs stand, `plan-build` derives the build phases from them and writes them into the `## Bauphasen` section: what gets built in which order, with what gate at the end, and why the order is that one. Derived from finished specs rather than guessed in advance, which is why the section stays empty until then.

It goes into this file rather than a document of its own. The roadmap already answers where the project stands; a second document answering the same question in more detail produces two answers that drift apart.
