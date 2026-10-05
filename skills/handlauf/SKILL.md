---
name: handlauf
description: "Walk a built phase through the real interface with a browser, with the eyes of a demanding user, and report what is wrong. Looks hard at every page (layout, alignment, consistency, spacing, overflow, states, feedback, speed, usability), clicks the happy paths and the edge cases, watches the dev server log, the console and the network while doing it, verifies that what looked saved really is, and writes a report with findings by severity. Report only, never fixes. Runs in a session of its own and deliberately takes no input from the code reviews, because its value is being the first look. Use it whenever a surface is to be checked in the browser - EN: manual test, smoke test, click through, UX review, walkthrough, e2e by hand, does it actually work, does it look right, sign off the pages; DE: Handlauf, durchklicken, im Browser testen, UI pruefen, funktional testen, sieht das gut aus, Seiten abnehmen, nach dem Fix nochmal alles pruefen. Also use it when a phase is built and the question is whether the interface works and looks right before the gate or after a round of fixes, even without the word handlauf. Not for automated tests (skill testing), not for code review (review-changes), not for designing a page (write-ui-spec)."
---

# Handlauf - check the interface the way a user experiences it

The name is the method: walk through the product holding the handrail, one page at a time, and notice everything a careful person would notice.

> **REPORT ONLY.** Find it, prove it, rank it. Fix nothing, not even a one-line triviality. Fixing runs separately afterwards, through `execute-plan`. A walkthrough that repairs as it goes ends up reviewing a state nobody built.

## What this is for

This is the review no test and no code review can do: **what is it like to use this page?** Does it look finished and tidy, or skewed? Is it clear what happened? Does it respond quickly and unambiguously? Does the layout hold when the data is not the data from the mockup? Does it still work when you do something unexpected?

The specs are **orientation, not a checklist**. They say what a page is for and what it must be able to do. Whether it does it *well* is decided by looking at the real page. A walkthrough that only ticks off whether every spec point is present misses the point: a page can satisfy every requirement and still be crooked, slow or confusing. That is exactly what should surface here.

**The standard:** an attentive person seeing the page for the first time and expecting quality, plus a designer who notices alignment and rhythm. Whatever either would notice at first glance belongs in the report.

**One tab, one step at a time.** No parallel subagents. The user is often working in the same browser and against the same dev server at the same time.

## A clean session, and no review input

**Run this in a session of its own**, started for this purpose. Not as a subagent of the gate chain, not in the session that built the phase, and not alongside the code reviews.

**It takes no input from `review-changes`, `thermo-nuclear-code-quality-review` or the per-block reviews.** No findings list, no review report, no "watch out for X" from a reviewer. If one of those has already run, its output stays out of this brief.

That is a deliberate restriction, and it is worth stating why, because it looks like waste. This pass judges layout, function and whether the interface makes sense at all - it is UX work, and its entire value is that it is a **first** look. A pass that has read "the permission check in the handler is fine" goes looking for the permission check instead of looking at the page. One that has read a list of nine findings spends its attention confirming those nine and stops noticing the tenth, which is the crooked column nobody wrote down. Primed eyes are no longer fresh eyes, and fresh is the only thing this pass has that the others do not.

What it **does** read is intent, not judgement: the phase plan with its goal, gate and decisions, the page's UI spec, the mockup, and earlier walkthrough reports. Those say what the page is supposed to be. A review says what someone already thought about the code, and that is the part that contaminates.

The findings go to the user and into the phase plan. The code reviews are not their audience either - they run on the same changes with their own heads, which is the point of having three gates instead of one.

## Phase 0 - understand, do not tick off

1. **The surfaces** from the request, or derived from the phase plan and briefly confirmed.
2. **Get oriented** - a few minutes per surface, not more. What is the page for, who uses it, what is the main path? Sources: the phase plan (goal, gate, decisions), the page's UI spec and its mockup, earlier walkthrough reports. Gate sentences become mandatory flows.
3. **An inventory, not a spec matrix**, written into the report file from `references/report-template.md`. Per surface:
   - the **states** that need to be seen (empty, one row, many, long, loading, error, locked, archived, draft, preview),
   - the **flows** (main path first, then the side paths),
   - the **data variants** that stress the layout (a very long name, many tags, no tags, many steps, accents, special characters).

   Give them ids (`V1.2` visual, `A1.3` flow, `E1.4` edge case) so the report can reference them.

## Phase 1 - set up

1. **Load the browser skill** for whichever browser this project drives, and load the tools you expect to need in **one** `ToolSearch` call (tabs, navigate, computer, read_page, find, get_page_text, javascript_tool, read_console_messages, read_network_requests, resize_window).
2. **A dev server with a log.** If one from this session is already running with a log, reuse it. Otherwise ask the user, then start it through `scripts/start-dev-logged.sh <logfile>` with `run_in_background`.
3. **Watch the log**: a `Monitor` on `scripts/watch-dev-log.sh <logfile>`, `timeout_ms` at its maximum, re-armed when it expires. Assign every message to the step that was running when it appeared.
4. **Your own window**: a tab of your own via `tabs_create_mcp`, with the window size fixed (`resize_window` 1440 x 900) so screenshots are comparable and the layout does not depend on the size of the user's window.
5. **Check the session**: which account, which role, which permissions. Expired - ask the user.
6. **Read `references/pitfalls.md` first.**

