# 决策记录：CP2 v8 热词消费端证据后的路线

Owner: Product Lead
Last updated: 2026-09-06
Source: `/Users/orderly_ray/Leader/orchestration/reports/CP2-ASR-V8-HOTWORDS-CONSUMER-SINGLE-BODY-REVIEW-001-report.json`（SHA-256 `51336e73331f9fee139211b04d35e82b2f10c5fec3c432fac272bb2801d2463d`）；同名 Markdown（SHA-256 `9a76f05180b6bfff8ac52a665f599927411d30b357e5c47a2da36b65c2bc7828`）；Leader verification（SHA-256 `d250701798ca6a61fa68de660281d4522ee32940db900090ebc4b3b8f5659ab0`）；acceptance（SHA-256 `38d718a932e5811600cd8f18e82765c3b40cf11ad1463826cf39fb70724f7a45`）
Confidence: High（单文件身份、一次请求、局部可见范围、观察事实与依赖停止均经 Leader 独立验收）；Medium（`online-recognizer-impl.h` 的信息增益来自精确本地委派引用，正文尚未取得）
Related decisions: prd-v0.1-2026-09-04.md；cp2-v8-local-configuration-route-decision-2026-09-06.md；cp2-narrow-runtime-boundary-design-decision-2026-09-05.md
Next review date: 2026-09-13

Research Quality: 97 · pass
Validation Level: V2
Next evidence: Leader 只使用已接受的第一方派生身份记录，为固定 tree 下单个 `online-recognizer-impl.h` 准备最后一份热词链正文授权请求；准备阶段不得读取新 metadata 或正文
Allowed next investment: 一项授权请求准备；若 Product Lead 以后明确批准，最多再审查一个正文对象，之后不论结果都回产品门，不自动追踪第三文件
Pause/Kill condition: 无法从既有派生身份记录固定 blob/mode/size、请求需要新 metadata、目标文件没有 `OnlineRecognizerImpl::Create(config)` 的定义或继续委派、需要第二个依赖才能回答，或任何人试图把局部证据写成完整 buffer-only／安全／可采用结论

## RESULT

**APPROVED — 只批准 `CP2-ASR-V8-HOTWORDS-IMPL-H-AUTHORIZATION-PREPARATION-001`：为固定 `sherpa-onnx/csrc/online-recognizer-impl.h` 准备一份新的、单文件、可供 Product Lead 审阅的授权请求。当前 sherpa-onnx 获取／采用路线继续 `PAUSED`，CP2 未通过。本决定不授权正文、metadata、网络、第二文件、v9、clearance、源码采用、实现、构建、模型、集成、CP2、CP3 或父亲 Alpha。**

该候选是热词源码链允许的最后一次正文补证机会。若未来获授权后的局部审查仍只得到声明、委派或新的依赖缺口，禁止继续逐文件追踪；必须暂停这条源码路线并回产品门，在“研究其他离线中文 ASR 候选”与“明确延期个性词表能力”之间重新决定。

## 已验收事实

### Observed

1. 用户批准后的任务只对固定 `sherpa-onnx/csrc/online-recognizer.cc` 发出 1 次 GET，取得 8,993 decoded bytes；没有 retry、redirect、metadata 请求或第二正文。授权已经消费。
2. 人工可见范围严格限制为 28 行／1,237 bytes，不是整文件审查；未查看的同文件行不作断言。
3. 可见 `Register` 局部把 `hotwords-file` 注册到 `hotwords_file` 配置参数。这是上游配置表面，不证明 `think` 业务 API 暴露该参数。
4. 可见 `Validate` 局部在 `hotwords_file` 非空且 decoding method 不匹配时返回失败；另一条 C++ 短路表达式只在该字符串非空时调用 `FileExists(hotwords_file)`。若 helper 返回 false，可见分支把路径值交给错误日志宏并返回失败。
5. 空字符串只绕过上述一个局部 `FileExists` 调用，不证明整个 `Validate` 成功、完整 selector 选择 buffer、构造后的运行时不接触文件或 buffer-only 架构成立。
6. 可见 `ToString` 局部包含 `hotwords_file`，形成路径值诊断输出表面；没有观察实际运行日志、真实路径数据或个人信息泄露。
7. 可见构造函数把完整 config 委派给 `OnlineRecognizerImpl::Create(config)`，且同一局部精确引用 `sherpa-onnx/csrc/online-recognizer-impl.h`。该依赖没有读取。
8. 对 8,993-byte 正文做的 exact-token 搜索没有找到 `hotwords_buf`。这只是受限词法事实，不能证明依赖、具体实现或运行时不支持 buffer。
9. 修正后的文本 scanner 为 1 个文本、0 skipped、0 findings，只表示没有命中其配置规则；不构成源码、漏洞、许可证或采用批准。制品仍是 `manual_review`。

### Inferred

