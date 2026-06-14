# AI Ching

**A State-Driven Safety Framework for AI Agents**
*Inspired by the structure of the I Ching, designed for autonomous agent governance.*

> ⚠️ **Experimental.** This is a working framework, not a finished theory.
> It has been reasoned through but not battle-tested in production.
> Feedback, counter-examples, and broken cases are exactly what it needs.

中文版见下方 ⬇︎ [中文](#中文)

-----

## Problem

Agents are good at knowing **how** to do something.
They are bad at knowing **when they should** — and how cautiously.

The same `delete` is trivial in a sandbox and catastrophic in production.
A pure read is harmless anywhere. Most agent harnesses don’t make this
distinction structurally; they either over-restrict everything or trust the
model’s in-the-moment judgment, which skews optimistic precisely when it
shouldn’t.

## Solution: State-Driven Safety

AI Ching reads the current **state** of an operation as six binary lines
(a *hexagram*), then prescribes a **stance** and concrete actions. It does not
predict all outcomes — it identifies where you are, and moves you toward a
safer state, one change at a time. That step-wise “change” is the core idea
borrowed from the I Ching.

## Core Concepts

Six lines, bottom to top, in three powers. **1 = safe, 0 = danger.**
When a line’s value is uncertain, take the **danger** side.

|Power                                      |Line              |Meaning                   |
|-------------------------------------------|------------------|--------------------------|
|**Earth** 地 (objective, detectable by code)|1 Production      |prod or not               |
|                                           |2 Blast Radius    |local or global           |
|**Human** 人 (the action)                   |3 Side Effects    |does it change the world  |
|                                           |4 Reversibility   |can it be undone          |
|**Heaven** 天 (your grasp)                  |5 Feedback Latency|how soon you’ll know      |
|                                           |6 Verifiability   |can correctness be checked|

- **Lower trigram (1-3) = context** (what I’m in) — sets the floor of caution.
- **Upper trigram (4-6) = safeguards** (what I’ve prepared) — can only tighten, never relax the stance.
- **Side Effects is the gate**: no side effect → proceed; only side-effecting ops get the full treatment.
- **Fault line**: a correspondence (Production↔Reversibility, BlastRadius↔Feedback, SideEffects↔Verifiability) where *both* lines are red. That’s uncovered risk — the only thing you must fix.
- **Repair**: flip one line of each fault toward safe, preferring what the agent can do itself (build a backup, narrow scope, write a checker). Move to a better hexagram, then re-judge.

## Usage

AI Ching separates **detection** (flexible, per-environment) from **judging**
(fixed). Three ways to use it:

1. **Autonomous** — the agent reads [`SKILL.md`](SKILL.md) and does
   detection → judging → execution itself. Simplest; judging is improvised.
1. **Deterministic judging (recommended for risky ops)** — detect the six
   lines (by AI or by hand), feed them to [`src/reference.py`](src/reference.py),
   and have the agent **execute strictly according to the hexagram and
   prescription it outputs**. Judging is locked to the canonical rules; the
   agent does not improvise the “how cautious” decision.
   
   ```bash
   python src/reference.py 010011    # six bits, bottom to top
   ```
1. **Manual casting** — a human sets the six lines, runs `reference.py`, and
   the agent follows the prescription. Judgment stays with the human.

> The point: **judging should not be left to the agent’s free improvisation.**
> Let `reference.py` (or a human) produce a definite hexagram + prescription,
> and have the agent execute against it.

## Example: dropping a production table

Detected: prod, global, side-effecting, no backup, slow feedback, no check →
`[000000]`, hexagram Qián/Qián ☰☰ → **Halt & Prepare**, three fault lines.

Repair, one flip at a time:

1. flip **Reversibility** → make a snapshot/backup → ☰☴
1. flip **Blast Radius** → drop one partition first, not the whole table → ☲☴
1. flip **Verifiability** → SELECT the rows to be hit, keep as baseline → ☲☷

Now: local, reversible, verifiable — execute that small step with rollback and
verification, confirm, then widen. If step 1 is impossible (no backup
mechanism at all) → **halt, request human**. (Full walk-through in
[`docs/03-Cases_EN.md (EN) / docs/03-Cases_ZH.md (中文)`](docs/03-Cases_EN.md (EN) / docs/03-Cases_ZH.md (中文)).)

## Limitations / Open Questions

This is where help is wanted. Known gaps:

- **Single-operation granularity.** The model judges one operation at a time.
  **Multi-agent / concurrent** settings — where blast radius and side effects
  compound across actors — are not yet modeled. Open.
- **Detection reliability.** Side-effect and reversibility detection lean on
  recognizing the operation type; novel tools / MCP calls may be misjudged.
- **Self-detection optimism.** When the same agent both detects and acts, it
  may skew lines toward “safe”. Mitigated by “burden of proof on the safe
  side” + deterministic judging, not eliminated.
- **Not production-validated.** No real-world incident data yet.
- **Untested domains.** Kubernetes changes, large migrations, MCP tool calls —
  each needs cases run and likely model fixes. PRs with broken cases welcome.

## Structure

```
SKILL.md                 # agent-facing instructions (detect + judge)
src/reference.py         # deterministic judging core (MIT)
docs/01-经.md            # Classic — the rules, for runtime (CC BY 4.0)
docs/02-传.md            # Commentary — why it's designed this way
docs/03-Cases_EN.md (EN) / docs/03-Cases_ZH.md (中文)            # Cases — worked examples
docs/附录-64卦查表.md     # Appendix — all 64 hexagrams (lookup table)
```

## License

- **Code** (`src/`): MIT — see <LICENSE>.
- **Docs** (`docs/`): CC BY 4.0 — see <docs/LICENSE-docs>.

## Appendix: relationship with the I Ching

AI Ching borrows the *structure*, not the divination: six lines from two
trigrams, the bottom-to-top reading, the **correspondence** between lower and
upper lines, and above all the idea of **change** — a state, and where it
moves next. Where the classic I Ching lets hexagram *names* carry meaning,
AI Ching deliberately drops that: meaning lives entirely in the six line
values and the rules over them. The I Ching was a finite mind’s way to face an
unknowable world by reading the present and the next step. An agent faces the
same condition. That parallel is the whole reason for the form.

-----

<a name="中文"></a>

# AI Ching（中文）

**面向 AI Agent 的状态驱动安全框架**
*借鉴易经结构，用于自主 Agent 的行动治理。*

> ⚠️ **实验性项目。** 这是一个可用的框架，而非完成的理论；经过推演但未经生产检验。
> 最需要的正是反馈、反例和跑不通的案例。

## 问题

Agent 擅长知道**怎么做**，却不擅长判断**该不该做、该多谨慎**。
同一个 `delete`，在沙箱里无足轻重，在生产里可能是灾难；纯读取在哪都无害。
多数 Agent 框架不从结构上区分这些——要么一刀切全部限制，要么信任模型当场的判断，
而这种判断恰恰在最不该乐观的时候偏乐观。

## 方案：状态驱动安全

AI Ching 把一个操作的当前**状态**读成六个二进制爻（一个**卦**），据此给出**姿态**
和具体动作。它不预测所有后果——只认清你此刻在哪，并带你一步步移向更安全的状态。
这种”步步迁移”正是从易经借来的核心思想。

## 核心概念

六爻由下到上，分三才。**1＝安全，0＝危险；取值不确定时取危险侧。**

|三才             |爻     |含义    |
|---------------|------|------|
|**地**（客观，代码可探测）|1 生产环境|是否生产  |
|               |2 波及范围|局部或全局 |
|**人**（动作本身）    |3 副作用 |是否改变世界|
|               |4 可逆性 |能否撤销  |
|**天**（认知把握）    |5 反馈延迟|多久知道结果|
|               |6 可验证性|能否验证对错|

- **下卦(1-3)＝处境**（我在什么环境）——决定谨慎度的地板。
- **上卦(4-6)＝保障**（我准备了什么）——只能加码，不能下调姿态。
- **副作用是大门**：无副作用直接放行；只有会改变世界的操作才走完整流程。
- **应位裂缝**：一对应位（生产↔可逆、全局↔反馈、副作用↔验证）中两爻同时危险，
  即风险裸露——这是唯一必须处理的地方。
- **翻爻**：把每条裂缝翻通一爻（优先 Agent 自己能做的：建备份、缩范围、写校验），
  移向更好的卦，再重判。

## 用法

AI Ching 把**探测**（灵活、因环境而异）与**判读**（固定）分开。三种用法：

1. **全自动**——Agent 读 [`SKILL.md`](SKILL.md)，自己探测→判读→执行。最省事，但判读是即兴的。
1. **确定性判读（高危操作推荐）**——探测出六爻（AI 或人工），喂给
   [`src/reference.py`](src/reference.py)，**Agent 严格按它输出的卦象与处方执行**。
   判读锁定在固定规则上，Agent 不自由发挥”该多谨慎”。
   
   ```bash
   python src/reference.py 010011    # 六爻，由下到上
   ```
1. **纯人工起卦**——人定六爻、跑 reference.py、Agent 照处方执行。判断权在人。

> 核心：**判读不交给 Agent 自由发挥。** 由 `reference.py` 或人工产出确定的卦象与处方，
> Agent 据此执行。

## 局限与开放问题

这正是需要帮助之处。已知缺口：

- **单操作粒度**：一次只判一个操作。**多 Agent／并发**场景下副作用与波及范围会跨主体叠加，尚未建模。
- **探测可靠性**：副作用、可逆性的探测依赖识别操作类型，新型工具／MCP 调用可能误判。
- **自探测乐观偏向**：同一 Agent 既探测又执行时，可能把爻判向”安全”。靠”举证责任在安全侧”+确定性判读缓解，未根除。
- **未经生产验证**：尚无真实事故数据。
- **未测领域**：K8s 变更、大型迁移、MCP 调用等都需跑卦验证、很可能要修模型。欢迎提交跑不通的案例。

## 许可

- **代码**（`src/`）：MIT，见 <LICENSE>。
- **文档**（`docs/`）：CC BY 4.0，见 <docs/LICENSE-docs>。

## 附录：与易经的关系

AI Ching 借的是易经的**结构**，不是占卜：两卦叠成六爻、自下而上读、上下爻的**应位**、
以及最重要的**变**——一个状态，与它的下一步去向。古易经让卦**名**承载含义，
AI Ching 刻意舍弃卦名：含义全在六爻取值与其上的规则。易经是认知有限的古人面对
不可知世界时，读懂当下与下一步的方式；Agent 面对的正是同样的处境——这层同构，
正是采用这一形式的全部理由。