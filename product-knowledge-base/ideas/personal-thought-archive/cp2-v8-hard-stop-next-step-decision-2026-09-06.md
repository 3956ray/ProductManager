# 决策记录：CP2 v8 active 硬停止后的下一步

Owner: Product Lead
Last updated: 2026-09-06
Source: ../../raw/SRC-20260906-think-cp2-v8-hard-stop-01.md
Confidence: High（获取身份、请求／停止顺序、5 active＋4 comment、零 adjudication 与权限文本均由多份第一方派生证据交叉确认）；Medium（尚未审查 active 命中的局部语义和可达性）
Related decisions: prd-v0.1-2026-09-04.md；cp2-review-token-provenance-decision-2026-09-06.md；cp2-review-timestamp-representation-decision-2026-09-06.md；cp2-source-semantics-readiness-decision-2026-09-06.md
Next review date: 2026-09-13

Research Quality: 95 · pass
Validation Level: V2
Next evidence: 对同一 retained header 的 5 个 active dynamic_paths occurrence 与 2 个新增 comment 做一次 Leader-owned、只读、离线局部语义审查，输出逐 occurrence 事实、同文件数据流／调用线索、仍缺的可达性证据和明确停止结论
Allowed next investment: 一个不修改任何候选／schema／freeze/run 的最小静态证据审查；不得获取新正文、形成 clearance、启动 v9、构建或继续 CP2
Pause/Kill condition: retained object 身份或权限不匹配、需要读取其他 body／依赖才能给局部结论、试图把 identifier 命中直接降级、只补 comment 绕过 active 硬停止，或需要新获取／改冻结规则才能继续

## RESULT

**APPROVED — 当前停线保持，只批准一个 Leader 执行的、同一 retained object、只读、离线静态证据审查，判断 5 个 active `dynamic_paths` 命中的局部语义、同文件数据流／调用线索及可达性缺口，并附带刻画 2 个新增 comment。该决定不生成 clearance，不修改 v8 或 denylist，不默认建立 v9，不授权新获取、源码采用、CP2 或 CP3。**

## 当前已接受事实

1. 提交 `393640b8a6825a9a0b42c479949646e1914da199` 只代表唯一 v8 获取尝试与正确停止的派生证据获接受；不是源码验收。run collection 为 `f3da5153c3622e5554bbd636eac3fb9aeb526cd59311caa4bccc31a8f15b99c9`，本次 run 已永久结束。
2. 只取得两个文件、19,297 decoded bytes：`LICENSE` 11,358 bytes 与 `online-recognizer.h` 7,939 bytes。剩余 7 个 seed、9 个 internal edges 与 3 个 external edges 均未获取／未排队，`fixed_point=false`。
3. 5 个 definite active `dynamic_paths` 独立触发 `denylist_capability`：行 15 是 directive 内 string literal；行 110、143、156、156 是 code。模式命中不证明恶意或真实可达，但在新证据成立前仍是高优先级硬停止。
4. 同一文件还有 4 个 definite comment。原 map 只覆盖行 57／60 两个 `websocket` occurrence；新增行 64／132 `dynamic_paths` 使完整集合 4≠2，产生 append-only `manual_complete_matching` rejection。成功 adjudication 为 0，original/effective pending 均未清除。
5. 两个阻塞相互独立。即使未来完整审查四个 comment，active 硬停止仍先于 comment clearance；因此不得只补 comment 后继续。
6. `source_verdict=insufficient_evidence`、LICENSE `manual_review`、scanner 原 `manual_review` 均不变；CP2 未通过。

## 路线判断

- **立即暂停 sherpa-onnx**：安全，但还没有利用已经合法保留的同文件证据区分“保守 identifier/path 模式”与“真实动态加载／路径能力”，现在暂停的信息价值不足。
- **只补两个新 comment**：不能解除 5 个 active 硬停止，会制造错误进展感，拒绝。
- **直接建立 v9 或放宽 detector**：没有语义与可达性证据，风险过高，拒绝。
- **同对象最小静态审查**：无需新获取或工具变更，可以先回答每个 active occurrence 在当前 header 中究竟承担什么语法／数据流角色，以及哪些引用实现仍必须证明；信息增益最高且可随时停止，批准。

若审查确认任何 active occurrence 在本 body 中直接执行、配置或暴露被禁止的动态路径／加载行为，则保持硬停止并暂停当前 sherpa-onnx 路线，不进入 comment 映射或 v9。若只能证明局部非操作、但可达性依赖未取得实现，则也不得 clearance；回到产品决策门判断是否值得提出一个全新、精确授权的依赖证据请求。

## 授权依据

本次最小静态审查无需再次请求 Product Lead：

- 用户 approval `694c69bc465663cb2a8ba58e21c9757d131d6135956a92df00ed78f997979c81` 精确批准请求 JSON `2114259dc42837e96d938c65bce2b165ee47836623408c4377ffb8d11d5a392b`；
- 该请求的 evidence review 条款明确允许：“Only new retained bounded evidence may be independently statically reviewed under the fixed gate”；raw source/envelope/metadata/scanner excerpts 仍留 private、不得进 Git；
- “一次”限制的是 acquisition/run_input。该 run 已消费且不得 retry/resume；对本次新 retained bounded evidence 的后置静态审查是请求中明确列出的独立阶段，不是再次使用 acquisition A/T 发起获取；
- 本决定只收窄审查对象和输出，不扩大到新文件、依赖、网络、clearance 或 checkpoint，不能被解释为新的用户获取授权。

若需要任何新 body、依赖、metadata、网络请求或超出同文件的实现上下文，现有许可不覆盖；必须停止，由 Leader 先准备绑定对象、路径、hash、预算、用途与停止条件的新授权请求，再询问用户。

