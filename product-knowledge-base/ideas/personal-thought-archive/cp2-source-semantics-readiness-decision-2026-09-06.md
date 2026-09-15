# 决策记录：CP2 源码语义就绪路线修订

Owner: Product Lead
Last updated: 2026-09-06
Source: ../../raw/SRC-20260906-think-cp2-semantics-readiness-01.md；../../raw/SRC-20260906-think-cp2-semantics-readiness-02.md；../../raw/SRC-20260906-think-cp2-semantics-readiness-03.md；../../raw/SRC-20260906-think-cp2-semantics-readiness-04.md
Confidence: High（v5 的两次请求、注释命中、canonical guard 形状、停止顺序和未请求范围已独立复核）；Medium（新的词法／能力／guard 子集尚未实现或离线验收）
Related decisions: prd-v0.1-2026-09-04.md；cp2-license-text-routing-decision-2026-09-06.md；cp2-narrow-runtime-boundary-design-decision-2026-09-05.md；cp2-acquisition-tool-scope-decision-2026-09-05.md
Next review date: 2026-09-13

Research Quality: 91 · pass
Validation Level: V2
Next evidence: 独立 v6 候选只用自建 fixture 证明词法通道、注释能力待审、活动能力硬停止、严格 canonical header guard 与其余预处理形式 fail closed，并由 Leader 双跑全部基线及新增矩阵
Allowed next investment: 一个独立新目录中的第一方离线语义就绪候选；只用 Python 标准库、自建 fixture、静态检查和独立验收，不读取第三方正文或执行网络
Pause/Kill condition: 需要忽略注释、删除单个 token、求值任意预处理表达式、支持宏展开／生成 include、降低 denylist、读取真实正文、联网、恢复旧 run、改变固定身份／范围或形成实现／构建输入

## RESULT

**REVISE — v5 按冻结合同正确停止，但现行源码语义合同尚不具备继续真实获取的就绪条件。批准且只批准下一项第一方离线语义就绪任务，同时处理“注释中的禁止能力词”与“canonical header guard”两个问题；不批准修改旧 run/freeze、读取第三方正文、重新获取、源码可行性、构建、模型、CP2 或 CP3。**

## 已确认事实

1. v5 一次授权执行仅发出两次请求：`LICENSE`／`license_text` 11,358 字节和 `online-recognizer.h`／`cpp_source_header` 7,939 字节，共 19,297 字节、22 条 ledger、59 个 metadata part、100 个私有文件；1,966 个冻结文件保持一致。
2. `LICENSE` 已正确作为惰性文本处理，产生一个 `text_review_pending` 且零 C++ edge，证明上一项精确 path/role 路由目标成立。
3. 第二个文件因两处 line comment 中的 `websocket` 字样触发 `denylist_capability`。这证明保守规则按合同工作，不证明存在可达 WebSocket 能力，也不能据此删除词或默认忽略所有注释。
4. 同一文件还记录 `ifndef`、无替换内容的 guard `define` 与闭合 `endif`。这些在旧冻结合同中是独立的预期停止；只改 comment detector 会立即撞上已知 guard 问题，不能称为就绪。
5. 9 个内部边均未排队，7 个 seed 未请求，`fixed_point=false`、`source_verdict=insufficient_evidence`。运行扫描仍为 `low_indicators`／0 finding；身份扫描仍为 `manual_review`／32／4 medium，且不改变 terminal 或其他制品裁决。
6. 原始 wire JSON／HTTP headers 不能独立重放；旧 run 已终止且没有续跑或第三次请求权限。

## 路线判断

| 选择 | 用户价值 | 隐私／安全 | 工作量与可验证性 | 决定 |
| --- | --- | --- | --- | --- |
| 只删 `websocket` 或跳过注释 | 最快，但会撞上已知 guard，不能回答源码边界 | 可能漏掉注释中的真实风险线索并弱化 denylist | 改动小但不可形成可信合同 | 拒绝 |
| 立即暂停 sherpa-onnx | 停止继续沉没成本 | 风险最低 | 放弃已形成的固定身份、窄边界与第一方工具资产 | 作为失败回退保留 |
| 第一方离线语义就绪子集 | 保留离线中文 ASR 路线 | 注释证据不丢失、活动能力仍硬停止、未知语义 fail closed | 范围可由自建 fixture 充分证明，不需要第三方正文 | **选择；现行合同需 REVISE** |

若下面的子集不能在不实现通用 C/C++ 预处理器的前提下确定性成立，立即暂停 sherpa-onnx 源码路线，回到产品决策门选择其他离线中文 ASR 候选；不得继续增加例外。

## 修订后的最小语义合同

### 1. 先做字节保真的词法通道划分

第一方分析器只承担静态证据提取，不编译、不执行，也不求值程序。它必须在处理 directive、include 或 deny token 前，把当前文件完整划分为：`code`、`line_comment`、`block_comment`、`string_literal`、`char_literal`、`preprocessor`。原始字节、行号、通道、正文 SHA 与派生记录哈希必须可复算。

