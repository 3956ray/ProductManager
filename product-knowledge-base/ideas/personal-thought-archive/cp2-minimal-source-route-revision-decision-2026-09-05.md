# 决策记录：CP2 最小源码发现与冻结路线修订

Owner: Product Lead
Last updated: 2026-09-05
Source: `../../raw/SRC-20260905-think-cp2-minimal-route-01.md`、`../../raw/SRC-20260905-think-cp2-minimal-route-02.md`、`../../raw/SRC-20260905-think-cp2-minimal-route-03.md`、`../../raw/SRC-20260905-think-cp2-minimal-route-04.md`、`../../raw/SRC-20260905-think-cp2-minimal-route-05.md`、`../../raw/SRC-20260905-think-cp2-minimal-route-06.md`、`../../raw/SRC-20260905-think-cp2-minimal-route-07.md`、`../../raw/SRC-20260905-think-cp2-minimal-route-08.md`
Confidence: High（首次任务停止、部分快照状态和五个闭包缺口已独立验收）；Medium（新的静态闭包发现能否收敛、TTS 耦合能否拆除仍待验证）
Related decisions: `prd-v0.1-2026-09-04.md`；`cp1-deferred-cp2-entry-decision-2026-09-05.md`；`cp2-runtime-security-route-decision-2026-09-05.md`
Next review date: 2026-09-12

## RESULT

**REVISE**

保留“可复现最小源码快照 → arm64-v8a、CPU-only、ASR-only 运行时”的方向，但撤销“下一任务直接冻结最终 allowlist 并取得快照”的流程。该流程已被证据证明存在循环：没有正文就不能知道完整 include 闭包；正文取得后又不能修改已冻结的最终清单。

本决定只修订前一份决定的下一任务协议，不改变既有制品裁决、P0/P1、三步录入／找回、原始录音不落盘不上传、CP1 延后门槛、CP2 真实性能与隐私门槛、Conformer 延后状态或 CP3 禁止状态。

## 已验收事实

