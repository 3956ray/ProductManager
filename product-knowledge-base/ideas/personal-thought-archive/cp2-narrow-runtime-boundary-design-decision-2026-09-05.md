# 决策记录：CP2 窄运行时边界设计准入

Owner: Product Lead
Last updated: 2026-09-05
Source: `../../raw/SRC-20260905-think-cp2-design-decision-01.md`、`../../raw/SRC-20260905-think-cp2-design-decision-02.md`、`../../raw/SRC-20260905-think-cp2-design-decision-03.md`、`../../raw/SRC-20260905-think-cp2-design-decision-04.md`、`../../raw/SRC-20260905-think-cp2-design-decision-05.md`、`../../raw/SRC-20260905-think-cp2-design-decision-06.md`
Confidence: High（设计身份、返工范围、输入集合和设计边界已由 Leader 独立验收）；Medium（固定上游源码能否满足窄边界仍需新正文与源码级静态门禁）
Related decisions: `prd-v0.1-2026-09-04.md`；`cp1-deferred-cp2-entry-decision-2026-09-05.md`；`cp2-runtime-security-route-decision-2026-09-05.md`；`cp2-minimal-source-route-revision-decision-2026-09-05.md`；`cp2-runtime-boundary-route-decision-2026-09-05.md`
Next review date: 2026-09-12

## RESULT

**APPROVED — 接受项目自有 handle 型 CPU-only／ASR-only 窄边界作为后续源码审查合同；不批准第三方源码、制品、适配器实现、构建输入、依赖、模型、集成、CP2 或 CP3。**

## 正式决定

1. 接受设计任务的 `design_feasible`，但把含义严格限定为：现有 28 项设计输入足以形成一份完整、可审查、可被后续源码证据推翻的合同。它不证明上游源码闭合、无需修改即可满足合同、可以构建或运行，也不构成任何安全制品批准。
2. 接受选项 2“项目自有 handle 型窄适配边界”作为唯一后续审查方向。业务层未来只能看到固定运行时 handle、另行批准模型的固定 handle、stream 生命周期、有界内存 PCM、decode、只读文字结果、版本和释放。
3. 拒绝选项 1“宽 API＋调用方规则”作为产品架构终态。它只能作为比较基线；危险能力仍可表达或被链接，控制依赖调用约定，升级与新增调用方都会扩大重复审计和漂移风险。任何未来实现不得以“当前 caller 不调用”为由保留宽 API。
4. 下一步只能是新的、独立授权的源码级边界可行性静态门禁。现有已提交证据足以定义该门禁，但不足以回答源码能否满足设计；因此下一任务**必须取得全新的、固定身份且有硬上限的第三方源码正文**。
5. 不得读取或复用旧隔离 discovery corpus、101 项候选、首次部分快照、被 `block` 的归档、AAR、模型或任何 `manual_review` 制品。新正文只在新的隔离目录中用于静态审查，任务结束后不能成为快照、实现或构建输入。
6. 若源码级门禁发现任一 P0 必需能力只能通过 denylist 能力、上游 broad JNI、用户可控路径或源码修改提供，结论必须为 `source_boundary_blocked`，并暂停 sherpa-onnx 路线；不得扩宽合同。若因上限、宏／生成边或外部依赖无法判断，则为 `insufficient_evidence`，停止并回到产品决策门。

## `design_feasible` 的准确边界

### 已验证

- 首版提交 `8eea68384efcb61cbea40a423b755edf3175f22d` 新增七个设计文件；返工提交 `a57f643bac24edef5d6601b8a59baa77060f3d2c` 只修改 `context.md` 与 `hardening.json`。
- 最终设计目录 tree 为 `31376c73f43caf3bbfd664d8316ffecdc589379d`。
- 设计输入为 28 条 canonical record，集合摘要为 `c318c5a5f91d4af1d2759895ab9d5296c5784eaa214548b92f25fba4096764d2`。
- 设计区分 Observed／Inferred／Proposed，为两个选项补齐 E01–E09 覆盖与安全、性能、内存、可靠性、可运维性、迁移权衡，并完整保留 denylist、回滚和未来九层验证计划。
- 没有 `implementation/`、产品源码、第三方正文、构建输入、依赖、模型、二进制或音频进入设计提交。

