# 决策记录：CP2 本地 ASR 运行时安全路线

Owner: Product Lead
Last updated: 2026-09-05
Source: `../../raw/SRC-20260905-think-cp2-runtime-01.md`、`../../raw/SRC-20260905-think-cp2-runtime-02.md`、`../../raw/SRC-20260905-think-cp2-runtime-03.md`、`../../raw/SRC-20260905-think-cp2-runtime-04.md`、`../../raw/SRC-20260905-think-cp2-runtime-05.md`、`../../raw/SRC-20260905-think-cp2-runtime-06.md`、`../../raw/SRC-20260905-think-cp2-runtime-07.md`、`../../raw/SRC-20260905-think-cp2-runtime-08.md`
Confidence: High（现有制品裁决与边界已经独立验收）；Medium（最小源码构建能否最终通过仍待验证）
Related decisions: `prd-v0.1-2026-09-04.md`；`development-start-decision-2026-09-05.md`；`cp1-deferred-cp2-entry-decision-2026-09-05.md`
Next review date: 2026-09-12

## 状态

**APPROVED — 只批准下一条安全受控路线；不批准任何现有第三方制品。**

CP2 仍为 `not passed`，CP3 与父亲 Alpha 仍为 `Not approved`。

## 正式决定

1. 选择“**可复现最小源码快照 → arm64-v8a、CPU-only、ASR-only 构建**”作为 sherpa-onnx 的唯一下一条安全技术路线。
2. 本决定只批准路线和门禁顺序，**不构成执行授权**。在获取第三方源码、修复／筛选／重打包、构建或产生新制品前，必须由 Product Lead 针对该路线另行明确授权。
3. Product Lead 授权后，下一项单一任务只能是 `CP2-ASR-MINIMAL-SOURCE-SNAPSHOT-GATE-001`：在全新隔离目录中，从不可变上游提交按 allowlist（允许清单）建立一个无符号链接的最小源码快照，输出文件清单、逐文件哈希、许可证材料、依赖闭包和完整静态门禁裁决。该任务不得构建、安装、加载模型、修改产品源码或集成。
4. 只有最小源码快照取得独立 `approved_with_controls` 后，Leader 才可再提交后续单独任务合同，审查固定工具链与依赖，并构建 arm64-v8a、CPU-only、ASR-only 运行时。构建产物、每项依赖和任何模型都必须按新哈希分别重走完整门禁，裁决不得继承。
5. Conformer 候选的静态门禁标记为 `Deferred, not removed`。在运行时最小路线尚未通过前暂不继续；运行时获得 `approved_with_controls` 后，为满足 CP2 至少两个中文模型的比较要求，再单独决定恢复 Conformer 或选择另一个离线候选。
6. 不切换到云端语音识别，也不在本决定中改用其他离线 ASR 框架。若最小路线失败或 Product Lead 不授权，回到产品决策门重新比较“等待上游／合格 reviewer”和“另一离线 ASR 候选”，不得由开发任务自行切换。

## 当前三项制品裁决