1. `CP2-ASR-MINIMAL-SOURCE-SNAPSHOT-GATE-001` 正确执行停止条件，TASK RESULT=`BLOCKED`；开发者没有增补或重冻清单，没有越权。
2. 冻结 allowlist 固定 commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`、tree `fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`，包含 151 个唯一 blob、887,313 声明字节；正文获取前已冻结，mode `120000` 未进入。
3. 首批 50 个文件共 258,363 字节，逐文件大小、Git blob SHA-1 语义和 SHA-256 均验证成功；0 符号链接、0 硬链接异常、0 特殊文件。
4. 50 个正文暴露 5 个清单外仓库内头文件：`cat.h`、`math.h`、`offline-tts-frontend.h`、`phrase-matcher.h`、`unbind.h`。其中 `offline-tts-frontend.h` 触碰明确排除的 TTS 能力。
5. 其余 101 个文件未取得；JNI/Kotlin、完整依赖与许可证、真实 arm64 CPU-only ASR-only 编译闭包均未验证。
6. scanner 原始 verdict=`sandbox_only`、40/100、2 个不可达 high、0 block signal；人工复核确认两项是帮助／诊断字符串。它们不构成已执行行为，但也不能解除清单闭包失败。
7. 当前部分快照最终 ARTIFACT VERDICT=`manual_review`，不得构建、配置、安装、加载、测试、导入或集成。接受的是有证据地停止，不是接受快照。

## 正式决定：两阶段、两制品、两次授权

### 阶段 A：静态闭包发现材料

下一项技术任务只能产生“静态闭包发现材料”，不能产生最终源码快照或构建输入。发现材料的目的，是在不执行第三方内容的条件下识别仓库内 include、上游 CMake source 列表、Android JNI/Kotlin 接口以及外部依赖声明。

任何新正文获取前，任务必须先冻结一份 `discovery-policy.json`，至少包含：

- 固定 repository、commit `917bed95...a60e`、tree `fd2c4e97...bdc0` 与 tree metadata hash；
- 精确列出的 seed 文件，不允许用目录 glob 直接获取正文；seed 只围绕 Android 在线 transducer ASR、Zipformer／Conformer transducer 的运行时接口、JNI/Kotlin 在线识别接口和静态构建元数据；
- 允许根仅为顶层 `LICENSE`／`CMakeLists.txt`、`cmake/`、`sherpa-onnx/csrc/`、`sherpa-onnx/jni/`、`sherpa-onnx/kotlin-api/`；允许类型仅为普通 Git blob，禁止 mode `120000`；
- 确定性闭包规则：可信只读解析器只跟随固定 tree 中、由已取得正文直接引用的仓库内 include；每条新边先写入 append-only ledger，再按 blob SHA 获取；不允许人工临时加文件；
- 上限为 256 个文件、2,097,152 正文字节（2 MiB）；达到任一上限即停止并报告，不得提高上限；这只是产品施加的发现面上限，不是对真实闭包大小的估计；
- 明确排除 TTS、VAD、speaker、punctuation、denoise、audio tagging、WebSocket、PortAudio、QNN/RKNN/ADSP、examples/tests、CI/release、Go/Node/Python/Flutter/Web/WASM、模型、音频、归档、安装器与预编译二进制；
- 唯一 TTS 例外是 `sherpa-onnx/csrc/offline-tts-frontend.h`，只允许取得该单一头文件作接口级静态耦合分析，不允许跟随它取得任何 TTS 实现或更多 TTS/eSpeak/Piper 文件。

发现任务可以对新取得的正文运行可信的只读文本／结构解析器和 scanner，但不得执行任何第三方 CMake、脚本、源码、测试、编译器入口或二进制。正文中出现的 `FetchContent`、下载函数和 source 列表只能记录为静态证据，不能触发网络获取或配置。

发现材料必须得到一个**仅限静态阅读范围**的独立四态裁决。即使结果为 `approved_with_controls`，也只表示该材料可用于形成候选闭包，不得作为构建输入；其裁决不继承给最终快照、依赖、工具链、运行时或模型。

### 阶段 B：最终闭合源码快照

阶段 B 本次不批准，也不属于下一任务。只有阶段 A 完成、Leader 验收且 Product Lead 再次单独授权后，才能建立最终快照：

1. 根据已审阅的静态闭包图，在任何重新取得正文前冻结最终逐文件 allowlist；
2. 在新的隔离目录中从同一不可变提交重新取得所有精确 blob，不复制阶段 A corpus，也不使用既有被 `block` 的源码归档或当前 `manual_review` 部分快照；
3. 逐文件验证来源、大小、Git blob SHA 和 SHA-256，并证明实际集合与最终 allowlist 完全相等；
4. 对相同正文重新计算 include 闭包，要求零未解析、零清单外、零被排除边；任何差异都必须停止，不能在任务内改表；
5. 最终快照取得新的独立四态裁决；只有 `approved_with_controls` 才可进入更晚、另行授权的依赖／工具链／构建门禁。

两个阶段的材料、清单、manifest、哈希和裁决均不得互相继承。阶段 A 解决“看见闭包”，阶段 B 才验证“冻结集合与闭包完全一致”。

## TTS 接口耦合处置

允许在阶段 A 读取精确的 `offline-tts-frontend.h`，仅为了回答三个静态问题：

1. `character-lexicon.h` 与 `lexicon.h` 实际使用了哪些类型／声明；
2. Android 在线 transducer ASR 的目标调用链是否真的需要 `character-lexicon`、`lexicon` 和 `homophone-replacer`；
3. 能否通过不依赖 TTS 的既有 ASR API，或一份后续需单独审查与授权的 ASR-only 接口拆分／适配设计，保留个性词典目标而排除 TTS。

最终快照不得包含原始 `offline-tts-frontend.h`、任何 TTS 实现、eSpeak/Piper、音频合成或临时文件路径。优先选择不依赖该头文件的在线 ASR API；若 P0 个性词典只能通过该耦合实现，则阶段 A 只能输出源级拆分设计和拟议变更，不得修改源码。若无法静态证明最终运行时可以完全排除 TTS，任务停止并回到 Product Lead 决定是否改用其他离线 ASR。

## 上游构建、JNI/Kotlin 与外部依赖处置

- **宽泛 sources**：上游顶层和 `csrc/CMakeLists.txt` 只作为发现证据，不得成为最终可执行构建定义。阶段 A 必须产出一个显式、逐文件的 ASR-only 候选 source graph，并标出所有被排除 source 和理由。
- **CMake 自动下载**：不得运行 `FetchContent` 或 ONNX Runtime 下载路径。未来构建描述必须由项目持有、显式列源、默认断网、没有下载函数，并只接受已独立批准的本地依赖输入；该描述的创建与审查不在下一任务内。
- **JNI/Kotlin**：阶段 A 必须静态取得并审查目标在线识别入口及其仓库内闭包，列出 public/native 方法、`System.loadLibrary`、日志、文件路径、provider/QNN/ADSP 和非 ASR 类型耦合。任何最终 API 都必须收敛到录音内存流、在线识别结果与必要版本信息；当前没有任何 JNI/Kotlin 结论获批。
- **外部依赖**：阶段 A 只登记名称、固定版本／commit、直接发布者、声明 hash、许可证和 source-to-binary 缺口，不得取得依赖正文或制品。每项外部依赖、ONNX Runtime、工具链和许可证随后都需要独立任务与独立裁决。

## 现有授权判断

前一份产品决定要求 Product Lead 对 `CP2-ASR-MINIMAL-SOURCE-SNAPSHOT-GATE-001` 单独授权。该授权的对象、目的和停止边界均绑定已结束任务；任务以 `BLOCKED` 正确终止后，授权已经耗尽。

它不授权新的正文获取、发现 corpus、第二份快照、重冻、源码裁剪、依赖、构建或集成。下一任务必须取得新的明确授权。

### 精确最小授权句

> 我批准 `CP2-ASR-STATIC-CLOSURE-DISCOVERY-GATE-002`：仅允许针对 sherpa-onnx commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`、tree `fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`，按任务合同在正文获取前冻结的 seed、允许根／类型、确定性 include 闭包规则及 256 文件／2,097,152 字节上限，从 GitHub Git Data blob API 获取逐文件正文，用于静态闭包发现；`offline-tts-frontend.h` 只可作接口级静态分析。此授权不允许使用现有 block 归档或 manual_review 快照，不允许执行、构建、配置 CMake、获取外部依赖或模型、修改产品源码、形成构建输入、集成、宣称 CP2 通过或进入 CP3。