### 没有验证

- `fixed_point=false` 没有改变；两条内部缺失边和 332 条 system/external 边仍未闭合。
- 101 项候选仍不是最终 allowlist、源码快照或构建输入。
- 上游源码能否在不修改的情况下提供全部 P0 能力，以及窄边界背后是否仍会链接 dormant 禁止能力，均未知。
- 外部依赖、许可证／NOTICE、ONNX Runtime、工具链、构建、制品、模型、源码—二进制 provenance 和动态行为均未知。
- 原始 PCM 不落盘、不上传、不进日志、内存清零、飞行模式、小米 15、双模型、准确率、30／90 秒延迟、内存、耗电、发热与 20 次 90 秒稳定性均未验证。

## 产品判断

| 维度 | 接受 handle 型窄边界合同 | 保留宽 API＋caller 规则 |
| --- | --- | --- |
| 用户价值 | 保留本地中文、飞行模式和按住说话的产品方向；不提前承诺准确率或速度 | 早期接入可能更快，但不能形成可长期信任的语音入口 |
| 隐私 | 业务层无法表达音频路径、provider、动态库／模型路径；生命周期有单一 owner | 隐私依赖每个 caller 持续守规，宽制品可能仍携带禁止能力 |
| 工程成本 | 需要维护 facade／未来 native adapter，并增加源码与制品双层证明 | 初始迁移成本低，但每次升级和调用点都需全量复核 |
| 残余风险 | “窄公开 API、宽内部制品”、native PCM 副本、模型与依赖仍未验证 | 漂移、旁路、分散释放责任和 dormant 能力风险更高 |
| 可逆性 | 当前只是合同；源码门禁失败即可暂停，没有实现沉没成本 | 删除规则容易，但会回到未批准状态，不是安全终态 |
| 决定 | **接受为审查合同** | **拒绝为产品架构终态** |

会改变本决定的证据：P0 必须依赖任一 denylist 能力；项目边界只能传递上游聚合配置或用户路径；固定源码无法在限额内形成可审查内部图；或外部依赖／生成逻辑是判断最小能力不可绕过的前置。出现这些情况不继续美化设计，而是阻塞或暂停。

## 下一项唯一任务

任务名：`CP2-ASR-NARROW-SOURCE-BOUNDARY-FEASIBILITY-GATE-001`。

### 唯一目标

在不执行、不修改、不构建第三方内容的前提下，对固定 sherpa-onnx 源码建立一个**仅供审查的、P0 在线 ASR 核心内部源码图**，判断现有源码是否能在完全排除 denylist、上游 broad JNI/Kotlin 和用户可控路径的情况下支撑项目自有 handle 型合同。

### 为什么需要新正文

已提交的设计与结构化发现证据可以描述“应当是什么”，却没有把所需 P0 操作逐项映射到完整源码定义、调用边和条件编译分支。旧 corpus 不得读取或复用，且已有材料为 `manual_review`。因此必须从同一不可变上游身份重新取得有限正文；没有新授权则不得开始。

### 固定身份、种子与硬上限

