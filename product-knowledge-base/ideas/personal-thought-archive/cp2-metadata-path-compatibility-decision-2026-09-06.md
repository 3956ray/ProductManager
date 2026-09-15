# 决策记录：CP2 metadata 路径兼容修复

Owner: Product Lead
Last updated: 2026-09-06
Source: ../../raw/SRC-20260906-think-cp2-metadata-path-01.md；../../raw/SRC-20260906-think-cp2-metadata-path-02.md；../../raw/SRC-20260906-think-cp2-metadata-path-03.md；../../raw/SRC-20260906-think-cp2-metadata-path-04.md；../../raw/SRC-20260906-think-cp2-metadata-path-05.md；../../raw/SRC-20260906-think-cp2-metadata-path-06.md
Confidence: High（固定输入身份、可复现停止点、171 个名称的范围、零网络／零正文及旧冻结状态已独立核对）；Medium（修复候选和两份真实 metadata 的兼容复验尚未完成）
Related decisions: prd-v0.1-2026-09-04.md；cp2-acquisition-tool-scope-decision-2026-09-05.md；cp2-first-party-tool-repair-decision-2026-09-05.md；cp2-narrow-runtime-boundary-design-decision-2026-09-05.md
Next review date: 2026-09-13

Research Quality: 86 · pass
Validation Level: V2
Next evidence: 新兼容候选通过原 100 项基线与新增名称／恶意路径合成回归，再由 Leader 对两份固定哈希 JSON 做只读、零网络、纯解析兼容验证
Allowed next investment: 独立新目录中的最小第一方 metadata 路径兼容修复、合成测试和限定真实 metadata 纯解析验收；不修改旧冻结，不请求正文
Pause/Kill condition: 需要过滤／重写真实 metadata、放宽实际可获取路径、改变 pins／seed／预算／denylist／隐私／checkpoint、联网、读取正文或复用旧 corpus

## RESULT

**APPROVED — 批准一个独立新候选中的最小第一方 metadata 名称兼容修复，并批准在严格条件下仅使用报告指定的两份固定哈希 JSON 做最终只读、零网络、纯解析兼容验证；不批准修改旧 v2/v3/冻结、正文获取、网络、源码采用、构建、模型、CP2 或 CP3。**

## 已确认事实

1. 完整获取候选 v3 提交 e4cd300ca50be776b7077f1d7fae783642a696a7 已通过 Leader 两轮各 100 项测试验收；冻结提交 e2d64f98aae52bd5e015962191a3bf2c121beeb2 也已被接受。两者及旧 v2 继续只读。
2. 预检输入 commit.json 为 2336 字节、SHA-256 e020549c1a78964acc8e400091ee54ba29f29ffd08e5b919a1bf06801dd68089；tree.json 为 2742250 字节、SHA-256 7643e529ba6588e5dbe425acb624569218596a6316a1be9bc7d55bacd105ccd2。二者与冻结 pin 完全一致。
3. canonical input 与 commit 解析通过；tree 有 8585 条记录、零重复路径。171 个名称含 @ 等当前受限字符规则不接受的字符，且全部位于 LICENSE 与 csrc 普通 .h/.cc 的正文获取范围之外。
4. 当前错误把“元数据中惰性名称能否被无损表示”和“路径能否被授权请求正文”混成同一规则。因此 tree_path_or_duplicate 是第一方协议兼容缺陷，不是固定源码闭包、源码可行性或安全结论。
5. 原始 scanner 的 manual_review 与四项 medium 保持不变；人工复核只确认四项为时间戳／SHA 数字子串误报，并只支持这两份固定 metadata 的静态解析用途。

## 正式决定

1. 旧 v2、v3、提交 e4cd300、冻结提交 e2d64f9 及其历史证据不得修改、补签或重冻。新修复只能在独立候选目录中进行。
2. 新候选必须把路径处理分成两个不可混同的层：
   - **惰性 metadata name**：保存 tree 中每条 path 的原始 Unicode 字符串、SHA、mode、type、size、原始索引和完整集合身份；不得过滤、重写、trim、大小写折叠、Unicode normalize、百分号解码、分隔符转换或用替代字符。
   - **acquisition path authorization**：只有某条原始 path 实际成为 seed 或确定性内部依赖候选时，才应用既有严格路径、允许根、后缀、mode/type、denylist、96 文件／1 MiB 和请求前授权规则。惰性接受不赋予请求资格。