## 下一任务完整边界

任务名：`CP2-ASR-STATIC-CLOSURE-DISCOVERY-GATE-002`。

唯一目标：产出一个有界、可追溯、只供静态分析的仓库内源码闭包证据包，并判断是否可以形成不含 TTS 和其他排除能力的最终 allowlist 候选。

允许：

- 在全新隔离目录中，按预先冻结的 `discovery-policy.json` 获取不可变 Git blob；
- 使用可信只读解析器分析仓库内 include、CMake source/target/option 文本、JNI/Kotlin 接口和依赖声明；
- 对发现 corpus 运行 scanner、文件类型／链接检查和人工静态复核；
- 输出候选最终 allowlist、明确排除清单和源级拆分建议，但不创建最终快照、不修改任何源码。

明确不做：

- 不使用当前被 `block` 的源码归档、官方 AAR、Zipformer、当前 `manual_review` 部分快照或任何既有第三方二进制；
- 不执行／配置 CMake、Gradle、脚本、源码、测试、编译器、JNI 或 Kotlin，不构建、不安装、不加载、不推理；
- 不取得外部依赖、工具链、模型、音频、预编译库、归档或真实父亲数据；
- 不修改 `/Users/orderly_ray/Projects/think` 产品源码，不集成，不进行真机测试，不进入 CP3；
- 不把候选 allowlist、发现 corpus 或 scanner 低告警写成最终快照批准。

