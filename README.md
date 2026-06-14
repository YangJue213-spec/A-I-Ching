# AI Ching

**A State-Driven Safety Framework for AI Agents**
*Inspired by the structure of the I Ching, designed for autonomous agent governance.*

> ⚠️ **Experimental.** This is a working framework, not a finished theory.

中文版见下方 ⬇︎ [中文](#中文版)

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
try to predict all outcomes — it identifies where you are, and moves you toward
a safer state. That step-wise *change* is the core idea borrowed from the
I Ching, and the reason for the form.

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

## The Four Structures

The framework is not a flat checklist. Its judgment comes from four structures
borrowed from the I Ching — this is the design philosophy in brief; the full
reasoning lives in the [Commentary](docs/02-Commentary_EN.md).

**1. Trigrams — Circumstance & Cognition.**
The lower trigram (lines 1–3) is *circumstance*: the objective world I’m in,
which I cannot change and which code can detect. The upper trigram (lines 4–6)
is *cognition*: the preparation I can marshal — a backup, a metric, a checker.
**Circumstance sets the floor of caution; cognition can only tighten it, never
relax it** — because the subjective estimate of one’s own grasp is exactly what
most easily deceives itself. (This is why a “perfect safeguards” hexagram with a
dangerous context still won’t lower its stance.)

**2. Three Powers — Earth, Human, Heaven.**
The six lines stack into three powers of two, with objectivity decreasing
upward: Earth is hard fact, Human is my doing, Heaven is my judgment. Line 3
(Side Effects) sits at the Earth–Human border — its value depends on the
environment below it (the same write differs on prod-global vs. local-temp), yet
it opens the question of the action itself. That border position is why **Side
Effects is the gate**: no side effect, and nothing above needs to unfold —
proceed.

**3. Correspondence — risk source ↔ safeguard.**
Lines answer across the trigrams: 1–4, 2–5, 3–6, each a pair of
*risk source ↔ safeguard* (Production↔Reversibility, BlastRadius↔Feedback,
SideEffects↔Verifiability). The question each pair asks: does this objective
risk have a subjective preparation answering it? When **both** lines of a pair
are red, the risk is uncovered — a **fault line**. **Only fault lines demand
action**; an isolated red line whose partner compensates is already caught.

**4. Change — moving to a better state.**
A finite mind cannot foresee everything; it can only know where it stands and
move toward a better state, then look again. This is why the system is built on
the **changing line**, not on scoring. Scoring pretends risk has a precise
number (the voice of an omniscient); a changing line only claims “this is safer
than that” (the honesty of a finite knower). An agent faces the same condition
as the diviner — hence the form.

### How repair works

**Each fault line is mended by flipping one of its two lines** toward safe — you
need not flip both. But **every fault line must be mended; you don’t stop after
one.** Three faults means three flips (one per fault), not a single move and
done. Priority:

1. **Flip the line you can do yourself**, no human needed (usually restoring a
   safeguard: build a backup, narrow scope, write a checker).
1. If both lines of a fault are un-flippable by you → **detour: flip another
   autonomous line** to lower overall risk, then re-judge.
1. If nothing is autonomously flippable → **halt, request human**.

Each flip transforms the hexagram into a safer one; 

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
`[000000]`, hexagram Qián/Qián ☰☰ → **Halt & Prepare**, **three fault lines**.
Mend each, one flip per fault:

1. flip **Reversibility** → make a snapshot/backup → ☰☴
1. flip **Blast Radius** → drop one partition first, not the whole table → ☲☴
1. flip **Verifiability** → SELECT the rows to be hit, keep as baseline → ☲☷

Now: local, reversible, verifiable — execute that small step with rollback and
verification, confirm, then widen. If a flip is impossible (e.g. no backup
mechanism at all) → **halt, request human**. Full walk-through in
[Cases](docs/03-Cases_EN.md).

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
SKILL.md                          # agent-facing instructions (detect + judge)
src/reference.py                  # deterministic judging core (MIT)
docs/01-Classic_{EN,ZH}.md        # Classic — the rules, for runtime (CC BY 4.0)
docs/02-Commentary_{EN,ZH}.md     # Commentary — why it's designed this way
docs/03-Cases_{EN,ZH}.md          # Cases — worked examples
docs/Appendix-64-Hexagrams_{EN,ZH}.md  # Appendix — all 64 hexagrams (lookup)
```

All docs are bilingual: `_EN` English, `_ZH` 中文.

## License

- **Code** (`src/`): MIT — see <LICENSE>.
- **Docs** (`docs/`): CC BY 4.0 — see <docs/LICENSE-docs>.

## Appendix: relationship with the I Ching

AI Ching borrows the *structure*, not the divination: six lines from two
trigrams, the bottom-to-top reading, the **correspondence** between lower and
upper lines, and above all the idea of **change** — a state, and where it moves
next. Where the classic I Ching lets hexagram *names* carry meaning, AI Ching
deliberately drops that: meaning lives entirely in the six line values and the
rules over them. The I Ching was a finite mind’s way to face an unknowable world
by reading the present and the next step. An agent faces the same condition.
That parallel is the whole reason for the form.

-----

<a name="中文版"></a>

# AI Ching（中文）

**面向 AI Agent 的状态驱动安全框架**
*借鉴易经结构，用于自主 Agent 的行动治理。*

> ⚠️ **实验性项目。** 这是一个可用的框架，而非完成的理论

## 问题

Agent 擅长知道**怎么做**，却不擅长判断**该不该做、该多谨慎**。
同一个 `delete`，在沙箱里无足轻重，在生产里可能是灾难；纯读取在哪都无害。
多数 Agent 框架不从结构上区分这些——要么一刀切全部限制，要么信任模型当场的判断，
而这种判断恰恰在最不该乐观的时候偏乐观。

## 方案：状态驱动安全

AI Ching 把一个操作的当前**状态**读成六个二进制爻（一个**卦**），据此给出**姿态**
和具体动作。它不预测所有后果——只认清你此刻在哪，并带你移向更安全的状态。
这种步步**变**迁，正是从易经借来的核心思想，也是采用这一形式的理由。

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

## 四重结构

这套框架不是一张扁平的清单。它的判断力来自借自易经的四重结构——这里是设计哲学的
简述，完整推演见[传](docs/02-Commentary_ZH.md)。

**一、上下卦——境与识。**
下卦（爻1–3）是「境」：我所处、改变不了、代码能探测的客观世界。上卦（爻4–6）是
「识」：我能调动的准备——一个备份、一个指标、一个校验器。**境决定谨慎度的地板，识
只能加固、不能松绑**——因为对自身把握的主观估计，恰恰最易自欺。（这正是为什么一个
「保障齐备」却处境危险的卦，姿态仍不下调。）

**二、三才——地、人、天。**
六爻每两爻叠成一才，客观性自下而上递减：地是铁的事实，人是我的作为，天是我的判断。
爻3（副作用）站在地人交界——它的取值依赖下方的环境（同一写操作，落在生产全量与本地
临时，轻重不同），却又开启了对动作本身的追问。正是这个交界位置，使**副作用成为大门**：
无副作用，其上皆不必展开——放行。

**三、应爻——风险源↔补偿器。**
爻在上下卦之间相应：1–4、2–5、3–6，各是一对*风险源↔补偿器*（生产↔可逆、全局↔反馈、
副作用↔验证）。每对在问：这一重客观风险，有没有一重主观准备来接住它？当一对中**两爻
同时危险**，风险便裸露——是为**裂缝**。**只有裂缝需要处理**；孤立的危险爻若有对位补偿，
已被接住。

**四、变爻——移向更好的状态。**
认知有限者无法预见一切，只能认清此刻所在、移向更好的状态，再重新观察。这正是系统建立
在**变爻**而非评分之上的原因。评分假装风险有个精确的数（全知者的口吻）；变爻只承认
「这样比那样安全」（有限认知者的诚实）。Agent 与占卦的古人面对同样的处境——故采此形式。

### 翻爻如何进行

**每条裂缝，翻通它那一对里的一爻即可**——不必两爻都翻。但**所有裂缝都必须翻通，不能修
一条就停。** 三条裂缝就翻三次（每条一爻），不是翻一次就收工。优先级：

1. **优先翻 Agent 自己能做的爻**，无需人工（多为恢复补偿器：建备份、缩范围、写校验）。
1. 一对两爻都翻不动 → **迂回翻别的自主爻**降低整体风险，再重判。
1. 全盘无自主出路 → **停下请求人工**。

每次翻爻都把卦象变得更安全；每翻一次重判一次

## 用法

AI Ching 把**探测**（灵活、因环境而异）与**判读**（固定）分开。三种用法：

1. **全自动**——Agent 读 [`SKILL.md`](SKILL.md)，自己探测→判读→执行。最省事，但判读是即兴的。
1. **确定性判读（高危操作推荐）**——探测出六爻（AI 或人工），喂给
   [`src/reference.py`](src/reference.py)，**Agent 严格按它输出的卦象与处方执行**。
   判读锁定在固定规则上，Agent 不自由发挥「该多谨慎」。
   
   ```bash
   python src/reference.py 010011    # 六爻，由下到上
   ```
1. **纯人工起卦**——人定六爻、跑 reference.py、Agent 照处方执行。判断权在人。

> 核心：**判读不交给 Agent 自由发挥。** 由 `reference.py` 或人工产出确定的卦象与处方，
> Agent 据此执行。

## 示例：删除生产数据库表

探测：生产、全局、有副作用、无备份、反馈慢、难验证 → `[000000]`，乾/乾 ☰☰ →
**停下准备**，**三条裂缝**。逐条翻通，每条一爻：

1. 翻**可逆性** → 建快照/备份 → ☰☴
1. 翻**波及范围** → 先删一个分区，而非整表 → ☲☴
1. 翻**可验证性** → 先 SELECT 出将影响的行作为基准 → ☲☷

此时：局部、可逆、可验证——在带回滚+单点验证下执行那一小步，确认后再扩大。若某次翻爻
无法做到（如根本没有备份机制）→ **停下请求人工**。完整推演见[例](docs/03-Cases_ZH.md)。

## 局限与开放问题

这正是需要帮助之处。已知缺口：

- **单操作粒度**：一次只判一个操作。**多 Agent／并发**场景下副作用与波及范围会跨主体叠加，尚未建模。
- **探测可靠性**：副作用、可逆性的探测依赖识别操作类型，新型工具／MCP 调用可能误判。
- **自探测乐观偏向**：同一 Agent 既探测又执行时，可能把爻判向「安全」。靠「举证责任在安全侧」+确定性判读缓解，未根除。
- **未经生产验证**：尚无真实事故数据。
- **未测领域**：K8s 变更、大型迁移、MCP 调用等都需跑卦验证、很可能要修模型。欢迎提交跑不通的案例。

## 结构

```
SKILL.md                          # 面向 Agent 的指令（探测+判读）
src/reference.py                  # 确定性判读内核（MIT）
docs/01-Classic_{EN,ZH}.md        # 经——规则，运行时读（CC BY 4.0）
docs/02-Commentary_{EN,ZH}.md     # 传——为什么这样设计
docs/03-Cases_{EN,ZH}.md          # 例——案例推演
docs/Appendix-64-Hexagrams_{EN,ZH}.md  # 附录——64卦查表
```

全部文档双语：`_EN` 英文，`_ZH` 中文。

## 许可

- **代码**（`src/`）：MIT，见 <LICENSE>。
- **文档**（`docs/`）：CC BY 4.0，见 <docs/LICENSE-docs>。

## 附录：与易经的关系

AI Ching 借的是易经的**结构**，不是占卜：两卦叠成六爻、自下而上读、上下爻的**应位**、
以及最重要的**变**——一个状态，与它的下一步去向。古易经让卦**名**承载含义，AI Ching
刻意舍弃卦名：含义全在六爻取值与其上的规则。易经是认知有限的古人面对不可知世界时，
读懂当下与下一步的方式；Agent 面对的正是同样的处境——这层同构，正是采用这一形式的
全部理由。
