# 决策记录：CP2 热词证据链终止后的路线

Owner: Product Lead
Last updated: 2026-09-06
Source: `/Users/orderly_ray/Leader/orchestration/tasks/CP2-ASR-HOTWORDS-CHAIN-TERMINATION-ROUTE-DECISION-001.json`（4,359 bytes；SHA-256 `9fcb533c661cbb652448f0fa6bfbe574c11e4161558392e0ec6ce6281d9a9aa9`）；`/Users/orderly_ray/Leader/orchestration/reports/CP2-ASR-V8-HOTWORDS-IMPL-H-SINGLE-BODY-REVIEW-001-report.json`（6,098 bytes；SHA-256 `d8d0888607c189a042c1808ef60b04abad15b549992f220260669885b1430d44`）；同名 Markdown（1,443 bytes；SHA-256 `28b19012996b440f2ebf7560f8f14b676d24d45403548d1a93fa3d7aad936bab`）；Leader verification JSON（3,657 bytes；SHA-256 `731abd580c46267bec3ce638428d06530ed3cfd4353bb65271104c851a0c80b2`）；acceptance JSON（3,672 bytes；SHA-256 `dfeef80f7f0cf8ad5b351910d00778b38d29ed0d9f8109ffcaa1665b4bb3c914`）；`/Users/orderly_ray/Projects/think/doc/cp2-v8-hotwords-consumer-route-decision-2026-09-06.md`（13,812 bytes；SHA-256 `f9d5fda7d29d242861b92af3641f69a69a7ce3f319da4e12d4e441ebaf0f14a8`）
Confidence: High（单文件身份、请求数量、可见范围、声明停止和产品仓库未变均经 Leader 独立验收）；Medium（替代候选尚未开始官方材料调研）
Related decisions: prd-v0.1-2026-09-04.md；cp2-v8-hotwords-consumer-route-decision-2026-09-06.md；cp2-runtime-security-route-decision-2026-09-05.md
Next review date: 2026-09-13

Research Quality: 98 · pass
Validation Level: V2
Next evidence: 对 3–5 个非 sherpa-onnx 的离线中文 ASR 候选执行有上限的官方公开材料调研，形成证据卡、比较矩阵与最多两个候选的后续安全门禁建议
Allowed next investment: 一项只读官方材料研究；不下载源码、模型、二进制或制品，不实现、不构建、不测试、不修改 `think`
Pause/Kill condition: 官方材料不能同时证明中文、Android、本地离线与可识别许可证／来源；需要读取源码、下载制品或实际运行才能继续判断；或在预算内不足两个可比较候选

## RESULT

**APPROVED — 永久终止当前 sherpa-onnx 热词逐文件补证链；只批准下一项 `CP2-ALTERNATIVE-OFFLINE-CHINESE-ASR-OFFICIAL-RESEARCH-001` 官方材料研究。个性词典／个性词表实现标记为 `Deferred, not removed`。当前核心 ASR 采用仍被阻塞，sherpa-onnx 既有 `block`／`manual_review` 制品不得恢复、继承或采用，CP2 未通过，CP3 与父亲 Alpha 未批准。**

本决定选择“研究其他离线中文 ASR 候选”，而不是只延期个性词表后继续现有运行时。原因是语音输入、本地中文识别和原始录音隐私是产品 P0；单独延期个性词表不能提供一个可采用的核心 ASR，也不能消除 sherpa-onnx 当前供应链、运行时边界、模型与真机门禁。

## 已验收事实

### Observed

1. 最后一个获授权的 `online-recognizer-impl.h` 任务只发出 1 次固定 GET，取得 2,286 decoded bytes；固定 Git blob 与正文 SHA-256 匹配。没有 retry、redirect、metadata 请求或第二正文请求，该次授权已经消费。
2. 人工只查看第 20、24、25 行，共 3 个唯一行／129 visible bytes；可见 `OnlineRecognizerImpl` 类名，以及以分号结束的 `Create(const OnlineRecognizerConfig &config)` 声明。
3. 该 occurrence 是声明，不是函数体。按预先批准的立即停止规则，任务没有查看其他方法、同文件其他定义或依赖，也没有跟随第二来源。
4. 文本 scanner 覆盖 1 个文本、0 skipped、0 findings、`low_indicators`；这只表示未命中已配置指标，不是安全、许可证、源码或采用批准。该正文仍为 `manual_review`。
5. Leader 已正式接受本次停止，并将当前热词 source-by-source evidence chain 标记为在本路线下永久终止；产品仓库提交 `0043d343d4cb30b9c212bcb111c618fb2ca1d6e9` 保持干净、未修改。

### Inferred