必须交付：

1. 正文前冻结且有 SHA-256 的 `discovery-policy.json`，以及“冻结前无新正文”的证据；
2. append-only acquisition/closure ledger，逐边说明引用方、include、解析目标、获取状态与排除理由；
3. corpus manifest：逐文件 immutable URL、Git blob SHA、大小、内容 SHA-256、文件类型和 lstat；
4. 固定点闭包结果、所有 unresolved/excluded edges、TTS 接口耦合图与非 TTS 替代／拆分结论；
5. 上游 CMake 宽泛能力与自动下载地图、显式 ASR-only 候选 source graph；
6. JNI/Kotlin public/native/API 能力表和外部依赖／许可证缺口清单；
7. scanner 原始报告、人工裁决、盲区、非继承声明、工作区状态和建议候选最终 allowlist；
8. 明确写明没有最终快照、没有构建输入、没有依赖／模型批准、CP2 未通过。

通过条件：预冻结策略未修改；全部获取严格由 frozen seed 或确定性闭包边产生；未超 256 文件／2,097,152 字节；所有哈希一致；零链接／特殊文件；闭包达到固定点；除精确 TTS 头文件接口例外外没有取得排除能力；能给出一个不含 TTS 的候选最终 allowlist及可审查的 API/source 边界。任务完成后停止，等待 Leader 验收与新的产品决定。

停止条件：

- 任一正文、路径、模式或大小不匹配固定 tree；发现链接、特殊文件、不可变身份缺口或 scanner `block` 证据；
- 需要人工临时加 seed、改变规则、扩大允许根／类型、超过 256 文件或 2,097,152 字节；
- include 使用宏、生成文件或构建配置，无法在不执行第三方内容时确定解析目标；
- `offline-tts-frontend.h` 继续要求其他 TTS/eSpeak/Piper 正文，或在线 ASR 最终边界无法排除原 TTS 头文件／实现；
- 上游宽泛 CMake 是唯一可行 source 定义，必须运行 CMake/FetchContent 才能判断闭包；
- JNI/Kotlin 静态闭包要求 QNN/RKNN/ADSP、文件式音频、非 ASR native 能力或其他排除内容，且无法只输出隔离设计；
- 判断需要取得任何外部依赖、模型、工具链、音频或执行／构建第三方内容；
- 需要修改产品源码、降低既有安全／隐私门槛或扩大到 CP3。

## 备选方案与理由

| 选项 | 优点 | 主要代价／风险 | 决定 |
| --- | --- | --- | --- |
| 原样重跑并补入五个文件 | 最快 | 仍会遇到下一层未知 include；正文后改最终清单破坏冻结意义 | 拒绝 |
| 暂停等待上游提供最小构建 | 不再自行解析上游边界 | 时间不可控，且上游是否会提供无法确认 | 保留为失败后的回退 |
| 两阶段静态发现 → 最终重取冻结 | 用预冻结算法代替预知完整文件列表；发现材料和构建输入隔离 | 多一次获取与审查；仍可能因 TTS/生成依赖停止 | **选定修订** |
| 立即切换其他离线 ASR | 可避开当前源码结构 | 重新开始供应链、中文准确率、许可证和真机验证；暂无总体风险更低的证据 | 当前不选 |

## 裁决继承规则

- 现有源码归档 `block`、AAR `manual_review`、Zipformer `manual_review`、部分快照 `manual_review` 分别保持，只约束各自精确制品。
- 阶段 A 发现 corpus 的裁决只约束静态阅读，不批准阶段 B、依赖、构建或集成。
- 阶段 B 最终快照必须重新裁决；只有其 `approved_with_controls` 才允许提出下一份依赖／工具链任务合同。
- 依赖、工具链、构建产物、模型、APK、真机与音频隐私证据各自独立，不能从源码或 scanner 结果继承批准。
- Conformer 继续为 `Deferred, not removed`；CP2 至少两个模型的比较要求不删除。

## 证据与内容哈希

