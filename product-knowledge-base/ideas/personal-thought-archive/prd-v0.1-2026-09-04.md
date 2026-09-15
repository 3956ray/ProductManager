# PRD：思（think）Android App v0.1

Owner: Product Lead
Last updated: 2026-09-11
Source: `../../raw/SRC-20260904-personal-thought-archive-01.md`、`../../raw/SRC-20260904-personal-thought-archive-10.md`、`../../raw/SRC-20260905-personal-thought-archive-01.md`、`../../raw/SRC-20260905-think-cp1-gate-01.md`、`../../raw/SRC-20260905-think-cp2-runtime-01.md`、`../../raw/SRC-20260905-think-cp2-minimal-route-01.md`、`../../raw/SRC-20260905-think-cp2-boundary-route-01.md`、`../../raw/SRC-20260905-think-cp2-design-decision-01.md`、`../../raw/SRC-20260905-think-cp2-tool-repair-01.md`、`../../raw/SRC-20260905-think-cp2-acquisition-tool-01.md`、`../../raw/SRC-20260906-think-cp2-metadata-path-01.md`、`../../raw/SRC-20260906-think-cp2-license-routing-01.md`、`../../raw/SRC-20260906-think-cp2-semantics-readiness-01.md`、`../../raw/SRC-20260906-think-cp2-manual-capability-01.md`、`../../raw/SRC-20260906-think-cp2-manual-capability-r1-01.md`、`../../raw/SRC-20260906-think-cp2-review-timestamp-01.md`、`../../raw/SRC-20260906-think-cp2-token-provenance-01.md`、`../../raw/SRC-20260906-think-cp2-v8-hard-stop-01.md`、`../../raw/SRC-20260906-think-cp2-local-configuration-01.md`；Leader `CP2-ASR-V8-HOTWORDS-CONSUMER-SINGLE-BODY-REVIEW-001` 派生报告；Android、Microsoft、CP1 审计、CP2 安全门禁与开源项目来源卡
Confidence: Medium-High（核心用户行为真实，技术路径有官方依据；目前只有一位核心用户，尚无成品使用数据）
Related decisions: `naming-decision-2026-09-04.md`；`development-start-decision-2026-09-05.md`；`cp1-deferred-cp2-entry-decision-2026-09-05.md`；`cp2-runtime-security-route-decision-2026-09-05.md`；`cp2-minimal-source-route-revision-decision-2026-09-05.md`；`cp2-runtime-boundary-route-decision-2026-09-05.md`；`cp2-narrow-runtime-boundary-design-decision-2026-09-05.md`；`cp2-first-party-tool-repair-decision-2026-09-05.md`；`cp2-acquisition-tool-scope-decision-2026-09-05.md`；`cp2-metadata-path-compatibility-decision-2026-09-06.md`；`cp2-license-text-routing-decision-2026-09-06.md`；`cp2-source-semantics-readiness-decision-2026-09-06.md`；`cp2-manual-capability-evidence-decision-2026-09-06.md`；`cp2-review-timestamp-representation-decision-2026-09-06.md`；`cp2-review-token-provenance-decision-2026-09-06.md`；`cp2-v8-hard-stop-next-step-decision-2026-09-06.md`；`cp2-v8-local-configuration-route-decision-2026-09-06.md`；`cp2-v8-hotwords-consumer-route-decision-2026-09-06.md`；`cp2-hotwords-chain-termination-route-decision-2026-09-06.md`；`cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md`；原生 Android App；Vosk 仅获批进入官方身份 intake 准备；只把文字发送给云端 AI；三步记录与三步找回
Next review date: 2026-09-18

Research Quality: 86 · pass（技术来源以官方文档与一方仓库为主；用户证据仍集中于单一家庭）
Validation Level: V2（存在长期、高频、自发的日历替代行为；尚未验证新产品使用与留存）
Next evidence: Leader验收全量UI范围后下发NOTES-UI-DEVICE-001，逐页完成Android设备的视觉、触控、返回栈、CRUD和无障碍验收
Allowed next investment: 现有NOTES-L1/L2/L3数据与工程逻辑已验收；最多一个UI设备验收任务，逐项记录device_unverified或通过；不自动新增开发阶段，ASR/CP2和父亲Alpha未放行
Pause/Kill condition: 本地中文转写在目标手机上不可用；父亲仍需反复协助才能记录或找回；模块确认比原日历更费力；导入或提醒无法可靠工作

## 0. 文档状态

`Draft for prototype`。

本 PRD 已确定 App 方向与第一版边界，但只授权进入技术验证与父亲单用户 Alpha，不代表公开上架、商业化或 roadmap 优先级已经确认。当前知识库仍有一个活跃 Discovery；本 PRD 不修改 `BOARD.md`。

2026-09-05 顺序更新：CP0 完整实机审计不再阻塞可逆开发启动，但属于延后而不是删除；需要验证 ASR、权限、提醒或进入父亲 Alpha 时，仍用小米 15 提供证据。产品目标、P0/P1 和所有隐私／范围边界保持不变，详见[开发启动决策](development-start-decision-2026-09-05.md)。

2026-09-05 CP1 门禁更新：合成原型工程范围已验收，但父亲人工可用性没有测试，CP1 整体没有通过。该人工门槛标记为 `Deferred, not removed`，仅批准进入 CP2 技术开发；必须在任何 CP3 准入决定前恢复。CP2、CP3 和父亲 Alpha 均未通过或预先批准，详见[CP1 延后与 CP2 准入决定](cp1-deferred-cp2-entry-decision-2026-09-05.md)。

2026-09-05 CP2 运行时安全更新：固定源码归档为 `block`，官方 AAR 与 Zipformer 14M INT8 四文件集均为 `manual_review`，三者当前都禁止采用且裁决互不继承。产品经理只批准“Product Lead 另行明确授权后，建立可复现最小源码快照并逐阶段门禁 arm64-v8a、CPU-only、ASR-only 构建”的路线；Conformer 静态门禁延后但不删除。CP2 仍未通过，详见[CP2 运行时安全路线决定](cp2-runtime-security-route-decision-2026-09-05.md)。

2026-09-05 CP2 最小源码协议修订：首次任务正确停止；151 项冻结清单只取得并验证 50 项后发现 5 个清单外 include，其中一个跨入 TTS，部分快照为 `manual_review` 且不得构建。旧授权已经随该任务结束。产品路线修订为“预冻结规则的有界静态闭包发现材料”与“以后另行授权、重新取得的最终闭合快照”两个独立阶段，裁决不得继承；下一单仍须 Product Lead 新授权，详见[最小源码发现与冻结路线修订](cp2-minimal-source-route-revision-decision-2026-09-05.md)。

2026-09-05 CP2 运行时边界路线更新：有界发现任务在 Leader 收敛后停止，112 文件／499,282 字节、615 条 ledger、`fixed_point=false` 与两条未完成内部边只说明任务没有完成，不能误写成上游无法闭合；但 `wave-writer.h` 路径写 WAV、`ADSP_LIBRARY_PATH`、QNN/RKNN 与宽 JNI/Kotlin 是独立边界缺陷，发现材料保持 `manual_review` 且不得进入阶段 B。产品经理只批准 Product Lead 另行授权后的纯设计任务，用已提交证据设计项目自有 CPU-only／ASR-only 窄 API／适配边界；设计失败则暂停 sherpa-onnx 并回到产品决策门，不自动启动替代运行时研究，详见[运行时窄边界路线决定](cp2-runtime-boundary-route-decision-2026-09-05.md)。

2026-09-05 CP2 窄边界设计准入更新：Leader 已接受返工后的七文件设计包，最终 tree `31376c73...379d`、28 项输入摘要 `c318c5a5...64d2`。`design_feasible` 只表示项目自有 handle 型边界可以成为后续源码审查合同，不表示源码、实现、构建、模型、音频隐私、CP2 或 CP3 获批。该决定当时要求 Product Lead 新授权；精确授权随后已经取得，但第一方准备审查在任何第三方正文获取前因工具缺陷停止。固定 commit/tree、9 seed、96 文件／1 MiB 与禁止范围继续有效，授权不能绕过停止条件。详见[窄边界设计准入决定](cp2-narrow-runtime-boundary-design-decision-2026-09-05.md)。

2026-09-05 CP2 第一方工具返工更新：源码正文获取尚未开始，准备阶段因第一方 policy／parser／controller 缺陷正确停止。该 `blocked` 不等于 sherpa-onnx 源码不可行。产品经理只批准在独立新目录用 Python 标准库和项目自建合成输入修复、测试第一方审查工具；旧尝试保持只读，不原地修复或补签。后续必须严格按“工具开发 → Leader 验收 → 单独正式冻结 → 单独真实获取”推进，当前不批准任何第三方正文、实现、构建、模型、CP2 或 CP3。详见[第一方审查工具离线返工决定](cp2-first-party-tool-repair-decision-2026-09-05.md)。

2026-09-05 CP2 完整获取工具范围更新：Leader 已接受提交 `da9279a` 的离线核心/schema/合成证据候选，两次各 66 项测试和 117 条记录、每次 83 条账本及终态重算通过；但该候选仍是 synthetic-only，没有真实传输和 metadata/input 入口，不能冻结成完整获取 release。产品经理只批准在独立新目录离线开发完整第一方组件，以合成 GitHub-like 响应和替身传输验证，实际网络／DNS 必须为零。完整候选经 Leader 验收后才能另行冻结，再另行映射既有授权执行真实获取。详见[完整第一方获取工具离线开发范围决定](cp2-acquisition-tool-scope-decision-2026-09-05.md)。

2026-09-06 CP2 metadata 路径兼容更新：v3 提交 `e4cd300` 已通过 Leader 两轮各 100 项测试验收，冻结提交 `e2d64f9` 也已验收；但固定真实 tree 的 8585 条 metadata 中有 171 个范围外名称含 @ 等字符，冻结 parser 因把获取路径字符规则施加于全部惰性名称而停止。产品经理只批准在新候选中分离“无损 metadata name”与“严格 acquisition path authorization”，保留全部条目、SHA、唯一性和穿越拒绝，不让 171 项获得正文请求资格。两份固定哈希 JSON 仅可在合成回归后用于 Leader 的只读、零网络、纯解析验收；旧冻结不改写，详见[metadata 路径兼容修复决定](cp2-metadata-path-compatibility-decision-2026-09-06.md)。

2026-09-06 CP2 LICENSE 文本路由更新：新候选与冻结完成后的一次真实获取只请求了固定 `LICENSE`，随后因自然语言撇号被错误送入 C/C++ 词法器而确定性停止；没有请求 8 个 C/C++ seed，`fixed_point=false`、`source_verdict=insufficient_evidence`。产品经理只批准在独立 v5 候选中按冻结合同的精确 path/role 将 `LICENSE` 路由为惰性 `license_text`，保留身份、扫描、账本和人工许可证审查，禁止扩展名猜测、内容嗅探及 C/C++ 规则放宽。旧 run 不恢复；离线修复无需重复用户授权，但任何新冻结后的第二次真实获取都须 Product Lead 新明确授权，详见[LICENSE 文本路由修复决定](cp2-license-text-routing-decision-2026-09-06.md)。

