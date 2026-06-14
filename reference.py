#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Ching - Reference Implementation / 参考实现
A State-Driven Safety Framework for AI Agents.

This is the DETERMINISTIC judging core. Detection of the six lines (yáo) is
context-dependent and meant to be done by an AI per environment (see SKILL.md);
but JUDGING must be deterministic, so it lives here as the canonical answer.

这是【判读】的确定性内核。六爻的【探测】因环境而异，交由 AI 完成（见 SKILL.md）；
但【判读】必须确定，故以此为标准答案，防止不同 AI 即兴跑偏。

Encoding / 编码: 1 = yin = SAFE, 0 = yang = DANGER.
Rule of thumb / 铁律: when a line's value is uncertain, take the DANGER side (0).
"""

from dataclasses import dataclass, field
from typing import List

# 8 trigrams: (line_low, line_mid, line_high) -> (name_pinyin, symbol)
TRIGRAM = {
    (1, 1, 1): ("Kūn 坤", "☷"), (1, 1, 0): ("Gèn 艮", "☶"),
    (1, 0, 1): ("Kǎn 坎", "☵"), (1, 0, 0): ("Xùn 巽", "☴"),
    (0, 1, 1): ("Zhèn 震", "☳"), (0, 1, 0): ("Lí 离", "☲"),
    (0, 0, 1): ("Duì 兑", "☱"), (0, 0, 0): ("Qián 乾", "☰"),
}

# Line names / 爻名 (index 1..6, bottom to top)
LINE = {
    1: ("Production 生产环境", "Earth 地"),
    2: ("Blast Radius 波及范围", "Earth 地"),
    3: ("Side Effects 副作用", "Human 人"),
    4: ("Reversibility 可逆性", "Human 人"),
    5: ("Feedback Latency 反馈延迟", "Heaven 天"),
    6: ("Verifiability 可验证性", "Heaven 天"),
}

# The three correspondences / 应位三对: (lower_line, upper_line, name)
# risk source (lower) <-> safeguard (upper)
CORRESPONDENCES = [
    (1, 4, "Production↔Reversibility 生产↔可逆"),
    (2, 5, "BlastRadius↔Feedback 全局↔反馈"),
    (3, 6, "SideEffects↔Verifiability 副作用↔验证"),
]

# Self-autonomous flips (Agent can do without a human) ordered by cost.
# 3 (Side Effects) is generally NOT self-flippable (intrinsic to the op).
FLIP = {
    4: ("Reversibility 可逆性", "create snapshot/backup/rollback path 先建快照/备份/可回滚"),
    2: ("Blast Radius 波及范围", "scope to single tenant / batch & throttle 缩到单租户、分批限流"),
    1: ("Production 生产环境", "run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度"),
    6: ("Verifiability 可验证性", "build a checker / define a correctness baseline 自建校验器/定正确性基准"),
    5: ("Feedback Latency 反馈延迟", "add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测"),
}
AUTO_COST = {4: 1, 2: 2, 1: 3, 6: 4, 5: 5, 3: 9}

# Work mode imposed by each red (0) upper line.
# exec = when there ARE side effects; cog = when there are NONE (cognitive).
WORK_MODE = {
    4: {"exec": "Do it reversibly: ensure each step can be undone; roll back on error / 带回滚地做",
        "cog": "Keep it retraceable: checkpoint key judgments; don't go past the point of no return / 留可回溯"},
    5: {"exec": "Proceed in batches: confirm each batch before the next; no racing ahead / 分批推进",
        "cog": "Confirm in segments: don't stack reasoning on unconfirmed intermediate results / 分段确认"},
    6: {"exec": "Verify as you go: confirm each change before continuing; unverified results don't flow downstream / 边做边验",
        "cog": "Flag & corroborate: mark confidence & basis; verify or seek human review on important claims / 标注求证"},
}

STANCE_EN = {
    "proceed": "Proceed", "small_step": "Small-step & Verify",
    "narrow": "Narrow & Proceed", "canary": "Canary into Prod",
    "halt": "Halt & Prepare",
}
STANCE_ZH = {
    "proceed": "放行", "small_step": "小步快验",
    "narrow": "缩范围推进", "canary": "灰度入生产", "halt": "停下准备",
}


@dataclass
class Verdict:
    lines: List[int]
    lower: tuple
    upper: tuple
    has_side_effect: bool
    stance_key: str
    fault_lines: list = field(default_factory=list)   # broken correspondences
    repairs: list = field(default_factory=list)        # ordered flip suggestions
    work_modes: list = field(default_factory=list)     # exec or cog constraints

    @property
    def stance_en(self): return STANCE_EN[self.stance_key]
    @property
    def stance_zh(self): return STANCE_ZH[self.stance_key]


def judge(lines: List[int]) -> Verdict:
    """lines = [y1..y6] bottom->top, each 0 or 1. Returns a Verdict."""
    assert len(lines) == 6 and all(v in (0, 1) for v in lines), \
        "Need six 0/1 lines, bottom to top / 需要六个 0/1 爻，由下到上"
    y1, y2, y3, y4, y5, y6 = lines
    lower = TRIGRAM[(y1, y2, y3)]
    upper = TRIGRAM[(y4, y5, y6)]
    has_se = (y3 == 0)
    layer = "exec" if has_se else "cog"

    # --- Stance: side-effect gate, then count red objective lines ---
    if not has_se:
        stance = "proceed"
    else:
        red = (1 - y1) + (1 - y2)
        if red == 2:
            stance = "halt"
        elif red == 1:
            stance = "canary" if y1 == 0 else "narrow"
        else:
            stance = "small_step"

    v = Verdict(lines, lower, upper, has_se, stance)

    # --- Fault lines: a correspondence where BOTH lines are red (0) ---
    for lo, up, nm in CORRESPONDENCES:
        if lines[lo - 1] == 0 and lines[up - 1] == 0:
            v.fault_lines.append(nm)

    # --- Repairs: flip every fault open (prefer self-autonomous, low cost) ---
    # Each fault must be mended; order by autonomous cost. (Stance never relaxed.)
    danger = [i for i in range(1, 7) if lines[i - 1] == 0]
    for i in sorted([d for d in danger if d != 3], key=lambda i: AUTO_COST[i]):
        in_fault = any(i in (lo, up) for lo, up, _ in CORRESPONDENCES
                       if lines[lo - 1] == 0 and lines[up - 1] == 0)
        name, act = FLIP[i]
        nl = list(lines); nl[i - 1] = 1
        new_lower = TRIGRAM[(nl[0], nl[1], nl[2])]
        new_upper = TRIGRAM[(nl[3], nl[4], nl[5])]
        v.repairs.append({
            "line": i, "name": name, "action": act,
            "in_fault": in_fault,
            "new_hexagram": f"{new_lower[0]}/{new_upper[0]} {new_lower[1]}{new_upper[1]}",
        })
    if y3 == 0:
        v.repairs.append({
            "line": 3, "name": "Side Effects 副作用",
            "action": "usually intrinsic; removable only if goal can be met read-only/dry-run "
                      "通常是操作本性，仅当目的能改用只读/dry-run 时才可消除",
            "in_fault": any("SideEffects" in f for f in v.fault_lines),
            "new_hexagram": None,
        })

    # --- Work modes from red upper lines (exec or cognitive) ---
    for i in (4, 5, 6):
        if lines[i - 1] == 0:
            v.work_modes.append(WORK_MODE[i][layer])

    return v


def format_verdict(v: Verdict) -> str:
    L = []
    code = "".join(map(str, v.lines))
    L.append(f"Hexagram 卦: {v.lower[0]} / {v.upper[0]}  {v.lower[1]}{v.upper[1]}  [{code}]")
    parts = []
    names = ["Production 生产", "BlastRadius 范围", "SideEffect 副作用",
             "Reversibility 可逆", "Feedback 反馈", "Verifiability 验证"]
    for i, val in enumerate(v.lines):
        parts.append(f"{names[i]}={'safe' if val else 'DANGER'}")
    L.append("Lines 六爻: " + " · ".join(parts))
    L.append(f"Stance 姿态: {v.stance_en} / {v.stance_zh}")
    if v.has_side_effect:
        if v.fault_lines:
            L.append("Fault lines 应位裂缝: " + "; ".join(v.fault_lines))
        else:
            L.append("Fault lines 应位裂缝: none — risks covered by safeguards / 无，危险已被补偿")
        if v.fault_lines:
            L.append("Repairs 翻爻 (mend every fault; prefer autonomous / 逐条翻通，优先自主):")
            for r in v.repairs:
                tag = " [fault 裂缝]" if r["in_fault"] else ""
                arrow = f" -> {r['new_hexagram']}" if r["new_hexagram"] else ""
                L.append(f"  - flip {r['name']}{tag}: {r['action']}{arrow}")
        if v.work_modes:
            L.append("Work mode 执行模式:")
            for w in v.work_modes:
                L.append(f"  - {w}")
    else:
        L.append("PROCEED (no side effects) — execution layer free / 放行，执行层自由")
        if v.work_modes:
            L.append("Cognitive mode 认知模式 (results may still be wrong / 结论仍可能错):")
            for w in v.work_modes:
                L.append(f"  - {w}")
        else:
            L.append("  Safeguards complete; results trustworthy. / 保障齐备，结论可信。")
    L.append("Fallback 兜底: if no line can be flipped autonomously and human help "
             "is unsuitable -> HALT and request human confirmation. / 全盘无自主出路则停下请求人工。")
    return "\n".join(L)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and len(sys.argv[1]) == 6 and set(sys.argv[1]) <= {"0", "1"}:
        lines = [int(c) for c in sys.argv[1]]
    else:
        print("Usage / 用法: python reference.py 000000   (six 0/1, bottom->top / 六爻由下到上)")
        print("  line1 Production | line2 BlastRadius | line3 SideEffects |")
        print("  line4 Reversibility | line5 Feedback | line6 Verifiability")
        print("\n--- Demo: 000000 (worst case / 最危险) ---")
        print(format_verdict(judge([0, 0, 0, 0, 0, 0])))
        sys.exit(0)
    print(format_verdict(judge(lines)))
