# AI Ching v0.8 · Appendix: 64 Hexagrams (Lookup)

> **This is a lookup table, not a tutorial.** Read the Classic first to learn
> the rules, then look up the matching hexagram when you face a concrete state.
> Like an HTTP status-code table — nobody memorizes the appendix; you learn the
> protocol and look things up when needed.
> 
> Six lines bottom to top: 1 Production · 2 BlastRadius · 3 SideEffects |
> 4 Reversibility · 5 Feedback · 6 Verifiability. 1=safe, 0=danger.
> Each entry: state/safeguards -> stance -> fault lines -> repair / work mode -> fallback.

-----

## 1. Qián 乾 / Qián 乾  ☰☰  `[000000]`

**State**: prod · global · side-effecting　|　**Safeguards**: irreversible · slow feedback · hard to verify
**Stance**: Halt & Prepare
**Fault lines**: Production↔Reversibility; BlastRadius↔Feedback; SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Reversibility: create snapshot/backup/rollback path 先建快照/备份/可回滚 -> Qián 乾/Xùn 巽 ☰☴
- flip Blast: scope to single tenant / batch & throttle 缩到单租户、分批限流 -> Lí 离/Qián 乾 ☲☰
- flip Production: run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度 -> Xùn 巽/Qián 乾 ☴☰
- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Qián 乾/Duì 兑 ☰☱
- flip Feedback: add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测 -> Qián 乾/Lí 离 ☰☲
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Proceed in batches: confirm each batch before the next; no racing ahead
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 2. Qián 乾 / Duì 兑  ☰☱  `[000001]`

**State**: prod · global · side-effecting　|　**Safeguards**: irreversible · slow feedback · verifiable
**Stance**: Halt & Prepare
**Fault lines**: Production↔Reversibility; BlastRadius↔Feedback
**Repair** (mend each fault, prefer autonomous flip):

- flip Reversibility: create snapshot/backup/rollback path 先建快照/备份/可回滚 -> Qián 乾/Kǎn 坎 ☰☵
- flip Blast: scope to single tenant / batch & throttle 缩到单租户、分批限流 -> Lí 离/Duì 兑 ☲☱
- flip Production: run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度 -> Xùn 巽/Duì 兑 ☴☱
- flip Feedback: add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测 -> Qián 乾/Zhèn 震 ☰☳
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Proceed in batches: confirm each batch before the next; no racing ahead
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 3. Qián 乾 / Lí 离  ☰☲  `[000010]`

**State**: prod · global · side-effecting　|　**Safeguards**: irreversible · fast feedback · hard to verify
**Stance**: Halt & Prepare
**Fault lines**: Production↔Reversibility; SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Reversibility: create snapshot/backup/rollback path 先建快照/备份/可回滚 -> Qián 乾/Gèn 艮 ☰☶
- flip Production: run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度 -> Xùn 巽/Lí 离 ☴☲
- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Qián 乾/Zhèn 震 ☰☳
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 4. Qián 乾 / Zhèn 震  ☰☳  `[000011]`

**State**: prod · global · side-effecting　|　**Safeguards**: irreversible · fast feedback · verifiable
**Stance**: Halt & Prepare
**Fault lines**: Production↔Reversibility
**Repair** (mend each fault, prefer autonomous flip):

- flip Reversibility: create snapshot/backup/rollback path 先建快照/备份/可回滚 -> Qián 乾/Kūn 坤 ☰☷
- flip Production: run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度 -> Xùn 巽/Zhèn 震 ☴☳
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 5. Qián 乾 / Xùn 巽  ☰☴  `[000100]`

**State**: prod · global · side-effecting　|　**Safeguards**: reversible · slow feedback · hard to verify
**Stance**: Halt & Prepare
**Fault lines**: BlastRadius↔Feedback; SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Blast: scope to single tenant / batch & throttle 缩到单租户、分批限流 -> Lí 离/Xùn 巽 ☲☴
- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Qián 乾/Kǎn 坎 ☰☵
- flip Feedback: add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测 -> Qián 乾/Gèn 艮 ☰☶
  **Work mode**:
- Proceed in batches: confirm each batch before the next; no racing ahead
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 6. Qián 乾 / Kǎn 坎  ☰☵  `[000101]`

**State**: prod · global · side-effecting　|　**Safeguards**: reversible · slow feedback · verifiable
**Stance**: Halt & Prepare
**Fault lines**: BlastRadius↔Feedback
**Repair** (mend each fault, prefer autonomous flip):

