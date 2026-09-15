# 决策记录：CP2 ASR 运行时窄边界路线

Owner: Product Lead
Last updated: 2026-09-05
Source: `../../raw/SRC-20260905-think-cp2-boundary-route-01.md`、`../../raw/SRC-20260905-think-cp2-boundary-route-02.md`、`../../raw/SRC-20260905-think-cp2-boundary-route-03.md`、`../../raw/SRC-20260905-think-cp2-boundary-route-04.md`、`../../raw/SRC-20260905-think-cp2-boundary-route-05.md`、`../../raw/SRC-20260905-think-cp2-boundary-route-06.md`
Confidence: High（停止点、独立边界缺陷与非继承状态已由提交证据和 Leader 复核确认）；Medium（项目自有窄边界能否在源码与构建层成立尚未验证）
Related decisions: `prd-v0.1-2026-09-04.md`；`cp1-deferred-cp2-entry-decision-2026-09-05.md`；`cp2-runtime-security-route-decision-2026-09-05.md`；`cp2-minimal-source-route-revision-decision-2026-09-05.md`
Next review date: 2026-09-12

## RESULT

**APPROVED — 只批准路线 A 的下一项纯设计任务；不批准 sherpa-onnx 发现材料、运行时、源码快照、构建、模型、集成、CP2 或 CP3。**

## 正式决定

1. 选择路线 A：先设计一个**项目自有、窄化的 CPU-only／ASR-only API 与适配边界**，判断产品能否完全避开上游宽泛 Kotlin/JNI 聚合表面。下一任务只使用提交 `0ded8eb54e5d4d529759b46c62b9b5eb10722fbb` 中已经提交的结构化证据与正式文档，不获取或执行任何新第三方正文。
2. 本次 `APPROVED` 是产品路线批准，不是下一任务执行授权，也不是安全制品批准。当前 Product Lead 授权只覆盖已经完成的产品决策任务；新的设计范围必须由 Product Lead 另行明确授权。
3. 路线 B 暂不启动。若窄边界设计返回 `design_blocked`／`insufficient_evidence`，或必须保留 WAV 路径 I/O、ADSP/QNN/RKNN、TTS、宽 JNI、自动下载、用户可控动态库／模型路径中的任一项才能满足 P0，sherpa-onnx 路线立即进入 `PAUSE`，回到产品决策门，再决定是否授权其他离线中文 ASR 候选的供应链研究与门禁。
4. 选择 A 不以已投入工作为理由。已有 sherpa-onnx 成本是沉没成本；本次只因“使用现有证据完成一次低成本、可停止的边界设计”比立刻重启另一供应链更快回答核心可行性问题。设计一旦失败，不继续用沉没成本为 sherpa-onnx 辩护。
5. Conformer 继续 `Deferred, not removed`。当前不继续其静态门禁；最迟仍须在运行时获得独立批准后、任何模型加载或 CP2 两候选性能比较前恢复。CP1 父亲人工门槛也继续 `Deferred, not removed`，最迟在任何 CP3 准入决定前恢复。

## 证据解释：未闭合不等于无法闭合

### 已观察事实

- 发现任务在 Leader 要求收敛后停止：112 个文件、499,282 字节、615 条 ledger；停止后没有新增正文。
- `fixed_point=false`，有两条内部边未完成：`offline-model-config.h` 指向 `offline-zipformer-ctc-model-config.h`，以及 `spoken-language-identification.h` 指向 `offline-stream.h`。
- 因此不能把当前停止状态写成“sherpa-onnx 本身无法闭合”，101 项候选路径也不能写成最终 allowlist。

### 独立成立的边界缺陷

- 冻结规则排除了 `audio` 却漏掉 `wave`，使 `jni.cc` 的 include 取得 `wave-writer.h`；该接口明确接受 filename/path 写 WAV，与“原始音频不落盘”目标冲突。
- `common.cc` 读取、修改并记录 `ADSP_LIBRARY_PATH`；Kotlin/Core 表面包含 QNN/RKNN provider/config 与分支。
- `OnlineRecognizer.kt`、`OnlineStream.kt`、`VersionInfo.kt` 含 `System.loadLibrary("sherpa-onnx-jni")`；现有加载与 JNI/Kotlin 聚合面没有被项目拥有的最小边界约束。
- 上游 CMake 含宽泛 source／平台能力与找不到 ONNX Runtime 时的下载路径；332 条 system/external 边及外部依赖、许可证和源码—二进制对应尚未闭合。