| 制品 | 固定身份 | 当前裁决 | 当前后果 |
| --- | --- | --- | --- |
| sherpa-onnx v1.13.7 固定源码归档 | commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`；SHA-256 `acf539e930283442c4237b7b23a06ebe3bff10cbc00694a4f09a3580e3c10e9e` | `block` | 不得解压、运行、构建、安装、导入或采用；最小路线不得以此归档为输入 |
| 官方 `sherpa-onnx-1.13.7.aar` | asset `539211387`；SHA-256 `c4ef49e309f24fcee5c106b8a279481aaecaabb078cd37b2cd6e9a62cc8a73c8` | `manual_review` | 不得安装、加载、构建、测试或集成 |
| Zipformer 14M INT8 四文件集 | commit `204ad334e2e683fd295359930cc16fc0432a23ac`；encoder `1c556ea57cec304e55ec4b72e52c1cc098bb01476ed7d90f3de939fe126487b1`；decoder `22f123bb8cba9b38974b3df18a3f45e7081f4985ebb2e075d9f21f618c468bbf`；joiner `a7cf9d82757bdcf786059454495a9ca95e4bd7347f72473fc08d794475c36169`；tokens `8b294db9045d6e5f94647f4c1eec1af4da143a75053c399611444b378ff966ac` | `manual_review` | 不得加载、推理、测试、打包或集成 |

三项裁决彼此独立：源码归档的 `block` 不自动继承给 AAR 或模型；两个 `manual_review` 也不削弱源码归档的 `block`。这些结论不表示整个 sherpa-onnx 项目已经确认恶意，不表示发生过音频或凭证外传，也不适用于未来不同哈希的新制品。

## 备选方案

| 选项 | 优点 | 缺点 | 决定 |
| --- | --- | --- | --- |
| 暂停等待上游或合格 reviewer | 外部信任边界最简单，不引入重打包判断 | 时间不可控；不能主动关闭 AAR provenance 和过宽能力面 | 保留为最小路线失败后的回退，不作为当前首选 |
| 可复现最小源码快照与 arm64 CPU-only ASR-only 构建 | 能缩小能力、ABI、依赖和审查面，并建立源码到二进制的可追溯链 | 需要 Product Lead 单独授权；仍需多阶段完整门禁，不能保证最终通过 | **选定** |
| 立即改用另一离线 ASR | 可能绕过 sherpa-onnx 当前制品缺口 | 会重启兼容、中文准确率、许可证、供应链和真机验证，当前没有证据表明总体风险更低 | 当前不选；失败后重新产品决策 |

## 选定路线的强制安全边界

最小源码快照必须：

- 来自不可变提交的逐文件身份，不能解压、复制或修补当前被 `block` 的归档；
- 只包含在线中文 ASR 所需源码和构建元数据，采用显式 allowlist；不得包含符号链接、release／CI 发布脚本、示例、测试、Go、Node、Python、Flutter 或 Web 代码；
- 固定全部直接和传递依赖的版本、来源、大小和 SHA-256，补齐 LICENSE、NOTICE、SBOM 与来源到构建产物的对应计划；
- 在任何执行前先通过归档边界、自动执行面、网络、文件写入、日志、native/JNI、依赖和许可证人工复核；新快照必须取得独立 `approved_with_controls`。

后续最小构建若获单独任务授权，必须：

- 仅产出 `arm64-v8a`，仅 CPU，本地流式 ASR；关闭 TTS、speaker embedding／diarization、denoise、language ID、keyword spotting、QNN、RKNN、ADSP、websocket、C/CXX 公共库、示例、命令行程序和不需要的 provider；
- 不暴露或调用 WaveWriter、文件式音频输入、音频保存、运行时下载、上传、遥测或用户可控动态库路径；原始 PCM 只进入可清零内存缓冲区；
- 使用固定、可信且重新门禁的 JDK、NDK、Gradle/CMake 与 ONNX Runtime 来源；构建过程可复现，输出逐文件哈希、SBOM、许可证和 build provenance；
- 让新运行时产物再接受独立静态／native 门禁；只有 `approved_with_controls` 才能进入单独授权的模型门禁和隔离集成任务。

现有 Zipformer 四文件集不会因运行时路线通过而自动获准。其 FP32 `PAIT-ONNX-200` 提示、量化来源、官方模型组合和许可证问题必须由合格模型安全 reviewer 或新的可复现来源证据关闭；否则应选择另一份具有独立来源与完整门禁的中文离线模型。

## 下一项单一任务合同边界

任务名建议：`CP2-ASR-MINIMAL-SOURCE-SNAPSHOT-GATE-001`。

进入前置：Product Lead 必须明确授权“从不可变上游提交获取 allowlist 文件并创建新的最小源码快照，用于安全审查”。没有这句或等价的明确授权，Leader 不得下发。

允许范围：

- 在全新隔离目录中只获取经合同列明的不可变、逐文件来源；
- 生成确定性的 allowlist 快照、manifest、逐文件哈希、依赖闭包、许可证清单和静态扫描／人工复核报告；
- 给该新快照独立裁决 `block`、`manual_review`、`sandbox_only` 或 `approved_with_controls`。

禁止范围：

- 使用或解压 SHA-256 `acf539e...10e9e` 的现有被 block 归档；
- 运行第三方脚本、Gradle、CMake、wrapper、编译器或测试；
- 下载 AAR、模型或未列入合同的依赖；
- 构建、安装、加载、推理、修改 `/Users/orderly_ray/Projects/think` 产品源码或提交新运行时；
- 把“无告警”“low_indicators”“官方发布者”或 GitHub/Hugging Face 平台标签写成批准。

交付要求：来源 URL／提交、逐文件 allowlist 与 SHA-256、零链接证明、自动执行面与能力面审查、依赖/许可证闭包、scanner 原始报告、人工裁决、盲区、非继承声明和工作区状态。任务结束后停止，不自动进入构建。

## 暂停与回退条件

出现任一项即停止当前路线并回到 Product Lead 决策：

- Product Lead 未明确授权第三方源码筛选／重打包，或撤回授权；
- 只能通过解压或修补现有被 block 归档才能建立快照；
- 新快照含越界链接、未固定来源、不可解释生成文件、自动执行入口或无法裁剪的联网／写盘／TTS 等非 ASR 能力；
- 任一依赖、工具链、运行时产物或模型不能取得独立 `approved_with_controls`；
- 无法建立源码、构建输入和输出二进制之间可复核的 provenance，或无法闭合许可证／NOTICE；
- 为继续推进必须放宽原始音频不落盘／不上传／不进日志、飞行模式、小米 15 真机、30 段真实语音、27/30、专名 90%、30 秒 P95、90 秒连续录音 20 次、内存／耗电／发热等任一 CP2 门槛；
- 路线要求云端音频、CP3 数据层、父亲 Alpha 或其他未批准范围。

## Conformer 决定

Conformer 静态门禁暂缓，状态为 `Deferred, not removed`，不是取消第二候选要求。理由是：当前关键阻塞是没有可获准的运行时；继续获取和扫描另一模型不会解除这一阻塞，反而扩大第三方制品和许可证审查面。

恢复最迟时点：运行时最小快照及其构建产物都取得独立 `approved_with_controls` 后、任何模型加载或 CP2 两候选性能比较之前。恢复时仍须由 Leader 提交单独合同，并按固定提交、逐文件哈希、模型安全、许可证和非继承要求完整门禁。

## 证据文件与内容哈希

| 证据 | SHA-256 |
| --- | --- |
| `current-task.json` | `26035a91105ef40db662ea233d31b81dddc9f013048b27414c98bf7850887747` |
| CP2 intake | `e121050e5fa79dea788c49f7cd055940f061abf895e5f3b0aa50dc1e82df9812` |
| 源码人工复核 | `4a3da4fa218904182b5a142eb3f4d7f6919a14ae300c84e7e1e3ff28672348ea` |
| AAR 人工复核 | `2717a68c429b27128b5ea132c3ca6ee6521b9af4a1c0dd682217f46d40704c3d` |
| Zipformer 人工复核 | `1180123535584be54eccf50eedd5eecc4f3938af29a7842a051c3a855493e990` |
| 源码门禁验收 | `8c76fc1ca8ef96e40d2ffc90b28cc348ea28bd016c3ff5bf05dbdda711a20d09` |
| AAR 门禁验收 | `963cc87c58f2ef1ff5286e747ad2c2170c5409fbdbc49a59339b483b8bec7e10` |
| Zipformer 门禁验收 | `b4da4035fa34ee0a6d2a1062f6c0cfbf101e45bd412a639e7058300b397f8208` |

## 未验证项

- 新最小源码快照是否能够建立并通过安全门禁；
- arm64-v8a、CPU-only、ASR-only 构建是否可复现及其 native 行为；
- ONNX Runtime 与全部构建依赖的来源、漏洞和许可证闭包；
- 任何中文模型的模型安全、来源、许可证、运行时兼容性和准确率；
- 小米 15 上的模型加载、30／90 秒延迟、内存、耗电、发热和 90 秒连续录音 20 次稳定性；
- 30 段真实语音 27/30 可理解、专名词典后 90%、飞行模式完整可用；
- 原始 PCM 不落盘、不上传、不进日志的集成审查、文件系统差分、网络观察与异常路径证据；
- CP1 父亲人工可用性门槛，以及 CP3、提醒、日历、云端文字分类和父亲 Alpha。

## 禁止声明

在后续对应门禁正式通过前，不得声称：

- sherpa-onnx、当前 AAR、当前 Zipformer 或未来最小运行时已经安全／已批准；
- 源码归档 block 证明整个 sherpa-onnx 项目恶意或已发生数据外传；
- CP2 已通过、本地中文识别已达标、90 秒已稳定或小米 15 已验证；
- 原始音频不落盘／不上传已被动态证明；
- Conformer 已取消、第二候选比较不再需要；
- CP3、父亲 Alpha、公开发布或更高 Validation Level 已获批准。

允许的准确表述是：

> 产品经理只批准在 Product Lead 另行明确授权后，按全新安全门禁探索可复现的最小源码快照与 arm64 CPU-only ASR-only 构建路线。现有源码归档、AAR 和 Zipformer 文件集均未获采用；CP2 未通过，CP3 未批准。

## Research Quality / Validation Level 影响

- Research Quality：保持 86；本次提高供应链和产品决策的可追溯性，不增加市场或用户证据。
- Validation Level：保持 V2；没有新增父亲真实产品使用。
- Allowed next investment：仅在 Product Lead 另行明确授权后，执行一个隔离、可回退的最小源码快照静态门禁任务。
- CP1 父亲人工验证仍为 `Deferred, not removed`，最迟在任何 CP3 准入决定前恢复。

## 复查触发条件

- Product Lead 批准或拒绝最小源码快照路线的执行授权；
- 最小源码快照门禁给出裁决；
- 请求开始构建、加载模型、恢复 Conformer、切换其他离线 ASR 或进入 CP3；
- 上游发布可验证修复、provenance、SBOM、许可证材料或合格 reviewer 新结论；
- 任何人试图把路线批准写成制品批准或 CP2 通过。
