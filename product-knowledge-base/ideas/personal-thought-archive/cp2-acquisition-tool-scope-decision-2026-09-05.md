# 决策记录：CP2 完整第一方获取工具离线开发范围

Owner: Product Lead
Last updated: 2026-09-05
Source: ../../raw/SRC-20260905-think-cp2-acquisition-tool-01.md；../../raw/SRC-20260905-think-cp2-acquisition-tool-02.md；../../raw/SRC-20260905-think-cp2-acquisition-tool-03.md
Confidence: High（离线核心验收身份、结果和缺失组件已由 Leader 独立核对）；Medium（完整获取组件与输入协议尚未开发或离线验收）
Related decisions: prd-v0.1-2026-09-04.md；cp2-narrow-runtime-boundary-design-decision-2026-09-05.md；cp2-first-party-tool-repair-decision-2026-09-05.md
Next review date: 2026-09-12

Research Quality: 86 · pass
Validation Level: V2
Next evidence: 完整第一方获取候选在零实际网络／DNS 下用合成 GitHub 响应通过端到端、F1–F9 回归、输入协议、传输约束、预算与证据持久化的 Leader 独立验收
Allowed next investment: 一个独立新目录中的第一方完整获取组件／输入协议离线开发；只用 Python 标准库、项目自建合成响应和替身传输，不冻结、不获取第三方正文
Pause/Kill condition: 需要真实网络／第三方 fixture／旧 corpus、改变固定身份／9 seed／96 文件／1 MiB／denylist／隐私／checkpoint，或无法在冻结前形成已独立验收的完整执行链

## RESULT

**APPROVED — 批准下一项唯一任务离线开发完整第一方获取组件与输入协议；不批准把提交 da9279a411d990e4c37191e22be680b2c4bfcb07 冻结为完整获取 release，不批准实际网络、真实获取、第三方正文、产品实现、构建、模型、CP2 或 CP3。**

## 已验收事实

1. Leader 已接受 da9279a411d990e4c37191e22be680b2c4bfcb07 的离线核心、schema 和合成证据候选。两次独立复跑各 66 项测试／117 条测试及子场景记录通过，规范化结果摘要为 9d86eccf2c898a772e9973f34faeec4b04cab5ccb258aaaba15ca04772fa4954；每次 83 条账本及终态哈希独立重算通过。
2. 该候选只接受 synthetic-only-unfrozen-v2、project-synthetic 与 SyntheticAdapter。它没有真实 HTTP／GitHub 传输、真实 metadata 身份导入或真实输入入口，且 source_verdict 恒为 insufficient_evidence。
3. 因此 tool_ready_for_freeze 只能解释为“离线核心候选已通过”，不能解释为“完整获取工具可以冻结”。移除 synthetic 标记、在外层先获取再喂给核心，或在冻结任务中补 transport／入口都会绕过请求前授权与独立审查。
4. 以上事实不重复推翻已经通过的 F1–F9 离线核心验收，也不证明真实传输、真实源码或 sherpa-onnx 可行。

## 正式决定

1. 保留 tools/asr_review_offline_v2/ 在提交 da9279a 的内容和验收结论不变，作为只读基线。下一开发任务不得修改该目录或把它重新标记为完整 release。
2. 批准在独立新目录建立完整获取候选 v3：从已验收核心明确派生，新增固定身份输入协议、真实形状 metadata/commit/tree/blob 解析、受限 blob 传输接口、未来 GitHub Git Data blob 传输实现、组合入口与端到端合成测试。
3. 编写未来网络组件不等于本轮执行网络。开发和验收必须使用项目自建的 GitHub-like 合成响应与替身传输；socket、DNS、HTTP、代理、外部服务和真实 API 调用必须为零。
4. 因 v2 controller 对 SyntheticAdapter 做精确类型限制，完整候选不能靠外层先 fetch 再转换为 synthetic。v3 可以在新目录内调整 adapter/controller 组合边界，但必须逐文件记录相对 da9279a 的来源与差异，并对全部 F1–F9、66 项基线和所有受影响语义重新验收。
5. 完整候选开发、Leader 独立验收、完整 release 冻结、真实获取仍是四个分离任务。冻结只能固定已经实现和验收的完整代码、输入协议与证据；冻结阶段不得新增、修改或补齐代码。
6. 用户已授权继续调度普通可逆第一方开发，本任务无需重复用户确认。既有第三方获取授权仍只在完整候选验收和另行冻结后，由 Leader 逐项映射；任何产品边界变化才需要新的 Product Lead 授权。

