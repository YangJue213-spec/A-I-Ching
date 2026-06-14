# AI Ching v0.8 · Commentary (Zhuàn 传)

> Why the Classic is designed the way it is. First its Way (the principle of
> change), then its structure (trigrams, correspondence, three powers), then
> its rules — each born from a real pitfall.

-----

## The Principle: State and Change

The essence of the I Ching is not prediction. It is **describing which state
you are in now, and indicating which state you can move to next.**

Those who made the *Yi* were finite individuals. They could not exhaust the
world’s possibilities, nor foresee all consequences of an act. So they gave up
“predicting the whole” — a conceit only an omniscient being could afford — and
did the two things they could: discern **which hexagram they stand in now**,
then judge **which better hexagram to move toward next**. A hexagram is a state;
a changing line is a migration. A finite person, by stepping “state → better
state,” seeks a safe path through an unknowable world.

An agent is no different. It cannot foresee all branches of an operation, nor
enumerate every consequence. What it can do is exactly what the diviner did:
identify its current state (cast the hexagram), then move to a lower-risk state
(change a line), observe again, and move again.

**This is why the system is built on *change*, not *scoring*.** Scoring pretends
you can put a precise number on risk — the voice of an omniscient. A changing
line only admits “this is safer than that” — the honesty of a finite knower.
AI Ching does not seek an optimal solution for each operation; it only moves the
agent from its current hexagram toward a better one. “Don’t fix everything at
once; just move one step toward a better hexagram” is not engineering
compromise — it is epistemic honesty.

And so, **when a value is uncertain, take the danger side**: a finite knower
facing the unknown, defaulting to the more dangerous state, is both safe and
honest.

-----

## Trigrams: Circumstance and Cognition

A hexagram’s six lines split into a lower and an upper trigram, describing two
utterly different things.

**The lower trigram is “circumstance” — the objective world I am in.** Whether
it’s production, how wide the blast radius, whether the action has effects:
these are the given conditions the agent cannot change, facts code can directly
detect. Circumstance does not shift with my optimism or pessimism.

**The upper trigram is “cognition” — my awareness of and preparation for that
world.** Whether I can undo it, how soon I’ll know, whether I can verify: these
the agent can marshal and build — make a backup, add a metric, write a checker,
and cognition strengthens.

A hexagram is the configuration of circumstance and cognition at this moment.
The Classic’s iron rule — better safeguards never downgrade the stance — is
rooted here: **circumstance is objective; cognition is subjective, and the
subjective is precisely what most easily deceives itself.** Letting “I think I
can control it” override “I am in fact in danger” is letting cognition disturb
circumstance. So circumstance sets the floor; cognition only reinforces above
it, never relaxes it.

-----

## Correspondence: the Tension Between Circumstance and Cognition

The *Yi* has “correspondence”: line 1 with 4, 2 with 5, 3 with 6, answering each
other. The system borrows this to carry a depth: **does each objective risk
(lower line) have a subjective preparation (upper line) answering it?**

Three correspondences, each a “risk source ↔ safeguard”:

- 1–4 (Production ↔ Reversibility): in the danger of production, is there an
  “I can undo it” to answer?
- 2–5 (Blast Radius ↔ Feedback): for breadth of impact, is there an
  “I’ll know early, can stop the bleeding”?
- 3–6 (Side Effects ↔ Verifiability): for changing the world, is there a
  “I can verify if it went wrong”?

If they answer (correspond), the risk is held by cognition — the fault heals,
and you may carry the risk forward. If they do not (both dangerous), the risk is
laid bare with nothing to catch it: that is a fault line, to be mended first.
**Correspondence describes exactly the one-to-one tension between circumstance
and cognition** — it does not look at a lone line’s danger, only at whether the
danger is caught by its corresponding preparation. This is also why the Classic
“mends only fault lines, never lists everything”: what matters is never where
risk exists, but where risk has no answering catch.

-----

## Three Powers: Earth, Human, Heaven

The six lines, bottom to top, also divide into three powers of two lines each —
another, vertical reading (running alongside the horizontal correspondence, just
as the old *Yi* held both).

- **Earth** (line 1 Production, line 2 Blast Radius): where I stand. Most
  objective, read directly by code.
- **Human** (line 3 Side Effects, line 4 Reversibility): the nature and retreat
  of my action. Semi-objective — the action is mine, but its consequence is
  constrained by Earth.
