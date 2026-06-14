# AI Ching v0.8 · Classic (Jīng 经)

> The agent’s pre-flight decision layer. This is the executable ruleset, for
> runtime reading. For rationale and philosophy see the Commentary, for worked
> examples the Cases, for the full table the Appendix.

-----

## The Six Lines and How to Detect Them

Six lines, bottom to top, in three powers. **1 = safe, 0 = danger. Whenever a
line’s value is uncertain, take the danger side (0).**

### Earth 地 (context · objective · detectable by code)

**Line 1 — Production** (non-prod = 1 / prod = 0)
Detect: read env vars (`NODE_ENV`/`APP_ENV`/`ENV` for prod/production); check
DB connection string, API endpoint, or domain pointing at production; check git
branch = main/master. Any production signal → 0. Cannot tell → 0.

**Line 2 — Blast Radius** (local = 1 / global = 0)
Detect: coverage of the target — single file/record/tenant = local; whole
table / all users / shared trunk / public interface = global. Read range flags
in the operation (`--all`, missing `WHERE`, wildcard paths, broadcast topics).
Cannot tell → 0.

### Human 人 (action · semi-objective)

**Line 3 — Side Effects** (none = 1 / has = 0)
Detect **after** lines 1 and 2, in their context. Read/query/dry-run/analyze →
none = 1; write/delete/migrate/publish/stateful external call → has = 0. The
same write is heavier when it lands on prod + global (line1=0, line2=0). Cannot
tell → 0.

**Line 4 — Reversibility** (reversible = 1 / not = 0)
Detect: is there an undo path — backup/snapshot/transaction/git commit/
reversible migration → 1; overwrite/physical delete/force-push/already
published → 0. With no side effects, this means “cognitive reversibility”
(whether the reasoning can be backed out). Cannot tell → 0.

### Heaven 天 (cognition · subjective)

**Line 5 — Feedback Latency** (fast = 1 / slow = 0)
Detect: how soon you’ll know right from wrong — sync return / second-level
visible → 1; async / long pipeline / surfaces in days → 0. No timely
observation available → 0.

**Line 6 — Verifiability** (verifiable = 1 / hard = 0)
Detect: is there a runnable correctness standard — tests/assertions/checksums/
baseline → 1; purely subjective output / no objective right-or-wrong → 0.
(No standard yet but buildable still counts as 0 now — building one is a “flip”,
see step 4.) Cannot tell → 0.

Lines 1·2·3 form the lower trigram; 4·5·6 the upper trigram. Kūn ☷ (111) is
safest, Qián ☰ (000) most dangerous.

-----

## Reading Procedure

**1. Take Earth first, then judge the first Human line.** Fix line 1 and line 2,
and **in that context** judge line 3 (Side Effects is the gate between Earth and
Human — it depends on the prior two).

**2. Side Effects is the gate:**

- Line 3 = none → execution-layer **Proceed**; skip to step 5.
- Line 3 = has → count red lines among Production + Blast Radius:
  - both red → **Halt & Prepare**
  - one red → **Canary into Prod** (prod red) / **Narrow & Proceed** (global red)
  - none red → **Small-step & Verify**

**3. Iron rule: better safeguards (upper trigram) never downgrade the stance.**
Objective context sets the floor; subjective safeguards can only tighten, never
relax.

**4. Find fault lines, mend each.** Three correspondences, each a
“risk source ↔ safeguard”: Production↔Reversibility, BlastRadius↔Feedback,
SideEffects↔Verifiability. A correspondence with both lines red = a fault line.
**Every fault line must be mended by flipping one of its lines so no risk stays
uncovered — you may do it stepwise.**
Flip priority: ① prefer a line the agent can flip itself (usually restoring a
safeguard: build backup / add instrumentation / write a checker); ② if both
lines of a fault are un-flippable → detour: flip another autonomous line to
lower overall risk; ③ if nothing is autonomously flippable → halt, request human.

**5. Upper lines set the work mode (active whether or not there are side
effects):** for each red (0) upper line, impose a constraint — on *execution*
when there are side effects, on *cognition* when there are none:

|Line           |Execution mode (has side effect)           |Cognitive mode (no side effect)                |
|---------------|-------------------------------------------|-----------------------------------------------|
|Reversibility=0|Do it reversibly, roll back on error       |Keep it retraceable, checkpoint key judgments  |
|Feedback=0     |Batch, confirm each batch                  |Confirm in segments, don’t stack on unconfirmed|
|Verifiability=0|Verify as you go, unverified not downstream|Flag & corroborate, review important claims    |

Proceed never means hands-off: the upper trigram always governs *how* to act.

-----

*End of rules.*