## 下一项唯一开发任务

任务名：CP2-ASR-FIRST-PARTY-ACQUISITION-TOOL-OFFLINE-001。

### 唯一目标

在独立新目录形成一个代码完整但开发期绝不联网的第一方获取候选，使固定合同输入、metadata 身份校验、请求前授权、受限 transport、响应／累计预算、blob 验证、include 图、P0 证据门和终态持久化能以合成响应端到端执行，并达到可提交 Leader 冻结前验收的状态。

### 允许范围

- 只读使用提交 da9279a 的离线核心、Leader 验收报告、现行产品决定和既有精确授权；不得读取旧 corpus 或第三方正文。
- 只在新的 tools/asr_review_acquisition_v3/ 目录创建第一方 Python 标准库代码、schema、说明、测试、合成 fixtures 与派生证据。
- 定义严格 canonical input：固定设计提交/tree/28 项摘要、固定 repository/commit/tree、9 seed、允许根／类型／mode、96 文件／1,048,576 解码正文字节、独立 metadata/blob 响应上限、denylist 与 policy/release hash。未知字段、重复字段、类型错误、身份不一致和非规范输入必须 fail closed。
- 定义内部 transport request 对象，不接受调用者提供任意 URL；在既有授权下 endpoint 只能由固定 GitHub host、固定 repository 和已授权 blob SHA 生成。commit/tree metadata 通过 canonical input 导入并核验，不在本任务中新增网络 endpoint；未来若需要联网取得 metadata，必须另行授权。
- 编写未来 GitHub Git Data transport 实现，但所有测试只能注入替身 opener/response。实现必须禁代理、禁重定向、禁自动重试，固定 HTTPS host/path，设置连接／读取时限并分块读取；不能信任 Content-Length 代替实际读取上限。
- commit/tree metadata 输入在消费前必须记录身份哈希与核验结果；blob 与任何后继正文 transport 动作都必须在请求前写入连续、持久化的授权和 before_request 检查点。跳转、重试或身份改变视为新请求并默认禁止。
- 对 metadata raw bytes、单次 blob raw bytes、累计 raw bytes、文件数和解码正文总字节设置相互独立的前置／累计预算；任何上限命中在正文采用、解析或后继授权前停止。

### 明确不做

- 不执行 socket、DNS、HTTP、代理或任何真实网络；不读取 GitHub 真实响应、第三方 fixture、旧 corpus、旧快照或 manual_review/block 制品。
- 不修改 tools/asr_review_offline_v2/、产品 App、Gradle、ASR 适配器、构建定义、模型、APK 或 Leader 控制面。
- 不安装依赖，不执行第三方代码，不形成真实 allowlist、snapshot、构建输入、源码可行性或许可证结论。
- 不冻结 release/policy，不映射或执行既有获取授权，不宣布 CP2 通过、CP3 获准或父亲 Alpha 可开始。

### 必须验收

1. **基线与派生**：da9279a v2 文件哈希保持不变；v3 清单逐项标识 reused／modified／new。全部原 66 项行为测试在 v3 语义上通过，任何 core 改动都有差异与回归映射。
2. **输入协议**：精确固定设计／上游身份、9 seed、范围、mode/type、预算和 denylist；重复／未知字段、路径穿越、任意 URL、错误 commit→tree 绑定、truncated != false 全部停止。
3. **完整合成链**：使用项目自建 commit/tree/blob GitHub-like 响应，从入口到终态至少两次独立运行；规范化输出、请求序列、ledger 与终态哈希逐字节一致。
4. **传输约束**：状态非 200、重定向、代理、重试、超时、短读／短写、异常大响应、错误媒体／JSON/base64/blob SHA/size、连接中断都 fail closed；失败后零未授权后续请求。
5. **授权与预算**：每次 metadata 输入消费前有身份核验记录，每次 blob transport 动作前有可重算授权和检查点；单次 raw、累计 raw、96 文件和 1 MiB 解码正文边界值与超限均有测试。
6. **零真实网络**：AST/import 审查、audit hook 与 socket/DNS/HTTP 陷阱共同证明全部开发／验收运行中实际网络事件为零；依赖仅 Python 标准库。
7. **结论门**：合成链完成也只能输出 simulation_result；真实 source_verdict 保持 insufficient_evidence，缺 P0／人工 reachability／fixed-point 任一证据时无 feasible 路径。
8. **Leader 独立验收**：Leader 静态阅读完整 v3 执行链，以独立目录重跑测试并独立重算请求序列、ledger、终态与文件清单。