- **Heaven** (line 5 Feedback, line 6 Verifiability): my grasp of the outcome.
  Most subjective.

Objectivity decreases from bottom to top: Earth is hard fact, Human is my doing,
Heaven is my judgment.

**Line 3 (Side Effects) is pivotal — it is the top line of the lower trigram and
the start of the Human power.** It serves two roles at once: downward, its value
depends on Earth (the same operation differs in weight landing on prod-global vs.
local-temp, so lines 1 and 2 must be taken first); upward, it opens Human — Side
Effects asks “will this act change the world,” the first stroke of action, paired
with line 4 “if changed, can it be undone” to constitute the Human power.

Side Effects is the “gate” precisely because it stands at the Earth–Human border:
the very pass from “objective circumstance” to “nature of the action.” Gate shut
(no side effect), nothing above Human and Heaven need unfold — proceed directly;
gate open (has side effect), you enter the Human and Heaven of “how to do this
safely.” Linking above and below, it is the hinge.

-----

## Rule Notes

> Below, each operational rule of the Classic is explained by the real pitfall
> behind it.

### Why “circumstance,” not “task,” leads

The earliest version gave “environment” its own line, and hit a dead end: the
real working environment is permanently “production, no sandbox,” so that line is
forever at its most dangerous value, and the system forever outputs “halt,”
unable to work. The lesson: **a constant variable carries no information and
should not enter the hexagram.** The fix was to lower the unit of judgment from
“environment” to “operation.”

### Why Side Effects is the leading line

An operation with no side effect — read a doc, read config, dry-run — changes
nothing no matter how dangerous the environment; worst case is a wasted trip. So
Side Effects is a gate: **no side effect, the execution layer proceeds directly,
the rest of the lower trigram need not be examined.** This frees half the
hexagrams (32) from the caution machinery, spending attention only on operations
that truly change the world.

### Why safeguards cannot downgrade the stance

The lower trigram is code-confirmed fact; in the upper trigram, reversibility and
verifiability largely depend on the agent’s own estimate. And **the agent’s
estimate of its own grasp is exactly the most over-confident link.** Letting
“I feel I can undo it, can verify it” cancel “I am operating on prod at full
scale” hands the reins to the side most likely to misjudge. Hence: **objective
circumstance sets the floor, subjective safeguards add on top but never dig
below.** This is “safety can tighten but never relax” cast into structure.

### Why only fault lines

An early version opened a prescription for every dangerous line, flattening all
six into a long risk checklist — exactly the “ever-accreting rule engine” to
avoid. Real wisdom is not “list all risks” but “know which one to touch.” Only a
fault line — both source and safeguard failed — leaves risk truly bare. Watching
only faults turns the system from a checklist back into a verdict.

### Why flip the safeguard first, and prefer autonomy

Mending a fault has two directions: remove the risk source (flip the lower line)
or restore the safeguard (flip the upper line). Lower lines are objective
circumstance, mostly task constraints, hard to change; upper lines are
safeguards, almost always buildable by the agent itself — make a backup, add a
metric, write a checker. So **prefer what you can do yourself, usually restoring
the safeguard.** Behind this is the core wish: let the agent move toward a safer
hexagram on its own; human help is a fallback, not a first resort.

### Why Proceed is still governed by the upper lines

Side effects only remove *execution risk* (can’t break the environment). There
remains an independent *cognitive risk*: a no-side-effect analysis can still have
slow feedback, be hard to verify, or run its reasoning down a path it can’t back
out of. So Proceed ≠ hands-off. The upper trigram always sets the work mode, only
its object switches: with side effects it governs “how to do this world-changing
op safely”; without, “how to think reliably on this non-changing but possibly
wrong cognitive task.” Same lines, same spirit (reversible = keep a retreat,
feedback = don’t race, verify = corroborate), now freed from a “side-effect-only”
switch — always working. This also gives the 32 no-side-effect hexagrams distinct
cognitive work modes, no longer a uniform “Proceed.”

-----

## In One Line

The Classic is short, the hexagrams many. The core is a dozen rules — side
effects as gate, circumstance sets stance, safeguards never relax, mend only
faults, flip prefers autonomy, Proceed isn’t hands-off — and the 64 hexagrams are
their unfolding. This is the very form of the I Ching: yin-yang, trigrams, and
the changing line are the core; the sixty-four are the derivation.