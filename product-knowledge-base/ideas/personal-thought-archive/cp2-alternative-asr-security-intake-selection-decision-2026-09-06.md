# 决策记录：CP2 替代 ASR 安全 intake 候选选择

Owner: Product Lead
Last updated: 2026-09-06
Source: `CP2-ALTERNATIVE-ASR-SECURITY-INTAKE-SELECTION-DECISION-001` 合同；`cp2-alternative-offline-chinese-asr-evidence-cards-2026-09-06.md`；`cp2-alternative-offline-chinese-asr-comparison-matrix-2026-09-06.md`；`cp2-alternative-offline-chinese-asr-research-memo-2026-09-06.md`；Leader R1 acceptance 与 verification
Confidence: Medium-High（候选选择依据已通过 R1 验收；精确版本、制品、安全、接口和真机均未验证）
Related decisions: `cp2-hotwords-chain-termination-route-decision-2026-09-06.md`；`cp2-runtime-security-route-decision-2026-09-05.md`；`cp2-alternative-offline-chinese-asr-research-memo-2026-09-06.md`；`prd-v0.1-2026-09-04.md`
Next review date: 2026-09-13

Research Quality: 92 · pass（继承已验收 R1 的研究质量，不新增外部证据）
Validation Level: V2
Next evidence: 单独执行 `CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001`，只确认一个 Android runtime 与一个中文小模型的官方身份、版本／发行坐标、来源和许可证，不取得任何制品
Allowed next investment: 一项最多 6 个官方公开页面／元数据端点的只读身份准备任务；不得下载源码、模型、二进制、AAR、APK、样本或归档，不扫描、不构建、不加载、不运行、不做真机测试
Pause/Kill condition: 6 个官方入口内无法同时固定 runtime 与中文模型的可复现身份；官方来源冲突；许可证或维护者无法分别识别；识别过程要求先下载制品、读取源码正文、登录或扩大候选

## RESULT

**APPROVED — 只选择 Vosk 进入下一项有界的官方身份安全 intake 准备。**

这里的 `APPROVED` 只批准候选选择和下述阶段 A 合同，不批准 Vosk 的源码、Android runtime、模型、二进制、实现、构建、加载、运行、集成、CP2、CP3 或父亲 Alpha。Vosk 仍是“待确认精确身份的候选”，不是获批技术方案。

ONNX Runtime Mobile + SenseVoiceSmall-onnx 不进入当前 intake。它继续保留为已验收研究中的第二候选，但本决定不并行推进、不下载、不补证，也不把它判定为不可用或不安全。

本任务没有联网、没有读取候选源码／源码树／corpus、没有取得第三方文件，也没有修改 `/Users/orderly_ray/Projects/think`。

2026-09-06 接管收尾：沿用同一选择任务，不重做研究或创建第二任务。当前回报 Leader 为 `01a07655-fdfd-7683-aa57-a4895188d2ff`；本决定的 `APPROVED` 是产品选择结果，尚待该 Leader 验收与单独下发阶段 A，不能解释为阶段 A 已执行。依据为 `/Users/orderly_ray/Leader/orchestration/current-task.json` 与 `handoffs/2026-09-06-leader-takeover.md`。

## 选择依据

### 为什么选择 Vosk

已验收 R1 的官方材料直接支持以下研究事实：

- 明确支持中文、Android、离线移动端与连续／流式识别；
- 官方材料直接描述可重配词表，最贴近 P0 个性词典和“专名加入词典后正确率至少 90%”的后续验证需求；
- 官方模型目录存在约 42 MB 的中文小模型条目，目标设备安装、内存和 30／90 秒性能验证的初始负担相对较小；
- runtime 与该中文模型条目均有 Apache-2.0 标识，维护者与官方入口可识别；
- 与“首页按住说话、松手结束、单段 90 秒、本地转写、原始音频不落盘不上传”的产品路径更直接，研究阶段接入复杂度为低至中。

以上只说明它是两个 shortlist 候选中更适合先做安全 intake 的对象。官方声称“离线”不能证明 Android 实现不落盘、不记录日志、不产生缓存，也不能替代源码、制品和小米 15 证据。

### 为什么当前不选择 ONNX Runtime Mobile + SenseVoiceSmall-onnx

该组合通过 R1 硬筛选依赖有限工程推断：SenseVoiceSmall-onnx 的同 URL 官方摘要支持中文 ASR、ONNX 与本地／离线入口；ONNX Runtime Mobile 官方页支持 Android 设备侧 ONNX 与默认 CPU。它没有被证明为现成的 Android ASR 方案。

若推进该组合，intake 必须同时关闭 runtime、模型、音频预处理、特征提取、tokenizer、decoder、标点、长音频切分、算子兼容与 JNI 等多个组件。模型页正文此前又未成功抽取，约 241.59 MB 也高于 Vosk 中文小模型的公开量级。当前并行投入会扩大供应链与验证面，不符合“最多选择一个、先用最小门禁消除最大不确定性”的要求。

该取舍是优先级选择，不是对 ONNX Runtime、SenseVoice 或组合安全性的负面裁决。

