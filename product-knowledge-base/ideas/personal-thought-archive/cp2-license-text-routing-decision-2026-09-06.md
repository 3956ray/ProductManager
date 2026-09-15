# 决策记录：CP2 LICENSE 文本路由修复

Owner: Product Lead
Last updated: 2026-09-06
Source: ../../raw/SRC-20260906-think-cp2-license-routing-01.md；../../raw/SRC-20260906-think-cp2-license-routing-02.md；../../raw/SRC-20260906-think-cp2-license-routing-03.md；../../raw/SRC-20260906-think-cp2-license-routing-04.md
Confidence: High（单次请求、固定身份、停止顺序和自然语言路由缺陷已由 Leader 与结构化证据复核）；Medium（修复候选、离线回归、新冻结和任何后继真实获取均未发生）
Related decisions: prd-v0.1-2026-09-04.md；cp2-metadata-path-compatibility-decision-2026-09-06.md；cp2-acquisition-tool-scope-decision-2026-09-05.md；cp2-narrow-runtime-boundary-design-decision-2026-09-05.md
Next review date: 2026-09-13

Research Quality: 89 · pass
Validation Level: V2
Next evidence: 独立 v5 候选以自建 fixture 证明精确 `LICENSE` 的 `license_text` 路由、未知类型 fail closed、C/C++ 既有停止语义不变，并由 Leader 双跑原 112 项及新增回归后决定是否冻结
Allowed next investment: 独立新目录中的最小第一方离线路由修复、Python 标准库、自建 fixture、静态检查与独立验收；不得读取真实 LICENSE 或其他第三方正文
Pause/Kill condition: 需要扩展名猜测／内容嗅探、扩大 seed／路径／类型／预算、放宽 C/C++ 解析语义、跳过扫描或人工许可证审查、读取第三方正文、联网、恢复旧 run、构建、执行或集成

## RESULT

**APPROVED — 只批准一个独立新候选中的第一方离线 `LICENSE` 文本路由修复。批准的含义仅是修复工具可把冻结合同中的精确 seed `LICENSE` 作为惰性 `license_text` 审查对象，而不是送入 C/C++ include 词法器；不批准第三方正文、现有 run、源码可行性、许可证适用性、冻结、后继获取、构建、制品、模型、CP2 或 CP3。**

## 已确认事实

