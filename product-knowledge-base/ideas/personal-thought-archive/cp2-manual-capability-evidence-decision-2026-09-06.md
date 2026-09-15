# 决策记录：CP2 精确人工能力裁定证据接收

Owner: Product Lead
Last updated: 2026-09-06
Source: ../../raw/SRC-20260906-think-cp2-manual-capability-01.md；../../raw/SRC-20260906-think-cp2-manual-capability-02.md；../../raw/SRC-20260906-think-cp2-manual-capability-03.md；../../raw/SRC-20260906-think-cp2-manual-capability-04.md；../../raw/SRC-20260906-think-cp2-manual-capability-05.md；../../raw/SRC-20260906-think-cp2-manual-capability-r1-01.md
Confidence: High（v6 候选／冻结身份、两处 occurrence 的授权和人工裁定边界及非循环 authority DAG 已由 Leader 复核）；Medium（新的证据接收机制尚未实现、离线验收或冻结）
Related decisions: prd-v0.1-2026-09-04.md；cp2-source-semantics-readiness-decision-2026-09-06.md；cp2-license-text-routing-decision-2026-09-06.md；cp2-narrow-runtime-boundary-design-decision-2026-09-05.md
Next review date: 2026-09-13

Research Quality: 92 · pass
Validation Level: V2
Next evidence: 独立 v7 候选以自建 fixture 证明可信 authority map、完整 occurrence 身份、双行哈希域、防篡改／缺失／额外／冲突／错对象／不可转移及所有高优先级硬停止，并由 Leader 双跑 158 项基线与新增矩阵
Allowed next investment: 一个独立新目录中的第一方离线人工裁定证据接收候选；只用 Python 标准库、自建 fixture 和独立验收，不读取真实 header 或调用网络
Pause/Kill condition: 需要 wrapper 绕过、修改旧 controller/run/freeze、全局 token／comment 豁免、弱化 active/uncertain/lexical/unsupported/file-safety、读取真实正文、联网或复用旧获取授权

## RESULT

**APPROVED — 只批准一个独立新候选中的第一方离线、逐 occurrence、精确身份绑定的人工 comment 裁定证据接收机制。此次两处 `comment_only_nonoperative_for_this_body` 只可成为未来映射的输入依据；当前 pending 未清除，不批准相邻字段、API、实现、整份源码、网络能力不可达、源码采用、真实获取、CP2 或 CP3。**

## 已确认事实

1. v6 R1 提交 `f55fda2dea237120ce09639112767c9857dab8d5` 已通过 Leader 两次各 158 tests／961 outcomes／133 scenarios／0 skip 与完整复算；其 `source_verdict` 仍是 `insufficient_evidence`。
2. 三文档冻结提交 `d78577b8bac1108791e0c4ba3c7a0cd672958c94` 已验收，bundle `99114c1a...6160`、policy `43b323b3...1ab7`、semantic contract `2b048314...3c86` 和 role contract `1c8a95b4...0125` 均固定。当前冻结没有人工 pending 清除接口，必须保持不可变。
3. 用户只授权复核一份既有 7,939 字节 header 的两个 `websocket` occurrence。Leader 将 57、60 行分别裁定为 `comment_only_nonoperative_for_this_body`：两处都是已终止的普通文档 line comment，注释字节自身不执行操作。
4. 两行注释文本相同，因此 historical line SHA-256 与 physical-line SHA-256 分别相同；它们仍是两个不可互换 occurrence，因 line number、line byte interval 和 token byte interval 不同。
5. 注释指向相邻布尔字段的服务端用途。该线索仍相关；本次裁定没有清除相邻字段、引用实现、整份文件、其他 source/version/occurrence 或真实 WebSocket 可达性。
6. 当前 `pending_cleared=false`、`pending_override_interface_exists=false`、`new_acquisition_authorized=false`。旧 run/freeze 未改，旧授权已终止且不可复用。

## 产品判断

暂停路线会避免继续投入，但会浪费已经独立证明的 v6 精确 occurrence evidence；直接包装 controller 或全局忽略 comment 则会破坏安全边界。当前证据支持第三条路线：建立一个小型、可测试的第一方接收层，只让受信 authority 对**同一 body 的同一 occurrence**产生独立、可审计的有效状态。它的投入可逆，并能完全使用自建 fixture 验收，因此继续的价值高于立即暂停。