1. 这 3 行没有显示 config 消费、file／buffer selector 或文件 I/O，因此不能关闭已识别的运行时边界缺口。
2. 继续追踪同文件其他位置、`.cc`、`FileExists`、具体 recognizer 或新的 include／symbol 会违反既定证据预算，并重新开启无上限的逐文件链；产品治理成本已经超过当前可接受的信息增益。
3. 转向官方材料层面的替代候选研究，能够在不接触源码和制品的前提下先筛掉不支持中文、必须上传音频、缺少 Android 路径或许可证不清的候选，用户价值与可验证性优于继续追踪第三来源。

### Unverified

- 不能由当前局部可见范围推断整个 `online-recognizer-impl.h` 没有定义，也不能推断 sherpa-onnx 的 buffer-only 热词能力可行或不可行。
- `Create` 实现、config 实际处理、file／buffer selector、`FileExists` 效果、具体 recognizer 分派、业务可达性和项目自有 adapter 约束仍未验证。
- sherpa-onnx 的完整源码闭包、许可证／来源、当前漏洞、模型、Android 集成、真实音频隐私、性能、发热、稳定性与小米 15 结果仍未通过。
- 尚未识别或批准任何替代 ASR 候选；也未证明替代候选具备个性词表、热词或短语偏置能力。

## 路线比较

| 路线 | 用户价值 | 隐私 | 工作量与可验证性 | 沉没成本 | 决定 |
| --- | --- | --- | --- | --- | --- |
| 继续 sherpa-onnx 第三来源链 | 可能补齐热词实现细节，但不直接提供可采用运行时 | 当前仍有未关闭的文件路径、动态能力和音频边界 | 范围继续扩张，且违反已承诺的停止规则 | 继续受已投入治理成本牵引 | 拒绝 |
| 只延期个性词表，继续现有运行时 | 保留基础语音设想，但没有合格核心运行时 | 不能恢复已失败或未通过的制品 | 表面工作量小，实际无法进入 CP2 真机门禁 | 容易把延期误写成解锁 | 不采用为主路线 |
| 研究其他离线中文 ASR 候选 | 直接服务“按住说话、本地中文转写”的 P0 | 可先排除强制云端音频候选 | 官方材料筛选成本有上限，可形成下一次安全门禁输入 | 接受停止现有链，减少继续加码 | **批准** |
| 暂停全部 ASR 工作 | 风险最低 | 不增加暴露 | 无法推进产品最关键入口 | 放弃当前学习机会 | 研究不足时的回退 |

## 个性词表状态

个性词典／热词／短语偏置仍是 P0 用户价值，尤其用于人名、地名、专有词和英文缩写，但实现路线从当前运行时中解耦，状态改为：

> `Deferred, not removed — implementation route unresolved`。

该延期只控制当前投入，不产生以下含义：

- 不表示核心 ASR 已可采用；
- 不恢复 sherpa-onnx 的任何 `block` 或 `manual_review` 制品；
- 不取消 CP2“常用专名在加入词典后正确率至少 90%”的现行门槛；
- 不允许把云端音频识别作为替代；
- 不允许默认把完整词典、原始音频或全部档案发送到云端。

在 CP2 通过前，必须二选一：验证最终候选的个性词表／热词／短语偏置机制并达到门槛；或由 Product Lead 通过新的正式产品决定修订该门槛。官方材料研究可以把不具备已证实个性词表能力的候选列为“核心 ASR 待门禁候选”，但不能因此宣称 CP2 已通过。

## 下一项唯一任务

任务名：`CP2-ALTERNATIVE-OFFLINE-CHINESE-ASR-OFFICIAL-RESEARCH-001`。

Owner：Leader。产品经理执行研究；Developer 保持空闲。

### 唯一目标

只基于官方公开材料，识别并比较 3–5 个非 sherpa-onnx 的 Android 本地／离线中文 ASR 运行时候选，输出可追溯证据卡、比较矩阵与最多两个值得进入未来独立安全 intake 的候选。该任务不是采用、源码审查、安全批准、实现或 CP2 验收。

### 允许输入与预算

- 官方产品／项目文档、官方仓库 README、LICENSE、官方 release metadata、官方 Android／平台集成文档；
- 本知识库与 Leader 已接受的派生产品／安全决定，只用于保持门槛一致；
- 3–5 个候选；每个候选最多 3 个官方页面，另加最多 3 个跨候选的 Android／许可证／安全官方页面，总计最多 18 个页面；
- 不使用社区热度、星标、营销转载或模型生成内容作为核心结论来源；未知项必须明确标为未知。

### 比较标准

每个候选必须逐项记录：

1. 是否有官方证据支持本地／离线处理，核心路径是否要求上传原始音频；
2. 普通话／简体中文支持，以及流式或录后识别形态；
3. Android 调用路径、arm64-v8a 与 CPU-only 可行性；
4. 音频输入是否支持内存 PCM／stream，是否强制文件路径；
5. 原始音频落盘、上传、日志与缓冲释放的可控性；
6. runtime／模型大小、最低系统或硬件要求的官方披露；
7. runtime 与模型许可证、商业使用边界及来源可识别性；
8. 维护者、发布渠道、版本与更新来源；
9. 个性词表、热词、phrase biasing 或转写后纠错支持；
10. 是否可在小米 15 上设计飞行模式、30／90 秒性能、90 秒 20 次稳定性和音频不落盘验证；
11. 后续供应链／源码／二进制安全门禁是否能够独立、可复现地执行；
12. 预计 Android 接入复杂度与主要未知。

