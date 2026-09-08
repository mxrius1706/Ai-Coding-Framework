---
name: write-ui-spec
description: "Specify one screen, decided against a working mockup rather than in prose. Covers what the page shows, how it is laid out, what the user can do there, which existing screen it reuses and where it leads next. Builds the mockup first and iterates on the picture before writing anything down. Use it when a screen needs designing or specifying, when someone asks how a page should look or behave, or when an existing screen is being reworked. Run it after the page plan exists, one call per screen."
---

# Write UI Spec

One call, one screen.

The difference to specifying anything else is that a screen can be looked at, and looking at it changes decisions. So the mockup comes before the document, not after it, and the document records what survived being seen.

That is not a nicety. Layouts that read perfectly well as a list of requirements turn out obviously wrong the moment they are rendered: a menu that made sense at one card and not at the other six, a counter on a row that has nothing to count, a control that explains itself nowhere. None of those are visible in prose.

## Phase 0: Sources

- **The page plan** for this surface: the entry for this page, the current inventory, the target navigation graph.
- **The component specs this page touches.** All of them, not skimmed. They are where the real content comes from.
- **The design system**, for what to build with and what is not allowed.
- **The current code** for this page, if it exists.

## Phase 1: What the specs already decided

Distil from the sources, each point with its citation:

- **Which data the page shows.** Fields, states, transitions.
- **Which actions the user can take, and what the specs say about how those must behave.** This is usually the most valuable find: a spec will say "no preselection on a suggestion" or "the closing note is mandatory in the same step as the status change" without ever mentioning a screen. Those are interface requirements written by someone thinking about correctness, and they are easy to miss precisely because they are not filed under interface.
- **Who sees this page**, from the roles and permissions.
- **Which routes lead here** in the target navigation graph, and which lead away.

## Phase 2: Propose, show, iterate

The core of this skill. Build a concrete proposal in four parts, and do not skip the fourth.

**Content.** What is on the page, in what order and grouping, each element traced to the spec that requires it.

**Layout.** The rough division: list, detail, dialog, multi-step form. The component patterns from the design system. Where actions sit.

**Flow.** Which click leads where. Each of these becomes an edge in the navigation graph later.

**The mockup, in the same pass.** Use the `artifact-design` skill to render the first three as an HTML page, and show it. Two rules keep it useful:

*It translates, it does not invent.* No new colours, no new layout thinking, no components the design system does not have. If the mockup needs something the design system lacks, that is a finding about the design system, not a licence to improvise.

*Real data, never placeholder text.* Actual area names, ticket numbers, categories from the domain. Lorem ipsum hides exactly the problems a mockup exists to expose: a label that wraps, a column that is too narrow, a number that is longer than the space for it.

Write the file into the repository as well as publishing it. A published link is convenient now; a file in the repository is still there when someone reads the spec in six months.

**Iteration is the normal case.** Changes go into the same file and the same published page, not a new link per round. And the changes are allowed to be purely visual: scroll behaviour, column balance, how a state reads at a glance. Those are the findings the picture exists to produce.

Where a genuine open question turns up, one the specs left undecided rather than a matter of taste, invoke `grill-me` instead of guessing. Where the answer only the customer has is missing, it stays an open point.

Only once content, layout, flow and mockup are all confirmed does anything get written.

## Phase 3: Reuse check

Against the inventory in the page plan: does an existing screen have the same shape as this one? Same shape means same structure, a filtered list with detail navigation, a table with the same action pattern, not merely the same subject.

**Yes** means recording what is reused and what changes, both in this spec and in the page plan, so that across all the pages it becomes visible which existing screens survive.

**No** gets written down too. "No existing screen fits as a basis" is information: this page is structurally new, and someone will otherwise assume the check was skipped.

## Phase 4: Write

Use the template. Write it to the location the page plan assigned, and put both mockup references in it, the published link and the repository path.

## Phase 5: Update the navigation graph

If the flows settled in phase 2 introduce routes the target graph does not have, add them. If this page firms up or renames a working-title route, correct it there.

A graph that is not updated as pages land describes the plan from before the first page was designed.

## Phase 6: Short report

Four things. What the proposal ended up being, including what changed during the discussion. The mockup link. Whether an existing screen is reused. Which open points remain and who has to answer them.

---

## Template

```md
---
title: <Screen>
status: draft
date: <YYYY-MM-DD>
surface: <portal | bot | app>
route: <path>
tags: [ui-spec, <surface>]
---

# <Screen>

<Two or three sentences. What this screen is for and who uses it.>

## Purpose and users

<The job this screen does. Which roles see it, and what differs between them.>

## Relation to the current state

<Which existing screen this reuses and what changes, or an explicit note that
none fits and this is structurally new.>

## Contents

<What is on the page, in order, each traced to the spec that requires it.>

## Layout and design

<The division, the component patterns used, where actions sit.>

**Mockup:** <published link> · repository copy `<path>`

## Flow and interactions

<Which click leads where. States, including empty, loading and error.>

## Requirements and rules

<Numbered so they can be referenced. REQ functional, GUD guideline,
CON constraint, SEC where visibility depends on a permission.>

- **REQ-001**: ...

## Open points

<What is unresolved, and who has to answer it.>

## Related documents

<Links: the page plan, the component specs behind this screen, neighbouring screens.>
```

Leave out sections with nothing in them. The relation to the current state and the mockup reference are the exceptions and always appear.

## Before finishing

Update the page plan with this page's status and the link, then the roadmap in the knowledge base: raise the written count and set the next action to the next screen. The page plan owns the per-page status, the roadmap only points at it.
