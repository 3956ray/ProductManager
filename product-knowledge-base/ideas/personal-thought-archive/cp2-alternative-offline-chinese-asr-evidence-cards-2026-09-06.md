# CP2 替代离线中文 ASR 官方证据卡（R1）

Owner: Product Lead
Last updated: 2026-09-06
Source: `CP2-ALTERNATIVE-OFFLINE-CHINESE-ASR-OFFICIAL-RESEARCH-001` 原始研究；`CP2-ALTERNATIVE-OFFLINE-CHINESE-ASR-OFFICIAL-RESEARCH-001-R1` 最小返工合同（4,480 bytes；SHA-256 `40faaf16b43a65582f241f2cb5a889f0f46f41827d8201c19ebfcab739e3de81`）；原 12 个官方页面
Confidence: Medium-High（官方能力、平台与许可证声明可追溯；未下载、执行、构建或真机验证）
Related decisions: cp2-hotwords-chain-termination-route-decision-2026-09-06.md；prd-v0.1-2026-09-04.md
Next review date: 2026-09-13

Research Quality: 92 · pass
Validation Level: V2
Next evidence: Product Lead 从合格 shortlist 中最多选择一个候选，另立安全 intake 决策；选择前不得取得源码、模型或二进制
Allowed next investment: 仅允许一次独立产品选择决策；本文件本身不授权安全 intake、下载、扫描、构建、运行、真机测试或集成
Pause/Kill condition: shortlist 候选不能在独立 intake 中关闭来源、许可证、Android CPU-only、内存音频、隐私与可复现供应链边界

## 研究合同与边界

本研究支持的唯一决策是：在不接触候选源码正文、源码树、模型、AAR、APK、库或其他制品的前提下，判断是否存在至少两个值得进入未来独立安全 intake 选择决策的非 sherpa-onnx 离线中文 ASR 候选。

本轮只读取官方产品／项目文档、官方仓库 README、LICENSE 和官方平台页面。GitHub 页面只使用 README、LICENSE 与仓库首页公开说明，没有读取源码文件。没有 clone、下载、登录、安装、执行、构建、推理、benchmark、访问 corpus 或修改 `/Users/orderly_ray/Projects/think`。

## R1 修订说明

初稿被 Leader 判定为 `REVISE`：错误地把 OpenAI Whisper 模型权重许可证写成未识别；遗漏 whisper.cpp 同一 README 中的模型磁盘／内存估计；ONNX Runtime Mobile + SenseVoiceSmall-onnx 的硬筛选推导没有逐项展示官方前提。R1 只复核原 12 个 URL，不增加页面、候选或技术权限，并保留初稿拒绝记录：`CP2-ALTERNATIVE-OFFLINE-CHINESE-ASR-OFFICIAL-RESEARCH-001-rejection.json`（1,237 bytes；SHA-256 `3831454e560e6dc58d5a32be6674881be964ebc6d984e5d86054e8a640f7f07a`）。

## 页面预算账本

页面从首次使用起即计入预算；即使页面正文抽取不完整，只要官方搜索摘要用于结论，也计为一个页面。