- 审查合同固定为设计返工提交 `a57f643bac24edef5d6601b8a59baa77060f3d2c`、设计 tree `31376c73f43caf3bbfd664d8316ffecdc589379d` 与 28 项输入摘要 `c318c5a5f91d4af1d2759895ab9d5296c5784eaa214548b92f25fba4096764d2`；不得在任务内修改合同。
- Repository：`https://github.com/k2-fsa/sherpa-onnx`。
- Commit：`917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`。
- Tree：`fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`，必须先验证 `truncated=false` 及 metadata hash 与既有正式证据一致。
- 新隔离目录；正文获取前冻结 `source-boundary-review-policy.json`，并证明目录内没有旧 corpus、快照或第三方正文。
- 精确 seed 共 9 项：
  1. `LICENSE`
  2. `sherpa-onnx/csrc/online-recognizer.h`
  3. `sherpa-onnx/csrc/online-recognizer.cc`
  4. `sherpa-onnx/csrc/online-recognizer-impl.h`
  5. `sherpa-onnx/csrc/online-recognizer-impl.cc`
  6. `sherpa-onnx/csrc/online-stream.h`
  7. `sherpa-onnx/csrc/online-stream.cc`
  8. `sherpa-onnx/csrc/online-model-config.h`
  9. `sherpa-onnx/csrc/version.h`
- 允许范围仅为 `LICENSE` 与 `sherpa-onnx/csrc/` 下固定 tree 中的普通 `.h`／`.cc` Git blob；禁止 symlink、生成文件、归档、二进制和其他目录。
- 只跟随已取得正文中的确定性、字面量、唯一解析的仓库内 C/C++ include；每条授权在获取前写入 append-only ledger，不允许人工临时增补 seed 或改变规则。
- 风险预算上限：最多 **96 个正文文件、1,048,576 正文字节**。这是安全审查上限，不是对真实闭包大小的估计；达到任一上限即停止，不得扩容。
- system/external include 只登记，不获取；CMake、JNI、Kotlin、外部依赖、工具链、模型和音频均不取得。

### Denylist 与获取前停止

以下路径、文件名或能力边一经发现，只登记引用方、位置和目标，**不得获取目标正文**：WAV／wave writer、任何文件式音频 I/O、ADSP、QNN、RKNN、TTS、VAD、speaker／diarization、denoise、punctuation、audio tagging、WebSocket、PortAudio、下载／FetchContent、上游 `jni/`／`kotlin-api/`、非必要 public C/C++、用户可控 provider／库名／模型或动态库路径。

若所需 P0 操作直接或传递依赖该边，返回 `source_boundary_blocked`。不得用“编译时可能关闭”“当前 caller 不调用”或“未来再裁剪”绕过，除非已有正文中的确定性条件能在不执行构建系统、不修改源码的情况下证明该边不属于目标核心图；此时仍须记录为条件性证据，不能视为制品排除证明。

### 允许动作

- 通过 GitHub Git Data blob API 按冻结规则取得上述新正文，仅作静态读取；
- 用预先完整人工复核的可信只读解析器提取 literal include、声明／定义、调用关系、配置与路径参数、日志／文件／网络／加载特征；
- 对审查材料做文件身份、lstat、UTF-8／NUL、哈希、scanner 与人工静态复核；
- 形成 P0 能力—源码符号—内部边映射、denylist reachability map、未决 external edge 清单和设计判定。

### 明确不做

- 不读取、复制或复用旧 discovery corpus、101 项候选、部分快照、block 归档、AAR、模型或其他 manual_review 制品；
- 不继续旧闭包、不重冻旧 policy／allowlist、不建立最终源码快照；
- 不运行／配置 CMake、Gradle、脚本、源码、编译器、JNI、Kotlin 或测试，不形成方法签名、适配器源码、头文件、patch、实现计划、build definition 或构建输入；
- 不取得 CMake、JNI/Kotlin、外部依赖、工具链、模型、音频、二进制或替代运行时；
- 不修改 `/Users/orderly_ray/Projects/think` 产品源码，不安装、加载、推理、真机测试、集成、通过 CP2 或进入 CP3。

### 必须交付

