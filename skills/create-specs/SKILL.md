---
name: create-specs
description: "Break a planned product into the software components it needs, and lay them out as a connected graph of specification documents rather than a pile of files. Produces the spec index, one placeholder per component with its responsibility and its declared boundaries, the dependencies between them and the order they should be written in. Use this after the product definition and the stack are settled and before any individual spec is written, when someone asks how to cut a system into components, what specs a project needs, or where the boundary between two parts should run. Also use it when specs already exist but nothing says how they relate."
---

# Create Specs

Cut the product into components, and connect them.

The cutting is the smaller half. A list of components is a filing system, and filing systems do not stop two documents from specifying the same field differently. What prevents that is every component stating what it does **not** cover and naming who does. Do that and the specs become a graph that can be navigated and checked. Skip it and they become a pile that slowly contradicts itself.

This skill lays out the graph. It does not write the specs; each one is written later, one at a time, against this map.

## What this produces

**A spec index.** Every planned component with its responsibility in one sentence, the components it depends on, and its status. This is the map, and it stays the map: it is updated whenever a spec is written or a component is added.

**One placeholder per component**, at its final path, carrying frontmatter and the declared boundaries and nothing else. Marked unmistakably as not yet written.

**A writing order**, derived from the dependencies.

## Order of operations

0. Read the foundation
1. Derive the structural layers
2. Derive the product domains
3. Settle the boundaries
4. Order by dependency
5. Write

## Phase 0: Read the foundation

The product definition, the stack decisions and, if the project has an interface, the design system. Everything here is derived from those, so working from a half-read product definition produces components that do not match what is being built.

If the project already has code, read that too. Components that already exist are facts, and a decomposition that ignores them describes a different system than the one on disk.

## Phase 1: Structural layers

Most systems need the same few layers regardless of what they do. Start from this set, then **remove what this project does not have**:

- **architecture** - how the system is put together, deployment shape, security posture, tenancy
- **data** - the entities, their relationships, the invariants that must hold
- **api** - the contracts other things call
- **ui** - the screens, if there are any
- **integrations** - external systems, one per system
- **decisions** - one document per architectural decision, kept separate because decisions outlive the documents that cite them

Prune honestly. A project with no external systems gets no integrations layer, and creating the folder anyway invites someone to fill it. A library has no ui. The set is a starting proposal, not a template to complete.

## Phase 2: Product domains

These come from the product definition and are different for every project. Look for two things.

**The nouns the product is about.** The things users create, find, change and talk about. A domain usually forms around a noun that has its own lifecycle.

**The flows.** A path that runs end to end through the system, that someone would describe as one thing, usually earns a document even though it touches everything. It is the document that explains how the pieces fit, and without it every reader has to reassemble the story from the parts.

Two useful signals that a domain is real rather than invented: it has vocabulary of its own, and it has rules that make no sense outside it. A "utilities" domain has neither, which is why that name always signals a bad cut.

## Phase 3: Settle the boundaries

This is the phase that matters, and it is a conversation, not a derivation.

Invoke `grill-me`. For each pair of components that could plausibly own the same thing, put the question to the user: which one owns it, and what does the other one say instead? The answer becomes a line in the losing component's boundary list.

The questions worth asking are the ones where a reasonable person could answer either way. Does the state machine own the permission to make a transition, or does the permissions component? Does the entity document define the validation rules, or the contract that receives them? There is no universally right answer, which is exactly why it has to be decided once and written down rather than decided repeatedly and differently.

Two rules for the outcome:

**Every component gets an explicit not-covered list.** Not an afterthought, a required section, with each entry naming the component that owns it instead. This is what makes the graph navigable and what stops the same rule being written twice.

**A boundary is a link in both directions.** If A says the model belongs to B, B is now responsible for the model, and that expectation is real even before B is written. Record it, because the component written later has to either honour the assumption or knowingly break it.

## Phase 4: Order by dependency

The order is not arbitrary and getting it wrong is expensive.

Write what everything else points at first. The entity model is almost always first, because contracts, flows and screens all reference fields, and specifying a contract before the fields exist means inventing fields that later turn out wrong. Then the domain logic that uses the entities, then the contracts that expose it, then the interface that consumes the contracts.

Where two components genuinely depend on each other, say so rather than pretending an order exists. Write the more stable one first and mark the other as expected to correct it.

## Phase 5: Write

**The index** carries every component with its one-sentence responsibility, its dependencies, its status, and the writing order. It is the entry point, so it stays current: a spec written without its index entry updated is a component nobody can find.

**A placeholder per component**, at the path it will keep, containing only frontmatter and the boundaries settled in phase 3. Two rules about these, and both matter:

*Create them at the correct path now.* In a linked knowledge base, a link to a document that does not exist is a trap: following it creates the document wherever the tool guesses, which is rarely where it belongs. Pre-creating the placeholders means every planned link resolves to the right place from the first day.

*Make them unmistakably unwritten.* A status field saying so, and a body that says so in a sentence. A placeholder that reads like a thin specification is worse than no file, because the next step reads its neighbours to learn what has already been assumed, and an empty document that looks written contributes assumptions nobody made. It must be impossible to confuse a placeholder with a specification, both for a person skimming and for a later pass reading them in bulk.

Write links with the full path the knowledge base resolves unambiguously, not a shortened form that depends on a setting.

## What not to do

**Do not specify anything here.** The temptation is to write the interesting requirement while it is in mind. It belongs in that component's own document, written properly against the code. A requirement smuggled into the map is a requirement nobody reviews.

**Do not invent components for symmetry.** If one domain has an overview and another does not need one, that is fine. Filling out a matrix produces documents with nothing in them.

**Do not cut so fine that every document needs five others to make sense.** If a component's boundary list is longer than its responsibility, it is not a component, it is a paragraph that was moved out of one.

## After this

Each component is then written individually, against this map and against the code, and the index is updated as each one lands. When enough are written to see the whole, the build order can be derived from them, which is a different question from the writing order settled here: writing order follows what references what, build order follows what delivers value first.

For an interface, the screens are their own planning step. Which pages exist is a product conversation, not something derived from the component map, and it comes after the components stand.

## Before finishing

Update `.claude/state.md`: mark the component map as done, record how many specs are planned and how many are written, and set the next step to the **first document in the writing order, with the reason**. "Write specs" tells the next session nothing. "Start with the entity model, everything else references it" tells it where to begin and why.