3. metadata 层仍必须 fail closed：path 必须是非空字符串且可按原值唯一索引；拒绝 NUL、控制字符、绝对路径、空／点／双点 segment、反斜线分隔混淆和其他可形成路径穿越的结构。良性 @、空格、加号、括号、非 ASCII Unicode 或组合字符本身不得因字符白名单而拒绝。
4. 唯一性按原始完整 path 精确检查。解析器不得用 normalization 合并名称；任何后续组件也不得把 metadata name 直接当作文件系统路径。实际授权层继续只接受既有严格的 LICENSE／csrc 普通 .h/.cc 路径，不允许 171 项因兼容修复进入可获取集合。
5. 不复制 v3 的数千份历史 evidence 作为新候选必要条件。新候选只保留代码、最小自建 fixture、测试、派生／差异清单和本次新证据；旧证据通过 commit、bundle、manifest 和报告哈希引用。
6. 普通可逆第一方修复无需重复请求用户授权。候选完成后必须独立验收，再建立新的独立冻结；旧冻结不重写。新冻结完成后，Leader 才能单独映射既有精确正文授权。

## 两份固定真实 metadata 的允许用途

**允许，但仅限最终兼容验收，不属于开发 fixture 或源码输入。**

同时满足以下条件时，Leader／独立验收方可以使用报告指定的 commit.json 与 tree.json：

1. 先完成所有自建合成测试、原 100 项基线回归和静态检查，固定待验候选代码 hash；真实 metadata 失败后不得原地补代码并继续同一次验收。
2. 只接受上述精确字节数与 SHA-256；从既有只读位置经 no-follow、普通单链接、目录链和有界读取检查复制到新的私有临时目录。不得枚举原目录或读取相邻 corpus／snapshot／正文。
3. 不复制进 fixture、工具目录、产品仓库、Git、构建输入或长期知识库；任务结束只保留允许的派生摘要、输入哈希和停止／通过证据。
4. 启用 NetworkGuard；只调用 candidate 的 canonical input／commit／tree 纯解析入口，不调用 run_input、transport、blob decode、正文读取或任何网络／DNS。
5. 成功只表示：8585 条条目、原始 identity 和 171 个良性范围外名称可以无损解析，同时 acquisition candidate 集合仍严格不包含这 171 项。它不表示源码闭合、可获取、可构建或 CP2 通过。
6. 若哈希／大小不符、scanner 新增未解释 block、解析发生过滤／重写、条目丢失、唯一性变化、恶意路径未停止或触发任何网络／正文请求，立即停止并返回兼容候选 blocked。

原始 scanner verdict 继续为 manual_review；本决定不把两份 metadata 宣称为普遍安全制品。

## 下一项唯一开发合同

任务名：CP2-ASR-METADATA-PATH-COMPATIBILITY-REPAIR-001。

### 唯一目标

在独立新目录中，从冻结 v3 的已验收代码形成最小兼容候选，区分惰性 metadata name 表示和 acquisition path authorization；先以自建合成数据证明良性名称兼容与恶意路径 fail closed，再交由 Leader 按上述边界对两份固定哈希 JSON 做一次纯解析兼容验收。

### 允许范围

- 只读使用 e4cd300/e2d64f9 的代码、冻结合同、Leader 报告和本决定；新候选目录建议为 tools/asr_review_acquisition_v4/。
- 只复制形成可审查候选所需的第一方源码、schema、最小测试与说明，不复制历史 run 目录、数千 evidence 或真实 metadata。
- 修改 tree metadata parser/index 与必要调用边，使全部原始 metadata 条目保留；实际授权、transport、正文 decode、ledger、预算、denylist 和 source verdict 语义保持不变。
- 使用完全自建 fixture 覆盖良性 @、空格、加号、括号、Unicode NFC/NFD、CJK 与 emoji 名称，以及绝对路径、空 segment、点／双点 segment、反斜线、NUL／控制字符、重复原始 path 和 normalization collision。
- 完整重跑原 100 项测试；为新增兼容规则、171 项不可进入授权集合、恶意路径拒绝和无损 round-trip 增加行为测试。至少两次独立合成运行的规范化结果必须逐字节一致。

### 明确不做

- 不修改 v2、v3、e4cd300、e2d64f9 或旧冻结；不在冻结阶段补代码。
- 不过滤、重写、删减真实 tree 条目，不更换 pin，不扩大 seed／允许目录／文件类型／mode、96 文件／1 MiB 或 denylist。
- 不联网，不调用 transport，不读取第三方源码正文、旧 corpus、snapshot、模型、二进制或现有 block/manual_review 制品。
- 不把两份真实 metadata 存为 fixture、提交到 Git、复制进产品仓库或用于生成 allowlist／snapshot／构建输入。
- 不构建、安装、推理、集成，不批准 CP2、CP3 或父亲 Alpha。