## 不继承与不恢复

- sherpa-onnx 热词逐文件证据链仍永久终止；现有 `block`／`manual_review` 只适用于各自精确制品，不继承给 Vosk，也不因本决定恢复旧 run、v9、源码链或 clearance。
- Vosk 的研究合格不继承为安全合格；runtime 与模型必须分别建立身份、许可证、来源和后续门禁。
- ONNX Runtime + SenseVoice 的研究资格不转移给 Vosk；本决定也不批准第二候选的任何动作。
- Conformer、CP1 父亲人工验证与个性词典实现仍为 `Deferred, not removed`，适用恢复时点与门槛不变。

## 下一项唯一任务合同

任务名：`CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001`

### 唯一目标

只通过官方公开说明和元数据，分别确认：

1. 一个可供 Android 后续审查的 Vosk runtime 精确身份；
2. 一个官方中文小模型的精确身份；
3. 两者各自的维护者、来源、版本／发行坐标和许可证入口；
4. 是否已具备召开“精确制品获取与安全扫描授权决策”的身份条件。

任务只产生身份证据与下一门状态，不取得对象本身，也不证明 Android API、arm64、CPU-only、内存 PCM、隐私或性能。

### 允许输入与来源

- 本决定及已验收 R1 三份研究产物；
- 已登记的 Vosk 官方入口：Alpha Cephei Vosk 官方站、官方模型目录、`alphacep/vosk-api` 官方仓库首页／README／LICENSE；
- 仅限上述官方入口直接指向的官方 release、tag、Android 发行坐标或模型元数据；
- `alphacep/vosk-api` 官方仓库的公开、只读 repository／release／tag 元数据；
- 若官方入口没有给出某字段，记录 `Unknown`，不得用第三方镜像、博客、论坛、聚合下载站或猜测补齐。

“官方入口直接指向”是本任务的来源边界。发现新域名、镜像或包名时，在读取前先判断是否能由现有官方入口建立一方归属；不能建立则停止，不把名称当身份。

本合同的制品禁令不包括上述明确允许的官方说明、README、LICENSE 与公开元数据正文；阶段 A 可在预算内读取并记录必要身份证据，不得借文档入口读取源码实现、遍历源码树或请求模型／二进制等制品。README／LICENSE 的网页路径含 `blob` 不单独构成源码实现读取；按实际对象及本节允许范围判断。此澄清不增加来源、页面预算或当前任务权限。

### 预算

- 最多读取 6 个官方公开页面或元数据端点；已验收 R1 文档的本地只读不计入该预算；
- runtime 最多 3 个，中文模型最多 3 个；
- 一个 URL／端点一旦用于结论即计数，重定向后的最终官方页面仍按一次访问记录；
- 不搜索或评估第二候选，不新增第三候选。

### 必须产出的证据

`runtime-identity.md` 至少包含：

- 官方项目／维护者；
- 精确 release／tag／版本；
- 官方 Android 发行坐标或官方声明的分发入口；
- 官方源码仓库身份；
- runtime 许可证入口与适用范围；
- 官方是否发布 checksum／签名／SBOM；没有则写 `Unknown`；
- 每项字段的官方 URL、访问日期、Observed／Unknown 标记。

`model-identity.md` 至少包含：

- 精确模型名称与官方条目；
- 版本、发布日期或官方可区分的修订身份；
- 官方下载入口的文件名／对象名（只记录，不请求文件）；
- 官方声明的大小；
- 模型许可证入口、维护者／发布者与来源；
- 官方是否发布 checksum／签名；没有则写 `Unknown`；
- 每项字段的官方 URL、访问日期、Observed／Unknown 标记。

`identity-readiness.md` 必须给出且只能给出以下之一：

- `identity_ready_for_artifact_intake_decision`：runtime 与模型均已由官方来源固定到足以在下一次授权中唯一指认的身份，且许可证与发布者分别可追溯；
- `identity_insufficient`：任一必要身份仍不可唯一指认、来源冲突、许可证不闭合或必须先取得制品／源码才能继续。

### 验收条件

- 只选择 Vosk，页面／端点总数不超过 6；
- runtime 与模型分开记录，不让 Apache-2.0 标识在两者之间自动继承；
- 不猜 release、坐标、版本、SHA、发布者或许可证；
- 页面事实、有限推断和 Unknown 分层；
- 没有任何源码实现正文、模型、二进制、AAR、APK、归档、样本或其他非本合同允许的制品被取得或保存；仅允许上述官方说明、README、LICENSE 与公开元数据的有界读取和必要身份证据记录；
- 没有扫描、构建、加载、运行、推理、性能测试、实机测试或 Think 代码修改；
- 结论不超过“是否具备提出下一次精确制品 intake 授权”的身份准备状态。

### 立即停止条件

出现以下任一情况，停止并返回产品门：