这些缺陷不依赖两条未完成边是否补齐，足以证明**当前候选不是 CPU-only／ASR-only、音频内存限定的产品边界**。发现材料继续为 `manual_review`，不得进入阶段 B。

## 路线比较

| 维度 | 路线 A：项目自有窄 API／适配边界设计 | 路线 B：暂停 sherpa-onnx，研究其他离线中文 ASR |
| --- | --- | --- |
| 用户价值 | 保留本地中文、飞行模式与低延迟方向；先回答能否支持“按住说话—本地转写”核心路径，但尚未证明准确率或性能 | 可能找到更小、更清楚的运行时；中文效果、Android 成熟度与 90 秒体验全部重新未知 |
| 隐私 | 可把“PCM 只在内存、无 WAV 路径、无上传、无内容日志”写成项目拥有的可证伪边界；当前只是设计，不是动态证明 | 新候选不天然更安全；仍需逐项证明音频、网络、日志、文件与模型行为 |
| 工作量 | 一项只读、设计型任务；复用已验收证据，不继续 corpus 或构建 | 重启候选搜索、许可证、供应链、模型兼容、Android、中文准确率、性能与真机门禁，工作量明显更高 |
| 可验证性 | 输出可形成明确 allow/deny API、数据流和未来测试计划；能快速得出可行、阻塞或证据不足 | 可从零定义门禁，但候选差异大，先有研究结果后才能比较真实可验证性 |
| 沉没成本 | 只复用知识，不继承任何制品裁决；失败即停止 | 放弃 sherpa-onnx 专属研究成本，但若 A 失败，这个代价应接受 |
| 当前决定 | **选定** | 作为 A 失败后的回退；不自动启动 |

## 证据身份与内容哈希

| 证据 | 固定身份／SHA-256 |
| --- | --- |
| 本次产品决策合同 | `ba885073ae2486b99954833ee131926faf4802bdcbe9b7d6fe9b94f652d314c5` |
| `think` 安全证据提交 | commit `0ded8eb54e5d4d529759b46c62b9b5eb10722fbb`；审查目录 Git tree `1bdd940c85554147b904b033c59095f849d22a46` |
| `manual-review.md` | `7f89be4b323340ec69a8f5cdc5af9b1418fb62237a0f74ac3a48c7f81d1a83af` |
| `security-verdict.json` | `8b0a87846101fe01f51aa1c6d4b6c560838e8b74724ac00f50305ea3af4673e0` |
| `acquisition-ledger.jsonl` | `8b58b9ae18a46a7fb46c5141dbbaf183b43d1da7b4e597f32b9e77143b8ef4cf` |
| `acquisition-stop-evidence.json` | `e1139b4c284ddb4ddde1c801ec3f0b62cb7b06f156e24769dc880c993ffef3ee` |
| `post-stop-static-analysis.json` | `b2af74b57e8dd62e0f8f1f23cd1949cb78a1a1fa9c5204a1e2f0245d614da319` |
| `candidate-final-allowlist-current.json` | `9a96c1887ba249390cbaac5b7d0beb0ed2e9aecbbe637b28a447f6c7e3ac9dab` |
| `dependency-license-review.md` | `f3c20b7caa7f6569c4e3c9b2fbe3b1fae2417686e81aae425b820a6c6b8d08c2` |
| Leader 验收报告 | `c413bcc7cd6b558463b0d88ffae31bbf5ce3cdb441c3cee0fd52b4159802545e` |

## 下一项唯一任务

任务名：`CP2-ASR-NARROW-RUNTIME-BOUNDARY-DESIGN-001`。

### 唯一目标

只基于已经提交的结构化证据和正式决定，形成一份**项目自有的 CPU-only／ASR-only 窄 API／适配边界设计**，并裁决该设计能否在不纳入已知禁止能力、不获取更多第三方正文且不形成实现／构建输入的前提下，为后续独立源码审查提供可验证合同。

### 允许输入

- `think` 提交 `0ded8eb54e5d4d529759b46c62b9b5eb10722fbb` 下 `doc/security-reviews/sherpa-onnx-static-closure-discovery/2026-09-05/` 已提交的 JSON／JSONL 结构化证据和正式 Markdown 复核文件；
- Leader 验收报告 `CP2-ASR-STATIC-CLOSURE-DISCOVERY-GATE-002.md`；
- 现行 PRD、CP1／CP2 决定和本决定；
- 只读分析工具可用于解析上述自有证据文件，但不得读取隔离 corpus、未提交临时材料或新的第三方正文。