### 必须交付

- v3 README、输入协议/schema、完整模块责任与威胁边界；
- v2→v3 provenance/diff map，F1–F9 与 66 项基线回归映射；
- 合成响应来源声明、测试矩阵、两次完整结果及零网络／DNS 证据；
- 请求前授权、预算、重定向／重试停止和异常持久化证据；
- 每文件 SHA-256、集合摘要、Git diff/status 和单一结论：complete_tool_candidate_ready_for_freeze 或 complete_tool_candidate_blocked。

complete_tool_candidate_ready_for_freeze 只允许进入下一项独立 Leader/产品冻结决定，不自动冻结或获取。

### 停止条件

- 需要真实网络、真实 GitHub 响应、第三方代码／fixture／依赖、旧 corpus 或现有受限制品；
- 需要修改既有固定身份、9 seed、允许范围／mode/type、96 文件／1 MiB、denylist、隐私或 checkpoint；
- 无法在动作前持久化授权，或需要允许任意 URL、代理、重定向、自动重试、未绑定 metadata；
- 对 v2 核心语义的改变无法完整列出并重跑全部受影响 F1–F9／基线；
- 开始冻结、真实获取、建立 snapshot/allowlist、产品实现、构建、模型、CP2／CP3 或父亲 Alpha。

命中任一项即返回 complete_tool_candidate_blocked 并停止，不在任务内扩大范围。

## 冻结前置与后续授权

只有 v3 完整执行链通过 Leader 独立验收，下一项单独冻结任务才可开始。冻结对象必须一次性包含：所有可执行代码、入口、输入 schema、固定 policy、transport、固定身份、9 seed、范围／类型／mode、所有响应与累计预算、denylist、测试与文件清单 hash。冻结任务只核对和签署，不改代码。

冻结完成后，再由单独真实获取任务把冻结对象逐项映射到既有 Product Lead 精确授权。完全一致时不重复要求用户确认；任何差异都停止并请求新授权。真实获取任务仍不得自动进入快照、构建、模型或 CP2 结论。

## 保持不变与未验证

- 固定设计 a57f643…f3d2c／tree 31376c73…379d／28 项摘要 c318c5a5…64d2，固定 sherpa-onnx commit 917bed95…a60e／tree fd2c4e97…bdc0、9 seed、96 文件／1 MiB 与 denylist 不变。
- 原始音频不落盘、不上传、不进日志；三步录入／找回、CP1 与 Conformer 的 Deferred, not removed 不变。
- 真实网络行为、GitHub 响应协议、固定源码闭包、P0 映射、许可证、构建、制品、模型、准确率、性能、90 秒 20 次稳定性、飞行模式、小米 15 和动态音频隐私均未验证。
- 现有 block/manual_review 裁决保持且互不继承；CP2 未通过，CP3 与父亲 Alpha 未批准。

允许的准确表述是：

> 提交 da9279a 的离线核心已通过合成验收；产品经理只批准下一步离线开发完整获取组件和输入协议。完整 release 尚未形成、未冻结，也没有实际网络、第三方正文或 CP2／CP3 批准。

## 复查触发条件

- 下一任务返回 complete_tool_candidate_ready_for_freeze 或 complete_tool_candidate_blocked；
- 请求冻结完整 release、映射既有授权或执行真实获取；
- 固定身份、seed、范围、限额、denylist、隐私或 checkpoint 需要变化；
- 有人把离线核心或完整合成候选误写为真实获取、源码可行、CP2 或 CP3 已通过。
