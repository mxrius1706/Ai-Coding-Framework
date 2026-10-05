# UX and visual checklist

Not every line on every page, but every page against every group. The questions are phrased so that a finding becomes concrete: *what* is wrong, *compared with what*.

## Contents
1. First impression
2. Alignment, grid, spacing
3. Stability under data variance
4. Text: overflow, truncation, wrapping
5. Hierarchy and the main action
6. Language and terminology
7. Consistency with the app
8. States and feedback
9. Speed
10. Interaction and error tolerance
11. Accessibility
12. Dark, other language, narrow

## 1. First impression
- In one sentence: tidy or restless, finished or a building site, clear or crowded?
- Does anything jarring jump out (a crooked edge, an empty gap, truncated text, something duplicated)? That is almost always a finding.
- Would you trust this page in front of a customer?

## 2. Alignment, grid, spacing
- **Repeated tables and cards:** columns and content line up across all groups - equal column widths, not auto-sized per table. Verify by measuring: compare `getBoundingClientRect().left` of the column headers across groups.
- Left edges of heading, filter row and content are flush.
- Equal elements are equally sized (buttons, pills, badges, row heights).
- Spacing follows a rhythm; no single gap larger or smaller than its siblings.
- Numbers right-aligned or at least consistently aligned, date and number formats uniform.
- Icons optically centred against their text.

## 3. Stability under data variance
- A very long name, a very short one, one with accents and special characters: do columns, buttons and menus stay where they are?
- Many tags or chips, none at all: does the row height jump? Do chips wrap cleanly?
- Large numbers (three or four digits), empty fields (an en dash rather than a gap).
- A list with one element, with many, with groups of different sizes.
- Layout shift while loading: does the skeleton have the same shape as the content? Does anything jump when data arrives, an image loads, a font swaps?

## 4. Text: overflow, truncation, wrapping
- Nothing protrudes from its box, nothing overlaps.
- Truncated text has an ellipsis and is reachable another way (tooltip, detail page).
- No mid-word break at normal lengths, no single word stranded on the last line of a heading where it looks wrong.
- Chart labels stay inside their shapes.

## 5. Hierarchy and the main action
- The main action is immediately recognisable and unambiguous (one primary button, not three).
- Destructive actions are set apart and ask first.
- What matters is larger or stronger than what does not; metadata recedes.
- Grouping is visible (proximity, rules, cards) without being busy.

## 6. Language and terminology
- One term per thing across all pages - not "process", "flow" and "workflow" mixed, unless the difference is deliberate.
- Buttons say what will happen ("Save version 3" rather than "OK").
- Error messages say what is wrong and what can be done, without codes or internals.
- No raw keys (`processes.detail.x`), no placeholders, no leftovers from the other language.

## 7. Consistency with the app
- The same building blocks as on neighbouring pages: header, filter row, table card, row menu, dialogs.
- Design tokens rather than one-off colours, the project's icon set rather than emoji, and whatever marking the project uses for generated content.
- The same interaction patterns: where a click on the row opens it, it does so everywhere; menus open in the same place.

## 8. States and feedback
- Loading: is there an indicator? Does it match in shape and size? How long does it take?
- Empty: a friendly text with the next step.
- Error: visible, understandable, with a way out ("Try again").
- Success: a confirmation (toast, status change) that is not missed and does not linger forever.
- Locked: the reason is stated, not just a greyed-out button.
- After an action: is the new state visible everywhere (list, counter, detail) without a reload?

## 9. Speed
- Time to visible content, after warm-up: note anything above roughly 2 s; above roughly 5 s is an S2.
- A reaction to a click is visible within roughly 100 ms (spinner, pressed state), even when the result takes longer.
- Long-running calls: interim text, cancellable, no freeze.

## 10. Interaction and error tolerance
- Hit areas large enough (touch at least 40 px), hover states present.
- A double click produces nothing twice; the button locks while the work runs.
- Cancel works everywhere; Escape closes dialogs; input is not lost on an accidental close, or the page asks.
- The Back button behaves as expected; the URL reflects the state (filters, an open dialog).

## 11. Accessibility
- Keyboard: everything reachable, order logical, focus visible, no focus trap.
- Contrast sufficient, including placeholders, disabled text and text on colour.
- Icons without text have a label (`aria-label`, tooltip).

## 12. Dark, other language, narrow
- Dark: no harsh white areas, borders visible, charts readable.
- The other language: longer words break nothing, nothing from the first language left over.
- Narrow (390 px): columns stack or scroll sensibly inside their card rather than the whole page scrolling sideways; the main action is reachable; dialogs fit.