2026-09-06 CP2 源码语义就绪更新：v5 离线修复、新冻结及新授权后的真实获取按合同停止；只取得 `LICENSE` 与 `online-recognizer.h`。前者文本路由正常，后者因 line comment 中的 `websocket` 命中 denylist，同时还暴露旧合同不支持的 canonical include guard。注释命中不是可达能力证明，guard 也不是实现 bug。现行获取合同标记为 `REVISE`：下一单只用自建 fixture 离线建立词法通道、comment pending／active deny 分级和严格 canonical guard 子集；任何 pending、活动 deny 或未知预处理仍阻止后继请求。普通离线准备无需重复授权，新的真实获取必须等独立验收／冻结后再向 Product Lead 请求，详见[源码语义就绪路线修订](cp2-source-semantics-readiness-decision-2026-09-06.md)。

2026-09-06 CP2 人工能力裁定接收更新：v6 R1 已通过 Leader 双跑 158 tests／961 outcomes，三文档冻结 `d78577b` 已验收且没有 pending 清除接口。用户精确授权的单份既有 header 人工复核只确认 57／60 行两个 `websocket` occurrence 为 `comment_only_nonoperative_for_this_body`；相邻布尔字段、引用实现、整份文件和真实能力可达性均未清除。产品经理只批准在独立 v7 候选中离线实现可信 authority map 与逐 occurrence 证据接收，原 pending/analysis/ledger/terminal 保持，active/uncertain deny、词法、预处理、文件安全与 checkpoint 继续硬停止。当前 pending 未清除，也没有新获取授权，详见[精确人工能力裁定证据接收决定](cp2-manual-capability-evidence-decision-2026-09-06.md)。

2026-09-06 AUTHORITY-DAG-01 R1：v7 候选 `C` 先独立验收；之后以单独任务创建不具操作授权的 `review_map_commitment K`；新 v7 execution freeze `F` 只绑定 `C＋K`，不预知最终 map；最终 `M` 再绑定 `F＋K＋R`，Product Lead 的新获取授权 `A` 精确绑定 `F＋M`，受信 driver 才据此构造不能从 input 学习的 `Trust T`。历史 `d78577b` 只是 review-context freeze `H`。旧分析／pending／ledger／terminal 原字节只读；v7 adjudication/effective status 属于新 run、新 hash，不能冒充旧 identity。该 R1 只消除合同循环，不创建 commitment/map/Trust 或获取权限。

2026-09-06 CP2 人工审查时间表示更新：v7 R1 `C=443bbb5…` 已通过 Leader 两轮各 167 tests／1210 outcomes，但真实 R 的 `reviewed_at=2026-09-06T06:48:22.579140+08:00` 无法由 v7 的整秒 UTC schema 无损表示；截断会丢失 579140 微秒，因此 K 前置检查正确停止且没有创建 `K/F/M/A/T/N`。产品经理只批准独立 v8 第一方离线时间修订：严格验证有效日期、1..6 位小数与明确 offset，同时绑定原始字符串、无损 UTC、precision、offset 和表示 digest；等时异串不得互换身份。v7 验收保持只读，新的 v8 C 独立验收后才可重新进入 `K→F→M→新 A→T/N`。详见[人工审查时间无损表示决定](cp2-review-timestamp-representation-decision-2026-09-06.md)。

2026-09-06 CP2 原 token 来源更新：v8 `C=1fe8574…` 已通过 Leader 双跑各 174 tests／1338 outcomes／0 skip；随后 K 因原 R/verification 未保存两处命中的原 9-byte token 而正确停止。历史验证脚本先 lower() 再定位，不能反推原大小写，schema 不得放宽。原用户批准精确覆盖同一 retained envelope/header 和行 57／60，且无一次性读取条款；产品经理确认一个更小、同对象、exact-slice、离线的 append-only provenance 补录仍在该权限内，不是复用旧 acquisition 授权。补录 P、P 验收、K、F、M、新 acquisition A、T/N 必须逐单分离。详见[原 token 证据补录决定](cp2-review-token-provenance-decision-2026-09-06.md)。

2026-09-06 CP2 v8 真实获取硬停止更新：P/K/F/M 与新的用户 acquisition A／T/input/package 后续均经独立步骤建立，一次性 v8 run 已执行并由 Leader 接受为“正确停止”，提交 `393640b8…`。只取得 `LICENSE` 与 `online-recognizer.h`，共 19,297 bytes；5 个 active `dynamic_paths` 独立触发 `denylist_capability`，4 个 comment 对比已授权 2 个又触发 complete-set rejection。成功 adjudication 为 0、pending 未清、`fixed_point=false`、源码仍 `insufficient_evidence`，run 永久结束。当前只批准利用原请求已包含的 post-acquisition review 权限，对同一 retained header 做一次局部静态证据审查；不能只补 comment、默认建立 v9、新获取或采用源码。详见[v8 active 硬停止下一步决定](cp2-v8-hard-stop-next-step-decision-2026-09-06.md)。

2026-09-06 CP2 v8 局部配置路线更新：七个 occurrence 的后置静态审查已由 Leader 验收，人工可见范围合计 55 行。一个 fixed include 在获准查看的目标 directive 局部没有显示运行时操作但依赖未审；四个 `hotwords_file` occurrence 是公开字段、参数与成员初始化，属于 policy-relevant 配置面，相邻文档说明 buffer/file 选择。这 55 行局部证据没有证明实际文件访问、selector 执行、动态加载、调用可达或未来业务 API 暴露，也不能据此宣告无害；未查看的同文件行与跨文件实现均不作断言。当前获取／采用路线继续暂停；只批准 Leader 为单个 `online-recognizer.cc` 准备一份固定身份、单次、需 Product Lead 新授权的正文证据请求。准备本身不得读新 metadata/body，不建立 v9。详见[v8 局部配置证据后的路线决定](cp2-v8-local-configuration-route-decision-2026-09-06.md)。

2026-09-06 CP2 v8 热词消费端路线更新：经 Product Lead 新授权的单文件任务只取得 `online-recognizer.cc` 8,993 bytes，人工可见 28 行／1,237 bytes，并在精确依赖处正确停止。可见局部显示非空 `hotwords_file` 会进入 `FileExists` 校验，失败分支把路径值交给错误日志宏，`ToString` 也包含该参数；但没有执行代码，helper 内部行为、完整 selector 与业务可达性仍未验证。空值只绕过这个局部调用，正文没有 `hotwords_buf` exact token 也不能证明下层不支持 buffer。构造函数把 config 委派给未审 `OnlineRecognizerImpl::Create(config)`。当前路线继续暂停；只批准为精确 `online-recognizer-impl.h` 准备最后一次单文件新授权请求。若该文件仍声明／委派或需要第二依赖，热词逐文件补证立即终止，不自动追踪第三文件。详见[热词消费端证据后的路线决定](cp2-v8-hotwords-consumer-route-decision-2026-09-06.md)。

2026-09-06 CP2 热词证据链终止与替代路线更新：最后一个获授权的 `online-recognizer-impl.h` 任务只请求 1 次、取得 2,286 bytes，人工仅查看 3 行／129 bytes；可见 `Create(config)` 以分号结束，是声明而非函数体，任务依预设停止规则没有查看其他定义或第二来源。该结果只表示证据预算终止，不能推断整文件没有定义或 buffer-only 可行／不可行。当前 sherpa-onnx 热词逐文件链永久终止，既有 `block`／`manual_review` 制品仍不得采用。产品只批准最多 18 个官方页面、3–5 个非 sherpa-onnx 候选的离线中文 ASR 研究，不下载、不执行、不实现；个性词表实现为 `Deferred, not removed`，但 CP2 专名准确率及全部隐私、真机、性能、稳定性门槛不变。详见[热词证据链终止后的路线决定](cp2-hotwords-chain-termination-route-decision-2026-09-06.md)。

2026-09-06 CP2 替代 ASR intake 选择更新：已验收 R1 在 Vosk 与 ONNX Runtime Mobile + SenseVoiceSmall-onnx 中提供两个研究合格候选。产品经理只选择 Vosk 进入下一项官方身份准备，因为其中文、Android、离线、流式、较小模型和可重配词表证据更直接，供应链与集成面相对更窄。该选择不批准任何 Vosk 源码、runtime、模型、下载、扫描、构建、加载、运行或集成。下一单仅可读取最多 6 个官方公开页面／元数据端点，分别固定一个 Android runtime 与一个中文小模型的官方身份；制品获取与扫描、构建／加载／真机是三个独立权限阶段。详见[Vosk 安全 intake 候选选择决定](cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md)。

2026-09-06 接管收尾澄清：上述 Vosk 候选选择待当前 Leader `01a07655-fdfd-7683-aa57-a4895188d2ff` 验收及独立下发阶段 A，本轮没有执行 intake。阶段 A 的制品禁令不禁止合同明确允许的官方说明、README、LICENSE 与公开元数据；源码实现、模型、二进制等制品仍禁止取得。历史“技术验证与父亲单用户 Alpha”的方向表述不构成当前 Alpha 准入，当前以 CP2 未通过、CP3 与父亲 Alpha 未批准为准。

2026-09-06 Android 身份缺口范围更新：旧身份任务累计5/6（runtime3/3、model2/3）后仍为 `identity_insufficient`，模型目录已指认 `vosk-model-small-cn-0.22`，但项目tag不能替代Android固定坐标。产品只批准一个独立、最多10次请求的官方Maven Central元数据批次，涵盖来源确认、固定版本和POM声明；全批次由Leader下发，不逐页追加产品审批，不重置旧账本、不挪用模型预算。本轮不执行查询，POM声明不证明AAR内容、安全或源码可复现。全部隐私／专名90%／CP1恢复／CP2未过／CP3与Alpha未批准保持，见[Android身份缺口补证范围决定](cp2-vosk-android-identity-gap-decision-2026-09-06.md)。

2026-09-06 精确制品静态审查范围更新：Leader已验收Central元数据身份，仅确认Android固定坐标0.3.75／aar，不是制品采用。下一单范围为先AAR、后small-cn-0.22模型ZIP，各最多1次GET／64MiB／120秒，总2次／128MiB；用户精确授权与正式文档同步均为前置，本轮未取得制品。异常主页不信任、不访问；JNA5.18.1、未读.module及sidecar／源码不隐式取得。对象独立裁决，静态无高风险迹象不等于全供应链通过，整体adoption_gate仍blocked；阶段C、CP2、CP3与父亲Alpha未批准，全部隐私／专名90%／CP1恢复标准不变。详见[精确制品审查范围与待确认授权句](cp2-vosk-artifact-review-scope-decision-2026-09-06.md)。

2026-09-08 工具预检补救：原审查因现有扫描器缺共享归档预算与硬停止等保护真实BLOCKED，零GET、两对象not_acquired。仅批准单模块有界离线适配及合成测试（最多16小时），系统资源保护先证实，不可落实即停；工具完成不自动取得制品。原精确用户授权不重复索取，但保存规则或其他实际约束改变不由旧授权自动覆盖；旧隔离目录及报告不得覆盖。见[工具缺口范围决定](cp2-vosk-tool-gap-decision-2026-09-08.md)。所有隐私／专名90%／CP1恢复／采用blocked及Checkpoint保持。