### 必须形成的设计内容

1. `Observed / Inferred / Proposed` 三层证据矩阵，所有允许或禁止能力都回到固定提交中的人类可读证据。
2. 项目公开边界的最小能力表：仅允许由 App 持有的固定运行时／固定已批准模型句柄、内存 PCM 输入、stream 生命周期、decode、结果读取、版本信息和释放；禁止向产品层公开任意音频 filename/path、任意 provider、任意动态库路径或上游聚合配置对象。
3. 加载所有权：只能由项目适配层以固定内部库名执行一次受控加载；不得把 `System.loadLibrary`、`prependAdspLibraryPath` 或用户可控路径暴露为业务 API。此条只是拟议设计，不批准任何库。
4. 音频数据流与不变量：原始 PCM 只在受控内存中短暂存在；取消、成功、错误与超时都必须释放；不得写 WAV／文件、上传、进入日志或遥测。模型资产与音频数据必须是两个不同信任边界。
5. 明确 denylist：`wave-writer`／文件式音频 I/O、ADSP、QNN、RKNN、TTS、VAD、speaker、denoise、punctuation、WebSocket、PortAudio、运行时下载、自动 FetchContent、上游 broad JNI aggregator、非必要 public C/C++ API 与用户可控动态加载全部排除。
6. 未来验证计划：说明后续若获授权，需要怎样在源码 allowlist、项目自有 JNI/Kotlin 适配、无下载构建、依赖、制品、模型、文件系统差分、网络观察和小米 15 上逐层验证；不得在本任务创建这些实现或输入。
7. 设计结论只能为 `design_feasible`、`design_blocked` 或 `insufficient_evidence`；不得使用 `approved_with_controls` 冒充第三方制品裁决，也不得建议直接进入构建。

### 明确不做

- 不继续或读取隔离 discovery corpus，不补两条内部边，不重冻 policy／allowlist，不建立最终快照；
- 不获取新正文、替代运行时、依赖、工具链、模型、音频或二进制；
- 不修改产品源码、JNI、Kotlin、CMake、Gradle、Manifest、权限或测试，不创建适配器代码、头文件、build definition 或可编译伪实现；
- 不运行、构建、配置、安装、加载、推理、真机测试或动态验证；
- 不启动路线 B，不通过 CP2，不进入 CP3，不批准父亲 Alpha。

### 验收条件

- 每个公开 API 都映射到 P0 用户路径；每个已知危险能力都有明确排除与证据引用；
- WAV／文件式音频、ADSP/QNN/RKNN、TTS、自动下载、宽 JNI/Kotlin 聚合面和用户可控加载不出现在允许边界；
- 受控固定库加载、模型资产、内存 PCM、结果和释放生命周期边界清晰，且不把设计写成动态证明；
- 明确保留 `fixed_point=false`、两条未完成内部边、外部依赖／构建／模型／真机等未知，不把设计当作源码闭包或可构建性证明；
- 输出完整的未来源码／构建／动态验证计划、失败回退和非继承声明；任务结束后停止，等待产品经理与 Product Lead 决定。

### 停止条件

出现任一项即停止并返回 `design_blocked` 或 `insufficient_evidence`：

- 需要新第三方正文、继续 corpus、重冻、运行 CMake／源码或修改产品代码才能完成设计判断；
- 任一 P0 必需能力只能通过 WAV／任意文件音频路径、ADSP/QNN/RKNN、TTS、宽 JNI、自动下载或用户可控动态加载提供；
- 无法用现有证据区分音频数据、模型资产、动态库和日志边界；
- 设计开始形成可编译源码、构建输入、依赖选择、模型批准、性能结论或 CP3 范围；
- 必须降低原始音频不落盘／不上传／不进日志、第三方安全门禁、飞行模式、真实语音、目标设备、90 秒 20 次稳定性或 CP1 延后人工门槛。

## Product Lead 新授权

需要新授权。前一任务授权绑定 `CP2-ASR-STATIC-CLOSURE-DISCOVERY-GATE-002`，已随该任务停止并验收而耗尽；本次产品决策合同也不自动授权新设计任务。

精确最小授权句：

