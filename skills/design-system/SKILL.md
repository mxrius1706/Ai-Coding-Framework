---
name: design-system
description: "Define a project's design system - the visual direction, colour, typography, spacing, radius, elevation, interaction states, component patterns and accessibility floor - then write the tokens into the codebase and the reasoning into the knowledge base, with a working example page to approve it by. Use this when a project needs a look defined, when someone asks about brand colours, fonts, spacing scale, dark mode, design tokens or a style guide, when a redesign is being considered, or when UI work keeps producing inconsistent screens because nothing says what consistent means. Run it after the stack is settled, since the stack decides the token format."
---

# Design System

Settle what the project looks like, write the values where the code can use them, and keep the reasoning where the code cannot express it.

A design system that exists only as prose gets ignored, because nobody can build from adjectives. One that exists only as token values gets violated, because nothing says why red is never a background. Both halves are needed, and they belong in different places.

## What this produces

**A token file in the repository.** The values: colours, type scale, spacing, radii, elevation, state styling. This is what the code reads and therefore the only place a value is allowed to live.

**A design schema in the knowledge base.** The named direction, the principles behind it, the rules that constrain use, the rationale for the choices, and a pointer to the token file. No value is repeated here.

**An example page.** A real rendering of the system, used to approve it. Approving a palette from a table of hex codes is guessing; approving a page is judgement.

## Order of operations

0. Establish what already exists
1. Settle the direction
2. Show it
3. Write it

## Phase 0: What already exists

Two situations, and they call for opposite instincts.

**Nothing is built yet.** There is no existing look to respect, so everything is a choice. Check whether a brand exists outside the code anyway: a brand guide, a logo with defined colours, an existing website, a colour the company already uses on invoices. A design system invented next to an existing brand is a second brand nobody asked for.

**Something is already built.** Then the current look is a fact, not a proposal, and it is read from the code. Find the stylesheet, theme file or token definitions and extract what is actually in use. Expect it to be inconsistent: five greys that should be three, a spacing scale with exceptions, a hover state that differs per component. That inconsistency is the finding, and it is what makes the system worth writing down.

Never present the existing look back as though it were freshly chosen, and never quietly replace it. Say what is in use, say where it contradicts itself, and let the user decide which version wins.

Also read the stack decisions before going further. They determine the token format, and writing tokens in a shape the project cannot consume is wasted work.

## Phase 1: Settle the direction

Invoke `grill-me` for what is genuinely open. Skip anything phase 0 already answered, and never ask the user to recite something that is in the code.

Worth settling:

- **The direction itself**, as a name plus a few principles. "Kinetic Precision, high-contrast minimalism, no decorative depth" carries further than a list of hex codes, because it decides the cases nobody enumerated. Without a stated direction, every later question gets answered from scratch.
- **Colour**, starting from the brand colour if one exists. Then the neutrals, the surface hierarchy, and the semantic roles: success, warning, danger, information.
- **Where the brand colour must not go.** The most useful colour rule is usually a prohibition, because the failure mode is using it everywhere.
- **Typography**, families and the scale, and what distinguishes a heading from a label beyond size.
- **Spacing**, a base unit and the multiples in use. Say which increments exist so exceptions become visible.
- **Radius and elevation**, including whether the project expresses depth at all. Deciding against shadows is a decision and needs stating.
- **Interaction states**, focus first. Focus is the one every system forgets and the one accessibility depends on.
- **Dark mode**, whether it exists at all. Half a dark mode is worse than none.
- **The accessibility floor**, as a target that can be checked, such as WCAG AA contrast with the ratios named.

Anything unresolved stays `TBD` with a note on what would settle it, rather than a plausible invention that later reads as a decision.

## Phase 2: Show it

Build an example page that renders the system in use, and present it before writing anything permanent.

Not a swatch sheet. A page with the things a real screen has: headings and body text at their real sizes, buttons in every state including focus and disabled, form fields with a validation error, a card, a table row, a status indicator, a navigation element. In light and dark, if dark mode was decided. The point is to expose the combinations that look fine in isolation and wrong together.

Use the `artifact-design` skill if it is available, so the page can be published and viewed. If it is not, write a self-contained HTML file and tell the user where it is. Either way, the tokens in the page are the proposed values, so what the user approves is what gets written.

Iterate here rather than after writing. Changing a token in a preview costs nothing; changing it after the codebase consumes it costs a sweep.

## Phase 3: Write

Only after the example page is approved.

### The token file, in the repository

Write the values in the shape the stack actually consumes. That shape follows from the stack decisions, so read them rather than assuming: a utility-first CSS framework, plain custom properties, a theme object in the language's own syntax, or a platform's native resource format are all different targets, and a token file in the wrong shape is decoration.

This file is the only place a value lives. Everything else points at it.

### The design schema, in the knowledge base

Everything the token file cannot say:

- The named direction and its principles
- Why these choices, and what was considered and rejected
- The rules that constrain use, such as where the brand colour may not appear, or which increments are allowed
- Component patterns, described by their intent rather than their exact values
- The accessibility target and how to check it
- A pointer to the token file for every value

The test for a line in this document: **could the code have told me this?** If yes, it belongs in the token file and the document points there. If no, it belongs here.

### What not to write

Do not restate the token values in prose. A table of hex codes in a document next to a token file in the code is two truths, and colours change. The first time they disagree, whoever reads the document builds the wrong thing and nothing warns them.

## Running it later

A redesign, a rebrand, or a decision to add dark mode is this same skill on a project that already has answers. Phase 0 then reads the existing tokens rather than a brand guide, and only what is changing goes through the interview.

When something is being replaced, the old value does not simply vanish from the document. Say what is changing, what it becomes, and until when the old one is still what the code does, so a session working during the transition is not told a future state as though it were present.

## When called by project-init

Runs after the stack is settled, because the token format depends on it. Return the direction, the token file location and any open `TBD`, so the area map can decide whether the interface deserves its own instructions and what they should point at.

## Before finishing

Update the roadmap in the knowledge base: mark the design system step, note where the token file lives, and set the next action. A half-finished design system belongs there as such, with what is missing, not as done.