- flip Blast: scope to single tenant / batch & throttle 缩到单租户、分批限流 -> Lí 离/Kǎn 坎 ☲☵
- flip Feedback: add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测 -> Qián 乾/Kūn 坤 ☰☷
  **Work mode**:
- Proceed in batches: confirm each batch before the next; no racing ahead
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 7. Qián 乾 / Gèn 艮  ☰☶  `[000110]`

**State**: prod · global · side-effecting　|　**Safeguards**: reversible · fast feedback · hard to verify
**Stance**: Halt & Prepare
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Qián 乾/Kūn 坤 ☰☷
  **Work mode**:
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 8. Qián 乾 / Kūn 坤  ☰☷  `[000111]`

**State**: prod · global · side-effecting　|　**Safeguards**: reversible · fast feedback · verifiable
**Stance**: Halt & Prepare
**Fault lines**: none — risks covered by safeguards.
Safeguards complete; proceed per stance.

- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 9. Duì 兑 / Qián 乾  ☱☰  `[001000]`

**State**: prod · global · no side effect　|　**Safeguards**: irreversible · slow feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 10. Duì 兑 / Duì 兑  ☱☱  `[001001]`

**State**: prod · global · no side effect　|　**Safeguards**: irreversible · slow feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 11. Duì 兑 / Lí 离  ☱☲  `[001010]`

**State**: prod · global · no side effect　|　**Safeguards**: irreversible · fast feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 12. Duì 兑 / Zhèn 震  ☱☳  `[001011]`

**State**: prod · global · no side effect　|　**Safeguards**: irreversible · fast feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 13. Duì 兑 / Xùn 巽  ☱☴  `[001100]`

**State**: prod · global · no side effect　|　**Safeguards**: reversible · slow feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 14. Duì 兑 / Kǎn 坎  ☱☵  `[001101]`

**State**: prod · global · no side effect　|　**Safeguards**: reversible · slow feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 15. Duì 兑 / Gèn 艮  ☱☶  `[001110]`

**State**: prod · global · no side effect　|　**Safeguards**: reversible · fast feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 16. Duì 兑 / Kūn 坤  ☱☷  `[001111]`

**State**: prod · global · no side effect　|　**Safeguards**: reversible · fast feedback · verifiable
**Stance**: Proceed
**Proceed** — safeguards complete, results trustworthy.

- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 17. Lí 离 / Qián 乾  ☲☰  `[010000]`

**State**: prod · local · side-effecting　|　**Safeguards**: irreversible · slow feedback · hard to verify
**Stance**: Canary into Prod
**Fault lines**: Production↔Reversibility; SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Reversibility: create snapshot/backup/rollback path 先建快照/备份/可回滚 -> Lí 离/Xùn 巽 ☲☴
- flip Production: run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度 -> Gèn 艮/Qián 乾 ☶☰
- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Lí 离/Duì 兑 ☲☱
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Proceed in batches: confirm each batch before the next; no racing ahead
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 18. Lí 离 / Duì 兑  ☲☱  `[010001]`

**State**: prod · local · side-effecting　|　**Safeguards**: irreversible · slow feedback · verifiable
**Stance**: Canary into Prod
**Fault lines**: Production↔Reversibility
**Repair** (mend each fault, prefer autonomous flip):

- flip Reversibility: create snapshot/backup/rollback path 先建快照/备份/可回滚 -> Lí 离/Kǎn 坎 ☲☵
- flip Production: run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度 -> Gèn 艮/Duì 兑 ☶☱
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Proceed in batches: confirm each batch before the next; no racing ahead
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 19. Lí 离 / Lí 离  ☲☲  `[010010]`

**State**: prod · local · side-effecting　|　**Safeguards**: irreversible · fast feedback · hard to verify
**Stance**: Canary into Prod
**Fault lines**: Production↔Reversibility; SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Reversibility: create snapshot/backup/rollback path 先建快照/备份/可回滚 -> Lí 离/Gèn 艮 ☲☶
- flip Production: run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度 -> Gèn 艮/Lí 离 ☶☲
- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Lí 离/Zhèn 震 ☲☳
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 20. Lí 离 / Zhèn 震  ☲☳  `[010011]`

**State**: prod · local · side-effecting　|　**Safeguards**: irreversible · fast feedback · verifiable
**Stance**: Canary into Prod
**Fault lines**: Production↔Reversibility
**Repair** (mend each fault, prefer autonomous flip):

