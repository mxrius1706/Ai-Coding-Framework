---
name: project-init
description: Set up the Claude Code configuration for a project from scratch - the Obsidian knowledge base, the PRD, and the full instruction layer of root and area CLAUDE.md files, path-scoped rules and hooks. Use this whenever a user starts a new project, says the PRD is done and they want to set the project up, asks to initialize or scaffold their Claude config, wants CLAUDE.md files created, or is standing in an empty repository wondering how to begin. Also use it when a project already has code but no configuration layer worth the name. Do not confuse this with the built-in /init command, which only summarizes an existing codebase into a single file.
---

# Project Init

Build the configuration layer a project needs so that every later session starts informed instead of guessing.

The output is not one file. It is a structure of three layers plus an external knowledge base, and the value comes from putting each statement in exactly one place.

## The idea in one paragraph

A project has three kinds of truth and they age at different speeds. Product truth (what we build and why) changes rarely and belongs outside the repository, where it is not tied to a branch. Working conventions (how we build here) change with the stack and belong in version control next to the code they govern. Current state (what the code actually does today) is only reliable when read from the code itself, so configuration must never claim it without evidence. Mixing these three is what makes documentation rot. Separating them is the entire point of this skill.

## Order of operations

Do these in order. Each phase depends on the one before it.

0. Knowledge base
1. PRD
2. Stack interview
3. Area map
4. Plan for approval
5. Write

Never skip ahead to writing files. The plan in phase 4 is presented and approved before anything is created.

---

## Phase 0: Knowledge base

This comes first, before the PRD, because the PRD needs somewhere to live that is not the repository.

Product truth in the repo is a trap. It sits on a branch, it gets copied into a second file for convenience, and six months later two versions disagree and nobody knows which one is binding. Keeping it in a vault outside the repo removes the temptation, because there is only ever one copy to read.

**Check for an Obsidian MCP server.** If Obsidian tools are already available, use them and move on.

If not, walk the user through it. Do not assume familiarity, since many people have never added an MCP server. Explain that this connects Claude to a folder of Markdown notes, and that Obsidian itself is optional because the folder works either way.

The simplest server takes a vault path directly and needs no plugin, no API key and no running Obsidian:

```json
{
  "mcpServers": {
    "obsidian": {
      "type": "stdio",
      "command": "obsidian-mcp",
      "args": ["<absolute path to the vault folder>"]
    }
  }
}
```

This goes in the global settings or the project `.mcp.json`. Ask which they prefer: global if they want one vault across projects, project-local if this vault belongs to this project alone. The server has to start before its tools appear, which usually means restarting the session. Say that up front, or they will wonder why nothing works.

A REST-based alternative exists that talks to a running Obsidian instance through a Local REST API plugin and an API key. Only suggest it if the user specifically wants live sync with the Obsidian app. It is more setup and more that can break, and an API key sitting in a config file is a liability worth avoiding when the simple server does the job.

**Create the vault structure.** Once the server answers, lay out the space for this project:

```
<Vault>/
  <Project>/
    PRD.md              product truth, the binding definition
    roadmap.md          build order, phases, status per phase
    specs/
      _index.md         one line per spec with its status
      decisions/        one file per architecture decision
```

Keep it this shallow at the start. Depth earns its way in later. Invented hierarchy only makes things hard to find.

---

## Phase 1: PRD

If no PRD exists, invoke the `prd` skill, which runs a proper interview through `grill-me` before writing anything. Write the result into the vault.

If a PRD already exists, read it, and check where it lives. A PRD sitting in the repository or in a stray folder gets **moved** into the vault, not copied. Someone may have run `prd` on its own before starting here, which is fine, but leaving the file where it landed while referencing a vault path is how a project ends up with two versions that slowly disagree. Move it, confirm the move with the user, and reference only the new location from then on.

Either way, the repository never holds a copy of the PRD.

The PRD supplies the product section of the configuration and, above all, the non-goals. Non-goals are the sharpest thing in a PRD: they are the only part that tells a future session what not to build, and they belong in the root configuration almost verbatim.

**What the PRD does not supply is the stack.** It says so itself, marking an unspecified stack as `TBD` rather than guessing. Do not read a technology choice out of a product document. That is phase 2.

---