### 候选硬筛选与交付

进入最多两个候选 shortlist 前，至少要有官方材料支持：中文／普通话、Android 调用路径、本地或离线核心识别、可识别的许可证与来源，并且核心能力不强制把原始音频发送云端。任一项目缺证时不得推断补齐。

交付物仅包括：

- 每个候选一张 Evidence Card；
- 一张按上述 12 项标准比较的矩阵；
- 一份结论备忘录，最多推荐两个候选进入未来单独的安全 intake；
- 个性词表能力状态与缺口；
- `research_sufficient_for_security_intake_decision` 或 `research_insufficient`。

### 明确不做

- 不读取任何候选的源码文件、源码树、私有内容或 corpus；
- 不 clone、不下载或保存源码归档、模型、AAR、APK、库、二进制、样本或安装包；
- 不安装依赖、不运行代码、不构建、不加载模型、不推理、不 benchmark；
- 不修改 `/Users/orderly_ray/Projects/think`，不形成可直接用于实现／构建的文件清单、脚本、补丁或集成输入；
- 不恢复 sherpa-onnx 热词链，不把它作为候选，只能作为已暂停基线；
- 不批准候选、安全 intake、源码、模型、实现、CP2、CP3、父亲 Alpha 或公开发布。

### 停止与回退

- 若判断某项必须读取源码、下载制品、登录、接受额外条款或运行代码，记录证据缺口并停止该候选，不越界补证；
- 若预算内不足两个满足硬筛选条件的候选，输出 `research_insufficient`，回产品决策门；
- 若有一至两个候选，只能请求下一次独立产品决定选择一个进入安全 intake，不能自动下载或执行；
- 若替代候选研究失败，暂停本地 ASR 运行时采用路线，保留产品原型与需求知识，不转向云端音频上传。

## 授权需求

本次委派已经要求产品经理在两条路线中选择，并明确允许在选择替代候选时定义官方材料研究。上述只读公开材料研究属于本决定直接批准的正常产品调研，不需要再次创造同义的 Product Lead 授权门。

但是，任何超出公开官方页面的动作——包括读取候选源码、下载源码／模型／二进制、建立安全 intake、扫描、构建、运行、真机测试或集成——都不在本决定内，必须在研究完成后由新的正式产品决定界定；其中需要外部制品取得或执行的任务，必须取得适用的精确新授权。

## 保持不变

- 产品定义、P0/P1、三步录入、三步找回、微信式按住说话和单段 90 秒不变。
- 原始录音不落盘、不上传、不进日志；只允许把转写文字发送云端 AI 做标题和分类。
- CP1 父亲人工验证与 Conformer 均为 `Deferred, not removed`；必须在任何 CP3 准入前恢复适用验证。
- 小米 15 仍是 ASR、权限、提醒和父亲 Alpha 的目标证据设备；当前没有新增真机证据。
- 真实中文语音、目标设备性能、30／90 秒耗时、90 秒 20 次稳定性、飞行模式、权限、提醒、动态音频隐私和个性词表准确率门槛全部保留。
- 不扩大到账号、同步、支付、Flutter、KMP、云端语音识别或公开发布。

允许的准确表述是：

> 最后一个热词链任务在 `Create(config)` 声明处按预设规则停止，当前 sherpa-onnx 热词逐文件补证链永久终止。这是证据预算停止，不是对整个文件或 buffer-only 能力的技术否定。产品只批准开展替代离线中文 ASR 的官方材料研究；个性词表实现延后但不删除，核心 ASR 与 CP2 仍未解锁。

禁止声称“整个 `impl.h` 没有定义”“已证明 buffer-only 不可行”“scanner 0 findings 表示安全”“延期个性词表即可采用 sherpa-onnx”“替代候选已批准”或“CP2／CP3 已通过”。

## 产品仓库后续同步清单

本任务不修改 `/Users/orderly_ray/Projects/think`。Leader 后续只需同步文档状态：

1. `impl.h` 最后单文件任务已接受：1 GET／2,286 bytes／3 行／129 visible bytes，在目标声明处停止；
2. 热词逐文件证据链永久终止，不允许第三来源；
3. 该停止不证明整个文件没有定义或 buffer-only 不可行；
4. sherpa-onnx 既有制品和路线仍不得采用，CP2 未通过；
5. 下一项唯一工作是非 sherpa-onnx 候选的官方材料研究，不下载、不执行、不实现；
6. 个性词表实现 `Deferred, not removed`，其准确率门槛及全部隐私、真机、性能、稳定性门槛不变。