1. v4 真实获取只请求了固定 seed `LICENSE`：blob SHA-1 `d645695673349e3947e8e5ae42332d0ac3164cd7`，11,358 字节，正文 SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`。该请求有请求前授权，16 条 ledger、59 个 metadata part、88 个私有文件复算和 1,024 个冻结文件检查可复核。
2. 任务在 `LICENSE` 第 183 行返回 `edge_unclosed_literal`。已验收报告确认触发点是自然语言撇号，而不是 C/C++ include；因此这是第一方内容类型路由缺陷。
3. 运行扫描为 `low_indicators` 且 0 finding。身份扫描仍为 `manual_review`；四个 medium 是此前已解释的时间戳／SHA 数字子串误报。它们不是新的 block，但也不把任何正文或制品提升为安全、可用或已批准。
4. 没有请求任何 C/C++ 文件；其余 8 个 seed 保持未请求，`fixed_point=false`，`source_verdict=insufficient_evidence`。现有证据不能判断 C/C++ 闭包、窄 API 可行性或源码可采用性。
5. 冻结工具没有保存原始 blob API JSON／HTTP headers，故 wire 字段不能独立重放。已验证的 body identity 与 ledger 不补足该限制。
6. 已停止 run 没有 successor authorization。旧获取授权不能被产品经理解释为自动续跑或第二次真实请求。

## 正式决定

1. `LICENSE` 的类型由冻结审查合同中的**精确 seed path 与精确 role 映射**决定：仅当原始授权对象精确等于 `LICENSE` 且其冻结 role 为 `license_text` 时进入文本路由。不得用扩展名、MIME 猜测、正文内容、大小写折叠、近似名称或运行时嗅探决定类型。
2. `license_text` 路由仍必须保留固定 repository/commit/tree、path、blob SHA、mode/type、大小、请求前授权、预算、body preservation、UTF-8/NUL、有界读取、静态 scanner、ledger、终态和普通文件保护证据；不得因“只是许可证”跳过任何供应链或文件系统门禁。
3. `license_text` 不进入 C/C++ `lex_lines`、quote/include 解析、内部依赖图或 fixed-point 扩展；其文字只作为惰性审查材料。结果必须明确记录 `license_review_status=manual_review` 或等价未决状态，不得自动识别并批准许可证，不得据此产生 `source_feasible`。
4. 只有冻结合同中明确标为 C/C++ source/header 的普通 `sherpa-onnx/csrc/` `.h`／`.cc` 才可进入既有 C/C++ 解析器。任何其他非 C/C++ seed、未知 role、role/path 不一致或近似 `LICENSE` 路径必须在正文请求前 fail closed 并回到产品决策门。
5. 不修改、补签或恢复提交 `9aa40913c57cccd31105ac88385102f0a0758d63` 对应的已停止 run，也不修改其 parent freeze `2f4760d0ff3ea78de929198fba88d3744353a321`、v4 候选或历史证据。修复只能在独立新目录形成新候选。
6. 本决定不解决、也不放宽 C/C++ include 语义。include guards、条件编译、宏／生成 include、未知预处理指令及冻结规则已声明不支持的形式仍是**合同预期停止**；若未来真实 C/C++ 正文触发，应有证据地停止并回到产品决策门，不得现场扩展解析器。

## 离线就绪清单：区分三种停止

在任何后继真实请求前，独立验收必须用完全自建 fixture 固定以下分类：

| 类别 | 判定 | 必须行为 |
| --- | --- | --- |
| 内容类型路由缺陷 | 精确 `LICENSE` 或其他冻结文本 role 被送入 C/C++ 词法器 | 测试失败；不得冻结或真实运行 |
| 实现缺陷 | 冻结规则明确支持的字面量 include、请求前授权、ledger 或终态语义失效 | 测试失败；修复后重新完整验收 |
| 合同预期停止 | C/C++ fixture 含 include guard／条件编译、宏或生成 include、未知指令、续行或其他冻结规则明确不支持形式 | 在任何派生请求前确定性 fail closed；不能把该停止误报为实现 bug 或源码不可行 |

就绪清单还必须确认：精确 `LICENSE` 中的自然语言撇号、双引号、URL、Markdown 样式和多语言字符不会生成 include edge；`LICENSE.txt`、`docs/LICENSE`、`license`、Unicode／分隔符混淆和未知 role 不会被近似匹配；所有文本路由仍产生 scanner 与人工许可证审查状态，但永不自动批准采用。

## 下一项唯一开发合同

任务名：`CP2-ASR-LICENSE-TEXT-ROUTING-REPAIR-001`。

### 唯一目标

在独立新目录形成最小第一方 v5 候选：按冻结合同的精确 path/role 把 `LICENSE` 路由为 `license_text`，保留全部既有安全、身份、预算和终态门禁，同时保证 C/C++ 路由与其预期停止语义不变。候选只能输出 `license_text_routing_candidate_ready_for_freeze` 或 `license_text_routing_candidate_blocked`。

### 允许输入与动作

- 只读使用已验收第一方 v4 候选／freeze 的代码与 schema、Leader 报告、本决定和既有自建 fixture；建议新目录 `tools/asr_review_acquisition_v5/`。
- 仅修改类型路由、`license_text` 惰性审查处理、schema/terminal evidence 和为此必需的第一方调用边；依赖只限 Python 标准库。
- 新增完全自建、不得摘录真实 LICENSE 的许可证样式文本 fixture，以及精确路径／近似路径／未知 role／C/C++ 支持与预期停止回归。
- 重跑 v4 原 112 项测试及全部新增测试，至少两次独立运行；规范化输出、请求序列、ledger 和终态须逐字节一致且无跳过。
- 形成相对 v4/freeze 的最小 provenance/diff map、文件 manifest、测试摘要、静态 scanner 与 hash 证据，供 Leader 独立验收。

### 明确不做

- 不读取或复制真实 `LICENSE`、API/metadata 原文、旧 corpus、snapshot、任何其他第三方正文、模型或二进制；不跟随派生报告中的正文指针。
- 不联网、不调用真实 transport、不恢复旧 run、不发出正文请求；不修改产品代码、v4、freeze、固定 identity、9 seed、允许路径／mode/type、96 文件／1,048,576 字节、denylist、隐私或 checkpoint。
- 不按扩展名／内容猜类型，不增加新的可获取文件类型，不放宽 C/C++ include guards、条件编译、宏／生成 include、未知指令或其他停止语义。
- 不构建、执行第三方代码、安装、加载、推理、集成、形成源码快照／实现／构建输入，不批准许可证、源码、CP2、CP3 或父亲 Alpha。

### 验收与停止条件

1. 精确 `LICENSE`＋`license_text` 只走文本路由；文本内所有 C/C++ 样式标点均不生成 edge。近似路径、role/path 冲突和未知 role 在任何请求前 fail closed。
2. 文本路由仍保留身份、请求前授权、预算、正文哈希、scanner、manual license review、ledger 和终态；缺失任一项即 blocked。
3. 原 112 项与新增回归双跑全部通过，无跳过；C/C++ 支持语义及合同预期停止均被单独锁定，不能把预期停止计为工具通过或源码失败。
4. 若修复需要真实正文、第三方 fixture／依赖、网络、恢复旧 run、修改冻结对象、扩大类型／路径／seed／预算、降低安全门禁或放宽 C/C++ 语义，立即返回 blocked。
5. `ready_for_freeze` 只允许 Leader 考虑独立冻结；冻结任务不得改代码。任何真实获取仍须另开任务并取得下述新授权。

## 后继真实获取授权

本离线修复不需要 Product Lead 重复授权；它是可逆的第一方工具修复。**但 v4 的真实获取任务已经停止且没有 successor authorization，因此任何新冻结后的真实正文获取必须取得新的 Product Lead 明确授权。** 精确最小授权句为：

> 我批准在 `CP2-ASR-LICENSE-TEXT-ROUTING-REPAIR-001` 通过 Leader 独立验收并形成不可修改的新冻结后，另开一次全新任务，以设计合同提交 `a57f643bac24edef5d6601b8a59baa77060f3d2c`、设计 tree `31376c73f43caf3bbfd664d8316ffecdc589379d`、28 项输入摘要 `c318c5a5f91d4af1d2759895ab9d5296c5784eaa214548b92f25fba4096764d2`，针对 sherpa-onnx commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`、tree `fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`，按原 9 个精确 seed、仅限 `LICENSE` 与 `sherpa-onnx/csrc/` 普通 `.h`／`.cc` blob、96 文件／1,048,576 字节、既有 denylist、请求前授权与全部停止条件，从空的隔离目录执行一次有限静态正文获取。不得复用旧 corpus 或已停止 run，不得扩展解析语义、建立可采用快照、构建、执行、安装、加载、推理、集成、宣称 CP2 通过或进入 CP3。