1. `hotwords_file` 已有可见的校验与诊断消费者，不再只是被动字段；但 `FileExists` 的内部行为、是否真实运行以及完整调用可达性仍未验证。
2. 精确委派点使 `online-recognizer-impl.h` 成为当前最直接、最小的下一证据候选；它可能回答 factory 是否在本地读取、丢弃、复制或继续传递配置，也可能只声明或再次委派。
3. 因此再允许一个正文对象仍有有限而明确的信息价值，但价值不足以支持后续无限 include／symbol 追踪。

### Unverified

- `FileExists` 的定义、实际文件系统效果和运行时可达性；本次没有执行代码。
- 完整 buffer/file selector、空值在其他路径的行为、具体 recognizer implementation 及编译／调用可达性。
- `think` adapter 能否在类型、构建和测试层阻止非空文件路径进入。
- 整体源码闭包、许可证／来源、当前漏洞、模型、设备性能和音频隐私门禁。

## 路线比较与投入上限

| 方案 | 信息价值 | 成本／风险 | 决定 |
| --- | --- | --- | --- |
| 现在停止 sherpa-onnx | 立即控制投入，但保留“精确 factory 下一层是否可封闭”的关键未知 | 放弃已出现的直接依赖线索 | 作为下一次失败后的默认回退 |
| 下一步查看 `FileExists` | 可解释 helper 的文件系统行为 | 不能回答完整 selector 或 adapter 能否始终传空值，容易开启另一条符号链 | 不批准 |
| 无限追踪 `impl.h`、`.cc` 和具体 recognizer | 可能逐渐补齐实现 | 无上限、审批碎片化，治理工作替代产品验证 | 拒绝 |
| 只把精确 `impl.h` 设为最后一份正文 | 可直接观察 `Create(config)` 是否在此定义、如何处理 config、是否出现文件／buffer 选择或继续委派 | 一次一对象、预算固定；若仍缺证据即终止链 | 批准请求准备 |

个性词表仍有真实用户价值，但当前产品不能为了这项能力无限消耗源码治理预算。最后一次正文机会结束后，若没有形成“可以设计可证伪的 buffer-only adapter 合同”的足够证据，就必须暂停 sherpa-onnx 源码采用路线；后续若研究其他离线 ASR，应另开独立产品决策，不能把当前材料转移为替代候选的安全结论。

## 下一项唯一任务

任务名：`CP2-ASR-V8-HOTWORDS-IMPL-H-AUTHORIZATION-PREPARATION-001`。

Owner：Leader。Developer 与产品经理保持空闲。

### 唯一目标

准备一份 pending authorization JSON＋Markdown，使 Product Lead 能决定是否允许对固定 upstream commit/tree 下的单个 `sherpa-onnx/csrc/online-recognizer-impl.h` 发起一次正文获取与局部静态审查。准备本身不获取正文、不读取新 metadata、不执行审查。

未来审查只回答：

- `OnlineRecognizerImpl::Create(config)` 是否在该文件中定义或以内联形式实现；
- 可见局部是否读取、复制、丢弃或继续传递 `hotwords_file` 或 buffer-related 配置；
- 可见局部是否包含 file/buffer selector、文件 I/O 调用或具体 recognizer factory 分派；
- 若仍委派，记录唯一 symbol/path 缺口后停止。

### 候选与身份准备

- repository：`k2-fsa/sherpa-onnx`；
- upstream commit：`917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`；tree：`fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`；
- logical path：`sherpa-onnx/csrc/online-recognizer-impl.h`；
- 候选依据只来自已验收 `online-recognizer.cc` 局部中 `OnlineRecognizerImpl::Create(config)` 与该 include 的精确引用；这不是新正文权限；
- Git blob、mode、decoded size 必须只从已接受、已提交的第一方派生 identity／manifest 记录取得并独立复核。若这些字段尚未派生保存，禁止读取 raw/private tree metadata 或联网补齐，准备任务以 `authorization_request_preparation_blocked` 停止。

### 请求上限

- 恰好 1 个正文对象、1 次 GET、0 retry、0 redirect、0 metadata 请求；
- decoded budget 写入精确文件大小，且不得超过 262,144 bytes；
- 人工可见范围最多 64 个唯一行、4,096 bytes，只限目标 factory、直接配置处理、selector／I/O 线索及最小 enclosing type/function；
- 可以对已取得的同一正文做 exact-token 定位和不变 scanner 覆盖，但零 findings 不能解释为安全；
- 禁止跟随任何 include、symbol、`.cc`、具体 recognizer、`FileExists` 或第二文件；禁止构建、执行、模型、网络扩展、产品实现、detector/schema/freeze/旧 run 修改或 v9。

### 准备任务验收

