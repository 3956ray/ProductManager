# 决策记录：CP2 第一方审查工具离线返工

Owner: Product Lead
Last updated: 2026-09-05
Source: `../../raw/SRC-20260905-think-cp2-tool-repair-01.md`、`../../raw/SRC-20260905-think-cp2-tool-repair-02.md`、`../../raw/SRC-20260905-think-cp2-tool-repair-03.md`、`../../raw/SRC-20260905-think-cp2-tool-repair-04.md`
Confidence: High（第一方工具缺陷、旧尝试停止状态与既有授权边界已由开发者和 Leader 独立静态复核）；Medium（修复版能否通过离线验收尚未验证）
Related decisions: `prd-v0.1-2026-09-04.md`；`cp1-deferred-cp2-entry-decision-2026-09-05.md`；`cp2-runtime-security-route-decision-2026-09-05.md`；`cp2-minimal-source-route-revision-decision-2026-09-05.md`；`cp2-runtime-boundary-route-decision-2026-09-05.md`；`cp2-narrow-runtime-boundary-design-decision-2026-09-05.md`
Next review date: 2026-09-12

Research Quality: 86 · pass
Validation Level: V2
Next evidence: 一个独立新目录中的第一方修复版工具及合成测试证据通过 Leader 离线验收；随后另开冻结任务，最后才可另开真实正文获取任务
Allowed next investment: 只允许可逆、第一方、离线、Python 标准库与合成输入的审查工具修复和验收；不允许第三方正文、网络、依赖、产品实现、构建或模型
Pause/Kill condition: 修复需要第三方正文／网络／依赖、改变固定上游身份或 9 seed／96 文件／1 MiB 边界、触碰产品隐私／checkpoint，或无法让缺失 P0 证据确定性阻止可行结论

## RESULT

**APPROVED — 批准一个全新目录中的第一方离线审查工具修复与合成输入验收；旧准备尝试保持 `BLOCKED` 并终止，不批准第三方正文获取、冻结、产品实现、构建、模型、集成、CP2 或 CP3。**

## 正式决定

1. 旧任务 `CP2-ASR-NARROW-SOURCE-BOUNDARY-FEASIBILITY-GATE-001` 在 `first_party_preflight_review_only` 阶段正确停止。旧 policy、parser、controller、fetcher、空目录证据和其哈希只能作为只读问题证据；不得原地修复、补签、重冻、强制运行或续接旧队列。
2. 当前阻塞对象是**第一方审查工具**，不是 sherpa-onnx 固定源码。现有证据没有取得或检查新的第三方正文，也没有证明上游源码可行、不可行、恶意或安全；不得把 `blocked` 外推为 `source_boundary_blocked`。
3. 批准下一项唯一任务开发独立的新版本工具，并只用项目自建合成输入验证策略、解析、控制、证据和结论语义。工具只能使用 Python 标准库，不得联网、访问旧 corpus、读取任何新第三方正文或产生产品实现／构建输入。
4. 工具开发、Leader 验收、正式冻结、真实源码获取是四个分离阶段。每个阶段只有一个冻结状态；不得在修复过程中反复重冻真实获取规则，也不得用后续修复追认旧冻结尝试。
5. 既有 Product Lead 精确授权继续作为未来源码门禁的产品范围依据，固定身份、9 seed、允许根／类型、96 文件／1 MiB 和禁止范围均不变；但本次修复任务不自动执行该授权，也不生成新的第三方获取任务。修复通过后仍须 Leader 先独立验收并另行完成正式冻结，再以单独任务启动真实获取。
6. 用户已经明确要求继续调度并开始开发。对本决定内普通、可逆、第一方离线修复不再增加额外授权仪式；若未来冻结或获取需要改变既有固定身份、seed、范围、限额、隐私或 checkpoint，必须停止并重新取得 Product Lead 明确授权。

## 已确认缺陷与必须修复的语义