## Phase 2 - look (for every page and every state)

This is the core. **A screenshot at full resolution**, not scaled down, and actually look at it: first as a whole (the impression in one sentence - tidy? finished? calm?), then area by area with `zoom`. Reading the text (`get_page_text`) never replaces looking; it supplements it.

Check against `references/ux-checklist.md`, above all:

- **Alignment and grid:** do the same things sit in the same place? Columns of repeated tables under one another, equal widths for equal elements, edges flush, spacing in one rhythm. **Always compare repeated blocks against each other** (groups, cards, rows, list entries): if they look different although they are the same thing, that is a finding.
- **Stability under different data:** does a long title, a missing tag or a large number change the layout around it? Does anything shift while loading, on hover, on open? Produce the data variants from phase 0 on purpose and look at the same page again.
- **Overflow and truncation:** text escaping its box, cut off without a hint, broken mid-word, tooltips missing where text is truncated.
- **Hierarchy and readability:** is it immediately clear what matters and what the main action is? Do elements compete? Are labels understandable, jargon-free, consistent in tone and terminology?
- **Consistency with the rest of the app:** the same building blocks as on neighbouring pages? The same button styles, pills, spacing, icons, design tokens?
- **States:** loading (how long? is the skeleton the right shape? does everything jump afterwards?), empty, error, locked (does the page say why?), success (is there any feedback?).

**Load time is UX:** note anything above roughly 2 seconds to content, with a measurement. After a fresh server start, load once before measuring - compilation does not count.

## Phase 3 - use it

The flows from the inventory, main path first. Act like a person: click, type, Enter, Escape, Back.

After every action, **three looks**:
- **The page:** what changed, and is it understandable? Is there feedback (toast, status change, focus)? Is the new state cleanly presented (the phase 2 look again)?
- **The network:** `read_network_requests`, called once before the action so the capture is running - 4xx/5xx, duplicate calls, unnecessary calls, slow responses.
- **Console and log:** `read_console_messages` filtered to `error|warn|Uncaught|hydration`, plus the monitor messages.

**Verify that it is really saved:** reload, reopen the page, call a read-only API route; read the database only. A success toast is not proof.

**Edge cases** from `references/edge-cases.md`, chosen to fit the surface: double clicks, two tabs, Back, reload mid-dialog, boundary inputs, deep links, foreign ids, caches after dialogs.

**Test data:** created only through the interface, prefixed `HL`, all of it noted in the report. Existing data is read only, unless the user releases it. Where a write path has to be checked against data you may not touch, use probes that write nothing (a wrong revision to provoke a conflict). Writing or deleting through the database only after asking.

## Phase 4 - the cross-cutting pass and roles

For **every** page checked, with a screenshot and the phase 2 look:
- **Dark mode:** contrast, invisible text, harsh white areas, charts.
- **The other language**, where the product has one: raw keys, untranslated leftovers, longer strings that break the layout.
- **Narrow** (`resize_window` 390 x 844): no horizontal scrolling of the page, nothing overlapping, the main action reachable.
- **Keyboard:** tab order, visible focus, Escape, Enter.

**Roles in one batch** at the end: send the user the list (account, role, scope, what will be checked), wait, verify the session, check, then ask to be switched back.

## Phase 5 - close

1. **The report**, following `references/report-template.md`. Severity:
   - **S1** broken or data lost (crash, 5xx, a save that disappears, the wrong record, a permission leak).
   - **S2** the main path is disturbed, or the page looks broken or unfinished at first glance (visibly skewed layout on a main page, 4xx in the normal flow, wrong data, a gate sentence violated, a load time that leaves you unsure whether anything is happening).
   - **S3** operation or appearance grates (inconsistency with neighbouring pages, unclear text, missing feedback, focus, overflow in edge cases, dark mode or narrow view with defects).
   - **S4** polish (a few pixels of spacing, wording, an icon).

   Every visual finding has a screenshot saved to disk with its path in the report, and says concretely *what* is wrong and *compared with what*: "the Status column starts at x=612 in group A and at x=540 in group B".
2. **An overall impression** per page in two or three sentences: how does it come across, and what is the single most valuable thing that would improve it?
3. **A plan entry** in the phase plan: a short decision entry with the numbers and a reference to the report.
4. **Clean up:** stop the monitor, close your own tab, leave the dev server running.
5. **To the user:** the overall impression, S1 and S2 individually, S3 and S4 summarised, what could not be checked, and the path to the report.

## Where this fits

`execute-plan` builds the phase. This runs after it and before the phase gate, or again after a round of fixes. It answers whether the thing works and looks right; `review-changes` answers whether the code is sound and `thermo-nuclear-code-quality-review` whether it stays maintainable. Three different questions, and this is the only one that requires looking at the product.