允许的词法子集仅含：NUL-free UTF-8、LF/CRLF、终止正确的 `//` 与 `/*...*/`、普通带转义的 string/char literal、单个物理行上的预处理指令。raw string、行续接、trigraph/digraph、未闭合 comment/string/char、无法唯一分类的 token 或编码异常全部是预期停止；不得猜测恢复。

### 2. 禁止能力证据分级，但不忽略注释

- deny token 出现在 `code`、`preprocessor`、include operand、string/char literal 或其他可能参与程序语义的通道时，继续返回 `denylist_capability` 硬停止。
- deny token 只出现在已确定的 comment 通道时，记录 `comment_capability_mention`：至少包含固定文件/body 身份、token/rule、line/channel、行哈希与证据链。它不是“安全”或“不可达”结论，必须把 `capability_review_status` 置为 `pending`。
- 分析器可以完成**当前已取得文件**的本地词法、guard、include 与能力证据汇总，但 `pending` 存在时不得排队、授权或请求任何后继正文，也不得返回 `source_boundary_feasible`。
- 未来只有独立、明确授权的人工源码能力复核才能对精确 body SHA＋line hash＋rule 给出 `forbidden`、`comment_only_nonoperative_for_this_body` 或 `unresolved`。裁定不得按 token 全局放行、不得继承给其他行／文件／版本；`forbidden` 或 `unresolved` 继续阻塞。该人工复核不属于本次离线任务。

### 3. 只支持严格 canonical header guard

唯一新增的条件结构是一个文件最外层 canonical guard：忽略空行和已确定的 comments 后，首个 directive 必须是 `#ifndef IDENT`；下一个 substantive directive 必须是 `#define IDENT`，identifier 完全一致且无 replacement tokens；最后一个 substantive directive 必须是结构上闭合该外层 guard 的 `#endif`。guard identifier 只能作为前两个 directive 的 operand，不能在正文参与其他语义；`#endif` 的可选尾随 comment 不参与匹配。不能有 `#else/#elif`、嵌套 conditional、额外 `#define/#undef` 或 directive token 拼接。

分析时不求值 guard；只把 guard 内正文作为首次 include 的保守上界进行静态检查，并记录 `canonical_header_guard`。所有其他 `#if/#ifdef/#ifndef/#elif/#else/#endif` 组合、宏表达式、feature/platform condition、宏／生成 include 与未知 directive 仍为合同预期停止。

### 4. 当前文件先完整汇总，再决定停止

对一个已取得文件，词法、能力 evidence、guard 形状和 literal include 发现必须形成一个原子本地报告；controller 不得因第一个 symptom 隐藏同一文件中其他已知停止。随后按固定优先级裁决：身份／文件安全错误 → active deny → lexical ambiguity → unsupported preprocessor → comment capability pending → 可排队的已授权 literal internal edges。任何停止或 pending 都发生在后继请求授权之前。

这只是让同一文件的停止原因完整可见，不授权多取文件，也不把 comment pending 当作通过。

## 下一项唯一任务

任务名：`CP2-ASR-SOURCE-SEMANTICS-OFFLINE-READINESS-001`。

### 唯一目标

在独立新目录形成 v6 第一方离线候选，用完全自建 fixture 证明上述词法通道、能力证据分级、canonical header guard 和原子本地裁决；输出只能是 `source_semantics_candidate_ready_for_freeze` 或 `source_semantics_candidate_blocked`。

### 允许范围

- 只读使用已验收的 v5 第一方代码/schema、freeze/Leader 报告、现行正式决定和既有自建 fixture；建议新目录 `tools/asr_review_acquisition_v6/`。
- 只修改为词法通道、deny evidence、canonical guard、本地结果聚合、schema/terminal 状态所必需的第一方代码和测试；依赖只限 Python 标准库。
- 新增完全自建、不摘录真实 LICENSE/header 的 fixture；逐文件记录 v5→v6 provenance/diff 和所有语义变化。
- 重跑 v5 全部基线及新增矩阵，至少两次独立执行；规范化结果、edge 集合、停止优先级、ledger 和终态必须逐字节一致且无跳过。

### 自建 fixture 的最低证明矩阵

1. **通道**：line/block comments、普通 escaped string/char、注释符出现在 string、引号出现在 comment、LF/CRLF；raw string、续行、trigraph/digraph、未闭合 token 和编码异常均确定性停止。
2. **能力**：同一 deny token 分别置于 code、directive/include、string、char、line comment、block comment；前四类硬停止，comments 产生 hash-bound pending 且零后继授权／请求。混合 active＋comment 必须保留两份证据并按 active deny 停止。
3. **guard 正例**：空行/comments 包围的精确 `ifndef IDENT`→无 replacement 的同名 `define`→末尾同名闭合 `endif`；guard 内 literal includes 被保守分析但不执行条件求值。
4. **guard 反例**：identifier 不同、replacement token、重复使用 guard macro、嵌套条件、`ifdef/#if/#elif/#else/#undef`、多个 guard、尾部 substantive token、宏 include、未知 directive；全部在后继请求前停止。
5. **原子裁决**：一个文件同时含 comment mention、canonical guard、internal/external includes 时，本地报告完整但 pending 阻止排队；active deny 与 unsupported conditional 同时存在时两者都记录且无后继请求。
6. **结论门**：任何 `capability_review_status=pending`、词法／预处理 stop、未闭合 edge、P0/reachability 缺失或 `fixed_point=false` 都不能走向 feasible。