## Phase 2: Stack interview

Invoke `grill-me` and settle the technical decisions. This is deliberately a separate conversation from the PRD.

The danger it avoids is worth naming. A configuration full of confident, specific rules for a stack nobody chose reads exactly like a configuration full of correct rules. It is fiction shaped like documentation, and it will be followed. Only write a technical rule once the user has confirmed the technology it belongs to.

Cover at least:

- **Language and runtime**, with versions where they matter
- **Framework**, and which of its conventions this project actually adopts
- **Data layer**: database, ORM or query layer, migration tooling
- **Validation**: where input is checked, and with what
- **Authentication and authorization**, including where the check happens
- **Testing**: framework, what must be covered, what is deliberately not
- **Deployment target**, in as much detail as it affects the code
- **Secret handling**: where secrets live and how the code reaches them

Anything the user cannot answer stays `TBD` in the generated files, with a note on what would settle it. A `TBD` a future session can act on beats an invented answer it will trust.

---

## Phase 3: Area map

Areas are not a matter of taste. They follow the structure the stack already has, so derive them from what phase 2 established. In a monorepo that usually means one per package; in a single tree, one per subsystem.

**Read `references/areas.md` before deciding.** It carries the catalogue of areas worth considering, how each mechanism loads into context, and the rule for choosing between them.

The test for every candidate: an area earns its own file when work inside it follows rules that do not apply elsewhere. Applied honestly this rules out most candidates in a small project, which is the correct outcome. A library or a CLI may need no areas at all, only a root file.

Then decide the form for each. Four mechanisms exist and they differ in when they enter the context window, which is the entire basis for the choice:

- **Area `CLAUDE.md`** for conventions belonging to a directory, versioned next to the code
- **Path-scoped rule** in `.claude/rules/` with `paths:` frontmatter, for rules that apply to files scattered across the tree or when conventions are better kept in one place
- **Skill** for a procedure done occasionally rather than a convention that is always in force
- **Hook** for anything that must happen without exception

That last distinction matters more than it looks. Instructions in any of the first three are context, not enforcement, and may not be followed. A hook runs as a script at a fixed point regardless of what the model decides.

---

## Phase 4: Plan for approval

Present the plan before creating anything. These files steer every later session, so the user should see the shape once before it lands.

The plan lists every file with a one-line summary of its contents, the area map with the reason each area exists, every point that will be written as `TBD` together with what would resolve it, and the vault paths that will be referenced.

Then wait for approval.

---

## Phase 5: Write

Create the vault structure first, then the repository files.

### Size is a hard constraint, not a preference

Target **under 200 lines per `CLAUDE.md`**. These files load into the context window at the start of every session and compete with the actual work. Past that length adherence drops, and the failure is silent: the model does not announce that it stopped following rule 40, it just stops.

The consequence is counterintuitive. A longer, more thorough configuration is a **worse** one, because the rules that matter get lost among the rules that do not. Being generous here actively harms the project.

For every line, apply the test: **would removing this cause a mistake?** If not, cut it.

What earns its place: commands that cannot be guessed, conventions that differ from the language or framework default, environment quirks, decisions specific to this project, non-obvious behaviour that has already bitten someone.

What does not: anything derivable by reading the code, standard conventions the model already knows, file-by-file descriptions of the tree, dependency lists, API documentation that should be a link, and self-evident advice like "write clean code".

Notes for human maintainers can go in block-level HTML comments. Those are stripped before the file reaches the context window, so they are free.

### Root CLAUDE.md

Sections in this order. Omit any that has nothing true to say, because an empty section invites someone to fill it with plausible noise later.

**Working agreement.** How the user wants to be worked with: execute or propose, when to ask, how much scope to take on. Take this from the user's own habits rather than inventing house rules.

**Product.** From the PRD: what this is, who it is for, and the non-goals. Then a pointer to the PRD in the vault for anything deeper. Two or three sentences, not a summary of the whole document. Duplicating the PRD here creates exactly the second version this structure exists to prevent.

**Stack.** From phase 2. Each entry names the technology plus the one thing this project does differently from its default.

**Architecture rules.** The invariants: what must always hold, what must never happen. Derive them from the constraints in the PRD and the decisions from phase 2. Each rule states the rule and then why it exists. A rule without a reason gets discarded by the first person who finds it inconvenient.