1. 正文前冻结的 policy、固定身份、9 seed、允许范围、denylist、96 文件／1 MiB 上限和 pre-body 空目录证据；
2. append-only 获取／解析 ledger 和逐文件 manifest，含 immutable path、Git blob SHA、size、SHA-256、lstat 与前置授权；
3. P0 操作到现有源码声明／定义／调用边的映射，只覆盖 runtime/model handle 概念对应的底层能力、stream、内存 PCM、decode、只读结果、版本和释放；
4. 每个 denylist 能力的可达／不可达／未知证据，及 broad JNI/Kotlin 不进入目标图的证明边界；
5. 仅限 `csrc` 仓库内部 literal include 的 `internal_review_fixed_point`、所有缺失／排除／external／条件边和上限状态；不得把它写成完整源码或依赖闭包；
6. scanner 原始结果、人工复核、盲区、工作区状态和非继承声明；只提交派生证据，不提交第三方正文；
7. 单一结论：`source_boundary_feasible`、`source_boundary_blocked` 或 `insufficient_evidence`。任何结论都不批准快照、实现、构建、制品、模型、集成、CP2 或 CP3。

### 通过条件

只有同时满足以下条件才可返回 `source_boundary_feasible`：

- 冻结规则未修改，全部正文有获取前授权，身份／哈希／类型／集合一致且在 96 文件／1 MiB 内；
- 对允许范围的确定性仓库内 literal include 达到 `internal_review_fixed_point=true`，没有 unresolved、macro-generated、ambiguous 或未记录边；
- 每个 P0 底层能力都有现有源码映射，不要求修改源码、使用上游 broad JNI/Kotlin、传递聚合配置或暴露用户可控路径；
- 目标内部图没有取得或依赖任何 denylist 能力；system/external 边被完整登记为后续独立门禁，而不是被假定安全；
- 输出明确只是审查材料和候选内部图，不是最终 allowlist、快照、实现或构建输入。

### 停止条件与失败回退

出现任一项即停止：

- 固定 commit／tree／path／mode／type／size／blob／内容哈希不一致，或发现链接、特殊文件、ledger 不连续、scanner `block` 证据；
- 需要人工增补 seed、修改冻结规则、超出 96 文件／1 MiB，或需要 CMake／生成逻辑／宏／多义路径才能解析；
- P0 必需路径触及 denylist、上游 broad JNI/Kotlin、用户可控路径或要求修改源码；
- 必须取得 system/external、依赖、模型、构建输入、音频或其他目录正文才能判断；
- 任务开始形成实现、构建、制品、集成、CP2、CP3 或父亲 Alpha 结论。

命中 denylist或需源码修改时返回 `source_boundary_blocked`，并将 sherpa-onnx 路线置为 `PAUSE`，等待 Product Lead 决定是否启动路线 B。因上限或证据类型无法判断时返回 `insufficient_evidence`，同样停止并回到产品决策门；不得在任务内扩容或获取更多内容。

## Product Lead 新授权

需要新授权。设计任务授权已随 `CP2-ASR-NARROW-RUNTIME-BOUNDARY-DESIGN-001` 和返工验收结束而耗尽；本产品决定不自动授权新正文或源码级门禁。

精确最小授权句：