若机制无法在不修改旧 freeze、不引入全局例外和不降低硬停止优先级的条件下完成，则停止投入并暂停 sherpa-onnx 源码路线。

## 唯一允许的证据语义

### 原始分析不得被改写

- v6 生成的 `comment_capability_mention`、原始 `capability_review_status=pending`、source report、ledger、terminal 和旧 run 必须原样保留。
- 新机制只能追加独立的 `manual_capability_adjudication` 证据链和 `effective_comment_review_status`；不得删除 occurrence、改写旧 terminal、把旧 pending 字段反写为 clear，或通过外部 wrapper 跳过 controller。
- 只有 controller 内部在所有验证成功后，才能把一个精确 occurrence 的**有效状态**标为 `comment_only_nonoperative_for_this_body`。这只解除该 occurrence 对后继静态取证的 pending 阻塞，不产生 source/runtime/license/P0/reachability approval。

### 可信来源与完整身份绑定

每个可消费的 review package 必须由独立可信 `review_authority_map` 授权，且运行时 `Trust` 必须从独立验收／授权记录取得最终 map 的精确 canonical SHA-256，不能从不可信输入学习。未来新 freeze 不直接包含尚未建立的最终 map digest；它改为绑定下文定义的非操作性 `review_map_commitment` 精确 digest、map schema/domain 与验证代码。当前两处裁定未来只可映射以下既有身份：

- authority record SHA-256 `df26a4884e47a63c3cdbd0e2afc118e4a4f70f4ef7db9a267d6307e01b4aa9c2`；review request SHA-256 `c66a9fe77a77e15ca6dfa8f958f47ac1de4e1816de52779add3b9eee497163c7`；
- review report SHA-256 `0d8b34a06960a2c82a07effc376b60efe3c06aea1c968fb5a83b160c0d0519e6`，verification report/script SHA-256 `ca492d93813eb41dc589dbf868c49a8d423c8611d8ee180265c388ed3cf7c102`／`923d0669081f5ad7d2d6c35dace85c5c34b8ce3fbf5443a777f0292179fbe3e9`；
- upstream commit/tree、精确 source path、Git blob SHA-1、body SHA-256、body bytes、envelope SHA-256/bytes/type/mode，以及固定 `websocket` rule；
- 每个 occurrence 各自的 line number、historical line hash＋其“无 terminator”domain、physical-line hash＋其“含 terminator”domain、line byte start/end、token byte start/end、raw token 和 decision。

`occurrence_id` 必须由上述 object identity＋rule＋line＋两个 hash domain＋全部 byte intervals 的 canonical tuple 单独计算。即使两行文本及两种行哈希完全相同，57 与 60 行的 byte intervals 不同，ID 也必须不同。

## R1 澄清：非循环 authority 身份 DAG

下列对象属于彼此不同的 canonical hash domain；字段名、domain tag、版本和排除项必须进入 schema，禁止把一个对象的摘要当成另一个对象的身份：