- flip Reversibility: create snapshot/backup/rollback path 先建快照/备份/可回滚 -> Lí 离/Kūn 坤 ☲☷
- flip Production: run in shadow/isolated env first, then canary 先在影子/隔离环境跑通再灰度 -> Gèn 艮/Zhèn 震 ☶☳
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 21. Lí 离 / Xùn 巽  ☲☴  `[010100]`

**State**: prod · local · side-effecting　|　**Safeguards**: reversible · slow feedback · hard to verify
**Stance**: Canary into Prod
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Lí 离/Kǎn 坎 ☲☵
  **Work mode**:
- Proceed in batches: confirm each batch before the next; no racing ahead
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 22. Lí 离 / Kǎn 坎  ☲☵  `[010101]`

**State**: prod · local · side-effecting　|　**Safeguards**: reversible · slow feedback · verifiable
**Stance**: Canary into Prod
**Fault lines**: none — risks covered by safeguards.
**Work mode** (risks compensated, act accordingly):

- Proceed in batches: confirm each batch before the next; no racing ahead
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 23. Lí 离 / Gèn 艮  ☲☶  `[010110]`

**State**: prod · local · side-effecting　|　**Safeguards**: reversible · fast feedback · hard to verify
**Stance**: Canary into Prod
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Lí 离/Kūn 坤 ☲☷
  **Work mode**:
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 24. Lí 离 / Kūn 坤  ☲☷  `[010111]`

**State**: prod · local · side-effecting　|　**Safeguards**: reversible · fast feedback · verifiable
**Stance**: Canary into Prod
**Fault lines**: none — risks covered by safeguards.
Safeguards complete; proceed per stance.

- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 25. Zhèn 震 / Qián 乾  ☳☰  `[011000]`

**State**: prod · local · no side effect　|　**Safeguards**: irreversible · slow feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 26. Zhèn 震 / Duì 兑  ☳☱  `[011001]`

**State**: prod · local · no side effect　|　**Safeguards**: irreversible · slow feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 27. Zhèn 震 / Lí 离  ☳☲  `[011010]`

**State**: prod · local · no side effect　|　**Safeguards**: irreversible · fast feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 28. Zhèn 震 / Zhèn 震  ☳☳  `[011011]`

**State**: prod · local · no side effect　|　**Safeguards**: irreversible · fast feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 29. Zhèn 震 / Xùn 巽  ☳☴  `[011100]`

**State**: prod · local · no side effect　|　**Safeguards**: reversible · slow feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 30. Zhèn 震 / Kǎn 坎  ☳☵  `[011101]`

**State**: prod · local · no side effect　|　**Safeguards**: reversible · slow feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 31. Zhèn 震 / Gèn 艮  ☳☶  `[011110]`

**State**: prod · local · no side effect　|　**Safeguards**: reversible · fast feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 32. Zhèn 震 / Kūn 坤  ☳☷  `[011111]`

**State**: prod · local · no side effect　|　**Safeguards**: reversible · fast feedback · verifiable
**Stance**: Proceed
**Proceed** — safeguards complete, results trustworthy.

- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 33. Xùn 巽 / Qián 乾  ☴☰  `[100000]`

**State**: non-prod · global · side-effecting　|　**Safeguards**: irreversible · slow feedback · hard to verify
**Stance**: Narrow & Proceed
**Fault lines**: BlastRadius↔Feedback; SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Blast: scope to single tenant / batch & throttle 缩到单租户、分批限流 -> Gèn 艮/Qián 乾 ☶☰
- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Xùn 巽/Duì 兑 ☴☱
- flip Feedback: add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测 -> Xùn 巽/Lí 离 ☴☲
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Proceed in batches: confirm each batch before the next; no racing ahead
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 34. Xùn 巽 / Duì 兑  ☴☱  `[100001]`

**State**: non-prod · global · side-effecting　|　**Safeguards**: irreversible · slow feedback · verifiable
**Stance**: Narrow & Proceed
**Fault lines**: BlastRadius↔Feedback
**Repair** (mend each fault, prefer autonomous flip):

- flip Blast: scope to single tenant / batch & throttle 缩到单租户、分批限流 -> Gèn 艮/Duì 兑 ☶☱
- flip Feedback: add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测 -> Xùn 巽/Zhèn 震 ☴☳
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Proceed in batches: confirm each batch before the next; no racing ahead
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 35. Xùn 巽 / Lí 离  ☴☲  `[100010]`

**State**: non-prod · global · side-effecting　|　**Safeguards**: irreversible · fast feedback · hard to verify
**Stance**: Narrow & Proceed
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Xùn 巽/Zhèn 震 ☴☳
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 36. Xùn 巽 / Zhèn 震  ☴☳  `[100011]`