> 我批准 `CP2-ASR-NARROW-RUNTIME-BOUNDARY-DESIGN-001`：仅允许使用 `think` 提交 `0ded8eb54e5d4d529759b46c62b9b5eb10722fbb` 中 `doc/security-reviews/sherpa-onnx-static-closure-discovery/2026-09-05/` 的已提交结构化证据与正式复核文件、Leader 验收报告和现行产品决定，设计项目自有 CPU-only／ASR-only 窄 API／适配边界；不得获取新正文、继续或读取隔离 corpus、重冻、修改源码、创建实现或构建输入、下载依赖／模型／替代运行时、执行／构建／集成、宣称 CP2 通过或进入 CP3。

## 失败回退

若设计为 `design_blocked`／`insufficient_evidence`，或发现 P0 必须依赖禁止能力：

1. 将 sherpa-onnx 路线标记为 `PAUSE`，不再继续 corpus、快照或实现；
2. 回到 Product Lead 产品决策，不自动切换；
3. 只有另行授权后，才可提出 `CP2-OFFLINE-ASR-ALTERNATIVE-SUPPLY-CHAIN-RESEARCH-001`，只研究候选身份、许可证、Android／arm64、离线中文与供应链门禁，不下载、安装、构建或加载候选；
4. 新候选不继承 sherpa-onnx、AAR、模型或发现材料的任何裁决，也不得降低 CP2 的真实语音、性能、稳定性、飞行模式与隐私门槛。

若设计为 `design_feasible`，也只允许回到产品决策门审查设计；任何源码级适配、最终快照、依赖或构建仍需新的单一任务与新授权。

## 现有状态与未验证项

- 现有源码归档 `block`；官方 AAR、Zipformer 四文件集、首次部分快照和本次发现材料均为各自范围的 `manual_review`，不得采用，裁决互不继承。
- 当前 discovery 未固定点，两条内部边及其后续闭包未验证；这不等于上游无法闭合。
- 项目自有窄 API／适配边界尚未设计或审查；上游 broad JNI/Kotlin 隔离可行性未知。
- TTS 最终排除、外部依赖、许可证／NOTICE、ONNX Runtime、工具链、源码—二进制 provenance、arm64 CPU-only 构建均未验证。
- 任何模型加载、中文准确率、30 秒延迟、内存、耗电、发热、90 秒录音 20 次、飞行模式与小米 15 均未验证。
- 原始音频不落盘、不上传、不进日志只有产品要求，尚无集成与动态证据。
- CP1 父亲人工可用性未通过；CP2 未通过；CP3、父亲 Alpha 与公开发布均未批准。

## 禁止声明

在对应门禁正式通过前，不得声称：

- sherpa-onnx 无法闭合，或本次未固定点证明上游整体不可用／恶意；
- 发现材料、候选 101 路径、项目自有边界、当前 AAR／模型／快照已经安全、闭合、可构建或获准；
- WAV、ADSP/QNN/RKNN、TTS、自动下载或宽 JNI/Kotlin 已经在源码或运行时排除；
- 本地中文识别、90 秒稳定性、飞行模式、小米 15或音频隐私已验证；
- Conformer 或 CP1 人工门槛已删除；
- CP2、CP3、父亲 Alpha、公开发布或更高 Validation Level 已批准。

允许的准确表述是：

> 产品经理只批准在 Product Lead 另行授权后，用已提交证据设计项目自有 CPU-only／ASR-only 窄边界。该设计任务不获取、修改、构建或集成第三方内容；现有发现材料仍为 manual_review，CP2 未通过，CP3 未批准。

## Research Quality / Validation Level 影响

- Research Quality：保持 86；本决定提高安全边界与路线选择的可追溯性，不增加市场、父亲使用或动态技术证据。
- Validation Level：保持 V2；没有新增真实产品使用。
- Allowed next investment：仅在 Product Lead 使用精确授权句批准后，完成一个只读、设计型、可停止的窄边界任务。
- 三步录入／找回、原始音频不落盘不上传、CP2 全部真机／性能／稳定性／飞行模式门槛保持不变。

## 复查触发条件

- Product Lead 批准、拒绝或修改下一设计任务授权；
- 设计任务返回 `design_feasible`、`design_blocked` 或 `insufficient_evidence`；
- 请求继续 corpus、补闭包、创建快照、修改源码、构建、下载依赖／模型、恢复 Conformer、切换其他 ASR 或进入 CP3；
- 出现上游最小 CPU-only／ASR-only API、可验证无下载构建或合格 reviewer 新证据；
- 任何人试图把路线批准写成制品批准或 CP2 通过。