- 达到 6 个官方页面／端点仍不能唯一固定 runtime 或中文模型；
- 官方入口互相冲突，或无法确认页面／仓库／发布者的一方归属；
- 页面要求登录、付费、接受额外条款或先下载文件才能读取必要身份；
- 请求将返回源码实现 blob、模型、二进制、AAR、APK、压缩包、样本或其他制品 bytes；本合同明确允许的 README／LICENSE／说明与元数据正文不在此列；
- 为关闭字段必须读取源码正文、遍历源码树、访问 corpus 或扩大到第二候选；
- 任何人试图把研究结论或身份结论写成安全、兼容、隐私或 CP2 通过。

停止不是候选失败，也不得自动切换到 ONNX Runtime + SenseVoice。后续改选必须回到新的产品决策。

## 三阶段权限边界

| 阶段 | 动作 | 本决定状态 | 后续授权要求 |
| --- | --- | --- | --- |
| A | 公开信息身份准备：读取最多 6 个官方页面／元数据端点，记录 runtime 与模型身份 | **已批准为下一项独立任务；本轮不执行** | 不需要重复 Product Lead 授权，但必须由 Leader 单独下发并受本合同约束 |
| B | 获取并扫描外部源码、模型、Android 包、二进制或其他制品 | **未批准** | 阶段 A 通过后，先做新的产品门决定；Product Lead 必须对每个精确对象给出新的明确授权 |
| C | 构建、加载、运行、推理、接入 App 或在小米 15 上测试 | **未批准** | 只有对应对象完成独立安全审查且产品再次批准后，Product Lead 才能另行授权；不得继承阶段 B 权限 |

普通知识库文档写回属于本任务已授权的可逆工作，不另造重复审批。网络只读身份准备被本决定限定为未来阶段 A；当前任务没有执行该权限。

### 阶段 B 的未来精确授权句

阶段 A 未产出精确身份前，不能形成有效的制品授权。届时 Product Lead 必须逐项填入官方身份，使用不含占位符的完整句子：

> 我授权 `CP2-VOSK-ARTIFACT-SECURITY-INTAKE-001` 仅获取并安全扫描：Vosk Android runtime【精确版本／tag、官方发行坐标、官方 URL、官方已发布 checksum 或“官方未提供”】与中文模型【精确名称／版本或修订、官方文件名、官方 URL、官方已发布 checksum 或“官方未提供”】。仅允许保存到该任务隔离目录，不构建、不加载、不运行、不推理、不接入 Think、不做真机测试；任一身份、重定向、字节数、摘要、许可证或来源不一致立即停止。

带有【】占位符的文本不是授权。阶段 A 只能准备上述句子，不能代 Product Lead 填写或生效。

### 阶段 C 的未来权限原则

即使阶段 B 的精确制品扫描通过，也不得自动构建或加载。阶段 C 必须另立合同，分别限定：获准对象摘要、Android arm64-v8a／CPU-only、禁止网络与文件式音频、只允许有界内存 PCM、日志／缓存／buffer 生命周期、合成音频先行、再到小米 15 的真实语音与 30／90 秒性能／90 秒 20 次稳定性／飞行模式。任何对象或摘要变化都回到阶段 B。

## 仍未验证

- Vosk 的精确 Android runtime release、tag、包坐标、官方制品 URL、SHA-256、签名、SBOM 与依赖闭包；
- 精确中文小模型名称、版本／修订、文件名、下载对象、SHA-256、签名、完整许可证文本、notice 与再分发义务；
- Android arm64-v8a、CPU-only、最低系统、JNI／Kotlin API、模型加载和释放；
- 麦克风 PCM 是否可全程只驻留内存，是否强制文件路径，以及 sample、临时文件、缓存、日志、崩溃报告、遥测与 buffer 释放；
- 中文普通话、父亲口音、数字、英文缩写、人名地名、标点和噪声下的真实准确率；
- 可重配词表在所选中文模型和 Android 路径中的真实机制、代价与“常用专名至少 90%”门槛；
- 小米 15 飞行模式、30 秒 P95、90 秒、90 秒连续 20 次、RAM、耗电、温升与异常恢复；
- 任何安全、隐私、法律、兼容、性能或产品使用结论。

## 保持不变与禁止声明

- 三步录入、三步找回、微信式按住说话、单段 90 秒不变。
- 原始录音不落盘、不上传、不进入日志；只允许把转写文字发送云端 AI 做标题和分类。
- 个性词典需求和专名 90% 门槛不删除；实现仍是 `Deferred, not removed`。
- CP1 父亲人工验证最迟须在任何 CP3 准入决定前恢复；CP2 未通过，CP3 与父亲 Alpha 未批准。
- 不扩大到账号、同步、支付、Flutter、KMP、云端语音识别或公开发布。
- 不得声称“Vosk 已批准采用／已安全／已验证不落盘／已支持小米 15”“官方 Apache-2.0 标识等于法律审查完成”“身份准备允许下载”“阶段 B 允许构建”“候选选择等于 CP2 通过”。

## 失败回退

若阶段 A 返回 `identity_insufficient`，暂停 Vosk intake 并回产品决策门。不得自动扩大页面预算、使用第三方镜像、下载文件辨认身份，或自动切换到 ONNX Runtime + SenseVoice。新的证据研究、候选改选或 P0／门槛修订都必须另立正式决定。