**State**: non-prod · global · side-effecting　|　**Safeguards**: irreversible · fast feedback · verifiable
**Stance**: Narrow & Proceed
**Fault lines**: none — risks covered by safeguards.
**Work mode** (risks compensated, act accordingly):

- Do it reversibly: ensure each step can be undone; roll back on error
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 37. Xùn 巽 / Xùn 巽  ☴☴  `[100100]`

**State**: non-prod · global · side-effecting　|　**Safeguards**: reversible · slow feedback · hard to verify
**Stance**: Narrow & Proceed
**Fault lines**: BlastRadius↔Feedback; SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Blast: scope to single tenant / batch & throttle 缩到单租户、分批限流 -> Gèn 艮/Xùn 巽 ☶☴
- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Xùn 巽/Kǎn 坎 ☴☵
- flip Feedback: add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测 -> Xùn 巽/Gèn 艮 ☴☶
  **Work mode**:
- Proceed in batches: confirm each batch before the next; no racing ahead
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 38. Xùn 巽 / Kǎn 坎  ☴☵  `[100101]`

**State**: non-prod · global · side-effecting　|　**Safeguards**: reversible · slow feedback · verifiable
**Stance**: Narrow & Proceed
**Fault lines**: BlastRadius↔Feedback
**Repair** (mend each fault, prefer autonomous flip):

- flip Blast: scope to single tenant / batch & throttle 缩到单租户、分批限流 -> Gèn 艮/Kǎn 坎 ☶☵
- flip Feedback: add instrumentation / proxy metric to shorten observation 加埋点/代理指标缩短观测 -> Xùn 巽/Kūn 坤 ☴☷
  **Work mode**:
- Proceed in batches: confirm each batch before the next; no racing ahead
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 39. Xùn 巽 / Gèn 艮  ☴☶  `[100110]`

**State**: non-prod · global · side-effecting　|　**Safeguards**: reversible · fast feedback · hard to verify
**Stance**: Narrow & Proceed
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Xùn 巽/Kūn 坤 ☴☷
  **Work mode**:
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 40. Xùn 巽 / Kūn 坤  ☴☷  `[100111]`

**State**: non-prod · global · side-effecting　|　**Safeguards**: reversible · fast feedback · verifiable
**Stance**: Narrow & Proceed
**Fault lines**: none — risks covered by safeguards.
Safeguards complete; proceed per stance.

- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 41. Kǎn 坎 / Qián 乾  ☵☰  `[101000]`

**State**: non-prod · global · no side effect　|　**Safeguards**: irreversible · slow feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 42. Kǎn 坎 / Duì 兑  ☵☱  `[101001]`

**State**: non-prod · global · no side effect　|　**Safeguards**: irreversible · slow feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 43. Kǎn 坎 / Lí 离  ☵☲  `[101010]`

**State**: non-prod · global · no side effect　|　**Safeguards**: irreversible · fast feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 44. Kǎn 坎 / Zhèn 震  ☵☳  `[101011]`

**State**: non-prod · global · no side effect　|　**Safeguards**: irreversible · fast feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 45. Kǎn 坎 / Xùn 巽  ☵☴  `[101100]`

**State**: non-prod · global · no side effect　|　**Safeguards**: reversible · slow feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 46. Kǎn 坎 / Kǎn 坎  ☵☵  `[101101]`

**State**: non-prod · global · no side effect　|　**Safeguards**: reversible · slow feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 47. Kǎn 坎 / Gèn 艮  ☵☶  `[101110]`

**State**: non-prod · global · no side effect　|　**Safeguards**: reversible · fast feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 48. Kǎn 坎 / Kūn 坤  ☵☷  `[101111]`

**State**: non-prod · global · no side effect　|　**Safeguards**: reversible · fast feedback · verifiable
**Stance**: Proceed
**Proceed** — safeguards complete, results trustworthy.

- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 49. Gèn 艮 / Qián 乾  ☶☰  `[110000]`

**State**: non-prod · local · side-effecting　|　**Safeguards**: irreversible · slow feedback · hard to verify
**Stance**: Small-step & Verify
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Gèn 艮/Duì 兑 ☶☱
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Proceed in batches: confirm each batch before the next; no racing ahead
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 50. Gèn 艮 / Duì 兑  ☶☱  `[110001]`

**State**: non-prod · local · side-effecting　|　**Safeguards**: irreversible · slow feedback · verifiable
**Stance**: Small-step & Verify
**Fault lines**: none — risks covered by safeguards.
**Work mode** (risks compensated, act accordingly):