| 对象 | 建立时间与内容域 | 可以引用 | 明确不得包含 |
| --- | --- | --- | --- |
| `H`：历史 review-context freeze | 已存在的 v6 冻结 `d78577b...` 及其 bundle/policy/semantic/role identity | 先前 v6 candidate、旧分析／ledger／terminal 身份 | v7 candidate、commitment、最终 map、Trust、新 run |
| `R`：人工 review package | 已存在的 Leader 报告 `0d8b34...`，绑定用户授权、`H`、精确 body 与两个 occurrence | `H`、授权／请求／verification identity | v7 candidate、新 freeze、最终 map、Trust |
| `C`：v7 candidate release | 离线开发完成时，对 v7 code/schema/tests/recalculator 的排序 path＋SHA canonical collection | v6 第一方来源身份和通用 intake 合同 | 真实 `R` 内容、真实 commitment/map、未来 freeze hash、Trust、运行输入 |
| `K`：`review_map_commitment` | `C` 经 Leader 接受后、v7 新 freeze 前，由单独任务建立的非操作性承诺 | `C`、`H`、`R` 的精确摘要、两个 occurrence、允许 decision、authority identity、map schema/domain | 尚未知的新 freeze digest、最终 map digest、Trust、获取授权；`operational_authority` 必须为 `false` |
| `F`：v7 execution-release freeze | 在 `K` 验收后建立，冻结 `C`、通用验证代码、policy/schema 与 `K` digest | `C`、`K` | 最终 map digest、Trust、运行输入；不得预留可后改写字段 |
| `M`：最终 `review_authority_map` | `F` 后由单独任务建立；把 `K` 已承诺字段与 `F` 的精确 digest 组合为 canonical map | `F`、`K`、`R` 及 occurrence 身份 | 自身 digest 字段、Trust、获取授权、未在 `K` 中承诺的新 clearance |
| `A`：新获取授权 | `M` 独立验收后由 Product Lead 另行批准，精确绑定一次后继获取的 release/map/scope | `F`、`M` 的精确 digest 与既有 acquisition scope | `Trust`、运行输入、旧授权或未验收 map |
| `T`：运行时 `Trust` | `A` 成立后由受信 driver 从独立验收 pins 构造 | `F`、`M`、`A` 的精确 digest | 从运行输入学习的 pin、旧 run 状态或可变 map |
| `N`：未来新 run | 只有 `A/T` 均成立后才可创建的新 release/run/ledger/terminal identity | `F`、`M`、`T`、新 input 与新证据链 | 对 `H` 或旧 run 的覆盖、resume、身份冒充 |

依赖图严格为：`H → R`，`H/R/C → K`，`C/K → F`，`F/K/R → M`，`F/M → A`，`F/M/A → T`，`F/M/T＋输入 → N`。不存在 `F → M → F`、对象引用自身最终 SHA、或从 input 回填 `Trust` 的边。

`K` 解决“freeze 时最终 map 尚不存在”的问题：`F` 只固定 `K` 的精确 digest 与 map 验证语义；`M` 建立后必须逐字段等于 `K` 已承诺的 review/occurrence/decision/authority 集合，并额外绑定 `F`。任何偏离都使 `M` 无效。防篡改的完整闭环来自 `F` 绑定 `K`、`M` 绑定 `F＋K`、`T` 独立绑定 `F＋M`，不是让 `F` 预知或包含 `M` 的最终摘要。

`R`／`K` 中所称 freeze 是历史 review-context freeze `H=d78577b...`；`M` 的 `execution_release_freeze` 字段必须指新的 v7 freeze `F`，同时通过 `K/R` 保留对 `H` 的上下文链。两个 freeze 必须使用不同字段和 domain tag，不能简称为同一个 `freeze_sha`。

任何 canonical 对象都不得在自身被哈希的 bytes 内含“自身最终 SHA”；对象摘要由外层 manifest／验收记录报告。任一阶段身份改变，都必须丢弃后续对象并从该阶段重新构建，不能原地补 hash。

### 旧记录与新记录的身份关系

“保留原 source analysis／pending／ledger／terminal identity”只表示**已发布的 v6/历史记录按原字节与原 hash 保持只读、不得覆盖或重写**。未来 v7 新 run 若应用人工裁定，只能在新的 release/run 下追加新的 adjudication／effective-status／ledger／terminal 记录；这些新记录和新状态必然拥有新的 hash 与新 identity，并只能引用旧记录摘要，绝不能把新 hash 描述成“原 identity 不变”或冒充旧 terminal 的延续。

### 不可转移与 fail closed

- clearance 不得按 token、rule、line text/hash、文件名、相邻行、body family 或 reviewer 身份扩散；任何新行、新 offset、新 body SHA、新 Git blob、新 path、新 commit/tree、新版本或新 occurrence 都重新 pending。
- 一个待处理 body 的 comment occurrences 必须与受信 map **一一且完整**匹配。缺少一个、额外一个、重复、排序／规范化歧义、unknown field、wrong object、错误 hash domain、越界／重叠 interval、token bytes 不符或身份变化，均在后继请求前 fail closed。
- 同一 occurrence 出现多个 decision、不同 authority/report、`forbidden` 与 clearance 冲突、或原始分析与人工 package 不一致时，按最保守结果停止；不得用“最后写入者”覆盖。
- `forbidden`、`unresolved`、`pending` 或未知 decision 一律继续停止。只有逐 occurrence 的 `comment_only_nonoperative_for_this_body` 可以解除其自身 pending；未被映射的新 comment mention 仍停止。