2026-09-08 用户批准简化分阶段：最新[简化分阶段决定](cp2-vosk-simplified-staged-review-decision-2026-09-08.md)优先于前述严格范围和工具补齐路线，16小时adapter不下发。阶段1只原AAR0.3.75和small-cn-0.22；每对象最多2次尝试／每次2跳，64MiB每响应、256MiB全单网络正文，新attempt安全路径检查后可临时解包，文件／实际展开／时间有界，不再强求1GiB系统硬隔离、全内存解包或专门精确header限额。高压缩比仅warning、损坏／越界仍停止，已读CRC与未读Unknown分开。上述变化用户已批准，不重复审批；阶段2在集成前检查嵌套代码/native/依赖许可，阶段3按PRD做CP2真机与隐私／90%／性能验证。初查不等于安全或采用通过，旧0GET预检保留，CP1恢复、CP2未过、CP3与Alpha未批准均不变。

2026-09-08 阶段1已验收、阶段2范围：两个对象实收13472638B／43898754B，总2GET／57371392B，外层13＋20成员、选定文本715B已核CRC，未读内容仍Unknown；两包无外层LICENSE/NOTICE，不能由POM／目录声明推定许可闭合。下一单只用固定SHA现有包做classes.jar／Manifest／四native身份及arm64有限静态能力、模型文本来源与许可交叉表，不重取、不联网或获取JNA/.module。包内工作不被外部未知阻止，外部缺口继续阻止集成；采用门blocked，静态符号不代替动态证据，全部隐私／90%／CP1恢复／CP2/CP3/Alpha门槛保持。详见[阶段2包内静态审查范围](cp2-vosk-stage2-scope-decision-2026-09-08.md)。

2026-09-08 集成缺口归并：Leader已验收阶段2有界静态审查（63项manifest、23静态工具），两对象仍manual_review。内存数组入口／close/free／StorageService文件辅助路径和popen导入均为静态证据，不证明动态隐私、恶意执行或正确生命周期。下一唯一12次官方元数据批次核JNA5.18.1、Vosk0.3.75.module及主对象许可来源，不下载新二进制；popen调用输入边界在受控运行前须有限论证，PCM／准确率等留获准动态验证。缺build-ID等记录来源风险，不无限追源码；许可／依赖／能力关键缺口未关闭前采用blocked，隐私／90%／CP1与Checkpoint不变。见[集成缺口处置决定](cp2-vosk-integration-gaps-decision-2026-09-08.md)。

2026-09-08 用户继续两步：命令路径有限核查已验收，但Model/config/grammar到popen完整可达性仍Unknown；停止逐函数补证及JNA/module查询。下一dev单先同步再实现独立内存PCM会话契约及fake ASR合成测试，覆盖长度、90秒、状态／过期结果、异常close及私有副本清零，不引用真实Vosk/JNA或构建产品，不是CP3或实际语音功能完成。未来真实运行仍需依赖许可、路径／配置／日志能力准入及适当执行授权；隐私／90%／CP1与Checkpoint不变。见[离线下一步决定](cp2-offline-next-step-decision-2026-09-08.md)。

2026-09-09 公开中文语料测试更新：用户要求搜索公开数据用于测试。允许有明确来源与许可的公共语料作为隔离工程fixture保存，不改变私密录音只在内存、不落盘／上传／日志的硬边界。AISHELL-1／THCHS-30官方页面只建立整包入口，本次未核可信小test子集、未取得音频；下一单仅交付有实际合成验算产物的离线CER工具，同单同步文档，工具完成后不续发准备链。已验收的Vosk/JNA文本元数据不等于JNA AAR或真实native执行许可。公共CER不能替代父亲口音／专名90%、小米15性能隐私及CP1恢复，CP2未过、CP3／Alpha未批准。见[公开中文语料测试决定](cp2-public-chinese-corpus-test-decision-2026-09-09.md)。

2026-09-09 JNA范围确认更新：Leader明确询问单AAR提案后用户回复“继续工作”，仅确认固定JNA5.18.1 AAR取得／离线静态检查；新[正式决定](cp2-jna-aar-static-review-decision-2026-09-09.md)沿用原预算与简化解包流程，不开发新scanner。dev下一同单先同步四文档再取得，包不进入产品。CER已由Leader验收（20测试、21黄金用例、961短字符串比较），不是待开发任务，也不是真实识别成绩；公共小语料仍暂停，真实ASR／采用／CP2继续blocked，CP3和父亲Alpha未批准。旧阶段权限文字按当时状态保留。

2026-09-09 受控实验方案更新：JNA单AAR已取得并由Leader验收有限静态工作，包SHA已固定，仍manual_review。新[受控实验决定](cp2-controlled-asr-experiment-decision-2026-09-09.md)一次归并许可归属、固定加载、JNA temp/log/FFI、Vosk命令输入和PCM生命周期风险；拟定一次性Android arm64隔离环境中一个1秒内存静音会话，但环境/离线构建/观测和Owner风险处置尚未核定，执行PAUSE。用户只确认制定方案，不授权安装或加载。静音不是中文识别测试，CER/PCM合成工具通过不代替真实CP2；唯一解阻动作是现有环境只读核对，不新建工具或继续源码链。

2026-09-10 笔记产品优先更新：用户明确要求真实记录、本地自动标题、小米笔记式默认首页及Obsidian式可切换关系图谱。[笔记首页正式决定](notes-home-redesign-decision-2026-09-10.md)批准CP3下NOTES-L1/L2/L3限定文字先行例外，覆盖必要本地持久化/草稿、标题所有权、真实搜索、首页编辑器及显式关系；不再由ASR准备阻塞这部分实现。CP1人工延期、CP2未过、CP3整体未过与Alpha未批准保持；其余CP3扩展或整体通过前仍须恢复CP1并审计CP2。下一单直接同步四文档并实现L1，不另开准备链。安装APK身份仍未核，假录音/保存/搜索不得继续出现在可用产品路径。

2026-09-11 小米笔记式全量UI范围更新：用户要求覆盖页面跳转、颜色、layout、滑动方式和CRUD。[正式决定](notes-home-xiaomi-full-scope-decision-2026-09-11.md)将其固化为UI-L1文字工作流、UI-L2默认笔记首页/搜索/筛选、UI-L3双视图显式关系图谱，复用已验收NOTES L1-L3逻辑，不复制品牌资产或截图私人内容。下一只允许NOTES-UI-DEVICE-001做一次真机UI/交互验收；设备未验证前不声称视觉、触控、主题、TalkBack或父亲可用性通过。CP3整体、CP1人工、CP2/ASR、Alpha门槛保持。

## 品牌名称

- 中文名称：`思`
- 英文名称：`think`，默认保持小写
- 内部项目代号：`personal-thought-archive`
- 产品类别描述：个人思想档案

面向用户的页面、原型和未来应用商店草稿统一使用「思」或 `think`；「思想档案」只用于解释产品是什么。命名依据见[正式命名决策](naming-decision-2026-09-04.md)。

## 1. 产品定义

为习惯随手记录观点、佳句和灵感，但不擅长复杂智能手机操作的人，提供一个以语音为主、离线优先的个人思想档案：

- 在三步内完成一条想法的录入与归类；
- 在三步内重新找到任何一条历史记录；
- 把过去散落在日历中的记录一次性迁入并形成初始模块；
- 通过可靠提醒让旧想法在合适时刻重新出现；
- 长期形成可搜索、可整理、可导出的个人思想档案。

这里的产品定义不是「导入日历并分类」。导入只是迁移前置条件；真正价值是以后每一次记录和找回都足够简单。

## 2. 问题

核心用户已经证明自己愿意长期记录：他每天阅读大量新闻、名人观点与新知识，会把当天的想法、标题或佳句放进手机日历，并设置每天某个时刻的提醒。

现有做法的问题不是“不愿意写”，而是：

1. 日历同时承担日程、笔记和提醒，内容越来越杂；
2. 记录数量变多后，重新打开通知、日程或旧记录的操作成本很高；
3. 内容没有稳定的主题结构，知道自己写过，却难以找回；
4. 用户愿意分享和积累，但复杂编辑、批量整理与多层导航不适合他；
5. 云端语音服务受网络影响，也会让原始语音与隐私暴露面变大。

## 3. 目标用户

### 核心用户

- 50 岁以上或不擅长复杂智能手机操作；
- 有稳定记录、收藏观点、佳句或个人思考的习惯；
- 更习惯像微信一样按住说话，而不是长篇打字；
- 已经使用日历、备忘录或聊天窗口作为替代工具；
- 重视内容重新出现和长期保留，而非复杂知识管理方法。

### 次级用户

- 帮助核心用户首次导入、确认模块和设置权限的家人；
- 未来希望整理个人观点、写作素材或决策记录的普通中文用户。

次级用户不能取代核心用户完成日常记录。若产品长期依赖家人代操作，即验证失败。

## 4. 分发与价值捕获假设

第一阶段不验证市场分发与付费，只验证一个真实核心用户能否持续使用。

- 初始分发：家人协助安装、下载模型、授权日历与麦克风；
- 使用触发：看到一句话或产生想法时立刻说；收到提醒时重新阅读；
- 潜在价值：减少记录摩擦、提高找回率、把多年思考变成个人档案；
- 潜在收费方向仍是假设：一次性买断、家庭套餐或加密备份订阅；在 V3 前不做定价投入。

## 5. 创始人时间预算

第一轮上限为 4–6 周的业余时间或约 80–120 小时，只做到父亲单用户 Alpha：

- 20%：真实设备、语音和日历数据验证；
- 25%：可点击原型与核心页面；
- 30%：本地转写、录入、存储与搜索；
- 15%：日历导入与 AI 分类；
- 10%：提醒、隐私检查和 Alpha 修复。

若 CP2 本地语音门禁不通过，不进入完整 App 开发。

## 6. 产品原则

1. **语音优先，不是语音附加。** 首页最显眼的控件必须是按住说话。
2. **本地先保存。** 网络不好时仍可转写、编辑、保存和搜索；AI 标题与分类可稍后补做。
3. **AI 给建议，用户做确认。** AI 不静默改变正文，不擅自拆分思想，也不强迫用户理解置信度。
4. **三步是硬约束。** 新功能不能把正常录入和找回路径推到第四步。
5. **大字、少选项、可撤销。** 一个页面只有一个明显主动作；危险操作必须可恢复或二次确认。
6. **迁移不破坏原资料。** 日历只读，任何导入结果都能回溯来源；不删除或修改原日历。
7. **音频最小化。** 用户原始录音只在内存中用于本地转写，转写完成或取消后立即丢弃，不写磁盘、不上传；公开许可工程fixture按14.8隔离管理，不属于用户录音保存功能。

## 7. 目标

### P0 目标

1. 父亲可以用按住说话完成一条新记录；
2. 本地模型把中文语音转成可修改正文；
3. 云端 AI 根据文字生成标题并推荐一个模块；
4. 用户确认或修改模块后保存，正常路径不超过三步；
5. 历史记录可通过搜索在三步内打开；
6. 从一个 Android 本机日历只读导入旧内容，并给出初始模块建议；
7. 支持为记录创建提醒，通知点击后直接打开正文；
8. 所有记录在无网状态仍可读取、编辑和搜索。
9. 用户或家人可维护简单的个性词典，修正常见人名、地名、专有词与英文缩写。

### P1 目标

- 模块新增、重命名、合并；
- 导出 JSON、Markdown 或 PDF；
- Outlook 未同步至本机时，通过 Microsoft Graph 导入；
- 加密备份与换机恢复。

## 8. 非目标