在 Product Lead 给出该句、Leader 完成新冻结逐项映射和单独下发前，不得进行第二次真实请求。

## 保持不变与未验证

- 三步录入／找回、原始音频不落盘不上传、CP1 与 Conformer `Deferred, not removed`、目标设备与父亲 Alpha 门槛均不变。
- 固定设计、上游 commit/tree、9 seed、允许目录／类型／mode、96 文件／1 MiB、denylist、请求前授权和所有停止条件不变。
- 原始 wire JSON／HTTP headers 独立重放、8 个 C/C++ seed、闭包 fixed point、P0／人工可达性、许可证适用性、源码安全／可采用性、外部依赖、构建、运行时、模型、中文识别准确率、性能、90 秒 20 次稳定性、飞行模式、小米 15 和动态音频隐私均未验证。
- 所有既有 `block`／`manual_review` 裁决保持且互不继承。CP2 未通过；CP3 与父亲 Alpha 未批准。

允许的准确表述是：

> 产品经理只批准离线修复精确 `LICENSE` 的文本路由。已停止获取仍是 `insufficient_evidence`；没有 C/C++ 正文、源码可行性或许可证批准，任何第二次真实获取都需要新的 Product Lead 明确授权。

## 复查触发条件

- 离线候选返回 `license_text_routing_candidate_ready_for_freeze` 或 `license_text_routing_candidate_blocked`；
- 请求冻结候选或发起新的真实正文获取；
- 发现修复需要内容嗅探、扩展名猜测、放宽 C/C++ 语义或改变任何固定范围；
- 有人把路由修复、scanner 误报解释或 LICENSE 获取写成源码、许可证、CP2 或 CP3 已通过。