### 必须验收与证据

1. 新候选相对 e4cd300/e2d64f9 的逐文件 provenance/diff map；旧 v2/v3/freeze 哈希未变证明。
2. 原 100 项基线和全部新增合成测试通过，无跳过；两次规范化输出、请求序列、ledger 和终态证据一致。
3. metadata round-trip 保留原始字符串和条目属性；良性扩展字符只可作为惰性名称，不能产生 acquisition authorization。
4. 恶意路径、重复原始 path 与路径穿越在任何请求授权前停止；normalization collision 被保留为两个不同惰性名称，但两者都不能绕过严格授权规则。
5. 实际网络／DNS／transport／正文请求为零；依赖仅 Python 标准库。
6. 不复制数千历史证据；新候选 file manifest、代码 bundle、测试和小型派生证据具备 SHA-256 和普通文件属性。
7. 合成验收通过并固定候选 hash 后，Leader 才执行两份固定 JSON 的只读纯解析复验；验证 8585／0／171 和 acquisition-scope unsupported 仍为空，且无过滤、重写或正文请求。
8. 单一结论：metadata_compat_candidate_ready_for_freeze 或 metadata_compat_candidate_blocked。前者仅允许进入新的独立冻结，不继承旧冻结。

### 停止条件

- 需要改写／过滤 metadata、放宽实际授权路径、改变固定 identity、9 seed、LICENSE/csrc .h/.cc、mode/type、96 文件／1 MiB、denylist、隐私或 checkpoint；
- 需要网络、transport、真实正文、第三方 fixture／依赖、旧 corpus、snapshot 或受限制品；
- 原 100 项基线回归失败，或候选需要修改非 metadata 兼容所必需的 controller／transport／授权语义；
- 两份固定 JSON 的 hash／大小不符，scanner 出现未解释 block，或纯解析不能保持 8585 条／0 重复／171 范围外不兼容名称的身份与统计；
- 发生任何正文请求、网络事件、旧冻结改写、冻结时补代码、构建、集成或 CP2／CP3 扩大。

命中任一项即返回 metadata_compat_candidate_blocked，停止并回到产品决策门。

## 后续顺序

1. 本决定批准的第一方兼容候选开发与合成回归；
2. Leader 独立静态复核、原 100 项与新增测试双跑，以及限定两份真实 metadata 的纯解析验收；
3. 另开任务冻结新候选的完整代码、schema、输入 pins、路径双层规则、测试与 manifest；冻结任务不得改代码；
4. Leader 再另开任务，把新冻结逐项映射到既有精确正文授权；完全一致时无需重复用户确认；
5. 真实正文获取仍是独立任务，并继续受 9 seed、96 文件／1 MiB、denylist 和所有停止条件约束。

## 保持不变与未验证

- 固定设计、固定 sherpa-onnx commit/tree、9 seed、LICENSE/csrc 普通 .h/.cc、mode/type、96 文件／1 MiB、denylist 与两个 metadata pin 不变。
- 原始音频不落盘、不上传、不进日志；三步录入／找回、CP1 和 Conformer 的 Deferred, not removed 不变。
- 实际网络／DNS／TLS／HTTP、源码正文、真实闭包、P0／人工可达性、许可证、构建、制品、模型、准确率、性能、90 秒 20 次稳定性、飞行模式、小米 15 与动态音频隐私均未验证。
- 现有 block/manual_review 裁决保持且互不继承；CP2 未通过，CP3 与父亲 Alpha 未批准。

允许的准确表述是：

> 产品经理只批准修复固定 tree metadata 的名称解析兼容性，并允许两份固定哈希 JSON 做零网络纯解析验收。171 个范围外名称不会获得正文请求资格；旧冻结、源码授权和 CP2／CP3 状态均未改变。

## 复查触发条件

- 下一任务返回 metadata_compat_candidate_ready_for_freeze 或 metadata_compat_candidate_blocked；
- 请求对新候选冻结、映射既有授权或执行真实正文获取；
- 发现 171 项中存在实际授权范围路径，或需要改变任何固定边界；
- 有人把 metadata 兼容通过误写为源码可行、制品安全、CP2 或 CP3 已通过。