- 第一版不做 iOS、桌面端或完整网页编辑器；
- 不做多人共同编辑、公开社区、点赞或算法信息流；
- 不自动朗读提醒内容，是否需要“提醒后直接听”留待验证；
- 不保存原始录音，不做录音暂停或音频回放；
- 不自动把一段话拆成多条记录；
- 不让 AI 改写正文或补充用户没有说过的事实；
- 不在第一版实现复杂标签、双向链接、知识图谱或 Markdown 编辑器；
- 不在第一版建立账号、跨设备实时同步和付费系统；
- 不在未经确认时修改或删除用户原日历事件。

## 9. 证据

| 来源 | 支持的判断 | 置信度 |
| --- | --- | --- |
| [SRC-01](../../raw/SRC-20260904-personal-thought-archive-01.md) | 核心用户长期用日历记录并提醒；产品交互与隐私约束来自真实需求 | High（单用户） |
| [SRC-02](../../raw/SRC-20260904-personal-thought-archive-02.md) | Android 官方支持单 Activity、分层、持久模型与离线单一事实来源 | High |
| [SRC-03](../../raw/SRC-20260904-personal-thought-archive-03.md) | `sherpa-onnx` 有 Android、本地运行与中文模型路径 | High（可行性）；性能待测 |
| [SRC-04](../../raw/SRC-20260904-personal-thought-archive-04.md) | Android 可经授权读取本机多个账户来源的日历事件与提醒 | High |
| [SRC-05](../../raw/SRC-20260904-personal-thought-archive-05.md) | 精确提醒受权限与电量政策约束，应先验证是否必须精确 | High |
| [SRC-06](../../raw/SRC-20260904-personal-thought-archive-06.md) | Outlook 可在本机同步缺失时用 Microsoft Graph 作为第二导入路径 | High（API 能力）；集成成本待测 |
| [SRC-07](../../raw/SRC-20260904-personal-thought-archive-07.md) | Android 官方绿地模板可作为 Compose/Room/Hilt 工程起点 | High |
| [SRC-08](../../raw/SRC-20260904-personal-thought-archive-08.md) | 极简、自动保存的笔记交互有开源参考；GPL 代码有复用边界 | Medium |
| [SRC-09](../../raw/SRC-20260904-personal-thought-archive-09.md) | 离线优先、全文搜索、导入导出的完整笔记形态有参考；AGPL 有复用边界 | Medium |

### 当前尚未验证

- 父亲是否愿意从日历迁移后持续改用新 App；
- 哪一个 `sherpa-onnx` 中文模型最适合他的口音、手机和专有词；
- AI 生成的模块是否比简单搜索更有帮助；
- 提醒必须精确到分钟，还是在时间窗口内出现即可；
- 除父亲外是否有足够多相似用户，是否愿意付费。

## 10. 核心交互与“步”定义

### 10.1 新增记录：三步

1. 打开 App；
2. 按住首页语音按钮说话，松手结束；
3. 查看转写正文与 AI 推荐模块，点击「存入此模块」。

按住、持续说话和松手视为同一个连续动作。AI 转写与分析是系统状态，不增加用户步骤。正常路径不能再要求用户填写标题、选择提醒或进入编辑页。

如果转写或分类不正确，用户可以修正；这是异常纠错分支，不计入三步成功目标，但要单独记录纠错成本。

上述语音三步为未来ASR门禁通过后的目标，当前不模拟可用。文字先行提供首页→新增文字并编辑→确认保存的最短路径，输入本身为持续编辑动作；标题/分类不作为必填额外步骤。真实ASR未准入时语音入口明确暂不可用，不计时、不显示假波形或合成转写。

### 10.2 找回记录：三步

1. 打开 App；
2. 点击「搜索」并输入或说出关键词；
3. 点击结果，直接打开完整记录。

搜索结果页必须直接显示标题、命中片段、模块与日期，不能再要求先进入模块。

### 10.3 提醒回看：一步

1. 点击系统通知，直接打开对应记录正文。

通知本身显示标题和正文首行。是否在通知中朗读或完整展示内容，暂不承诺。

## 11. 信息架构

底部主导航只保留三个入口：

- **首页**：记录与最近内容；
- **档案**：模块与全部记录；
- **提醒**：今天、即将到来与已完成提醒。

「搜索」放在所有主页面顶部固定位置；「设置」放在首页右上角。录音结果、记录详情与导入流程使用全屏页面，不增加底部导航项。

## 12. 页面与内容展示

### P01｜首次启动与权限

目的：让家人一次性协助设置，之后父亲不再面对复杂配置。

展示：

- 一句话说明：「说下想法，自动归类，以后找得到」；
- 三张能力卡：本地语音、日历迁移、提醒；
- 权限逐项解释与按钮：麦克风、日历、通知；
- 「稍后导入日历」与「现在开始」；
- 隐私摘要：录音不保存；只有文字会在用户允许后发给云端 AI。

规则：权限必须按使用时机逐项请求，不在第一屏一次弹出全部系统弹窗。

### P02｜选择日历与导入范围

展示：

- 本机可读取的日历列表：名称、账户来源、事件数量估算；
- 只允许选择一个日历；
- 日期范围：全部、近一年、自定义；
- 可导入字段预览：标题、描述、日期、原提醒；
- 明确提示「只读取，不会修改原日历」；
- 分析授权说明：「选中的标题和正文会发送给云端 AI 进行初始分类；账户名称、参与者和地点不会发送」；
- 主按钮「扫描并分析」。

默认先走 Android Calendar Provider。若 Outlook 日历没有同步到系统日历，只展示说明，不在 P0 强迫用户完成 Microsoft 登录。

### P03｜导入分析与初始模块确认

导入结果分三组：

1. **建议导入**：像观点、佳句、灵感或自我提醒；
2. **待确认**：AI 不能确定是想法还是普通日程；
3. **建议忽略**：会议、航班、生日、节假日等明显日程。

页面先展示总数，再展示 AI 建议的 5–8 个初始模块。每个模块显示名称、记录数与 2–3 条代表样例。支持：

- 重命名模块；
- 合并两个模块；
- 将某批记录移入其他模块；
- 查看「待确认」；
- 批量确认导入。

进入「待确认」的条件：

- 分类置信不足或前两类接近；
- 内容过短、只有模糊标题或没有可理解正文；
- 一条记录明显包含多个主题；
- AI 建议创建新模块；
- 疑似重复、周期日程或同一条内容多次提醒；
- 结构更像普通日程，但正文又包含观点。

AI 置信度只用于系统分流，不直接显示百分比给核心用户。所有阈值在 CP4 根据人工标注调整。

### P04｜首页／快速记录

默认笔记视图：适度大标题、顶部真实搜索、横向真实分类筛选、按updatedAt倒序的笔记卡片及明确新增文字动作。两列卡片显示真实标题/正文预览/日期，窄屏或大字体自动一列；正文基准18sp、关键触控56dp、系统明暗模式、高对比，不嵌套装饰面板。空库不填demo，草稿与正式记录区分。L1先最小真实列表，L2完成视觉与搜索。

L3启用笔记/关系图谱切换，共用记录id与数据源；冷启动默认笔记，图谱不成为找回的必经步骤。尚未实现的搜索或图谱入口禁用/隐藏，不提供合成结果。语音入口可发现但在真实backend未准入时明确不可用，禁止假引擎加载、计时、震动和波形；中心巨大录音按钮不再主导默认首页。

图谱只显示用户显式建立的真实笔记关系；同分类不自动连边，保留孤立/单节点/空态，支持选择打开、平移缩放/重置/聚焦与TalkBack关系列表回退。规模上限200节点/400边，超限说明可视/总数并提供筛选，详细关系交互见笔记首页决定。

### P05｜录音状态层

仅真实ASR准入并有实际采集时启用以下状态；文字先行不展示模拟录音层。

按住后覆盖首页但保留上下文，展示：

- 实时波形或音量条；
- 计时 `00:00 / 01:30`；
- 「松开结束」；
- 手指左滑后变为红色「松开取消」；
- 到 80 秒提示剩余 10 秒；90 秒自动结束并开始转写。

不支持暂停。取消、权限丢失或录音失败时不创建空记录。

### P06｜转写、标题与分类确认

文字先行编辑器使用全宽正文、可编辑标题、日期与真实保存状态；默认空草稿，无AI模块必选步骤。下列转写/AI推荐布局只在相应功能实际获准并完成后启用，不用合成内容代替。

展示：

- 可直接编辑的转写正文；
- 自动标题；
- `AI 推荐：模块名` 的大尺寸选择框；
- 主按钮「存入此模块」；
- 次动作「换一个模块」；
- 次动作「继续按住补充」，新转写追加到正文末尾；
- 网络不好时显示「已保存在本机，联网后补充标题与分类」。

标题规则：

1. 持久化titleMode=AUTO|MANUAL；AUTO取正文第一非空句或前24个Unicode码点，超限加省略号，正文变化实时更新；具体断句/规范见笔记首页决定，正文原文不改。
2. 用户非空标题编辑为MANUAL，后续改正文/重启/AI均不得覆盖；清空手动标题回AUTO，提供恢复自动命令。导入原有标题按MANUAL保留。
3. 标题/正文/mode同一revision原子保存，空正文不可创建正式记录，占位文案不入库；保存成功只在事务成功后显示，错误保留草稿可重试。
4. 自动标题完全本地、不依赖云AI；未来AI只能给用户可拒绝的建议，不能覆盖手动标题或正文。

多想法规则：整段作为一条长记录保存，不自动拆分；AI 先根据全文分类，无法判断时以第一个想法为主，并标记为待确认。

### P07｜搜索

展示：

- 进入即聚焦的搜索框；
- 文字输入为 P0，语音搜索为 P1；
- 最近搜索与常用模块快捷项；
- 结果卡显示标题、命中片段、模块、记录日期和提醒状态；
- 输入时即时更新，不需要额外点击「搜索」。

搜索范围：用户标题、AI 标题、正文、模块名、导入来源标题与日期。P0 使用本机全文索引，不依赖云端语义搜索。

### P08｜档案／模块列表

展示：

- 初始模块卡片：模块名、记录数、最近一条摘要；
- 「待确认」固定在顶部，仅在有内容时出现；
- 「全部记录」固定入口；
- 新增模块；
- 长按或更多菜单中提供重命名、排序、合并，不直接删除含记录模块。

模块数量不是预先固定。导入后 AI 建议 5–8 个主模块，超过 10 个时要求合并建议，避免首页变成复杂目录。

### P09｜模块详情

展示：

- 模块标题、记录数；
- 按最近、最早或提醒时间排序；
- 每条记录显示标题、正文首行和日期；
- 搜索只筛选当前模块；
- 右下角保留按住说话按钮，录入后默认推荐当前模块，但仍需确认。

### P10｜记录详情与编辑

展示：

- 标题、完整正文、模块、创建日期；
- 来源：语音新建／日历导入；
- 日历导入记录可查看原事件标题和原日期；
- 编辑正文、移动模块、创建提醒；
- 删除进入 30 天回收站；
- 不展示不存在的原始音频播放器。

### P11｜提醒中心与提醒编辑

提醒中心展示：今天、未来、已完成。提醒编辑支持：

- 日期和时间；
- 单次、每天、每周；
- 通知预览；
- 关闭或删除提醒；
- P1：稍后提醒。

P0 默认使用非精确提醒；CP7 若证明用户必须在具体分钟收到，才申请精确闹钟权限。设备重启、权限撤销与省电模式必须有可见状态。

### P12｜设置、个性词典与导出

展示：