> 我批准 `CP2-ASR-NARROW-SOURCE-BOUNDARY-FEASIBILITY-GATE-001`：以设计返工提交 `a57f643bac24edef5d6601b8a59baa77060f3d2c`、设计 tree `31376c73f43caf3bbfd664d8316ffecdc589379d` 和 28 项输入摘要 `c318c5a5f91d4af1d2759895ab9d5296c5784eaa214548b92f25fba4096764d2` 为不可修改的审查合同；仅允许在全新隔离目录中，针对 sherpa-onnx commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`、tree `fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`，按正文前冻结的 9 个精确 seed、仅限 `LICENSE` 与 `sherpa-onnx/csrc/` 普通 `.h`／`.cc` blob、确定性字面量 include 规则及 96 文件／1,048,576 字节上限，通过 GitHub Git Data blob API 重新取得新正文，仅用于静态源码边界可行性审查。此授权禁止读取或复用旧 corpus、候选清单、快照、block／manual_review 制品，禁止获取 denylist、CMake、JNI/Kotlin、外部依赖、模型、音频或二进制，禁止执行、修改源码、重冻旧清单、建立快照、形成实现／构建输入、构建、安装、加载、推理、集成、宣称 CP2 通过或进入 CP3。

## 证据身份与内容哈希

| 证据 | 固定身份／SHA-256 |
| --- | --- |
| 本次产品决策合同 | `b1f1b45eb0d83f2a4673ae0a19e3c09606034b121ad9352989f17b11226b6717` |
| 设计首版提交／tree | `8eea68384efcb61cbea40a423b755edf3175f22d`／`5e7de6b170a55a52e0e9e07eb96fe1d64381b81f` |
| 设计返工提交／最终 tree | `a57f643bac24edef5d6601b8a59baa77060f3d2c`／`31376c73f43caf3bbfd664d8316ffecdc589379d` |
| 28 项设计输入集合 | `c318c5a5f91d4af1d2759895ab9d5296c5784eaa214548b92f25fba4096764d2` |
| 最终 `context.md` | `4d7fd8a0457cf6c59de2d42c9a67bba59087f4820dc3a68ef78bb3425b53f8b1` |
| 最终 `hardening.json` | `2186efe25543b051a6cf7ac583c8beb1b67610602d968a1ac784d244169b1d7d` |
| 最终 `hardening.md` | `a79fb62ca93c08f91e8140c80be3e7f4414f179acc697572e3615cf30148c216` |
| 最终 proposal | `257469cf982dafd0a0a6701090270ad54d4512fbdccf422afda0e8a2776e803e` |
| before／两份 after Mermaid | `d68a604c6e4e5716ed81a5f2c327937510ac4357889dc6a8e138c6472ff380da`／`683979bcf02f01c0a929abf2096b4ec0ccb350cb336c09dfe7b5790ed9f594fb`／`5fce0ad5b45df1ad06f205db01be03c73080a65e8fc943983f17be716f736031` |
| Leader R1 验收报告 | `5981edfe0e6c295529d80e0b9b2f418284c6c46431e6441aa4615b9b118dd3f2` |

## 状态、非继承与禁止声明

- 现有源码归档 `block`；AAR、Zipformer、首次部分快照和静态发现材料的 `manual_review` 裁决均保持，且只适用于各自精确对象。
- 本设计 `APPROVED`／`design_feasible` 不继承给新正文、源码图、最终快照、适配器、构建输入、依赖、工具链、制品、模型、APK、真机或 checkpoint。
- CP1 父亲人工门槛继续 `Deferred, not removed`，最迟在任何 CP3 准入决定前恢复；Conformer 也继续 `Deferred, not removed`。
- Research Quality 保持 86；Validation Level 保持 V2；三步录入／找回与原始音频不落盘、不上传、不进日志的要求不变。

在对应独立门禁前，不得声称：窄边界已经实现；固定源码可以闭合或构建；禁止能力已从源码或制品排除；模型、准确率、性能、稳定性、飞行模式、小米 15 或音频隐私已经验证；CP2、CP3、父亲 Alpha 或公开发布已经批准。

允许的准确表述是：

> 产品经理接受项目自有 handle 型窄边界作为后续源码审查合同。`design_feasible` 只表示可以定义下一门禁；任何新正文都需要 Product Lead 新授权，当前没有源码、实现、构建、模型、集成或 CP2／CP3 批准。

## 复查触发条件

- Product Lead 批准、拒绝或修改源码级门禁授权；
- 源码级门禁返回 `source_boundary_feasible`、`source_boundary_blocked` 或 `insufficient_evidence`；
- 请求扩容、读取旧 corpus、修改源码、建立快照、获取依赖／模型、构建、集成、恢复 Conformer 或进入 CP3；
- 上游提供新的最小 CPU-only／ASR-only 接口、无下载构建或合格 reviewer 新证据；
- 任何人把设计批准误写为源码／制品批准或 CP2 通过。