| 门 | 已确认问题 | 修复后必须成立的规则 |
| --- | --- | --- |
| 内部边发现 | 尖括号 include、固定 tree 中暂缺的引号目标、相对路径、注释／续行／非法定界符可能被漏记或误分 | 每条 literal／unresolved／generated／ambiguous／条件边都必须显式登记；无法唯一解析的仓库内候选必须停止，不得静默归为 external |
| denylist 即停 | 允许目录内的禁止路径可能先入队，继续处理其他 seed 后才停止 | 一发现路径、文件名或能力 denylist 命中，就在任何后续请求之前写证据并终止；不得等目标出队 |
| P0 结论门 | 队列闭合即可输出 `source_boundary_feasible`，没有强制 P0 source map、人工扫描和 denylist reachability 完整 | 任一 P0 映射、人工裁决、denylist 可达性或 fixed point 证据缺失，都只能输出 `insufficient_evidence`／blocked，绝不能输出 feasible |
| 请求身份 | 同主机重定向可请求 ledger 未授权的其他 blob | 禁止自动重定向，或在每次跳转前重新验证并写入同一已授权 blob 身份；不能先取后验 |
| 资源上限 | 网络响应可能完整读入后才检查，1 MiB 正文上限不限制 JSON/base64 开销 | 对响应体设置独立、前置、可测试的读取上限；超限在解析或持久化正文前停止 |
| 接口兼容 | 带格式换行的 base64 可能被严格解码直接拒绝 | 只允许明确规范化的 ASCII 空白并在解码后重验 Git blob SHA／size；任何其他字符停止 |
| 中断证据 | 某些解析、写报告或中断路径不持久化结构化终态与队列 | 对可捕获失败原子写入停止原因、最后授权、队列／边状态和证据哈希；恢复不得依赖第三方正文 |
| 文件系统保护 | 父目录链接、ledger 短写及 corpus 枚举顺序未形成完整前置不变量 | 访问前逐级拒绝链接／特殊文件，使用排他且不跟随的写入，核验完整写入并 fsync；检查通过前不枚举 corpus |

以上规则是最小修复语义，不是完整安全证明。有限 denylist 正则仍不能取代后续人工能力映射；合成测试也不能证明真实上游闭包。

## 下一项唯一任务

任务名：`CP2-ASR-FIRST-PARTY-REVIEW-TOOL-REPAIR-001`。

### 唯一目标

在独立新目录中实现一个修复版第一方源码边界审查工具，并仅用合成的最小 tree、blob、include 与失败场景证明：请求前授权、内部边完整登记、denylist 发现即停、P0 证据缺失时不可误报 feasible、证据持久化和硬上限语义可确定复现。

### 允许输入与动作

- 只读使用本决定、两份 preflight 报告、既有精确授权归档、现行窄边界设计决定，以及旧尝试中的第一方文本作为缺陷证据；旧文件不得复制为“已批准版本”或被修改。
- 在新的、与旧尝试隔离的第一方工具目录中创建 policy schema、parser、controller、纯内存／本地合成 fetch adapter、测试和说明；只用 Python 标准库。
- 创建完全由项目自有的合成 fixtures；其路径、正文、blob identity 与期望结果都必须在仓库内可复核，不含任何第三方代码片段、源码正文、模型、音频或二进制。
- 进行静态检查、单元／golden 测试、故障注入、确定性重跑和只读 Leader 复核；测试不得联网。

### 必须覆盖的合成验收场景

1. 引号与尖括号的仓库内边、已见／重复边、固定 tree 中缺失边、相对路径、多义路径、宏／generated、条件分支、注释／续行、非法定界符；所有非唯一情况均显式登记并停止。
2. 非最后 seed 首次发现允许目录内的 denylist 路径或能力时，停止发生在任何后续 fetch 前，ledger 不出现停止点后的授权。
3. 队列闭合但 P0 symbol map、人工扫描裁决、denylist reachability 或任一必需证据缺失时，输出只能为 `insufficient_evidence`，不能为 feasible。
4. 重定向至未授权 blob、异常大响应、错误 SHA／size／mode／type、含非法 base64 字符、NUL、非 UTF-8、链接／特殊文件、预算临界值与超限都在正文采用前停止。
5. 可捕获异常和模拟中断产生结构化终态、连续 append-only ledger、最后安全检查点和确定性哈希；同一输入至少两次重跑结果一致。
6. 负向能力测试证明工具没有网络调用、subprocess／shell、动态代码执行、第三方依赖、产品构建入口或第三方正文 fixture。

### 必须交付

1. 新目录清单和旧尝试只读身份／未修改证明；
2. 修复版 policy schema、工具源码、合成 fixtures、测试与操作说明；
3. 每个 F1–F9 缺陷到测试编号、预期停止点与实际结果的映射；
4. 测试命令、完整结果、两次确定性重跑摘要、文件 SHA-256 和 Git diff／status；
5. 明确的 `tool_ready_for_freeze` 或 `tool_repair_blocked` 单一结论。前者只表示可进入独立冻结验收，不表示真实获取或源码可行。