- 本地语音模型状态、版本、占用空间；
- 个性词典：添加「这个词应该写成……」；
- 云端 AI 开关与隐私说明；
- 日历导入记录与重新导入；
- 字号：标准／大／特大；
- 导出全部档案；
- 回收站；
- 清除本机数据。

清除本机数据必须要求明确二次确认，并优先引导先导出。

## 13. 功能需求

### FR-01｜微信式按住说话｜P0

- 首页直接录音，不先打开编辑器；
- 按下开始、松手结束、左滑取消；
- 单段最长 90 秒，不支持暂停；
- 第一段转写完成后可再次按住，结果追加到正文末尾；
- 每段独立失败、重试或取消，不能覆盖已成功文字；
- 录音过程中阻止屏幕自动熄灭；来电、音频焦点丢失或权限被撤销时安全结束并提示。

### FR-02｜本地中文转写｜P0

- 使用通过 CP2 独立安全与真机门禁的本地离线中文 ASR runtime 封装为 `AsrEngine`；Vosk已完成有限制品／静态／元数据验收，但尚未获准采用或真实运行，sherpa-onnx 热词逐文件链已终止且既有制品不得采用；
- 用户原始音频只进入内存缓冲，不写文件、不上传；未来公开fixture测试也通过内存PCM入口，不允许引擎额外保存音频；
- 支持简体中文为主，兼顾数字、英文缩写、人名与地名；
- 转写后正文可直接修改；
- 识别结束、取消或异常后立即释放音频缓冲；
- 模型必须经过 CP2 后冻结，不能只凭公开 Demo 选择。

### FR-03｜个性词典｜P0

状态：`Deferred, not removed — implementation route unresolved`。需求和 CP2 专名准确率门槛保留，但在替代 ASR 候选研究与后续独立门禁前不实现；该延期不解锁核心 ASR 或 CP2。

- 用户或家人可新增特定词与正确写法；
- 词典同时用于转写后替换建议与云端标题/分类提示；
- 自动替换必须可撤销；
- 不把全部词典默认上传，只有本次处理相关词可进入 AI 请求。

### FR-04｜AI 标题与模块 Skill｜P0

- 只发送转写文字、现有模块的 `id + name` 和必要语言信息；
- 不发送原始音频、全部档案或日历账户信息；
- 返回严格结构化结果；
- 请求失败、超时或无网时，记录先以本地暂存标题保存到「待确认」；
- AI 不修改正文，不自动拆分记录，不静默创建模块；
- 每次建议都由用户确认，后续用确认结果评估模型，而不是自动训练。

建议契约：

```json
{
  "requestId": "uuid",
  "title": "从文字提取或生成的短标题",
  "suggestedModuleId": "existing-module-id-or-null",
  "suggestedNewModuleName": "string-or-null",
  "alternatives": ["module-id"],
  "needsReview": false,
  "reasonCode": "TOPIC_MATCH"
}
```

`reasonCode` 仅用于调试和评估，不显示给核心用户。服务端不得记录正文到普通应用日志。

### FR-05｜记录保存｜P0

- 本机数据库是记录、模块和提醒的单一事实来源；
- 用户点击确认后才成为正式记录；
- 网络 AI 状态与正文保存状态分离，AI 失败不能丢正文；
- 每个保存动作有唯一请求编号，重复点击不能生成重复记录；
- App 被系统杀死或旋转屏幕后，已转写草稿可恢复。

文字先行L1使用真实存储：空初始库、不导入合成常量；已有数据非破坏升级。输入空闲500ms提交独立草稿，旋转不丢，已提交草稿/正式保存重启可恢复，提交前最后500ms不虚称已保存。更新失败保留旧正式版本；重复保存不重复创建；正文/标题/mode原子提交。不以假成功或只存在内存的列表作为持久化验收。

### FR-06｜搜索与找回｜P0

- 使用本机全文索引搜索标题与正文；
- 结果应在输入后 300ms 内开始更新，1000 条记录内 P95 小于 500ms；
- 结果直接打开详情，不能多一层中间页；
- 支持无网搜索；
- 没有结果时建议查看全部记录或模块，不自动伪造语义匹配。

NOTES-L2搜索真实标题/正文，中文连续子串及空白多词AND、拉丁大小写不敏感；完整标题相等→标题包含→正文包含，再updatedAt/id稳定排序。保存/编辑/删除与索引一致，显示命中片段，FTS无法支持中文子串时使用受限本地回退。首版无模糊纠错/语义推荐；L1未接真搜索时禁用，不保留固定合成结果。

### FR-06a｜显式关系与双视图｜NOTES-L3

笔记与图谱共用正式记录集合；用户在详情“关联笔记”搜索选择其他真实笔记并确认，创建唯一无向关系，两端可见来源“用户建立”。拒绝自环/重复，确认解除只删关系；已有删笔记操作须事务清理其边。图谱孤立节点也显示，连线不得来自装饰或同分类推测；选择节点后明确打开同id记录，提供缩放/重置/聚焦、规模提示和完整可访问关系列表。未实现前不得假装存在关系或图谱功能。

### FR-07｜日历只读导入｜P0

- 请求 `READ_CALENDAR`，不请求 `WRITE_CALENDAR`；
- 一次只导入一个用户选择的日历；
- 保存来源账户类型、日历 ID、事件 ID、原始标题、描述、日期与提醒信息；
- 本地先排除空事件和明显系统节假日；只有用户确认分析后，才把候选事件的文字与不透明 ID 批量发送给云端 AI；
- 识别重复与周期事件，默认不把每次重复提醒都变成一条思想；
- 导入可中断和继续；重复导入必须幂等；
- 不修改、删除或标记原事件；
- 若 Outlook 已同步到本机，优先经 Calendar Provider 读取；否则把 Graph 集成延后到 P1。

### FR-08｜初始模块生成｜P0

- AI 基于建议导入的历史文字生成 5–8 个模块；
- 模块命名使用用户能理解的日常词，不用抽象知识管理术语；
- 每个模块必须展示代表样例；
- 用户或家人批量确认后才正式写入档案；
- 未确认项进入「待确认」，普通日程留在导入报告但默认不进入档案；
- 后续可新增、重命名、排序与合并模块。

### FR-09｜提醒｜P0

- 用户可从记录详情创建单次或重复提醒；
- 通知展示标题与正文首行，点击直接打开记录；
- 无账号、无网络时仍能提醒；
- 设备重启后重新安排；
- 权限被关闭时在提醒中心明确显示；
- 是否要求精确到分钟由 CP7 决定，未验证前不默认申请高敏感权限。

### FR-10｜导出与删除｜P1

- 可导出全部记录、模块、提醒和来源映射；
- 至少提供人可读 Markdown 与机器可读 JSON；
- 删除记录先进入 30 天回收站；
- 清除全部数据前提示导出；
- 不声称“永久保存”，除非备份、恢复与迁移完成验证。

## 14. 初步技术架构

### 14.1 端与云边界

```text
Android App
├─ 麦克风 PCM（仅内存）
├─ 待通过 CP2 的本地离线中文 ASR
├─ Room：正文、模块、提醒、导入映射、全文索引
├─ Android Calendar Provider：只读导入
├─ AlarmManager / WorkManager + Notification：本地提醒
└─ HTTPS：只发送文字与模块候选
          ↓
   AI Skill Gateway
   ├─ 身份/频率限制
   ├─ 标题与分类结构化输出
   ├─ 超时、重试、Schema 校验
   └─ 可替换的云端模型提供商
```

本地数据库是唯一正式档案；云端 AI 是可失败、可替换的建议服务。AI 服务故障时，用户仍能记录、编辑、保存、搜索和提醒。

### 14.2 Android 客户端

| 层 | 初步选型 | 责任 |
| --- | --- | --- |
| UI | Kotlin、Jetpack Compose、Material 3 | 大字低摩擦页面、录音状态、搜索与导入确认 |
| 导航 | 单 Activity + Navigation Compose | 三个主入口、详情与导入全屏流程、通知 deep link |
| 状态 | ViewModel + StateFlow + 单向数据流 | 屏幕状态、草稿恢复、系统事件 |
| Domain | Use Cases | `CaptureThought`、`ImportCalendar`、`ClassifyThought`、`ScheduleReminder`、`SearchThoughts` |
| Data | Repository | 协调本地数据库、系统日历、本地 ASR 与云端 AI |
| 本地数据 | Room + FTS；DataStore | 记录、模块、提醒、导入批次、全文搜索；设置与词典 |
| 异步 | Kotlin Coroutines；WorkManager | AI 延迟分类、导入批处理、提醒重建、未来备份 |
| 依赖注入 | Hilt | 替换真实/测试 ASR、AI、日历与提醒实现 |
| 语音 | 待通过门禁的 Android 本地离线 ASR runtime | 本地中文转写；Vosk 只获批进入官方身份准备，runtime 与模型仍须分别通过 CP2 安全、隐私和目标设备门禁 |
| 系统集成 | Calendar Provider、AlarmManager、Notification | 只读日历、提醒、通知直达记录 |
| 测试 | JUnit、Compose UI Test、Macrobenchmark | 业务规则、三步流程、无障碍、启动与搜索性能 |