| Source ID | 候选 | 官方页面 | 类型／维护者 | 访问状态 | 本研究使用的主张 |
| --- | --- | --- | --- | --- | --- |
| SRC-20260906-think-asr-alt-01 | Vosk | https://alphacephei.com/vosk/index.zh.html | 官方中文介绍／Alpha Cephei | complete | 支持中文、离线移动端、Android、流式 API、约 50 MB 小模型、可重配词表 |
| SRC-20260906-think-asr-alt-02 | Vosk | https://github.com/alphacep/vosk-api | 官方仓库 README／Alpha Cephei | complete | 开源离线、Android API、连续转写、流式 API、词表重配、Apache-2.0 仓库许可证 |
| SRC-20260906-think-asr-alt-03 | Vosk | https://alphacephei.com/vosk/models | 官方模型目录／Alpha Cephei | complete | 中文模型条目、模型大小与许可证字段；小型中文模型约 42 MB，许可证标为 Apache-2.0 |
| SRC-20260906-think-asr-alt-04 | WeNet | https://wenet-e2e.github.io/wenet/runtime.html | 官方 runtime 文档／WeNet | complete | 流式与非流式统一模型、Android device 路径、逐帧输入、LibTorch runtime |
| SRC-20260906-think-asr-alt-05 | WeNet | https://github.com/wenet-e2e/wenet/blob/main/docs/pretrained_models.md?plain=1 | 官方预训练模型文档／WeNet | complete | 多个中文模型与 Android runtime 包；模型许可证跟随相应数据集许可证 |
| SRC-20260906-think-asr-alt-06 | WeNet | https://github.com/wenet-e2e/wenet/blob/main/LICENSE | 官方 LICENSE／WeNet | complete | WeNet runtime 仓库采用 Apache-2.0 |
| SRC-20260906-think-asr-alt-07 | ONNX Runtime Mobile + SenseVoiceSmall-onnx | https://onnxruntime.ai/docs/tutorials/mobile/ | 官方移动端文档／Microsoft | complete | Android Java／C／C++ 包、模型在设备上加载和运行、默认 CPU、arm64 库示例、应在目标设备测量大小与性能 |
| SRC-20260906-think-asr-alt-08 | ONNX Runtime Mobile + SenseVoiceSmall-onnx | https://www.modelscope.cn/models/iic/SenseVoiceSmall-onnx | 官方模型页／iic、ModelScope | partial | 2026-09-06 访问；同一 URL 的官方搜索摘要可见 `CN/ASR`、`ONNX`、`Apache License 2.0`、`241.59MB`、`2024-09-26`，并摘要本地／云端、离线文件转写及 `.pcm` client 示例；页面正文在抓取器中为 0 行、浏览器只渲染标题和 loading，因此只按摘要字段使用 |
| SRC-20260906-think-asr-alt-09 | ONNX Runtime Mobile + SenseVoiceSmall-onnx | https://github.com/Microsoft/onnxruntime/blob/main/LICENSE | 官方 LICENSE／Microsoft | complete | ONNX Runtime 采用 MIT License |
| SRC-20260906-think-asr-alt-10 | whisper.cpp | https://github.com/ggml-org/whisper.cpp | 官方仓库 README／ggml-org | complete | C／C++、CPU-only、Android、离线设备侧示例、量化、C API、MIT 仓库许可证；`Memory usage` 表给出 tiny 75 MiB／约 273 MB、base 142 MiB／约 388 MB |
| SRC-20260906-think-asr-alt-11 | whisper.cpp | https://github.com/ggml-org/whisper.cpp/blob/master/examples/whisper.android/README.md?plain=1 | 官方 Android 示例 README／ggml-org | complete | Android 示例把模型和样本放入 app assets，并建议 tiny／base 模型 |
| SRC-20260906-think-asr-alt-12 | whisper.cpp | https://github.com/openai/whisper | 官方模型仓库 README／OpenAI | complete | 多语言模型、模型规格与相对资源需求、非英语能力、整文件按 30 秒窗口转写；`License` 段明确 code 与 model weights 均以 MIT License 发布 |

预算汇总：Vosk 3；WeNet 3；ONNX Runtime Mobile + SenseVoiceSmall-onnx 3；whisper.cpp 3；跨候选公共页面 0；合计 **12/18**。本轮不再扩展页面。

### R1 同页复核访问记录

| 复核日期 | Source ID | 同一 URL 复核内容 | 结果／限制 |
| --- | --- | --- | --- |
| 2026-09-06 | SRC-20260906-think-asr-alt-07 | ONNX Runtime Mobile 的设备侧加载／运行、Android package、默认 CPU 原文 | complete；没有点击页面中的其他文档链接 |
| 2026-09-06 | SRC-20260906-think-asr-alt-08 | ModelScope 固定模型 URL 的页面标题、浏览器渲染与原官方搜索摘要字段 | partial；浏览器可见标题为“SenseVoice多语言语音理解模型Small-onnx”，正文持续 loading，未改用新页面补齐 |
| 2026-09-06 | SRC-20260906-think-asr-alt-10 | whisper.cpp README 的 Android／CPU-only 与 `Memory usage` 表 | complete；tiny／base 数字来自同一 README |
| 2026-09-06 | SRC-20260906-think-asr-alt-12 | OpenAI Whisper README 的 multilingual、资源参考与 `License` 段 | complete；code／model weights MIT 来自同一 README |

R1 没有增加页面计数：以上均是原 ledger URL 的复核，预算仍为 **12/18**。

## Evidence Card：Vosk

### E-VOSK-01｜中文、离线、Android 与流式路径

- Claim: Vosk 官方资料明确列出中文，支持离线移动设备和 Android，并提供流式／连续识别能力。
- Evidence: SRC-20260906-think-asr-alt-01；SRC-20260906-think-asr-alt-02。
- Evidence type: Observed。
- Source class: B（项目官方文档与官方仓库 README）。
- Limits: 官方页面没有在本轮证据内固定具体 Android release、arm64-v8a ABI、最低 Android 版本或 Xiaomi 15 性能。
- Product implication: 满足“中文 + Android + 本地离线 + 不强制上传原始音频”的硬筛选基础，适合优先进入未来安全 intake 选择决策。

### E-VOSK-02｜体积、许可证与来源