### 明确不做

- 不读取／复制真实 LICENSE、header、private/raw corpus、API、metadata、source、scanner context、旧 body 或报告指针；不使用第三方 fixture。
- 不联网、不调用真实 transport、不恢复 v5 run、不发出正文请求；不修改 v5、freeze、提交 `5dbfe9ad300a8750cf2f76588983a7069760f200` 的派生证据或产品 App。
- 不删除／重命名 `websocket` 规则，不 blanket-ignore comments，不建立 token 全局例外，不求值任意预处理表达式，不宏展开，不支持生成 include，不扫描或取得新目录／类型。
- 不改变固定设计/upstream identity、9 seed、允许路径／mode/type、96 文件／1,048,576 字节、denylist、音频隐私或 checkpoint；不构建、执行、安装、加载、推理、集成或批准 CP2/CP3。

### 必须交付与验收

1. 完整 supported/unsupported grammar、capability channel policy、裁决优先级和 threat-boundary 文档；不能只提供代码行为。
2. v5→v6 provenance/diff、基线与新增矩阵映射、每文件 SHA/集合摘要，以及旧 v5/freeze 哈希未变证明。
3. 所有基线与新增测试双跑通过，无跳过；独立复算规范化事件、edge、pending、ledger 和 terminal。
4. 零真实网络/DNS/transport/第三方读取，依赖仅 Python 标准库；审计 hook 与替身传输证明 pending/stop 后零请求。
5. `ready_for_freeze` 仅表示离线语义候选可以交给 Leader 做独立验收与未来冻结，不批准任何真实正文或人工 capability 裁定。

### 停止条件与失败回退

- 无法仅靠上述严格子集唯一划分通道或识别 canonical guard；
- 需要 C/C++ 编译器、第三方 parser、任意预处理表达式求值、宏展开、真实源码 fixture 或 per-token 全局豁免；
- comment evidence 无法在不放行后继请求的情况下保留，或 active deny 不能保持硬停止；
- 需要修改任何固定身份、seed、路径、预算、denylist、隐私、checkpoint 或旧冻结；
- 开始形成源码快照、实现／构建输入、依赖、模型、CP2/CP3 或父亲 Alpha 结论。

命中任一项即返回 `source_semantics_candidate_blocked`，暂停 sherpa-onnx 源码路线并回到产品决策门；不得在同一任务扩大语法子集。

## 授权与后续顺序

用户已持续授权普通可逆第一方准备，因此本离线任务**无需重复 Product Lead 确认**。后续必须保持分离：

1. v6 离线开发与自建 fixture 双跑；
2. Leader 独立验收；
3. 另行决定是否冻结，冻结任务不得改代码；
4. 若需处理真实 comment capability evidence，另开精确 body/line/rule 绑定的人工复核任务；
5. 只有上述证据与新冻结均可审查后，才向 Product Lead 请求一次新的、精确 hash-bound 真实获取授权。

本决定不提前请求或授予新的真实获取权限，也不允许复用 v5 的授权、旧 run 或旧 body。

## 保持不变与未验证

- 固定 handle 型 CPU-only／ASR-only 设计、上游 commit/tree、9 seed、允许路径／类型／mode、96 文件／1 MiB、denylist 与请求前授权不变。
- 三步录入／找回、原始音频不落盘不上传不进日志、CP1 与 Conformer `Deferred, not removed` 不变。
- comment 中两处 token 的人工能力裁定、7 个剩余 seed、9 个内部边、真实闭包、P0/reachability、许可证适用性、源码漏洞／可采用性、wire replay、依赖、构建、制品、模型、中文准确率、小米 15 性能、90 秒 20 次、飞行模式和动态音频隐私均未验证。
- 现有 `block`／`manual_review` 裁决保持且互不继承；CP2 未通过，CP3 与父亲 Alpha 未批准。

允许的准确表述是：

> v5 按合同正确停止；注释 token 不是可达能力证明，canonical guard 也不是实现 bug。产品经理只批准用自建 fixture 建立严格、可停止的离线语义子集，任何 comment pending、未知预处理形式或活动 deny 能力仍会阻止后继正文请求。

## 复查触发条件

- 下一任务返回 `source_semantics_candidate_ready_for_freeze` 或 `source_semantics_candidate_blocked`；
- 请求冻结、人工裁定真实 comment evidence 或重新获取正文；
- 需要扩大预处理语法、引入第三方 parser、修改 denylist 或固定范围；
- 有人把 v5 正确停止、comment-only 解释或离线语义候选写成源码安全、可行、CP2 或 CP3 已通过。