## 下一项唯一任务

任务名：`CP2-ASR-V8-ACTIVE-DYNAMIC-PATHS-STATIC-REVIEW-001`。

Owner：Leader。开发者与产品经理保持空闲，不读取原始材料。

### 精确对象

- 已接受交付提交：`393640b8a6825a9a0b42c479949646e1914da199`；output tree `7ad02a8d60493469511116950cf6020e8480d779`；
- upstream commit/tree：`917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`／`fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`；
- path：`sherpa-onnx/csrc/online-recognizer.h`；Git blob `a4559f413cae739f055509a01d5684879e4a626c`；body SHA-256 `382e6bcc6e26079419c0a0f972d89b6c48de5d9ecda49ceca592bd0786482836`，7,939 bytes；
- 本次 run 的 retained body envelope evidence SHA-256：`290e9fd9b193bf0b8a5c465de6403a6a2d0ee4021d9a22dd545e27cc5706ff8f`；原 source analysis SHA-256：`90a03a3f41409632b9de40d08578fc8d89596295832fba11af7627f4d6c01fac`。

目标 occurrence：

| 类别 | 行／绝对区间 | 已知 carrier |
| --- | --- | --- |
| active | 15 `[404,411)` | directive 内 definite `string_literal` |
| active | 110 `[3577,3590)` | definite `code` |
| active | 143 `[4756,4769)` | definite `code` |
| active | 156 `[5350,5363)` | definite `code` |
| active | 156 `[5364,5377)` | definite `code` |
| 新 comment | 64 `[2139,2146)` | definite `line_comment` |
| 新 comment | 132 `[4297,4310)` | definite `line_comment` |

### 可读边界

在 descriptor-relative、逐层 no-follow、regular-single-link、0600 文件／0700 私有目录、size/hash/body/Git blob 全部复核后，可在内存读取这一个 7,939-byte header。人工可见范围只限七个 occurrence 所在的完整 directive／声明／语句，以及解析其局部语法所必需的最小 enclosing type/function/namespace；不得展示或导出完整 header、整份 source tree 或无关行。

允许记录同文件中由目标直接引用的字段、类型、函数、默认值和调用／赋值关系，但不得跟随 include、symbol、API、metadata 或文件路径打开其他材料。任何跨文件语义只能登记为“待证据引用”，不能猜测。

### 必须判断与不得判断

对 5 个 active occurrence 逐一记录：精确 token/carrier/区间、所在语法结构、是否只是名称／声明／默认值、是否在本 body 中参与路径拼接、动态库／provider／model/token/hotword/encoder/decoder/joiner 选择、文件访问或调用，以及可达性仍依赖的精确 symbol／实现证据。

每项只能给出：

- `operative_or_policy_relevant_in_this_body`；
- `locally_nonoperative_but_reachability_unresolved`；
- `unresolved`。

不得输出“safe”“unreachable”“clear”或修改 frozen classification。对行 64／132 只做同样 hash-bound 的局部 comment 语义刻画，可标记 `comment_only_nonoperative_for_this_body`、`forbidden` 或 `unresolved`，但该记录不是 authority-map clearance，不能补写当前 run。

不得判断整个文件／源码安全、恶意性、完整闭包、P0/reachability、许可证、源码采用、构建、模型、运行时或 checkpoint。

### 必须交付与验收

- append-only 第一方 JSON＋Markdown review，绑定用户 approval/request、本决定、accepted run/source identities、七个 occurrence 完整 tuple、reviewer/time 和逐项依据；
- 独立验证报告／脚本，复算 no-follow/type/mode/size/hash、body/Git blob、七个区间/token/carrier、输出最小化和报告 hash；
- 明确列出读取的唯一 retained file、人工可见行／byte 范围、零其他 body、零网络、零执行、零候选／scanner/controller 运行；
- 输出只能是 `active_paths_review_complete_for_product_decision` 或 `active_paths_review_blocked`，然后回产品决策门；不得开始 comment map、v9 或 acquisition。

### 停止条件

- 任一 object、目录、权限、link、size、hash、Git blob、line／interval／carrier 不匹配；
- 需要其他文件、依赖、include、metadata、scanner context 或网络才能解释局部语法；此时保留 `unresolved` 并停止，不扩大读取；
- 试图把模式命中、无调用的 header 声明或 comment 直接写成运行时不可达／安全；
- 试图修改 denylist、v8、freeze/run、R/P/K/F/M/A/T、旧证据或形成 clearance；
- 发现任一 active occurrence 在本 body 中已经明确体现禁止能力：完成最小证据记录后停止并建议暂停路线，不继续审查工程化方案。

## 保持不变与未验证

- 当前 run 永久结束；旧 C/P/K/F/M/A/T/input/package/run/ledger/terminal 全部只读，不 retry/resume。当前没有新的 acquisition 授权。
- 5 个 active 硬停止与 comment complete-set rejection 均保持；pending 未清，成功 adjudication 为 0。
- 剩余 7 seed、9 internal edges、3 external edges、完整闭包、P0/reachability、许可证、源码采用性、构建、制品、模型均未验证。
- 中文准确率、小米 15 性能、90 秒 20 次、飞行模式和动态音频隐私未验证。
- 三步录入／找回、原始音频不落盘／不上传／不进日志、CP1 与 Conformer `Deferred, not removed` 不变。
- 既有 `block`／`manual_review` 裁决互不继承；CP2 未通过，CP3 与父亲 Alpha 未批准。

允许的准确表述是：

> v8 唯一获取尝试已被接受为正确停止。5 个 active dynamic_paths 模式命中仍是独立硬停止；产品经理只批准对同一 retained header 做一次局部静态证据审查，不批准 comment 绕过、v9、新获取或源码采用。
