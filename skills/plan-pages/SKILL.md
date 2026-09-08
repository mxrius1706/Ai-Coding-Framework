---
name: plan-pages
description: "Decide which screens a product needs and how they connect, before any of them is specified. Produces one overview per interface surface with the inventory of what exists today, a navigation graph, the findings about the current state, and the target list of pages split into new, kept with changes and dropped. Use it once the component specs stand and screens are the next thing, when someone asks what pages a product needs, how the navigation should work, or which existing screens survive a rebuild. Derived from the component specs rather than the product definition, because only the specs describe an actual working day."
---

# Plan Pages

Settle which screens exist and how you get between them.

Doing this before the component specs stand produces a page list from the product definition, which sounds reasonable and is wrong. A product definition says what the product can do. Only the specs say what a working day looks like, and screens follow the working day.

The leading question is not "what does the product definition mention" but **"what daily work do these specs actually describe"**. Read the component specs fully rather than mining the product document for nouns.

## One overview per surface

A surface is a place with its own navigation and its own layout rules. A web portal, a chat bot, a mobile app, an admin console. Ask which surfaces exist before anything else.

Each gets its own overview, because two surfaces share neither navigation nor layout conventions, and a shared page list becomes a table with a column saying "does not apply here".

## What the overview contains

Four parts. The first three are about what is, the fourth about what should be, and keeping them apart is what stops the plan from quietly describing a rebuild as though it were already done.

### 1. The inventory of what exists

Every screen that exists today, with its route and its file path, verified by reading the code. Only real, only cited. If nothing exists yet, say so in one line rather than leaving the section out; "greenfield" is information.

### 2. The navigation graph

Mandatory, not decoration. A diagram of which screen reaches which, with the edges that depend on a permission marked as such.

It is the only artefact that shows whether a screen is reachable at all. A target list without a graph can contain an island nobody can navigate to, and that surfaces during the build instead of during the planning. Marking the gated edges has a second effect: it makes missing gating visible, because an edge that should be restricted and is not stands out next to the ones that are.

Draw both the current graph and, once the target list exists, the target graph. The difference between them is a large part of the work ahead.

### 3. Findings, without judgement

What the code review of the current surface turned up, stated as observation rather than verdict: dead controls that do nothing, more than one layout family, inconsistent permission gating, filters over a field that is being removed.

Separate this from the target list deliberately. A finding is something true today; a target is something decided for tomorrow. Merging them produces a list where nobody can tell which entries are observations and which are plans.

### 4. The target page list

Three groups, and each entry carries its reason:

- **New pages.** What they are for, and why a page rather than a panel or a dialog. That reasoning is worth writing down, because the alternative gets proposed again in six months.
- **Kept, with changes.** What stays, what changes, what is removed. Naming the removals matters most; they are the part that gets forgotten and left in the code.
- **Dropped.** With the reason. A page removed without a recorded reason gets rebuilt by someone who assumes it was an oversight.

Derive each entry from a spec and cite it. A page nobody can trace back to a component spec is either a missing spec or a page nobody needs.

## Settle the cuts by conversation

Invoke `grill-me` for the decisions that could reasonably go either way, and they are the same shape as the component boundaries one level up:

**Page or panel?** A separate screen or a section inside an existing one. The test is how many independent decisions the user makes there at once, not how much data it shows.

**One screen or several?** Where two jobs share data but not rhythm, they usually want separate screens. Where they share rhythm, one screen with a filter.

**Which screen owns an action** that plausibly belongs to two.

**What the navigation looks like.** Whether related screens become one entry with tabs or several entries. That decision is visible on every page and is cheap now, expensive later.

Give a recommendation with each question and let the user decide. These are product decisions about how the work feels, not derivations.

## Status per page

The overview also carries how far each target page has got: planned, specified, with a link to its spec once written. It is the entry point for the next step, so it stays current as each page spec lands.

## What not to do

**Do not specify a page here.** Contents, layout and interactions belong in that page's own spec, decided against a mockup. A page half-specified in the overview is a decision nobody reviewed and a second version of what the spec will later say.

**Do not derive from the product definition.** It describes capability, not a working day, and a page list built from it mirrors the document structure instead of the work.

**Do not leave a page unreachable.** Every target page has at least one inbound edge in the target graph, or an explicit note saying why it is entered from outside the surface.

## Before finishing

Update the roadmap in the knowledge base: mark the page planning step, record how many pages are planned, and set the next action to the **first page spec, with the reason it goes first**. Usually that is the screen the most other screens lead into, because its decisions constrain theirs.
