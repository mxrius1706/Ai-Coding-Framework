# Report template

File: `.claude/plans/phase-<n>-handlauf-<YYYY-MM-DD>.md`. Readable in an editor: lists rather than wide tables, short sentences. The inventory is created before the first click and filled during the run.

```markdown
# Handlauf phase <n> · <surfaces> · <YYYY-MM-DD>

## Contents
1. Frame
2. Overall impression
3. Findings
4. Inventory and results
5. Log balance
6. Coverage
7. Test data created

## 1. Frame
- **State:** branch `<branch>`, commit `<hash>`
- **Account:** role, scope, relevant permissions
- **Window:** 1440 x 900 (and 390 x 844 for narrow)
- **Environment:** dev server since <time>, log `<path>`, anything unusual

## 2. Overall impression
### <page>
Two or three sentences: how it comes across, what carries it, and the single most valuable thing that would improve it.
- Numbers: <x> findings (S1 <a>, S2 <b>, S3 <c>, S4 <d>)

## 3. Findings
### F1 · S<k> · <short title>
- **Where:** page, state, id (V/A/E)
- **What:** concrete, with the comparison ("the Status column starts at x=612 in group A and at x=540 in group B")
- **Reproduce:** 1. ... 2. ...
- **Evidence:** screenshot `<path>` · log `<time> <line>` · request `<method> <path> <status>` · console
- **Why it counts:** one sentence from the user's point of view
- **Guess (unverified):** ...

## 4. Inventory and results
### <page>
- **States:** V1.1 empty · V1.2 one group · V1.3 several groups · V1.4 long name ... -> each: checked / finding Fx
- **Flows:** A1.1 ... -> passed / Fx / not checkable (reason)
- **Edge cases:** E1.1 ... -> ...
- **Cross-cutting:** dark / other language / narrow / keyboard -> ...

## 5. Log balance
- `<time>` `<line>` -> step A1.2 (F3)
- `<time>` `<line>` -> environment / not attributable

## 6. Coverage
- **Checked:** ...
- **Not checked:** ... because ...

## 7. Test data created
- `HL ...` (id ...), ...
```

The plan entry, short, under the phase plan's decisions:

```markdown
- **D-<x> Handlauf <surfaces>.** *(<date>, state `<hash>`, account <role>)* Findings S1 <a> / S2 <b> / S3 <c> / S4 <d>. Report `phase-<n>-handlauf-<date>.md`.
    - **S1/S2:** F1 <one sentence>. F2 <one sentence>.
```

Two rules make the report usable rather than merely complete.

**Every finding carries its evidence.** A screenshot for anything visual, a log line or a request for anything behavioural. A finding without evidence is an opinion, and it gets argued about instead of fixed.

**"Not checkable" is a real answer.** A gate sentence that cannot be verified without something the run did not have says so, with the reason. Recording it as passed is the one failure mode that makes the whole report worthless.