### 不能被人工裁定覆盖的硬门禁

无论 review package 内容为何，下列优先级和结果保持不变：identity／role／path／mode/type／budget／file-safety 错误；active 或 uncertain deny；lexical ambiguity/trap；unsupported preprocessor／ineligible include；证据持久化／容量失败；P0、reachability、fixed point、scanner、license review 与其他 checkpoint。人工 comment 裁定不得改变、降级、隐藏或重新排序这些停止。

## 下一项唯一任务

任务名：`CP2-ASR-MANUAL-CAPABILITY-EVIDENCE-INTAKE-OFFLINE-001`。

### 唯一目标

在独立新目录形成 v7 第一方离线候选，为 v6 controller 增加上述受信、逐 occurrence 的人工裁定证据接收路径；只用自建 fixture 证明完整绑定、不可转移、冲突处理和硬停止优先级。输出只能是 `manual_capability_intake_candidate_ready_for_freeze` 或 `manual_capability_intake_candidate_blocked`。

### 允许范围

- 只读复制已验收 v6 R1 的必要第一方代码/schema，并记录 v6→v7 provenance/diff；建议新目录 `tools/asr_review_acquisition_v7/`。提交 `f55fda2`、冻结 `d78577b` 与旧证据保持只读。
- 只新增 canonical review package、`review_map_commitment`／`review_authority_map`／Trust 的非循环 domain schema、controller 内部消费、append-only adjudication evidence、effective status 和测试；依赖仅 Python 标准库。离线候选不得创建真实 `K/M/A/T`，只能用自建 identity fixture 证明验证逻辑。
- 开发和测试只能使用完全自建的 source/body/line/rule/authority/review fixture；不得复制或转写真实 header、两行原文、private envelope 或真实 review report 作为 fixture。
- 保留 input/review package 的独立大小、记录数和 canonical encoding 上限；未知字段、重复键、非规范 JSON、非有限值、类型混淆和超限均停止。实际数值须在候选文档中冻结并覆盖边界测试。

### 最低回归矩阵

1. 完整重跑既有 158 tests／961 outcomes 基线，所有旧 expected stop、pending/no-successor、schema、预算、角色和隐私语义保持；新增矩阵不得用修改旧断言掩盖回归。
2. 两条文本和两种行 hash 都相同、但 line/byte intervals 不同的自建 comments：必须产生两个不同 occurrence ID，单个 clearance 不能清除另一个。
3. 分别篡改 authority/report/request/freeze/source commit/tree/path/blob/body/bytes/rule/line、两种 hash/domain、line/token intervals、raw token、decision、reviewer、时间与 verification identity；每项均 fail closed 且零 successor。
4. 缺失、额外、重复、错序歧义、unknown field、wrong object、partial review、重叠／越界 interval、冲突 authority/decision、replay 到新 body/version/line/token；均不得转移 clearance。
5. `forbidden`、`unresolved`、`pending`、未知 decision 和 mixed cleared＋uncleared 的结果；任何未清项继续停止。
6. review 声称 clear 但同一文件同时存在 active/uncertain deny、lexical trap、unsupported guard/directive、file-safety/role/path/budget/persistence error；原硬停止必须获胜，全部原始与人工证据仍保留。
7. 合法 package 只产生 append-only adjudication/effective status；原 source analysis、pending、ledger 和 terminal identity 不变。不得出现 wrapper bypass、全局 allowlist 或 token-wide exemption。
8. 至少两次独立完整运行；全部旧基线和新增 tests/subtests 无跳过，规范化 JSON、occurrence/evidence hash chain、ledger、terminal 与集合摘要逐字节一致，并由独立 recalculator 复算。

### 必须交付与验收