### 通过条件

只有以下条件全部满足，Leader 才可接受 `tool_ready_for_freeze`：

- F1–F9 均有对应修复或明确的更严格 fail-closed 处置，并由合成测试覆盖；
- 所有请求都能在动作前对应一条不可变授权记录，denylist 命中后零后续请求；
- 缺少任一 P0 或人工证据时，无路径产生 feasible；
- 两次离线重跑的规范化输出与哈希一致，异常终态可独立重算；
- 依赖仅为 Python 标准库，没有网络、第三方正文、产品源码、构建入口、模型、音频或二进制；
- 旧尝试和旧冻结证据逐字节未变，产品三步路径与隐私／checkpoint 没有被修改。

### 停止条件

- 需要读取／复用任何旧 corpus 或取得任何新第三方正文；
- 需要网络、第三方包、外部服务、被审工具执行环境或真实上游 fixture；
- 需要修改旧尝试、补签旧冻结状态，或在修复中冻结／重冻真实获取 policy；
- 需要改变固定设计或上游身份、9 seed、允许根／类型、96 文件／1 MiB、denylist、音频隐私或 CP2／CP3 门槛；
- 工具开始形成 snapshot、allowlist、适配器、产品源码、build definition、构建输入、模型、APK 或集成结论；
- 无法在合成输入上确定性证明 fail-closed 语义。

命中任一项即返回 `tool_repair_blocked`，停止并回到产品决策门，不得边修复边扩大授权。

## 后续阶段顺序与授权边界

1. **工具开发**：执行上述唯一任务；不冻结真实获取规则，不读取第三方正文。
2. **Leader 验收**：独立复核新目录、F1–F9 映射、合成测试、依赖与哈希；只决定工具是否 `tool_ready_for_freeze`。
3. **正式冻结**：另开单一任务，把 Leader 接受的工具 release hash、policy schema、固定设计／上游身份、9 seed、范围和限额一次性冻结；冻结前不得有第三方正文。
4. **真实获取**：再另开单一任务，从空的新隔离目录按已冻结合同执行。若冻结内容与既有 Product Lead 精确授权完全一致，可由 Leader 映射并调度；若任何身份、范围、seed、限额、隐私或 checkpoint 发生变化，必须先取得 Product Lead 新授权。

不得把第 1–3 阶段合并成“修好一次就重冻一次”，也不得让工具通过合成验收自动触发第 4 阶段。

## 保持不变与未验证项

- 固定设计提交 `a57f643bac24edef5d6601b8a59baa77060f3d2c`、tree `31376c73f43caf3bbfd664d8316ffecdc589379d`、28 项摘要 `c318c5a5f91d4af1d2759895ab9d5296c5784eaa214548b92f25fba4096764d2` 不变。
- 固定上游 commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`、tree `fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`、9 seed、`LICENSE`／`csrc` 普通 `.h`／`.cc`、96 文件／1,048,576 字节不变。
- 原始录音不落盘、不上传、不进日志；三步录入／找回、CP1 `Deferred, not removed`、Conformer `Deferred, not removed` 均不变。
- 固定源码闭包、P0 映射、denylist 可达性、外部依赖、许可证、构建、制品、模型、准确率、性能、20 次 90 秒稳定性、飞行模式、小米 15 和动态音频隐私均未验证。
- CP2 未通过，CP3 与父亲 Alpha 未批准；现有 `block`／`manual_review` 裁决不变且互不继承。

允许的准确表述是：

> 产品经理只批准修复和离线验收第一方审查工具。旧源码获取准备尝试保持 blocked；这既不表示 sherpa-onnx 源码不可行，也不批准任何第三方正文、制品、实现、构建、模型、CP2 或 CP3。

## 复查触发条件

- Leader 返回 `tool_ready_for_freeze` 或 `tool_repair_blocked`；
- 请求开始正式冻结或真实第三方正文获取；
- 任何固定身份、seed、范围、限额、denylist、隐私或 checkpoint 需要改变；
- 工具需要网络、第三方依赖、旧 corpus、真实上游 fixture 或产品实现／构建输入；
- 有人把工具通过误写为源码可行、制品批准、CP2 通过或 CP3 获准。