| 证据 | SHA-256 |
| --- | --- |
| `current-task.json` | `afd86ba0f3b14cdeac448c33a9500cf5559459c839fde194832662a0a330e96b` |
| `dependency-license-review.md` @ `6952167` | `3840fd2300e7c0ee8a829402a62f8fc5c0b3fedcfcb74ad0a91f1d5789761f43` |
| `frozen-allowlist.json` @ `6952167` | `d6ca88c3bab331ea0034613d7412e74d4cb3c3ec2317f37d1bf35e0b52fc3097` |
| `manual-review.md` @ `6952167` | `57e96839fd593f004f378d28ecb985c9bcfc6858236f1785a67d34c37a2f0062` |
| `scan-report.json` @ `6952167` | `d4c79694c48485270125c764d5717036551f185beae75540f875b98f11f0a4c4` |
| `scan-report.md` @ `6952167` | `80d4be94b8c49d9b26975069c9b0a3a69fdec7c61b006dd7ee9ba7ad47443ae5` |
| `snapshot-manifest.json` @ `6952167` | `e31d674b1f2c355aa74c744a355d6e8333f99f5dc9baae2072b35baa045089f4` |
| Leader 验收报告 | `8bb51bfbb10414189ea3a95f1ce2a055334de26d9c1355617419a32722992691` |

## 未验证项

- 新的 256 文件／2,097,152 字节上限内能否达到静态闭包固定点；
- 101 个未取得文件及可能出现的更多内部 include；
- `offline-tts-frontend.h` 的具体类型耦合，以及不依赖 TTS 的在线 ASR API／源级拆分是否成立；
- 显式 ASR-only source graph、独立无下载构建描述及真实可编译性；
- JNI/Kotlin public/native 方法、动态加载、日志、文件路径和 provider 能力；
- ONNX Runtime、kaldi-native-fbank、kaldi-decoder、OpenFst、SentencePiece、JSON 等全部外部依赖、许可证、NOTICE、漏洞与 provenance；
- 最终源码快照、工具链、arm64-v8a CPU-only 构建产物和任何模型的独立安全裁决；
- 小米 15 的准确率、性能、内存、耗电、发热、90 秒 20 次稳定性、飞行模式和原始音频不落盘／不上传动态证据；
- CP1 父亲人工可用性，以及 CP3、父亲 Alpha、日历、提醒和云端文字分类。

## 禁止声明

不得声称当前部分快照安全、闭合或可构建；不得声称五个遗漏文件就是全部缺口；不得声称 TTS 已排除、JNI/Kotlin 已验证、依赖已批准或新发现协议必然收敛；不得把 scanner 的不可达命中解释为已执行恶意行为。

在对应正式门禁前，也不得声称本地中文 ASR、音频隐私、小米 15、CP2、CP3、父亲 Alpha 或 Conformer 已通过／取消。

允许的准确表述是：

> 首次最小源码任务正确停止，部分快照保持 manual_review。产品路线修订为“有界静态闭包发现”与“最终闭合快照”两个独立阶段；任何新正文获取都需要 Product Lead 对下一单重新明确授权，CP2 仍未通过。

## Research Quality / Validation Level 影响

- Research Quality：保持 86；本次提高供应链边界和失败证据的可追溯性，不增加市场或用户验证。
- Validation Level：保持 V2；没有新增父亲真实产品使用。
- Allowed next investment：仅在 Product Lead 使用本文精确授权句明确批准后，执行一个有界的静态闭包发现任务。
- CP1 人工门槛继续 `Deferred, not removed`，最迟在任何 CP3 准入决定前恢复。

## 复查触发条件

- Product Lead 批准或拒绝新的静态闭包发现授权；
- 下一任务达到固定点、触发停止条件或提交验收；
- 请求创建最终快照、源码拆分、外部依赖门禁、构建、模型、恢复 Conformer 或进入 CP3；
- 上游提供真正独立、无下载、ASR-only 的构建定义或合格 reviewer 新证据；
- 任何人试图把发现材料写成构建输入或把 `REVISE` 写成 CP2 通过。