第一版从 Android 官方 `architecture-templates` 的单模块 `base` 起步，按 feature package 分区；只有当构建时间、团队人数或独立交付需要出现后才拆 Gradle 多模块，避免样机阶段过度设计。[Android 官方模板](https://github.com/android/architecture-templates)提供可直接使用的 Apache-2.0 脚手架；[Now in Android](https://github.com/android/nowinandroid)用于研究更完整的离线优先与模块化做法；[Compose Samples](https://github.com/android/compose-samples)中的 Jetchat 可参考文字输入与 UI 状态，但不照搬聊天产品结构。

### 14.3 建议代码边界

```text
app/
core/
  model/ database/ designsystem/ common/
feature/
  onboarding/ capture/ search/ archive/ importcalendar/ reminder/ settings/
data/
  thought/ module/ reminder/ calendar/ ai/
asr/
  api/ runtime/
```

样机可先保留在一个 Gradle module 中，但包边界和接口从第一天建立。`asr/api` 只暴露开始、输入音频、结束、取消与结果状态，使未来替换模型时不改 UI。

### 14.4 本地数据模型

| 对象 | 核心字段 | 说明 |
| --- | --- | --- |
| `ThoughtRecord` | id、title、titleMode、body、moduleId、createdAt、updatedAt、revision、sourceType、reviewStatus | 正式记录；AUTO/MANUAL所有权持久化，正文不被AI覆盖 |
| `NoteDraft` | draftId、recordId、title、titleMode、body、revision、savedAt | 独立草稿；未提交修改不冒充正式保存 |
| `NoteRelation` | minId、maxId、createdAt、source=user_explicit | L3唯一无向边，端点外键，拒绝自环，删笔记清边 |
| `Module` | id、name、sortOrder、createdBy、archivedAt | 用户模块；合并时保留旧 ID 映射 |
| `Reminder` | id、thoughtId、triggerAt、repeatRule、systemId、status | 本地提醒与系统闹钟映射 |
| `ImportBatch` | id、calendarId、range、status、counts | 一次导入的进度与审计 |
| `ImportSource` | thoughtId、eventId、originalTitle、originalBody、originalTime、fingerprint | 可追溯与幂等导入 |
| `VocabularyTerm` | id、spokenForm、writtenForm、enabled | 个性词典 |
| `AiJob` | id、thoughtDraftId、requestHash、status、result、attempts | 离线重试与结构化响应审计 |

标题和正文建立 Room FTS 索引。日历事件生成稳定指纹，避免同一个事件重复导入。

### 14.5 AI Skill 服务

云端层先做一个薄网关，不把具体模型 SDK写进 App：

- 接收文字、当前模块列表和客户端请求编号；
- 调用可替换的 AI 提供商；
- 验证 JSON Schema，拒绝多余字段或正文改写；
- 超时后返回可重试状态；
- 默认关闭正文日志，错误日志只保留哈希、状态码、延迟和模型版本；
- 不用客户端内置长期 API Key；
- 未来若完全本地模型达到要求，可替换此网关而不改产品流程。

云端供应商、托管平台与模型在 CP5 后决定。PRD 不先绑定某一家。

### 14.6 日历导入路线

1. P0：Android Calendar Provider，验证父亲设备能否看到目标日历；
2. 若 Outlook 日历已同步到系统层，仍走 P0；
3. 只有目标日历不可见时，P1 才加入 Microsoft Graph OAuth；
4. 所有路线都写入统一 `ImportSource`，不把账户提供商泄漏到核心 UI。

### 14.7 提醒路线

- 普通提醒：非精确 `AlarmManager`，减少权限与耗电影响；
- 稍后分类、批处理：`WorkManager`，不承诺精确时间；
- 精确提醒：仅 CP7 验证必要后申请 `SCHEDULE_EXACT_ALARM`，并处理权限撤销和重启重排；
- 通知点击通过 deep link 直达 `ThoughtRecord`。

### 14.8 隐私与安全

- 私密用户录音数据不得写入磁盘、缓存、崩溃报告、日志、网络请求或备份；
- 经来源／许可核定并在取得合同中固定的公开语料可在工程fixture目录保存原音频、原标注及归属材料；与产品数据、麦克风录音、云同步和用户备份隔离，不随APK发布、不向第三方上传。仅标记public或匿名化不构成许可核定，用户录音不得套用此例外；
- AI 请求使用 TLS；新记录只发送最小文字和模块名，初始导入只发送用户已授权日历中的候选文字与不透明 ID；
- 任何分析 SDK不得收集正文、搜索词和日历内容；
- 数据库加密是否 P0 取决于设备威胁模型，至少先依赖 Android 应用沙箱并禁用明文备份；
- 导出文件由用户主动触发并显示保存位置；
- 崩溃日志、截图测试和调试日志必须使用合成数据；
- 上架前完成数据安全表、隐私政策和第三方模型许可证核查。

## 15. 开源模板与参考项目

| 项目 | 用途 | 建议 | 许可证边界 |
| --- | --- | --- | --- |
| [Android Architecture Templates](https://github.com/android/architecture-templates) | 新项目脚手架 | **可作为代码起点**；先用单模块 base | Apache-2.0，保留许可与声明 |
| [Android Architecture Samples](https://github.com/android/architecture-samples) | Repository、测试与分层参考 | 遇到架构问题时按需借鉴 | Apache-2.0 |
| [Now in Android](https://github.com/android/nowinandroid) | 完整 Compose、离线优先、性能测试 | 参考做法，不直接复制整套复杂度 | Apache-2.0 |
| [Compose Samples / Jetchat](https://github.com/android/compose-samples) | 文字输入、UI 状态与 Compose 测试 | 参考录入确认页交互 | Apache-2.0 |
| [Vosk](https://github.com/alphacep/vosk-api) | Android 本地离线中文 ASR 候选 | **仅用于官方身份 intake 准备**；未批准下载、采用或集成 | runtime 与中文模型须分别固定身份、来源、许可证并通过 CP2 |
| [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | 历史 Android 本地 ASR 研究对象 | 当前热词逐文件链已终止，不作为实现起点 | 既有 `block`／`manual_review` 制品仍不得采用 |
| [Fossify Notes](https://github.com/FossifyOrg/Notes) | 极简记录、自动保存、桌面小组件 | 只做体验研究 | GPL-3.0；闭源分发前不复制代码 |
| [Joplin](https://github.com/laurent22/joplin) | 离线优先、全文搜索、导入导出 | 只研究信息架构和边界 | 默认 AGPL-3.0-or-later；逐目录核查 |

GitHub Star 不是需求证据，也不作为选型标准。工程起点优先官方 Android 模板；笔记产品仓库只帮助理解成熟交互和数据能力。

## 16. 非功能需求

### 可靠性

- 已确认正文不得因 AI、网络、应用重启或权限变化丢失；
- 导入和保存幂等；
- 数据库迁移有自动测试；
- App 进程被杀后，提醒仍可触发，重启后可恢复；
- 无法分类时进入「待确认」，不能阻止保存。

### 性能

- 冷启动至首页可操作：目标手机 P95 小于 2.5 秒；
- 首页按下录音至收到反馈：小于 150ms；
- 常见 30 秒以内语音，松手后转写完成 P95 目标小于 5 秒，最终门槛以 CP2 基准调整；
- 90 秒录音不得崩溃、OOM 或写入临时音频文件；
- 1000 条记录全文搜索 P95 小于 500ms。

### 可用性与无障碍

- 核心字号不小于 18sp，可切换特大字号；
- 主要点击目标不小于 56dp；
- 色彩不是唯一状态提示；
- TalkBack 能读出按钮状态、录音剩余时间和分类选择；
- 左滑取消之外同时提供可见取消区域；
- 关键错误使用人话和明确下一步，不展示模型或网络堆栈。

### 兼容性

- `minSdk` 在 CP0 查看父亲手机后冻结，默认建议 Android 10/API 29；
- `targetSdk` 使用开发时 Google Play 要求的最新稳定版本；
- 首发只保证父亲目标手机和至少一台中档 Android 对照机。

## 17. 验收标准

### 三步录入

- [ ] 打开 App 后无需再进入编辑页面即可按住说话；
- [ ] 松手后自动本地转写，不上传音频；
- [ ] 用户在同一确认页看到正文、标题和推荐模块；
- [ ] 点击一次主按钮即可正式保存；
- [ ] 正常路径从打开 App 到保存不超过三步；
- [ ] 可再次按住补充，文字追加而不覆盖；
- [ ] 左滑取消和 90 秒自动结束均正确工作。

### 三步找回

- [ ] 任一主页面都有明显搜索入口；
- [ ] 输入时直接显示结果，无需额外提交；
- [ ] 结果卡包含标题、命中片段、模块和日期；
- [ ] 点击结果直接打开正文；
- [ ] 无网时仍可完成。

### 导入

- [ ] 只申请日历读取权限；
- [ ] 用户只能明确选择一个日历和日期范围；
- [ ] 原日历零修改；
- [ ] 同一事件重复导入不会产生重复记录；
- [ ] 建议导入、待确认和建议忽略可追溯；
- [ ] 初始模块有名称、数量和代表样例；
- [ ] 批量确认后仍可移动与合并。

### AI 与隐私

- [ ] 网络抓包中不存在原始音频；
- [ ] 云端请求不包含全部档案、日历账户或无关记录；
- [ ] AI 失败时正文已经本地保存；
- [ ] AI 输出不改变正文；
- [ ] Schema 不合法时进入安全回退而非保存错误字段；
- [ ] 日志与崩溃报告不含正文。

### 提醒

- [ ] 通知点击直接打开对应记录；
- [ ] App 被划掉、设备重启后提醒仍按设计恢复；
- [ ] 权限关闭时用户看得到问题与修复入口；
- [ ] 不需要精确权限时不申请；
- [ ] 重复提醒不会重复创建记录。

## 18. 指标与事件

### 核心结果指标

- 录入任务成功率：无需帮助完成保存的任务数 / 尝试数；
- 三步达成率：正常录入和找回在目标步数内完成的比例；
- 无需重录率：转写后无需重新说一遍即可保存的比例；
- 模块一次确认率：接受首个 AI 推荐模块的比例；
- 找回成功率：给定历史记录后在 60 秒内打开的比例；
- 7 日与 28 日主动记录天数；
- 提醒回看率：通知后打开对应正文的比例。

### 诊断指标

- 本地转写耗时、实时率、崩溃、OOM、设备温度；
- 转写文字修改字符数、专名修正次数；
- 标题修改率、模块修改率、待确认率；
- AI 请求失败、超时、重试与离线积压；
- 日历候选数、导入数、忽略数、重复数；
- 搜索无结果率与结果点击位置；
- 提醒延迟与权限异常。

### 最小事件

- `capture_pressed`、`capture_cancelled`、`capture_completed`
- `transcription_completed`、`transcription_edited`、`transcription_failed`
- `classification_returned`、`module_changed`、`thought_saved`
- `search_started`、`search_result_opened`、`search_no_result`
- `calendar_scan_completed`、`import_confirmed`、`import_item_reviewed`
- `reminder_created`、`reminder_delivered`、`reminder_opened`

埋点只记录状态、耗时和匿名本机 ID，不记录正文、搜索词或日历内容。父亲 Alpha 可先本机导出测试报告，不接第三方分析平台。

## 19. 开发 Checkpoint 与验证节点

每个 checkpoint 都有明确“进入条件—产物—通过门槛”。未通过不得用“后面再优化”绕过。

### CP0｜目标设备与数据审计（0.5–1 天）

状态：`Deferred, not removed`。根据 2026-09-05 的批准，可逆的 UI、本地数据、接口和测试骨架可以先行；CP0 不再是开发启动的总前置门。小米 15 为 Product Lead 本人持有并可随时用于验证。任何 ASR、日历权限、提醒可靠性通过结论，以及进入父亲 Alpha，仍须先补齐对应的小米 15 实机证据。

进入条件：技术设备检查可由 Product Lead 使用小米 15 进行；涉及父亲的日历内容、真实语音或行为测试时，仍须取得父亲同意并使用脱敏数据。

产物：

- 手机型号、Android 版本、CPU/内存/剩余空间；
- 目标日历名称、账户类型、记录数量、日期范围；
- 20–30 条脱敏日历样本；
- 30 段覆盖短句、佳句、专名、数字、英文缩写和较长想法的真实语音测试集；
- 明确 Outlook 是否已同步进 Android 系统日历。

通过门槛：目标手机可安装测试 APK；可授权麦克风和日历；样本足够覆盖真实场景。未完成时不阻塞 CP1 或其他可逆骨架开发，但不能宣布 CP2、日历权限、提醒门禁通过，也不能进入父亲 Alpha。

### CP1｜可点击交互原型（2–3 天）

状态：`Deferred, not removed — CP1 not passed`。首页、录入、追加、搜索、详情与导入确认的合成 Compose 路径及 38 个 JVM 测试已经验收；父亲五任务人工可用性、按钮理解、实际触摸／字号／滚动／键盘、左滑阈值和 TalkBack 均未测试。Product Lead 已接受延期风险，产品经理只批准继续 CP2 技术开发。该人工验证必须在任何 CP3 准入决定前恢复，不能晚于父亲 Alpha。

范围：首页、按住说话、转写确认、搜索、结果详情、导入确认。

验证任务：

1. 录入一条新想法；
2. 左滑取消一次误触；
3. 给同一条记录补充第二段；
4. 找回昨天的一条记录；
5. 修正错误模块。

通过门槛：父亲在一次讲解后，5 个任务至少 4 个无需协助；正常录入和找回都不超过三步；能清楚说出下一步按钮。若失败，先改交互，不写完整数据层。

### CP2｜本地离线中文 ASR 技术门禁（3–5 天）

状态（2026-09-11）：`Vosk/model/JNA bounded static reviews accepted, manual_review; NOTES L1/L2/L3 engineering accepted; UI device verification pending; adoption/runtime admission blocked; CP2/CP3 overall not passed`。当前全量UI范围见[正式决定](notes-home-xiaomi-full-scope-decision-2026-09-11.md)，下一任务只做设备验收，不把host测试变成视觉或真机通过。ASR、私密音频、CP1人工、专名/性能/稳定性/飞行模式和Alpha门槛不变。

当前制品门禁：

- sherpa-onnx v1.13.7 固定源码归档（SHA-256 `acf539e930283442c4237b7b23a06ebe3bff10cbc00694a4f09a3580e3c10e9e`）为 `block`，不得解压、运行、构建、安装、导入或采用；
- 官方 AAR（SHA-256 `c4ef49e309f24fcee5c106b8a279481aaecaabb078cd37b2cd6e9a62cc8a73c8`）为 `manual_review`，不得安装、加载、构建、测试或集成；
- Zipformer 14M INT8 四文件集为 `manual_review`，不得加载、推理、测试、打包或集成；
- 首次 151 项最小源码清单只完成 50 项，因 5 个清单外 include 与 TTS 边界冲突停止；部分快照为 `manual_review`，不得构建、配置、安装、加载、测试、导入或集成；
- 各项裁决只适用于各自精确制品，互不继承，也不表示整个 sherpa-onnx 项目已经确认恶意。

静态闭包发现已在 Leader 收敛后停止：112 文件／499,282 字节、615 条 ledger、`fixed_point=false`，两条内部边未完成。该未完成状态不能外推为 sherpa-onnx 本身无法闭合；但当前证据已独立确认 `wave-writer.h` 的路径写 WAV、ADSP/QNN/RKNN 与 broad JNI/Kotlin 表面，候选集合不是 CPU-only／ASR-only 边界，发现材料为 `manual_review` 且不得进入阶段 B。Product Lead 新授权后，下一单只能使用提交 `0ded8eb...22fbb` 的已提交证据和正式文档，设计项目自有的窄 API／适配边界；不得继续 corpus、获取新正文、修改源码或形成构建输入。设计必须排除文件式音频、TTS、ADSP/QNN/RKNN、自动下载与宽 JNI，只保留受控固定加载、内存 PCM、识别生命周期／结果与释放。若设计阻塞或证据不足，暂停 sherpa-onnx 并回到产品决策门，再决定是否研究其他离线中文 ASR。Conformer 继续 `Deferred, not removed`。具体边界见[运行时窄边界路线决定](cp2-runtime-boundary-route-decision-2026-09-05.md)。

窄边界设计已经完成返工并由 Leader 验收为 `design_feasible`。该词只表示现有证据足以定义可证伪的源码审查合同：业务层未来仅允许固定 runtime／model handle、stream 生命周期、有界内存 PCM、decode、只读文字结果、版本和释放；宽 API＋caller 规则被拒绝为产品架构终态。它不改变 `fixed_point=false`、两条内部缺失边、332 条 system/external 边或任何动态未知。Product Lead 随后已对固定 sherpa-onnx commit `917bed95...a60e`／tree `fd2c4e97...bdc0`、9 seed、96 文件／1,048,576 字节和完整禁止范围给出精确授权；但授权不能绕过第一方工具的停止条件，也没有自动触发任何正文获取。具体设计边界见[窄边界设计准入决定](cp2-narrow-runtime-boundary-design-decision-2026-09-05.md)。

源码可行性门禁的第一方准备审查随后确认旧工具不具备执行条件：内部边可能漏记、denylist 不能发现即停、P0 证据缺失仍可能误报 feasible，并存在重定向、响应上限、异常持久化与文件系统保护缺口。旧准备任务保持 `BLOCKED`，不能原地修复、补签或续跑；这不是 sherpa-onnx 源码结论。下一单只修复新的第一方离线工具并用合成输入验收，不获取第三方正文。工具通过后仍须分别完成 Leader 验收、正式冻结和真实获取，固定上游身份、9 seed、96 文件／1 MiB 与全部禁止范围不变。具体边界见[第一方审查工具离线返工决定](cp2-first-party-tool-repair-decision-2026-09-05.md)。

第一方离线核心已在提交 `da9279a` 完成返工并通过 Leader 合成验收，但其 adapter/controller 明确只接受 `project-synthetic` 与 `SyntheticAdapter`，没有真实 HTTP/GitHub metadata/input 入口，`source_verdict` 恒为 `insufficient_evidence`。因此不能冻结为完整获取 release，也不能在冻结时补 transport。下一单只在新目录开发完整第一方候选，允许编写未来 GitHub Git Data 传输代码，但全部测试必须用合成响应和替身传输，实际网络与 DNS 事件为零；完整候选通过 Leader 验收后仍须另开冻结与真实获取任务。具体边界见[完整第一方获取工具离线开发范围决定](cp2-acquisition-tool-scope-decision-2026-09-05.md)。

完整 v3 候选随后在提交 `e4cd300` 通过 Leader 双跑 100 项测试，提交 `e2d64f9` 的旧冻结也已验收；但真实 metadata 预检在零网络、零正文请求下返回 `tree_path_or_duplicate`。8585 条路径无重复，171 个受当前字符规则拒绝的名称全部在实际获取范围外。下一单只修复 metadata 名称表示层：允许良性 @／Unicode 等惰性名称无损保留，仍拒绝绝对路径、点／双点 segment、NUL／控制字符和分隔混淆；只有真正进入 seed／内部依赖候选时才应用既有严格正文授权规则。候选经合成回归和两份固定 JSON 纯解析验收后必须重新独立冻结，旧冻结不得修改。具体边界见[metadata 路径兼容修复决定](cp2-metadata-path-compatibility-decision-2026-09-06.md)。

后续 v4 候选和新冻结通过验收后，一次全新真实获取取得并只取得 `LICENSE`，随即在第 183 行因自然语言撇号触发 `edge_unclosed_literal`。请求前授权、固定 blob/body 身份、16 条 ledger 和停止顺序已被核对；但原始 blob API wire JSON／HTTP headers 未保留，且 8 个 C/C++ seed 未请求。下一单只在独立 v5 候选离线修复精确 `LICENSE`＋冻结 `license_text` role 的路由，使其保留 scanner 与人工许可证审查但不进入 include 图；未知类型和近似路径继续请求前停止，C/C++ include guard／条件编译／宏与未知指令等既有不支持形式继续是合同预期停止。旧 run 不恢复；任何新真实获取都须 Product Lead 新授权。具体边界见[LICENSE 文本路由修复决定](cp2-license-text-routing-decision-2026-09-06.md)。

v5 离线修复和新冻结随后通过独立验收；新授权的一次真实获取只请求 `LICENSE` 与 `online-recognizer.h`，共 19,297 字节。LICENSE 路由正常；头文件两处 line comment 中的 `websocket` 按冻结 denylist 触发硬停止，但这不证明可达 WebSocket 能力。同一解析还记录 `ifndef`／guard `define`／`endif`，它们是旧合同独立不支持的 canonical guard 形状。现行合同因此必须一起修订，不能只删 token：下一单仅离线实现字节保真词法通道、comment capability pending、active deny 硬停止，以及不求值表达式的单一外层 canonical guard；所有其他 conditional／macro／生成 include 与词法歧义继续 fail closed。v5 run 已终止、无续跑权；新获取须未来独立授权。具体边界见[源码语义就绪路线修订](cp2-source-semantics-readiness-decision-2026-09-06.md)。

v6 R1 提交 `f55fda2` 随后通过 Leader 两次各 158 tests／961 outcomes／133 scenarios／0 skip，冻结提交 `d78577b` 只固定三份文档与既有候选身份，不执行候选、读取正文或增加 pending-clearance API。用户另行精确授权后，Leader 只对既有 `online-recognizer.h` 的两个 `websocket` comment occurrence 做离线人工复核：两处注释 bytes 在该 body 中不执行操作，但它们描述相邻服务端用途字段，不能外推到字段、API、实现或可达性。下一单只在独立 v7 候选以自建 fixture 验证 hash-bound review authority、双 line-hash domain、line/token byte intervals、逐 occurrence 不可转移和 fail-closed 冲突处理；原始分析保留，任何 active/uncertain deny、词法／预处理／文件安全停止仍优先。具体边界见[精确人工能力裁定证据接收决定](cp2-manual-capability-evidence-decision-2026-09-06.md)。

v8 的 P/K/F/M 与全新 acquisition A/T/input/package 后，一次且仅一次的真实获取 run 取得同样两个文件、19,297 bytes，并在 `online-recognizer.h` 的 5 个 active `dynamic_paths` 与 comment 完整集合不匹配处正确停止。active 命中位于行 15、110、143、156（两处）；comment 为原 57／60 与新增 64／132。模式命中不等于恶意或实际可达，但 active hard stop 独立且优先，不能以 comment 裁定覆盖。当前唯一允许工作是 Leader 在已批准 post-acquisition review 范围内审查同一 retained header 的七个 occurrence；任何新文件、依赖或网络都须另行产品决定与用户授权。具体边界见[v8 active 硬停止下一步决定](cp2-v8-hard-stop-next-step-decision-2026-09-06.md)。

七个 occurrence 的局部审查随后完成，人工可见范围合计 55 行：行 15 include 在获准查看的目标 directive 局部没有显示运行时操作；四个 `hotwords_file` occurrence 构成字段、参数与成员初始化的 policy-relevant 配置面，相邻说明区分 `hotwords_buf` 和 file-based loading；两处 comment bytes 在获准查看的局部上下文中不操作。实际 selector、文件 I/O、依赖、调用可达与业务 handle 暴露仍完全未证，未查看的同文件行与跨文件实现均不作断言，不能生成 clearance。个性词表有明确用户价值，但产品目标不是开放文件路径，因此只允许下一步准备单个 `online-recognizer.cc` 的新授权请求，以后若获明确授权才审查 buffer-only 是否可证；若单文件仍需依赖，立即停止而不自动扩张。当前路线继续暂停，具体见[v8 局部配置证据后的路线决定](cp2-v8-local-configuration-route-decision-2026-09-06.md)。

该授权后的消费端单文件任务已完成并停止：只请求 `online-recognizer.cc` 一次、8,993 decoded bytes，局部人工可见 28 行／1,237 bytes。可见 `Validate` 只在 `hotwords_file` 非空时调用 `FileExists`，失败分支可把路径值传给日志宏；`ToString` 也包含该参数。以上证明配置具有局部校验和诊断消费者，但没有证明 helper 的文件系统效果、实际运行、完整 file/buffer selector 或 `think` 业务暴露。空值短路和 `hotwords_buf` exact token 为 0 都不能证明完整 buffer-only。构造函数精确委派给未审 `OnlineRecognizerImpl::Create(config)`。只允许下一步准备 `online-recognizer-impl.h` 的最后一个单文件授权请求；若未来该文件仍继续委派，必须终止热词逐文件补证并回产品门，不能追踪第三文件。具体见[热词消费端证据后的路线决定](cp2-v8-hotwords-consumer-route-decision-2026-09-06.md)。

最后一个热词链任务随后完成并由 Leader 接受：`online-recognizer-impl.h` 只请求 1 次、2,286 bytes，人工仅查看第 20、24、25 行，共 3 行／129 bytes。可见 `OnlineRecognizerImpl::Create(config)` 以分号结束，属于声明；立即停止规则因此触发，没有查看同文件其他定义、其他方法或第二来源。热词逐文件证据链在当前路线下永久终止。该停止是证据预算决定，不能外推为整个文件没有定义或 buffer-only 能力不可行。下一步只研究 3–5 个非 sherpa-onnx 的离线中文 ASR 候选，每个最多 3 个官方页面并加最多 3 个跨候选页面，总计最多 18 个；研究只生成证据卡、比较矩阵和最多两个待未来独立安全 intake 的候选，不下载、读取源码、运行、构建、测试或集成。个性词表实现 `Deferred, not removed`；在 CP2 通过前仍须验证其机制与专名准确率，或另行正式修订门槛。具体见[热词证据链终止后的路线决定](cp2-hotwords-chain-termination-route-decision-2026-09-06.md)。

替代候选研究 R1 已被 Leader 接受并独立核验：Vosk 与 ONNX Runtime Mobile + SenseVoiceSmall-onnx 通过研究硬筛选；后者仍是需要闭合完整前后处理与 Android 兼容链的组合假设。产品选择为 Vosk，理由是它对中文、Android、离线、流式、约 42 MB 中文小模型和可重配词表的官方证据更直接，且后续可先用更小身份门禁停止。唯一下一任务是 `CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001`：最多 6 个官方公开页面／元数据端点，分别固定 runtime 与模型身份并输出 `identity_ready_for_artifact_intake_decision` 或 `identity_insufficient`。它不取得制品；后续源码／模型／二进制获取与扫描必须新决定和 Product Lead 精确授权，构建／加载／小米 15 测试再另立权限。具体见[Vosk 安全 intake 候选选择决定](cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md)。

当前补充状态（2026-09-09）：JNA单AAR已取得522677bytes并静态验收，SHA7f053e3ec99e14dd71259c82c1c8a02738d64a13c31226b2acc170f3060951e0，仍manual_review。Vosk/model/JNA真实执行及公共中文识别均未运行；一次1秒内存静音草案因环境/观测/Owner处置未具备而PAUSE，不能在macOS加载Android.so，也不能把jna.nosys或飞行模式当完整沙箱。前述取得权限是历史已完成范围，不批准新运行或产品集成。

公开语料CER按冻结test ID、原始参考文本与normalization-v1计算sum(S+D+I)/sum(N)，附raw-CER及完成率；缺结果仍计全删除，失败不从分母移除。保留训练／调参重叠Unknown，不将合成验算或公开朗读分数当父亲语音验证。固定选样及评分口径以[公开语料决定](cp2-public-chinese-corpus-test-decision-2026-09-09.md)为准；CER和JNA静态任务已完成，当前受控方案PAUSE及唯一解阻动作见受控实验决定。

比较至少两个适配设备的候选模型，包括流式或离线方案；记录模型大小、首载时间、30/90 秒转写耗时、字符错误率、关键专名召回、内存峰值、耗电与发热。

通过门槛：

- 30 段真实语音中至少 27 段无需重录即可理解；
- 常用专名在加入词典后正确率至少 90%；
- 常见 30 秒语音 P95 在松手后 5 秒内出结果，或取得父亲明确接受的基线；
- 90 秒连续录音 20 次无崩溃、OOM 或音频落盘；
- 飞行模式下完整可用。

若候选 runtime、模型包体或性能不通过，先在已获批候选范围内评估量化模型或分包下载；仍不通过则暂停本地方案并回产品决策门，而不是偷偷改回云端音频上传。

### CP3｜离线记录与搜索骨架（4–6 天）

状态：`NOTES-L1/L2/L3 limited text-first exception approved; CP3 overall not passed`。[2026-09-10笔记首页决定](notes-home-redesign-decision-2026-09-10.md)仅覆盖本地文字先行，明确优先于旧CP1延期决定对CP3的全面阻塞：L1真实持久化/草稿/自动手动标题，L2默认笔记首页/编辑器/真实搜索，L3同源显式关系图谱。后续合同checkpoint=CP3、stage=NOTES-L1/L2/L3并绑定该例外，各最多8小时串行验收，不将所有阶段一次标通过。

第一单NOTES-TEXT-FOUNDATION-001同单先同步四正式文档再实现L1；不靠云AI、ASR或截图私人内容。CP1人工仍延期未删除；非本例外CP3扩展/CP3整体通过、完整语音路径及Alpha准入前须恢复CP1并独立审计CP2。ASR运行/隐私、90秒/专名90%门槛不变。

范围：真实本地存储/索引、草稿、新建编辑保存重启打开、标题所有权、真实搜索、首页/关系；优先现有Room/FTS，缺Room可用平台SQLite事务，不新增下载准备链。AI和日历未实现功能隐藏/禁用，不以假数据进入产品路径。

通过门槛：

- 飞行模式可录入、保存、重启恢复和搜索；
- 1000 条合成记录搜索 P95 小于 500ms；
- 进程被杀与旋转后正式记录不丢失；
- 单元测试覆盖标题规则、追加规则、模块移动、幂等保存和删除回收；
- Compose UI 测试锁定三步路径。

### CP4｜日历导入与初始模块（4–7 天）

先只导入脱敏副本或测试日历，再在父亲手机做只读演练。

人工标注至少 100 条：思想记录／普通日程／不确定，并比较 AI 分流与模块建议。

通过门槛：

- 原日历零写入、零删除；
- 100% 导入记录可回溯到来源事件；
- 重复导入零重复正式记录；
- “建议导入”抽样准确率至少 85%，无法判断项进入待确认；
- 初始模块控制在 5–8 个，父亲或家人能看懂名称与样例；
- 一次批量确认可完成迁移，不要求逐条维护全部历史。

### CP5｜云端 AI Skill 标题与分类（3–5 天）

用至少 100 条脱敏文字做冻结评测集，输出严格 JSON。

通过门槛：

- 标题无需修改率至少 80%；
- 首选模块直接接受率至少 75%；
- 正文被改写或虚构的保存案例为 0；
- 非法 Schema、超时和无网全部回退到本地暂存；
- 抓包确认只有文字和候选模块进入网络；
- 服务器普通日志不存在正文。

若分类接受率低但搜索好用，保留“待确认 + 搜索”，不要为了 AI 强行增加用户步骤。

### CP6｜父亲单用户 Alpha（7–14 天）

安装真实 APK，不由开发者坐在旁边指导。第一天由家人完成权限和导入，之后观察自然使用。

通过门槛：

- 至少 7 天中有 5 天主动新增记录；
- 录入任务成功率至少 90%；
- 正常三步录入达成率至少 85%；
- 给定 10 条旧记录，至少 9 条在 60 秒、三步内找到；
- 需要家人救助不超过 1 次；
- 相比日历，父亲主观选择继续使用 App。

同时记录失败原因：没想到打开、按钮看不懂、转写错误、分类困惑、通知忽略、搜索词想不到。若只是家人推动使用，不升级验证等级。

### CP7｜提醒可靠性（2–4 天，可与 CP6 后半并行）

测试单次、每天、每周，覆盖 App 前台、后台、被划掉、设备重启、省电模式和权限撤销。

通过门槛：

- 测试矩阵内通知全部到达或明确显示系统限制；
- 点击通知 100% 直达正确正文；
- 无重复通知、无重复记录；
- 父亲能独立创建、关闭提醒；
- 只有父亲明确要求精确到分钟且非精确方案不满足时，才进入精确闹钟权限实现。

### CP8｜隐私、恢复与发布前门禁（3–5 天）

通过门槛：

- 设备文件、网络抓包、崩溃日志均找不到原始音频；
- 日志与埋点无正文、搜索词和日历内容；
- 数据库迁移、导出、回收站恢复可用；
- 依赖与模型许可证完成清单；
- 权限文案、隐私说明与 Android 数据安全表一致；
- Alpha 崩溃率与 ANR 达到可接受水平后，才讨论 3–5 位相似用户的小范围 Beta。

## 20. 验证升级与停止规则

### 从 V2 升到 V3 的最低条件

- 父亲完成 CP6，不依赖持续指导；
- 至少另外 3 位相似用户完成两周 Beta；
- 大多数用户主动记录并成功找回，而非只说“这个想法不错”；
- 记录、找回和提醒至少一项行为显示新 App 明显优于原替代方案。

### 必须暂停的情况

- 三步约束只能通过重新定义“步”才能达成；
- 语音错误导致用户频繁重录或放弃；
- 用户大部分时间在修正 AI 模块，而不是记录思想；
- 导入要求逐条人工整理，迁移成本超过继续用日历；
- 提醒在目标手机上不可靠且没有清楚降级；
- 产品只有 Product Lead 代替父亲操作时才显得好用。

## 21. 风险与应对

| 风险 | 影响 | 当前应对 |
| --- | --- | --- |
| 单用户偏差 | 误把父亲习惯当成市场 | V2 只允许父亲 Alpha；V3 前补 3–5 位相似用户 |
| 中文 ASR 在旧手机过慢 | 核心入口失效 | CP2 先行；量化模型、分包下载、设备基准 |
| 日历中普通日程太多 | 导入噪声与维护负担 | 三分流、批量确认、只读与幂等 |
| AI 分类增加认知负担 | 三步目标破坏 | 只显示一个推荐与“换一个”；失败进入待确认 |
| Android 提醒权限复杂 | 用户以为会提醒但没有 | 非精确优先、权限状态可见、重启重排 |
| 音频或正文泄漏 | 高隐私风险 | 音频内存化、最小文字请求、无正文日志、抓包门禁 |
| 模块长期膨胀 | 档案再次变杂 | 初始 5–8、超过 10 给合并建议、搜索始终独立存在 |
| 开源许可证误用 | 商业发布受限 | 官方 Apache 模板优先；GPL/AGPL 只研究，复用前审查 |
| 无账号导致换机丢失 | 长期档案承诺不成立 | Alpha 明确仅本机；P1 先做导出，再验证加密备份 |

## 22. 开放问题

1. 父亲的手机型号、Android 版本和可用存储是多少？
2. 目标 Outlook 日历是否已经同步到 Android Calendar Provider？
3. 提醒需要精确到分钟，还是在 10–15 分钟窗口内出现即可？
4. 通知只显示标题和正文首行是否足够，是否确实需要自动朗读？
5. 初始导入应覆盖全部年份，还是先用最近一年降低确认成本？
6. 个性词典更适合由父亲自己维护，还是允许家人在设置页协助？
7. Alpha 前是否必须提供导出，还是可在 CP8 前补齐？
8. 思想档案与 Family Chronicle 未来是两个独立产品，还是共享语音、档案与提醒底层？这不影响当前 App 技术样机。

## 23. 上线／灰度

1. **Developer build**：合成数据，只验证 CP1–CP3；
2. **Father Alpha**：本地安装 APK，完成 CP4–CP8；
3. **Family-assisted Beta**：3–5 位相似用户，邀请制、可随时回滚；
4. **Closed testing**：通过 Google Play 封闭测试，补崩溃、兼容与隐私材料；
5. **Public launch**：只有 V3 行为证据、数据恢复、许可证、隐私和提醒可靠性全部过门后讨论。

公开上架不是本 PRD 当前批准事项。
