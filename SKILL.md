-----

## name: ai-ching
description: >
State-driven safety check before an agent acts. Use this skill BEFORE
executing any operation that may change state (writing/deleting files,
database ops, deployments, API calls with side effects, infra changes,
shell commands). It casts a six-line “hexagram” from the current
operation+environment, then tells the agent what stance to take, which
risks are uncovered (fault lines), how to mend them, and how to execute.
Trigger on: “should I run this”, “is it safe to”, deploy/migrate/delete/
drop/push/publish, or any irreversible or production-facing action.

# AI Ching — State-Driven Safety Check / 行动前状态判读

A safety pre-flight for autonomous agents, structured like the I Ching.
You DETECT six lines from the current context, then JUDGE with fixed rules.

> Detection is yours (it depends on this environment). Judging is fixed —
> do not improvise it; it mirrors `src/reference.py`, the canonical answer.

-----

## When to use / 何时使用

Run this BEFORE any operation that could change the world: file writes/deletes,
DB writes/migrations, deployments, infra (k8s/terraform) changes, shell
commands with effects, external API calls that mutate state.
Skip only for pure reads/queries you are certain have no side effect — but
even then, run it: the side-effect line will simply let you proceed.

-----

## Step 1 — Detect the six lines / 探测六爻

Six lines, bottom to top, grouped in Three Powers (Earth/Human/Heaven).
**1 = yin = SAFE, 0 = yang = DANGER.**

> **Burden of proof is on the SAFE side.** Do not assume safe by default.
> Unless you can POINT TO concrete evidence that a line is safe, mark it
> DANGER (0). For every line, STATE YOUR EVIDENCE for the value you assign.
> 举证责任在安全侧：除非能指出确证安全的证据，否则判危险(0)，并为每爻说明依据。

### Earth 地 (objective; detect from the environment)

- **Line 1 — Production 生产环境** (non-prod=1 / prod=0)
  Detect: env vars (`NODE_ENV`/`APP_ENV` for prod), DB connection string /
  API endpoint / domain pointing at production, git branch = main/master.
  Any production signal, or cannot tell → 0.
- **Line 2 — Blast Radius 波及范围** (local=1 / global=0)
  Detect: scope of the target — single file/record/tenant = local; whole
  table / all users / shared trunk / public interface = global. Look for
  `--all`, missing `WHERE`, wildcard paths, broadcast topics. Cannot tell → 0.

### Human 人 (semi-objective; the action itself)

- **Line 3 — Side Effects 副作用** (none=1 / has=0)
  Detect **after** lines 1&2, in their context. Read/query/dry-run/analyze →
1. Write/delete/migrate/publish/stateful external call → 0. (Line 3 is the
   gate between Earth and Human — it depends on where & how wide the op lands.)
   Cannot tell → 0.
- **Line 4 — Reversibility 可逆性** (reversible=1 / not=0)
  Detect: is there an undo path — backup/snapshot/transaction/git commit/
  reversible migration → 1; overwrite/physical delete/force-push/already-
  published → 0. If no side effects, this means “cognitive reversibility”
  (can the reasoning be backed out). Cannot tell → 0.

### Heaven 天 (subjective; your grasp of the outcome)

- **Line 5 — Feedback Latency 反馈延迟** (fast=1 / slow=0)
  Detect: how soon will you know it’s right/wrong — sync/seconds → 1;
  async/long pipeline/days → 0. No timely signal available → 0.
- **Line 6 — Verifiability 可验证性** (verifiable=1 / hard=0)
  Detect: is there a runnable correctness standard — tests/assertions/
  checksums/baseline → 1; purely subjective output → 0. (No standard yet but
  buildable still counts as 0 now — building one is a “flip”, see Step 4.)
  Cannot tell → 0.

**Output of Step 1:** six bits `[y1..y6]` plus one line of evidence each.

-----

## Step 2 — Stance / 定姿态

The side-effect line is the gate:

- **Line 3 = none (1)** → **Proceed 放行** (execution layer). Skip to Step 5.
- **Line 3 = has (0)** → count red lines among Production(1)+BlastRadius(2):
  - both red → **Halt & Prepare 停下准备**
  - one red → **Canary into Prod 灰度入生产** (prod red) / **Narrow & Proceed 缩范围推进** (global red)
  - none red → **Small-step & Verify 小步快验**

**Iron rule:** safeguards (upper lines) NEVER downgrade the stance. Objective
context sets the floor; subjective safeguards can only tighten, never relax.
保障再好不下调姿态。

-----

## Step 3 — Fault lines / 找应位裂缝

Three correspondences, each a “risk source ↔ safeguard”:

|Risk source (lower)|Safeguard (upper)|
|-------------------|-----------------|
|Production 生产      |Reversibility 可逆 |
|Blast Radius 全局    |Feedback 反馈      |
|Side Effects 副作用   |Verifiability 验证 |

A correspondence where BOTH lines are red (0) = a **fault line** — risk fully
uncovered. Only fault lines demand action; isolated red lines are governed by
the stance. 只处理裂缝，孤立危险爻看姿态。

-----

## Step 4 — Repair: move toward a better hexagram / 翻爻

Do not try to fix everything at once. **Mend every fault line by flipping one
of its lines**, so no fault stays uncovered. You may do it stepwise.

Priority:

1. **Flip the line you can do yourself, no human needed** (usually restoring a
   safeguard): build backup (L4), narrow scope (L2), write a checker (L6),
   add instrumentation (L5), run in shadow env (L1).
1. If both lines of a fault are un-flippable by you → **detour: flip another
   autonomous line** to lower overall risk, then re-judge.
1. If nothing can be flipped autonomously → **Halt, request human**.

Side Effects (L3) is usually intrinsic (it’s what the op does) and only
removable if the goal can be met read-only/dry-run.

This is the core “Change” idea: you cannot foresee everything; you can only
move from this state to a safer one, then look again. 不求一步到位，只求朝更好的卦移动一步。

-----

## Step 5 — Work mode / 定工作模式

For each red (0) UPPER line, impose a constraint. With side effects it shapes
EXECUTION; without, it shapes COGNITION (the result may still be wrong):

|Line           |Execution (has side effect)                |Cognition (no side effect)                            |
|---------------|-------------------------------------------|------------------------------------------------------|
|Reversibility=0|Do it reversibly, roll back on error       |Keep it retraceable, don’t pass the point of no return|
|Feedback=0     |Batch, confirm each batch                  |Confirm in segments, don’t stack on unconfirmed       |
|Verifiability=0|Verify as you go, unverified not downstream|Flag & corroborate, seek review on important claims   |

Proceed never means hands-off: upper lines always govern HOW to act.

-----

## Optional: deterministic check / 确定性核对

To verify your judging matches the canonical rules, run:

```
python src/reference.py 010011   # your six bits, bottom to top
```

It prints stance, fault lines, repairs, and work mode. If your reasoning
disagrees with it, trust `reference.py` — detection is yours, judging is fixed.

-----

## One-line summary

Detect six lines (evidence on the safe side) → side-effect gate → stance from
objective context (never relaxed) → mend fault lines by the cheapest
autonomous flip → impose work mode from red safeguards → fall back to human
only when no autonomous move remains.