- Claim: 官方介绍把便携模型描述为约 50 MB；官方模型目录列出约 42 MB 的小型中文模型及 Apache-2.0，runtime 仓库同样标为 Apache-2.0。
- Evidence: SRC-20260906-think-asr-alt-01；SRC-20260906-think-asr-alt-02；SRC-20260906-think-asr-alt-03。
- Evidence type: Observed。
- Source class: B。
- Limits: 本轮没有取得模型文件、散列、发布签名、SBOM 或固定 release；许可证识别不替代法律审查。
- Product implication: 四个候选中，它对 P0 的体积和来源边界最清晰，但仍不能直接下载或采用。

### E-VOSK-03｜个性词表与剩余隐私缺口

- Claim: 官方资料明确说明词表可以快速重配。
- Evidence: SRC-20260906-think-asr-alt-01；SRC-20260906-think-asr-alt-02。
- Evidence type: Observed。
- Source class: B。
- Limits: 词表重配是否适用于选定中文模型、动态更新代价、专名准确率、内存 PCM API、原始音频是否可能被 sample／日志／缓存落盘、buffer 释放均未验证。
- Product implication: 个性词表能力状态优于其他候选，但 P0 的 90% 专名门槛仍须实测。

## Evidence Card：WeNet

### E-WENET-01｜中文、Android 与流式路径

- Claim: 官方 runtime 文档描述流式／非流式统一模型、Android device 路径和逐帧输入；官方模型文档列出多组中文 runtime 模型。
- Evidence: SRC-20260906-think-asr-alt-04；SRC-20260906-think-asr-alt-05。
- Evidence type: Observed。
- Source class: B。
- Limits: 本轮官方页面没有给出可固定的 Android arm64-v8a、CPU-only 包、最低系统、完整 Java／JNI API 或内存 PCM 接口合同。
- Product implication: 产品能力方向相关，但 Android 接入与验证成本明显高于 Vosk。

### E-WENET-02｜runtime 与模型许可证不闭合

- Claim: WeNet runtime 仓库采用 Apache-2.0；模型文档说明预训练模型许可证跟随相应数据集许可证。
- Evidence: SRC-20260906-think-asr-alt-05；SRC-20260906-think-asr-alt-06。
- Evidence type: Observed。
- Source class: B。
- Counterevidence: 在每候选三页预算内，没有关闭一个具体中文 Android runtime 模型的数据集许可证文本、模型权利边界和可重分发条件。
- Product implication: 不满足本轮“runtime 与模型许可证／来源均可识别”的硬筛选，不进入 shortlist。

### E-WENET-03｜工程边界未知

- Claim: 逐帧输入和设备 runtime 暗示可以设计本地流式处理。
- Evidence: SRC-20260906-think-asr-alt-04。
- Evidence type: Inferred。
- Limits: 是否强制文件路径、音频落盘／日志、buffer 释放、模型大小、内存占用、热词机制、目标设备性能与可复现依赖闭包均为 Unknown。
- Product implication: 若未来补齐模型许可证，仍需要单独的高成本预 intake；本轮不推荐。

## Evidence Card：ONNX Runtime Mobile + SenseVoiceSmall-onnx

### E-ORTSENSE-01｜Android 设备侧 CPU runtime

- Claim: ONNX Runtime Mobile 官方文档支持在 Android 上通过 Java／C／C++ 将模型加载并运行于设备，所有目标默认支持 CPU；文档也展示 arm64 库尺寸示例。
- Evidence: SRC-20260906-think-asr-alt-07。
- Evidence type: Observed。
- Source class: B。
- Limits: arm64 尺寸是文档中的 ONNX Runtime 1.18／ResNet 示例，不是本候选当前 ASR 组合的精确体积、版本或性能。
- Product implication: 提供可识别的 Android 本地 CPU 推理底座，但不是开箱即用的 ASR SDK。

### E-ORTSENSE-02｜中文模型、体积与双许可证

- Claim: 2026-09-06 对固定 ModelScope URL 的官方搜索摘要可见 `CN/ASR`、`ONNX`、`Apache License 2.0`、`241.59MB`、`2024-09-26`，并摘要本地／云端、离线文件转写和 `.pcm` client 示例；ONNX Runtime 官方 LICENSE 为 MIT。
- Evidence: SRC-20260906-think-asr-alt-08；SRC-20260906-think-asr-alt-09。
- Evidence type: Observed（模型页为 partial extraction）。
- Source class: B。
- Limits: 模型页正文抓取结果为 0 行，浏览器只成功渲染页面标题与 loading；以上字段只来自同一 URL 的官方搜索摘要，support 为 partial。未固定模型文件、散列、依赖、tokenizer、前后处理实现或精确 runtime release。
- Product implication: runtime 与模型来源／许可证可分别识别，满足研究阶段硬筛选，但 intake 首项应复核模型页及完整依赖边界。

### E-ORTSENSE-03｜组合路线的关键推断