- 完整 schema/threat boundary、`H/R/C/K/F/M/A/T/N` domain、commitment/map 与 occurrence canonicalization 规范、双 line-hash domain 定义、非循环构建顺序、裁决优先级和非继承声明；
- v6→v7 逐文件 provenance/diff、158 基线映射、新增矩阵、每文件 SHA/集合摘要和旧 v6/freeze 哈希未变证明；
- 依赖仅 Python 标准库，开发／测试中真实网络、DNS、transport、第三方正文读取与执行均为零；
- Leader 在独立目录静态审查，双跑全部测试并独立复算 authority、occurrence、adjudication、no-successor、ledger 和 terminal；
- `ready_for_freeze` 只允许另行考虑 v7 冻结，不自动映射真实报告、清除当前 pending 或授权真实获取。

### 停止条件与失败回退

- 需要修改旧 v6/controller/freeze/run、通过 wrapper/sidecar 绕过内部队列门、硬编码全局 token/comment 例外或放宽任何硬停止；
- 无法区分相同行 hash 的不同 occurrence，或缺失／额外／冲突证据不能确定性 fail closed；
- 需要真实 header/report 作为 fixture、private/raw 读取、网络、第三方 parser/依赖、旧授权或真实 transport；
- 需要改变固定设计/upstream identity、9 seed、96 文件／1 MiB、path/type/mode、denylist、音频隐私或 checkpoint；
- 开始形成源码／API／字段许可、快照、实现／构建输入、模型、CP2/CP3 或父亲 Alpha 结论。

命中任一项即返回 `manual_capability_intake_candidate_blocked`，暂停 sherpa-onnx 源码路线并回到产品决策门；不得在同一任务扩大机制。

## 授权与后续顺序

普通可逆第一方离线准备已有持续授权，下一任务无需重复询问用户。后续必须分离：

1. v7 离线候选与自建 fixture 双跑；
2. Leader 独立验收；
3. 候选验收后，另开任务建立并验收非操作性 `review_map_commitment K`；它只承诺当前 `R`、两个 occurrence、decision、authority 与 map schema，不能产生 clearance 或获取权；
4. 另行建立不可修改的新 v7 execution-release freeze `F`，绑定 `C＋K`；冻结阶段不得改代码，也不得创建最终 map；
5. `F` 完成后，另开任务建立并验收最终 `review_authority_map M`，要求逐字段满足 `K` 且绑定 `F`；该映射仍不是源码获取授权；
6. 只有 `C/K/F/M` 均可复核后，才向 Product Lead 请求一项全新的、hash-bound 获取授权 `A`，再由受信 driver 构造不可从 input 学习的 `Trust T`。

当前不请求或授予新获取权限；v5/v6 旧 run、旧授权和 `d78577b` freeze 均不可复用或修改。

## 保持不变与未验证

- 两处裁定只证明注释 bytes 自身在该 body 中不执行操作；相邻布尔字段、对外 API、引用实现、WebSocket 可达性和整份源码均未清除。
- 7 个剩余 seed、9 个内部边、真实闭包、P0/reachability、许可证、源码漏洞／可采用性、wire replay、依赖、构建、制品、模型、中文准确率、小米 15 性能、90 秒 20 次、飞行模式与动态音频隐私均未验证。
- 三步录入／找回、原始音频不落盘不上传不进日志、CP1 与 Conformer `Deferred, not removed` 不变。
- 所有既有 `block`／`manual_review` 裁决保持且互不继承；`source_verdict=insufficient_evidence`，CP2 未通过，CP3 与父亲 Alpha 未批准。

允许的准确表述是：

> 两处精确 comment occurrence 已被人工确认在该 body 中不执行操作；产品经理只批准开发一个逐 occurrence、不可转移的离线证据接收机制。它不清除相邻字段、实现、真实能力或源码状态，也不授权任何新获取。

## 复查触发条件

- 下一任务返回 `manual_capability_intake_candidate_ready_for_freeze` 或 `manual_capability_intake_candidate_blocked`；
- 请求冻结、映射真实人工报告或重新获取源码；
- 出现新的 comment occurrence、不同 body/version、冲突裁定或需要改变 authority model；
- 有人把局部注释裁定或离线 intake 候选写成字段/API/源码许可、WebSocket 不可达、CP2 或 CP3 已通过。
