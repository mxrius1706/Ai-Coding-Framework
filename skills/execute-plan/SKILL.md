---
name: execute-plan
description: "Execute a released implementation plan task by task, each task in a fresh subagent, each followed by two reviews before the next one starts. The coordinator reads the plan once, bundles the context and delegates; it writes no code itself. Use it when a plan file is to be built, implemented or worked through, or when the user points at a plan and says to go. Not for planning and not for reviewing a finished phase."
---

# Execute Plan

Work a released plan, one task at a time.

**The coordinator's job is context, not code.** Read the plan once, assemble a bundle per task, dispatch, judge the result. Writing code yourself defeats the purpose twice: it fills your context with detail that belongs in a subagent, and it leaves nobody with an outside view of what was produced.

Two rules shape everything else. **A fresh subagent per task**, because an implementer that has already built three things carries three things' worth of assumptions into the fourth. And **two reviews after every task, before the next one begins**, because a task built on top of a wrong one costs both.

## Step 1: Read the plan, extract the tasks

Once, completely: context, goal, decisions, critical files, order, tests, verification, out of scope.

Extract each task **with its full text**, not its title. File paths, types, constraints, dependencies. The subagent will not read the plan; whatever is not in the bundle does not exist for it.

Put the tasks in a todo list. Work them in the plan's order.

## Step 2: Dispatch the implementer

Sequential, never parallel. Two implementers in one working tree produce conflicts that cost more than the time they saved.

The bundle carries everything the subagent needs and nothing it does not:

- **The project's binding rules** for the paths this task touches: the root instructions, the area instructions, the path rules that match. **Embed the content, do not name the file.** A path in a prompt is a suggestion; text in a prompt is context.
- **The plan's goal and decisions**, so the subagent knows the why and does not re-decide what was already settled.
- **The task, in full.**
- **The critical files** relevant to it.
- **The definition of done**, meaning the project's own verification commands and its test rules.

Two instructions that always belong in the brief: **do not commit**, and **answer with exactly one status code**.

```
DONE
DONE_WITH_CONCERNS: <the concerns>
NEEDS_CONTEXT: <what is missing>
BLOCKED: <the blocker>
```

Fixed status codes exist so the coordinator can act on the answer without interpreting prose, and so "it mostly works" cannot be reported as done.

**Model choice by judgement, not by size.** One or two files against a clear spec is mechanical. Several files with dependencies, or anything with a design decision, a schema change or a debugging element in it, is not. When in doubt, one step up: a task redone costs more than a stronger model.

### Handling the status

**DONE** goes to step 3.

**DONE_WITH_CONCERNS** gets read first. A correctness or scope concern is resolved before the review; a plain observation ("this file is getting large") is noted and passed on.

**NEEDS_CONTEXT** means the bundle was incomplete. Supply what is missing, dispatch a new subagent with the same task and the better bundle.

**BLOCKED** has four causes and each has a different answer. Missing context means a bigger bundle. A task too large means splitting it. A task the model could not carry means one step up. **A plan that is itself wrong means stopping and going to the user**, and nothing further is dispatched.

Never re-dispatch the same task unchanged after a block. Repeating an attempt without changing an input is not a retry, it is a loop.

## Step 3: Spec compliance review

A fresh reviewer, carrying the task text and the plan's goal. It judges one thing only, and it is not quality:

- Is everything the spec requires implemented?
- Is anything implemented that the spec does **not** ask for? Scope creep counts as non-compliance, and it is the finding this review catches that no other does.
- Do paths, names, types and constraints match?

Answer: compliant with a reason, or non-compliant with a list of what is missing, extra or different.

**Non-compliant means a new implementer with the gaps in the bundle, then reviewed again.** There is no "close enough": the plan is the contract, and a contract that is approximately kept is not kept.

## Step 4: Quality review

Only once compliance is green. A different question, so a different head.

The checklist is the project's own: whatever the rules and the specs make mandatory on these paths. Where the project has security-relevant invariants, they are checked explicitly and by name rather than in general terms.

Severity in four steps: something exploitable or data-destroying, something that breaks a rule the project made binding, something that weakens a defence or leaves a gap in the tests, and cosmetics. **The first two block; the rest are collected.**

Blocking findings mean a fix and another review. Collected ones go to the final review at the end so they are seen together, where a pattern is visible that no single task shows.

## Step 5: Close the task, then the plan

Mark the task done only when both reviews are green. Then the next task.

When all tasks are through, run `review-changes` over the whole diff and hand it the collected minor findings as context. The per-task reviews looked at pieces; this one looks at what they add up to.

## What the coordinator does not do

- Write the implementation itself.
- Send subagents off to read the plan on their own.
- Run implementers in parallel.
- Run the quality review before the compliance review.
- Mark a task done with a blocking finding open.
- Accept a deviation from the plan because it looks reasonable.
- Commit per task. Subagents never commit; committing happens once at the end.

## Where this fits

`planning` writes the plan and gets it released. This skill builds it. `review-changes` is the gate at the end of the phase. Running this without a released plan means building something nobody agreed to, and the plan is what the review is later measured against.