**Security baseline.** Where authentication is checked, where input is validated, what gets logged, how secrets are handled.

**Testing requirements.** What must have tests, what coverage is expected, where tests live.

**Definition of done.** A checklist someone can actually work through: compiles, lint clean, tests green, new logic covered, no unexplained escape hatches.

**Scope discipline.** Solve the task that was asked. No improvements to neighbouring code. Ask when scope is unclear instead of guessing.

**File conventions.** A table of path patterns with one real example each.

**Language.** Which language for code and comments, which for user-facing text, which for documentation and commits.

**Knowledge base map.** A table from question type to vault location: product questions to the PRD, decisions to `specs/decisions/`, technical detail to the relevant spec. This table is what stops a later session from creating a local copy of something that already exists in the vault.

**Phrase routing.** One table mapping what the user says to the skill that should run. The only routing table in the project. See below.

**Known weak spots.** Start empty, with a note that reviews fill it once a pattern has appeared twice. An empty section with a stated filling rule is honest. A pre-filled one is invention.

### Area CLAUDE.md

One per area from phase 3. Each opens with a single line on what the area covers, then its rules, then a short list of anti-patterns specific to it. Anti-patterns earn their space: they catch the plausible-but-wrong move that general rules miss.

Where an area has a mandatory sequence, such as a fixed order of steps in a request handler or a procedure for schema changes, write it as a numbered sequence or a code skeleton rather than prose. Sequences get followed when they look like sequences.

### .claude/rules/

Detail that applies to some paths but not others goes here, one topic per file, with `paths:` frontmatter naming the globs it covers:

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API rules

- Validate at the boundary before anything reaches the database
- Errors use the shared response shape
```

The frontmatter is what makes this worth doing. A rule with `paths:` enters the context window only when a matching file is touched. A rule without it loads in every session, exactly like the root file, and should therefore be held to the same test.

Rules also suit anything that applies across scattered paths, where an area file would have to be duplicated: migrations wherever they live, generated files wherever they sit.

Create one only when there is real content for it. An empty rule file is a promise that will not be kept.

### CLAUDE.local.md

Anything personal to one developer, such as a sandbox URL or preferred test data, belongs in `CLAUDE.local.md` at the project root, added to `.gitignore`. Keeping it out of the shared file prevents one person's setup from becoming everyone's instruction.

### Two rules that hold across every generated file

**One truth, one place.** No statement appears in two files. Where a second file needs it, it links. Two copies of a rule will disagree eventually, and then the work follows the wrong one. When a fact would fit in several places, put it in the most specific one and link from the others.

**Stock with an expiry date.** When something exists but is on its way out, say so in the document that describes it: what runs today, what replaces it, which decision settled that, and what may no longer be built on it. Documentation that describes a doomed system as though it were the target quietly teaches the wrong thing to every session that reads it.

### Routing

Path routing needs no table. A rule with `paths:` frontmatter is loaded by the tooling when a matching file is touched, without the model having to remember to consult anything. Write the globs; do not restate them as a table somewhere.

**Phrase routing** does need writing down: a table in the root file mapping what the user actually says to the skill that should run. Use the phrases they really use, in every language they work in. This is the only routing table, and it lives in the root file alone. Routing kept in two places drifts apart, and then the wrong one gets followed.

Where a phrase must always trigger its skill, a `UserPromptSubmit` hook can enforce it. The table then documents what the hook does rather than hoping the model reads it.

---

## Working with an existing codebase

When the project already has code, one rule overrides everything above: claims about the current state come from the code, not from the user's description and not from a specification.

Read before writing. Check the real paths, the real function names, the real field names. Where the user's account and the code disagree, the code wins, and the disagreement is worth mentioning, because it usually means something moved and nobody updated their mental model.

Specifications describe intent, and intent is usually ahead of reality. Writing intent into configuration as though it were fact produces rules that refer to things nobody built.

## When done

Report the files created, every `TBD` together with what would resolve it, and the areas deliberately left without a file.

Then say plainly that this is a scaffold and not truth. Its accuracy about the code is at its lowest right now, because there is barely any code yet. It becomes true through use: by being corrected when it turns out wrong, and by having what gets learned written back into it.