- Official premise A: SenseVoiceSmall-onnx 的同一官方页面摘要把它标为中文 ASR、ONNX 模型，并明确存在本地／离线文件转写与 `.pcm` client 示例。`08`
- Official premise B: ONNX Runtime Mobile 官方页说明 ONNX 模型由 mobile app 在设备磁盘／内存中加载并运行，Android 使用 `onnxruntime-android`，所有目标默认支持 CPU。`07`
- Inference: 若该官方 ONNX 模型能由 ONNX Runtime Mobile 支持的算子和输入合同承载，则 Android app 可以把核心推理放在设备侧；“本地／离线转写”与“设备侧加载运行”共同表明云端上传不是这条候选架构的必需前提。
- Evidence: SRC-20260906-think-asr-alt-07；SRC-20260906-think-asr-alt-08。
- Evidence type: Inferred。
- Hard-filter treatment: 本轮把“存在 Android 路径”和“核心路线不强制云端上传”计为 **有限工程推断 PASS**，因为模型格式／用途／离线入口与 mobile runtime 的设备侧 ONNX／Android／CPU 前提均来自原页；不是只凭通用 runtime 加文件扩展名猜测。
- Counterevidence: 尚未证明该模型在 `onnxruntime-android` 上端到端算子兼容，也未证明 Android 端音频预处理、特征提取、tokenizer、解码、标点、长音频切分、内存 PCM、不落盘和许可证闭包；这些是 future intake 的明确 Unknown，不被硬筛选 PASS 覆盖。
- Product implication: 可列为第二候选，但属于高复杂度组合路线；若 future intake 发现模型无法由 Android ORT 承载，或完整 ASR 必须云端／强制落盘／引入来源不清组件，应立即停止。

## Evidence Card：whisper.cpp

### E-WHISPER-01｜Android、CPU-only 与离线路径

- Claim: whisper.cpp 官方 README 声明 C／C++、CPU-only、Android 支持和设备侧离线使用，并提供 C API 与量化路径。
- Evidence: SRC-20260906-think-asr-alt-10。
- Evidence type: Observed。
- Source class: B。
- Limits: 本轮没有固定 Android ABI 包、JNI 接口、runtime release、准确体积或最低系统。
- Product implication: 平台方向相关，但不足以单独满足全部硬筛选。

### E-WHISPER-02｜Android 示例与文件导向风险

- Claim: 官方 Android 示例把模型和音频样本放入 app assets，并建议使用 tiny／base 模型。
- Evidence: SRC-20260906-think-asr-alt-11。
- Evidence type: Observed。
- Source class: B。
- Counterevidence: 该示例是文件／assets 导向，本轮页面没有证明生产 API 可直接消费内存 PCM 并保证不落盘。
- Product implication: 与“按住说话后仅内存转写、原始录音不落盘”仍有待关闭的接口边界。

### E-WHISPER-03｜上游许可证已识别，中文证据仍不足

- Claim: OpenAI Whisper 官方 README 说明模型为 multilingual、支持非英语，并给出模型规格和整文件 30 秒窗口处理方式；同页 `License` 段明确 code 与 model weights 均以 MIT License 发布。
- Evidence: SRC-20260906-think-asr-alt-12。
- Evidence type: Observed。
- Correction: 初稿把模型权重许可证写成未识别是错误；R1 修正为 runtime 仓库 MIT、上游 code 与 model weights MIT 均有官方识别。未来仍须核查具体转换 ggml 制品的来源、转换链、散列、notice 与再分发，但这不能倒写为“上游模型许可证未知”。
- Additional resource fact: whisper.cpp 同一 README 的 `Memory usage` 表给出 tiny 75 MiB／约 273 MB、base 142 MiB／约 388 MB；它是项目官方估计，不是 Android 或 Xiaomi 15 实测，也不同于 OpenAI README 的 A100 VRAM 参考。
- Counterevidence: 本轮选定官方页面仍没有明确写出 Mandarin／Chinese；multilingual／non-English 不能按合同自动替代中文官方证据。
- Product implication: 许可证硬条件改为 PASS，但中文硬条件仍为 Unknown／FAIL，因此 whisper.cpp 仍不进入 shortlist。

## Evidence Eval

- Decision Alignment: 15/15
- Source Quality: 18/20
- Citation Coverage: 18/20
- Fact/Inference/Unknown Separation: 15/15
- Counterevidence: 9/10
- Decision Value: 8/10
- Maintainability: 9/10
- Total: **92/100 · pass（R1）**

扣分原因：SenseVoiceSmall-onnx 官方页面只有同 URL 官方搜索摘要可用，正文未成功渲染；ONNX 组合仍依赖一段已明确的工程推断；没有在预算内固定候选版本、制品身份或目标设备结果。Whisper 许可证错误和资源遗漏已修正，中文缺口未被许可证修正替代。