- Do it reversibly: ensure each step can be undone; roll back on error
- Proceed in batches: confirm each batch before the next; no racing ahead
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 51. Gèn 艮 / Lí 离  ☶☲  `[110010]`

**State**: non-prod · local · side-effecting　|　**Safeguards**: irreversible · fast feedback · hard to verify
**Stance**: Small-step & Verify
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Gèn 艮/Zhèn 震 ☶☳
  **Work mode**:
- Do it reversibly: ensure each step can be undone; roll back on error
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 52. Gèn 艮 / Zhèn 震  ☶☳  `[110011]`

**State**: non-prod · local · side-effecting　|　**Safeguards**: irreversible · fast feedback · verifiable
**Stance**: Small-step & Verify
**Fault lines**: none — risks covered by safeguards.
**Work mode** (risks compensated, act accordingly):

- Do it reversibly: ensure each step can be undone; roll back on error
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 53. Gèn 艮 / Xùn 巽  ☶☴  `[110100]`

**State**: non-prod · local · side-effecting　|　**Safeguards**: reversible · slow feedback · hard to verify
**Stance**: Small-step & Verify
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Gèn 艮/Kǎn 坎 ☶☵
  **Work mode**:
- Proceed in batches: confirm each batch before the next; no racing ahead
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 54. Gèn 艮 / Kǎn 坎  ☶☵  `[110101]`

**State**: non-prod · local · side-effecting　|　**Safeguards**: reversible · slow feedback · verifiable
**Stance**: Small-step & Verify
**Fault lines**: none — risks covered by safeguards.
**Work mode** (risks compensated, act accordingly):

- Proceed in batches: confirm each batch before the next; no racing ahead
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 55. Gèn 艮 / Gèn 艮  ☶☶  `[110110]`

**State**: non-prod · local · side-effecting　|　**Safeguards**: reversible · fast feedback · hard to verify
**Stance**: Small-step & Verify
**Fault lines**: SideEffects↔Verifiability
**Repair** (mend each fault, prefer autonomous flip):

- flip Verifiability: build a checker / define a correctness baseline 自建校验器/定正确性基准 -> Gèn 艮/Kūn 坤 ☶☷
  **Work mode**:
- Verify as you go: confirm each change before continuing; unverified results don’t flow downstream
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 56. Gèn 艮 / Kūn 坤  ☶☷  `[110111]`

**State**: non-prod · local · side-effecting　|　**Safeguards**: reversible · fast feedback · verifiable
**Stance**: Small-step & Verify
**Fault lines**: none — risks covered by safeguards.
Safeguards complete; proceed per stance.

- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 57. Kūn 坤 / Qián 乾  ☷☰  `[111000]`

**State**: non-prod · local · no side effect　|　**Safeguards**: irreversible · slow feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 58. Kūn 坤 / Duì 兑  ☷☱  `[111001]`

**State**: non-prod · local · no side effect　|　**Safeguards**: irreversible · slow feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 59. Kūn 坤 / Lí 离  ☷☲  `[111010]`

**State**: non-prod · local · no side effect　|　**Safeguards**: irreversible · fast feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 60. Kūn 坤 / Zhèn 震  ☷☳  `[111011]`

**State**: non-prod · local · no side effect　|　**Safeguards**: irreversible · fast feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Keep it retraceable: checkpoint key judgments; don’t go past the point of no return
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 61. Kūn 坤 / Xùn 巽  ☷☴  `[111100]`

**State**: non-prod · local · no side effect　|　**Safeguards**: reversible · slow feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 62. Kūn 坤 / Kǎn 坎  ☷☵  `[111101]`

**State**: non-prod · local · no side effect　|　**Safeguards**: reversible · slow feedback · verifiable
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Confirm in segments: don’t stack reasoning on unconfirmed intermediate results
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 63. Kūn 坤 / Gèn 艮  ☷☶  `[111110]`

**State**: non-prod · local · no side effect　|　**Safeguards**: reversible · fast feedback · hard to verify
**Stance**: Proceed
**Proceed** (execution free). Cognitive mode:

- Flag & corroborate: mark confidence & basis; verify or seek human review on important claims
- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----

## 64. Kūn 坤 / Kūn 坤  ☷☷  `[111111]`

**State**: non-prod · local · no side effect　|　**Safeguards**: reversible · fast feedback · verifiable
**Stance**: Proceed
**Proceed** — safeguards complete, results trustworthy.

- **Fallback**: if no line is autonomously flippable and human help is unsuitable -> halt, request human.

-----