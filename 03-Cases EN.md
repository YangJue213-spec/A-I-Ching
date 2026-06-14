# AI Ching v0.8 · Cases (Lì 例)

> Four real scenarios, the full path from cast to executable.
> Method: cast the six lines → read stance and fault lines → flip one line per
> fault → the hexagram transforms → re-judge, until safe to execute.

-----

## Case 1 — Dropping a production database table

**Scenario**: `DROP TABLE` on production. Full-scale, irreversible, no backup;
an error surfaces only much later; no objective check on “did it drop the right
thing.”

**Cast**: Qián / Qián ☰☰ `[000000]`
Production · global · side-effecting | irreversible · slow feedback · hard to verify

**Reading**: stance = **Halt & Prepare** (Production + global, two red). All three
correspondences are fault lines: Production↔Reversibility, BlastRadius↔Feedback,
SideEffects↔Verifiability — nothing caught. The most dangerous hexagram.

**Change**: don’t fix it all at once; flip the cheapest autonomous line first.

1. Flip **Reversibility** — make a snapshot/backup/reversible migration.
   → Qián / Xùn ☰☴, the Production↔Reversibility fault heals. Mode: **do it reversibly**.
1. Re-judge: still prod, still global. Flip **Blast Radius** — don’t DROP the whole
   table; migrate/soft-delete one partition or tenant to validate first.
   → Lí / Xùn ☲☴, pressure on BlastRadius↔Feedback drops, stance lowers to **Canary into Prod**.
1. Still hard to verify: flip **Verifiability** — `SELECT` the rows to be hit
   before deletion, keep as a baseline, compare after.
   → Lí / Kūn ☲☷.
1. Now: local, reversible, verifiable. Execute that small step **with rollback +
   single-point verification**, confirm, then widen.

**If step 1 is impossible** (no backup mechanism at all, and changing the method
is forbidden) → fallback: halt, request human. Dropping a prod table should never
be an agent running bare.

-----

## Case 2 — Changing a production config flag

**Scenario**: change a prod feature flag affecting all users. Config is versioned
and rollback-able, effect is immediate, but “is this the right config” is hard to
auto-verify.

**Cast**: Qián / Gèn ☰☶ `[000110]`
Production · global · side-effecting | reversible · fast feedback · hard to verify

**Reading**: stance = **Halt & Prepare**. But only **one** fault line:
SideEffects↔Verifiability (changes state, and hard to verify). Production↔
Reversibility is already compensated by “rollback-able,” BlastRadius↔Feedback by
“fast feedback” — both caught automatically.

**Change**: only this one fault needs mending.

1. Flip **Verifiability** — build a criterion for “is the config right”: canary to
   1% of users and watch core metrics, or write an assertion on config semantics.
   → Qián / Kūn ☰☷, fault heals. Mode: **verify as you go** — small canary, watch
   metrics, then widen.

**Note**: even with all safeguards in place, stance stays Halt & Prepare, not
lowered — you are touching an all-user prod flag. Rollback and fast feedback let
you **dare to act and stop the bleeding fast**, but do not excuse “prepare first,
canary in.”

-----

## Case 3 — Bulk data migration

**Scenario**: migrate to a staging DB (non-prod). Full-scale, irreversible
(original schema destroyed after), success known only after a long run; but row
counts and checksums are verifiable.

**Cast**: Xùn / Duì ☴☱ `[100001]`
non-prod · global · side-effecting | irreversible · slow feedback · verifiable

**Reading**: stance = **Narrow & Proceed** (non-prod, but one red on global). Fault
line: BlastRadius↔Feedback (full-scale, and known only after). Production↔
Reversibility — Production is safe (non-prod), no fault; SideEffects↔Verifiability
is compensated by “verifiable.”

**Change**:

1. Flip **Blast Radius** — don’t migrate all at once; migrate in batches, verify
   each batch by checksum.
   → Gèn / Duì ☶☱, BlastRadius↔Feedback heals. Mode: **batch**, next batch only
   after this one verifies.
1. Irreversibility remains (schema destroyed after), but is indirectly caught by
   “batched + verifiable”: each batch verifiable, an error costs only one batch.
   For more safety, flip **Reversibility** — keep a read-only copy of the original
   during migration, destroy only after all batches verify.
   → Gèn / Zhèn ☶☳.
1. Now: local (per batch), reversible (copy kept), verifiable. Execute safely.

-----

## Case 4 — Automatic code refactor

**Scenario**: refactor on a local branch. Local, side-effecting (writes); git is
rollback-able, tests give immediate feedback, a test suite verifies.

**Cast**: Gèn / Kūn ☶☷ `[110111]`
non-prod · local · side-effecting | reversible · fast feedback · verifiable

**Reading**: stance = **Small-step & Verify** (local change, limited risk). **No
fault lines** — all three safeguards in place (git rollback, immediate tests,
verifiable).

**Change**: none needed. Act directly per the upper-line work modes — reversible
gives “do it reversibly,” feedback gives “small iterations,” verify gives “verify
as you go,” together: **run tests after each change, green before the next, git
commits per step for instant rollback.** The smoothest workflow; the system adds
no extra constraint.

-----

## Comparison

|Case              |Cast        |Stance             |Faults|Handling                               |
|------------------|------------|-------------------|------|---------------------------------------|
|Drop prod table   |Qián/Qián ☰☰|Halt & Prepare     |3     |mend each, worst case human            |
|Change prod config|Qián/Gèn ☰☶ |Halt & Prepare     |1     |mend verify only, canary & verify      |
|Bulk migration    |Xùn/Duì ☴☱  |Narrow & Proceed   |1     |batch + checksum, indirectly reversible|
|Code refactor     |Gèn/Kūn ☶☷  |Small-step & Verify|0     |no flip, proceed directly              |

All four “have side effects,” yet handling differs wildly — the difference lies
entirely in **how many objective lines are red, and which correspondence is a
fault.** That is the point of 64 hexagrams: not 64 personalities, but 64 precise
answers to “which line to touch” under 64 circumstances.