- 请求绑定本决定、当前任务合同、固定 path/commit/tree/blob/mode/size、单次预算、可见范围、用途和终止条款；
- 独立记录每个身份字段来自哪份既有派生记录，证明没有读取新 metadata/body、没有联网；
- 输出只能为 `authorization_request_ready_for_product_lead` 或 `authorization_request_preparation_blocked`；
- ready 后由 Leader 向 Product Lead 展示完整请求并等待新明确授权，不能自动创建正文获取任务。

### Product Lead 授权模板

只有当 `<BLOB_SHA>`、`<MODE>` 与 `<EXACT_BYTES>` 已由准备任务替换成独立核对的固定值后，以下句子才可提交 Product Lead；含占位符的文本无效：

> 我批准 `CP2-ASR-V8-HOTWORDS-IMPL-H-SINGLE-BODY-REVIEW-001`：只针对 repository `k2-fsa/sherpa-onnx`、upstream commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`、tree `fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`、path `sherpa-onnx/csrc/online-recognizer-impl.h`、Git blob `<BLOB_SHA>`、mode `<MODE>`、decoded size `<EXACT_BYTES>`，允许 1 次 GET 和一次离线局部静态审查；人工可见范围最多 64 个唯一行／4,096 bytes，只判断 `OnlineRecognizerImpl::Create(config)` 是否定义、config 的直接处理、file/buffer selector、文件 I/O 线索与是否继续委派。不得请求 metadata、重试、重定向、跟随任何 include／symbol／`.cc`／`FileExists`／具体 recognizer 或第二正文，不得构建、执行、加载、测试、集成、联网扩展、修改 detector/schema/freeze/旧 run、建立 v9 或形成 clearance。任一身份不匹配、超过 262,144 bytes、目标未定义或继续委派时立即停止并回产品决策门；该结果是热词源码链最后一次正文补证，不授权第三文件。本授权不批准源码采用、CP2、CP3 或父亲 Alpha。

该模板现在不是授权。

## 最终停止规则与失败回退

未来若该单文件任务获批并完成，不论结果都必须回产品决策门：

- 若目标缺失、只有声明或继续委派：热词源码逐文件补证终止；当前 sherpa-onnx 路线保持 `PAUSED`，下一产品决定只可选择替代离线 ASR 候选研究或延期个性词表，不再批准当前链第三正文。
- 若可见局部显示文件路径不可避免或 buffer-only 无法在窄边界下被证伪验证：保持 hard stop，暂停 sherpa-onnx 路线。
- 若可见局部支持构造一个可证伪的 buffer-only adapter 合同：仍不形成 clearance 或采用；只能回产品门决定是否值得开展一个不读取更多正文的项目自有 adapter／测试合同设计。
- Product Lead 不授权、身份无法从既有派生记录取得或预算超限：保持 `PAUSED`，不再投入当前热词链。

## 保持不变

- 旧 v8 run、冻结工具、denylist、comment pending、hard stop、零 clearance／adjudication 和所有历史对象保持只读。
- 本次单文件任务的 `manual_review` 不继承给其他文件，也不证明项目恶意、安全或可采用。
- 三步录入／找回、原始录音不落盘／不上传／不进日志，以及只把转写文字发送云端 AI 的边界不变。
- CP1 与 Conformer `Deferred, not removed`；CP2 未通过；CP3、父亲 Alpha、公开发布均未批准。
- 中文识别准确率、小米 15 性能、90 秒 20 次稳定性、飞行模式、权限、提醒和动态音频隐私仍未验证。

允许的准确表述是：

> 单文件消费端局部证据确认：非空 `hotwords_file` 在可见 Validate 分支触发 `FileExists` 校验，并存在路径值诊断表面；构造配置继续委派给未审的 `OnlineRecognizerImpl::Create(config)`。这不证明实际文件系统效果、完整 buffer-only 或业务可达性。当前路线继续暂停，只批准为 `impl.h` 准备最后一次单文件新授权请求。

禁止声称“已经证明 sherpa-onnx 实际读文件”“空值保证纯内存”“没有 `hotwords_buf` token 就不支持 buffer”“scanner 0 findings 表示安全”“可以继续第三文件、v9、构建或集成”。

## 产品仓库后续同步清单

本任务不修改 `/Users/orderly_ray/Projects/think`。Leader 后续同步时只需登记：

1. `online-recognizer.cc` 单文件获取／局部审查已验收，1 GET／8,993 bytes／28 行／1,237 visible bytes；
2. 非空文件参数存在局部 `FileExists` 校验和路径诊断表面，但实际 helper、完整 selector 与业务可达性未验证；
3. 当前 route 继续 `PAUSED / CP2 not passed`，不得计为 App 功能进度；
4. 唯一下一动作是 `impl.h` 授权请求准备，尚无新正文权限；
5. 若以后审查 `impl.h` 仍继续委派，终止热词逐文件链，不自动获取第三文件；
6. 全部产品、隐私、真机、性能、稳定性和 Checkpoint 门槛不变。
