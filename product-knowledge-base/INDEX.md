# 产品知识地图

Owner: Product Lead
Last updated: 2026-09-10
Source: 本工作区长期知识、项目文件与来源登记
Confidence: High
Related decisions: `decisions/one-person-pm-knowledge-loop-2026-08-23.md`
Next review date: 2026-09-30

## 当前入口

- [thinkV2换机恢复与最新状态](ideas/think-v2/migration-handoff-2026-09-17.md)：三份正式原文、许可来源映射、校验清单和新机任务重绑；产品缺口不因迁移消失。

- [BOARD.md](BOARD.md)：活跃 Build、Discovery、Parking Lot、阻塞与待决策。
- [LOG.md](LOG.md)：Ingest、Query、Lint 和人工决策操作记录。
- [运行规则](agents/operating-rules.md) 与 [agent roster](agents/agent-roster.yaml)。
- 来源记录位于 `raw/`；一次性交付物位于 `outputs/`。

## 正式决策

- [产品调研工作流标准化](decisions/product-research-workflow-2026-08-18.md)
- [一人公司 PM 知识循环与 WIP](decisions/one-person-pm-knowledge-loop-2026-08-23.md)
- [暂停「哎呀，早知道」项目](decisions/sold-too-soon-pause-2026-08-30.md)

## 已暂停 Build：哎呀，早知道

- [暂停决策](decisions/sold-too-soon-pause-2026-08-30.md)
- [CP7 进度来源](raw/SRC-20260830-sold-too-soon-progress-01.md)
- [产品策略](ideas/sold-too-soon/product-strategy-2026-08-04.md)
- [PRD v0.1](ideas/sold-too-soon/prd-v0.1-2026-08-07.md)
- [PRD 批准记录](ideas/sold-too-soon/prd-approval-decision-2026-08-07.md)
- [双轴补充后的研究 Eval](ideas/sold-too-soon/product-research-eval-2026-08-18.md)
- [账号、图库与品牌](ideas/sold-too-soon/account-library-and-brand-2026-08-04.md)
- [单输入体验](ideas/sold-too-soon/one-input-experience-2026-08-04.md)
- [定价](ideas/sold-too-soon/pricing-decision-2026-08-04.md)
- [计算口径](ideas/sold-too-soon/calculation-method-decision-2026-08-05.md)
- [固定模板](ideas/sold-too-soon/fixed-template-rendering-decision-2026-08-05.md)
- [结果文案](ideas/sold-too-soon/result-copy-decision-2026-08-05.md)
- [支付、额度与退款](ideas/sold-too-soon/payments-credits-refunds-2026-08-05.md)

## 活跃 Discovery：Family Chronicle

- [Idea Brief](ideas/family-chronicle/idea-brief.md)
- [父母／祖辈个人回忆录市场研究](ideas/family-chronicle/elder-memoir-market-research-2026-08-17.md)
- [20 来源公开证据地图与双轴评估](ideas/family-chronicle/evidence-map-2026-08-23.md)
- [5 个可追溯 Query 前向测试](ideas/family-chronicle/query-test-2026-08-23.md)
- 原始证据：见 `raw/SRC-20260823-family-chronicle-*.md`

## Parking Lot 与其他想法

### 思（think）Android App

- [PRD v0.1：产品、页面、技术架构与开发 Checkpoint](ideas/personal-thought-archive/prd-v0.1-2026-09-04.md)
- [正式命名决策：「思」／「think」](ideas/personal-thought-archive/naming-decision-2026-09-04.md)
- [开发启动决策：CP0 延后但不阻塞可逆开发](ideas/personal-thought-archive/development-start-decision-2026-09-05.md)
- [CP1 门禁决策：人工验证延后，仅批准进入 CP2](ideas/personal-thought-archive/cp1-deferred-cp2-entry-decision-2026-09-05.md)
- [CP2 运行时安全路线：仅批准另行授权后的最小源码快照门禁](ideas/personal-thought-archive/cp2-runtime-security-route-decision-2026-09-05.md)
- [CP2 最小源码路线修订：静态发现与最终快照分阶段](ideas/personal-thought-archive/cp2-minimal-source-route-revision-decision-2026-09-05.md)
- [CP2 运行时边界路线：仅批准已提交证据上的项目自有窄边界设计](ideas/personal-thought-archive/cp2-runtime-boundary-route-decision-2026-09-05.md)
- [CP2 窄边界设计准入：接受 handle 型合同，仅允许新授权后的源码可行性门禁](ideas/personal-thought-archive/cp2-narrow-runtime-boundary-design-decision-2026-09-05.md)
- [CP2 第一方工具返工：仅批准离线、标准库与合成输入修复](ideas/personal-thought-archive/cp2-first-party-tool-repair-decision-2026-09-05.md)
- [CP2 完整获取工具范围：仅批准第一方完整组件的零网络离线开发](ideas/personal-thought-archive/cp2-acquisition-tool-scope-decision-2026-09-05.md)
- [CP2 metadata 路径兼容：分离惰性名称与正文授权路径](ideas/personal-thought-archive/cp2-metadata-path-compatibility-decision-2026-09-06.md)
- [CP2 LICENSE 文本路由：只批准精确 path/role 的离线修复](ideas/personal-thought-archive/cp2-license-text-routing-decision-2026-09-06.md)
- [CP2 源码语义就绪：注释能力证据与 canonical guard 的有界修订](ideas/personal-thought-archive/cp2-source-semantics-readiness-decision-2026-09-06.md)
- [CP2 精确人工能力裁定：逐 occurrence、不可转移且 authority DAG 非循环的离线证据接收](ideas/personal-thought-archive/cp2-manual-capability-evidence-decision-2026-09-06.md)
- [CP2 人工审查时间表示：只批准独立 v8 的无损小数秒／时区离线修订](ideas/personal-thought-archive/cp2-review-timestamp-representation-decision-2026-09-06.md)
- [CP2 原 token 来源：同一 retained object 的最小离线证据补录](ideas/personal-thought-archive/cp2-review-token-provenance-decision-2026-09-06.md)
- [CP2 v8 active 硬停止：只批准同一 retained header 的局部静态证据审查](ideas/personal-thought-archive/cp2-v8-hard-stop-next-step-decision-2026-09-06.md)
- [CP2 v8 局部配置路线：保持暂停，只准备单文件新授权请求](ideas/personal-thought-archive/cp2-v8-local-configuration-route-decision-2026-09-06.md)
- [CP2 v8 热词消费端路线：只准备 `impl.h` 最后一次单文件授权请求](ideas/personal-thought-archive/cp2-v8-hotwords-consumer-route-decision-2026-09-06.md)
- [CP2 热词证据链终止路线：转入替代离线中文 ASR 官方材料研究](ideas/personal-thought-archive/cp2-hotwords-chain-termination-route-decision-2026-09-06.md)
- [CP2 替代离线中文 ASR 官方证据卡 R1：修正 Whisper 许可证／资源与组合推导](ideas/personal-thought-archive/cp2-alternative-offline-chinese-asr-evidence-cards-2026-09-06.md)
- [CP2 替代离线中文 ASR 十二维比较矩阵 R1](ideas/personal-thought-archive/cp2-alternative-offline-chinese-asr-comparison-matrix-2026-09-06.md)
- [CP2 替代离线中文 ASR 研究结论 R1：两候选可进入后续 intake 选择决策](ideas/personal-thought-archive/cp2-alternative-offline-chinese-asr-research-memo-2026-09-06.md)
- [CP2 替代 ASR 安全 intake 选择：只选择 Vosk 进入官方身份准备](ideas/personal-thought-archive/cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md)
- [Vosk runtime 身份：精确发行未核定](ideas/personal-thought-archive/cp2-vosk-runtime-identity-2026-09-06.md)
- [Vosk 中文模型身份：目录对象 small-cn-0.22 已核定，制品未取得](ideas/personal-thought-archive/cp2-vosk-model-identity-2026-09-06.md)
- [Vosk 身份准备：identity_insufficient 与完整访问 ledger](ideas/personal-thought-archive/cp2-vosk-identity-readiness-2026-09-06.md)
- [Vosk Android 身份缺口：独立 Maven Central 元数据批次范围决定](ideas/personal-thought-archive/cp2-vosk-android-identity-gap-decision-2026-09-06.md)
- [Vosk Android Central 元数据：0.3.75／aar 身份就绪与原始 XML](ideas/personal-thought-archive/cp2-vosk-android-maven-metadata-2026-09-06.md)
- [Vosk 精确制品静态审查范围与待用户确认授权句](ideas/personal-thought-archive/cp2-vosk-artifact-review-scope-decision-2026-09-06.md)
- [Vosk 工具预检缺口：单模块离线补齐范围决定](ideas/personal-thought-archive/cp2-vosk-tool-gap-decision-2026-09-08.md)
- [Vosk 最新规则：简化分阶段审查，替代未执行adapter](ideas/personal-thought-archive/cp2-vosk-simplified-staged-review-decision-2026-09-08.md)
- [Vosk 阶段2范围：固定SHA包内静态审查与新增获取边界](ideas/personal-thought-archive/cp2-vosk-stage2-scope-decision-2026-09-08.md)
- [Vosk 集成缺口归并：下一官方依赖／许可元数据批次](ideas/personal-thought-archive/cp2-vosk-integration-gaps-decision-2026-09-08.md)
- [Vosk 依赖／许可批次：权限前置BLOCKED与零请求记录](ideas/personal-thought-archive/cp2-vosk-dependency-license-metadata-2026-09-08.md)
- [Vosk 依赖／许可恢复批次：固定AAR选择器及分对象许可处置](ideas/personal-thought-archive/cp2-vosk-dependency-license-metadata-resumed-2026-09-08.md)
- [公开中文语料测试：公共fixture边界与有限CER评分工具](ideas/personal-thought-archive/cp2-public-chinese-corpus-test-decision-2026-09-09.md)
- 公开测试进度（2026-09-09）：CER工具已由Leader验收，20测试／21黄金用例／961短字符串比较通过，仅合成评分验证，真实ASR未运行；AISHELL-1/THCHS-30可信小test子集未核，语料取得仍暂停。公共许可fixture隔离保存与私密录音不落盘/上传/日志边界不变。
- [JNA单AAR正式范围：用户确认取得及有限静态检查](ideas/personal-thought-archive/cp2-jna-aar-static-review-decision-2026-09-09.md)
- JNA已完成进度：单AAR取得522677B，SHA7f053e3ec99e14dd71259c82c1c8a02738d64a13c31226b2acc170f3060951e0，Leader验收有限静态工作，仍manual_review；不再重复下载或派静态准备工具。
- [受控ASR先行实验：固定加载/静音方案与执行PAUSE](ideas/personal-thought-archive/cp2-controlled-asr-experiment-decision-2026-09-09.md)
- [真实笔记首页与图谱：CP3限定文字先行范围](ideas/personal-thought-archive/notes-home-redesign-decision-2026-09-10.md)
- [小米笔记式全量UI：页面、主题、手势与CRUD验收范围](ideas/personal-thought-archive/notes-home-xiaomi-full-scope-decision-2026-09-11.md)
- 当前UI状态（2026-09-11）：NOTES L1/L2/L3数据与工程逻辑已由Leader验收；全量小米笔记式UI范围已固化为UI-L1/L2/L3，但Android视觉、主题、触控、IME、返回栈、TalkBack、首次启动和父亲可用性仍device_unverified。下一唯一任务NOTES-UI-DEVICE-001，一次设备验收；不再自动拆开发阶段，不复制截图私人内容或小米品牌资产。ASR/CP2/CP3整体/CP1/Alpha门槛保持。
- 当前产品开发优先级（2026-09-10）：NOTES-HOME-SCOPE-001 APPROVED，后续checkpoint=CP3、stage=NOTES-L1真实文字持久化/标题→NOTES-L2笔记首页/真实搜索→NOTES-L3用户显式关系图谱，各最多8小时串行验收。下一NOTES-TEXT-FOUNDATION-001同单同步四文档和L1实现，不重复方向审批、不另开准备链。CP1/CP2不阻塞该窄文字例外，CP3整体/Alpha仍未通过，ASR运行及隐私门禁保留；假录音/保存/搜索退出产品路径，截图私人内容不用作数据。
- ASR支线裁定保留：CP2-CONTROLLED-RUN-PLAN-001方案COMPLETE/PAUSE，环境/观测/Owner处置未核，真实ASR/采用仍blocked；该支线下一动作仅现有环境只读核对，不阻塞最新NOTES文字先行。1秒静音不算中文测试，CP3整体与Alpha未批准；CP3窄文字例外以上述2026-09-10决定为准。
- 原始依据与技术来源：见 `raw/SRC-20260904-personal-thought-archive-*.md`
- CP2 安全依据：见 `raw/SRC-20260905-think-cp2-runtime-*.md`
- CP2 最小源码失败与修订依据：见 `raw/SRC-20260905-think-cp2-minimal-route-*.md`
- CP2 静态发现与边界路线依据：见 `raw/SRC-20260905-think-cp2-boundary-route-*.md`
- CP2 窄边界设计与源码门禁依据：见 `raw/SRC-20260905-think-cp2-design-decision-*.md`
- CP2 第一方工具缺陷与返工依据：见 `raw/SRC-20260905-think-cp2-tool-repair-*.md`
- CP2 完整获取工具范围依据：见 `raw/SRC-20260905-think-cp2-acquisition-tool-*.md`
- CP2 metadata 路径兼容依据：见 `raw/SRC-20260906-think-cp2-metadata-path-*.md`
- CP2 LICENSE 文本路由依据：见 `raw/SRC-20260906-think-cp2-license-routing-*.md`
- CP2 源码语义就绪依据：见 `raw/SRC-20260906-think-cp2-semantics-readiness-*.md`
- CP2 人工能力裁定依据：见 `raw/SRC-20260906-think-cp2-manual-capability-*.md`
- CP2 人工审查时间表示依据：见 `raw/SRC-20260906-think-cp2-review-timestamp-*.md`
- CP2 原 token 来源依据：见 `raw/SRC-20260906-think-cp2-token-provenance-*.md`
- CP2 v8 硬停止依据：见 `raw/SRC-20260906-think-cp2-v8-hard-stop-*.md`
- CP2 v8 局部配置依据：见 `raw/SRC-20260906-think-cp2-local-configuration-*.md`
- 状态：替代离线中文 ASR 官方研究 R1 已完成并由 Leader 接受。产品选择结果为 `APPROVED`：两个研究合格候选中只选择 Vosk 进入下一项官方身份准备；ONNX Runtime Mobile + SenseVoiceSmall-onnx 保留为第二研究候选但不并行推进。下一单最多读取 6 个 Vosk 官方公开页面／元数据端点，分别固定一个 Android runtime 与一个中文小模型的身份、来源、版本／发行坐标和许可证；不取得任何源码、模型、二进制或制品。公开身份准备、制品获取与扫描、构建／加载／小米 15 测试是三个独立权限阶段。Vosk 尚未获准采用，CP2 未通过，CP3 与父亲 Alpha 未批准；所有三步、音频隐私、专名 90%、真机、性能、稳定性和飞行模式门槛保持

- 接管收尾历史：选择文档当时待当前 Leader `01a07655-fdfd-7683-aa57-a4895188d2ff` 验收；当时阶段 A 尚未下发或执行。其允许的官方说明、README、LICENSE、公开元数据不属于禁止取得的源码实现／模型／二进制制品；6 端点及全部门槛不变。
- 首次身份停止（2026-09-06，历史）：Leader 已验收选择文档同步 `92e50278` 并下发阶段 A。首个 runtime 官方入口请求因 Firecrawl 额度不足失败，计 1/6（runtime 1/3、model 0/3），成功页面 0；当时结果为 `identity_insufficient`、Research Quality 55/100 · fail。该失败及旧记录保留。
- 身份续接停止（2026-09-06，历史）：官方模型目录确认 `vosk-model-small-cn-0.22`／`42M`／Apache 2.0；安装说明确认 `com.alphacephei:vosk-android:0.3.32+` 动态范围，官方项目 release 为 `v0.3.50`、assets为空，但未证明两者绑定到精确 Android 包。累计5/6次（runtime3/3、model2/3），成功3端点；runtime预算耗尽，仍 `identity_insufficient`，不挪用模型预算。Research Quality 82/100 · fail，V2不变。
- 范围决定历史：`CP2-VOSK-ANDROID-IDENTITY-GAP-DECISION-001` 为 APPROVED，仅批准独立 `CP2-VOSK-ANDROID-MAVEN-METADATA-001` 的最多10次请求批次；范围裁定当时未联网执行。旧停止与预算不重置。
- 已验收元数据结果（2026-09-06）：`identity_ready_for_artifact_intake_decision`，Central release与同版本POM核定 `com.alphacephei:vosk-android:0.3.75`／`aar`、Alpha Cephei Inc及Apache2声明；9/10次、140727 bytes、单版本、零父POM。POM异常主页 `alphacephei.com.com` 未访问或纠正，身份链使用官方Central与匹配SCM。原XML及SHA已保存，Research Quality90/100、V2不变；仅元数据身份就绪，不批准制品。
- 最新范围决定：`CP2-VOSK-ARTIFACT-REVIEW-SCOPE-DECISION-001` 为APPROVED，仅定义下一单先主AAR后中文ZIP的串行静态审查及待确认授权句；各1次GET／64MiB／120秒，总2次／128MiB，重定向／资源／结构硬停止即停，不继承裁决。用户精确授权与开发执行前正式文档同步尚需完成；不取得JNA／.module／sidecar或新源码，不访问异常主页，整体adoption_gate继续blocked。未联网或改think，C、CP2、CP3与父亲Alpha未批准，待Leader验收。

- 工具缺口历史（2026-09-08）：原预检BLOCKED、零GET、两对象not_acquired，曾提出16小时adapter；该未执行路线已由用户简化决定取代，不下发，原报告／授权／旧规则保持历史。
- 最新状态：CP2-SIMPLIFIED-STAGED-REVIEW-DECISION-001为APPROVED，用户已批准简化类别，一次明确首阶段两原对象／有限重试跳转／安全新attempt解包／现实读取时间限额，不再要求1GiB硬隔离或专用工具链。下一单CP2-VOSK-STAGE1-ACQUISITION-INSPECTION-001需先由Leader同步新决定/PRD及Think两个入口；PM本轮不下载或改think。集成前静态深查及CP2真机分阶段，未覆盖Unknown、采用blocked，CP1/隐私/90%/Checkpoint不变，无重复用户批准链。

- 最新阶段2状态（2026-09-08）：Leader已验收阶段1两对象2GET／57371392B、13＋20外层成员及715B文本；未读nested/native、完整许可、依赖和动态行为仍Unknown。CP2-VOSK-STAGE2-SCOPE-DECISION-001为APPROVED，下一唯一包内静态审查单最多8小时，只现有固定SHA包，不重新取得或联网；JNA/.module等后续身份／授权准备与包内工作分开，采用仍blocked。新决定/PRD及Think两个入口由Leader下一单同步，PM本轮不改Think或读二进制。

- 最新集成缺口（2026-09-08）：阶段2已验收，runtime/model仍manual_review，采用blocked。CP2-VOSK-INTEGRATION-GAPS-DECISION-001为APPROVED，仅下一CP2-VOSK-DEPENDENCY-LICENSE-METADATA-001最多12次官方说明／metadata批次；固定JNA5.18.1/Vosk0.3.75.module/两主对象许可来源，旧包不重取，新AAR仍需精确授权。popen导入非恶意证明，首次受控运行前需有限调用输入边界论证；PCM生命周期/准确率等留动态验证，不自动集成，隐私/90%/CP1/Checkpoint保持。

- 历史执行停止：CP2-VOSK-DEPENDENCY-LICENSE-METADATA-001结果BLOCKED／metadata_insufficient；Q01在进程创建前被自动审批拒绝，实际HTTP0／0B，保守占用1次；拒绝原文与旧报告保留，不改写为已成功。
- 最新元数据结果：CP2-VOSK-METADATA-RESUME-001按Leader转交用户恢复确认完成，metadata_batch_complete，待Leader验收。本次9GET／1807434B、无跳转，含旧Q01共10/12尝试，保守恢复1/2；固定JNA5.18.1默认POM为jar，Vosk.module API/runtime显式选择aar并排除传递依赖。发布Vosk AAR SHA与历史验收值一致，仅元数据对照；runtime和model Apache2声明分开确认，完整组件归属／模型训练权利处置仍open。未取JNA AAR、未读旧包、未执行或改Think；采用及运行继续blocked。

- [CP2离线下一步：PCM会话契约与fake ASR合成验证](ideas/personal-thought-archive/cp2-offline-next-step-decision-2026-09-08.md)
- 离线两步范围记录：PM决定APPROVED→Leader验收后dev同单同步与实现一个第一方离线模块；CP2-MEMORY-PCM-FAKE-ASR-CONTRACT-001最多6小时、5工程＋4同步文件。当时JNA/module查询暂停，现文本恢复结果见上；popen全可达性Unknown不继续逐函数追踪。不构建App或加载真实引擎，不进入CP3，fake测试不等于真实ASR通过，采用与运行门继续blocked。

### Rapid Situation Interpreter

- [Idea Brief](ideas/rapid-situation-interpreter/idea-brief.md)
- [Research Brief](ideas/rapid-situation-interpreter/research-brief.md)
- [市场与用户研究](ideas/rapid-situation-interpreter/market-user-research-2026-07-22.md)
- [竞品能力演进](ideas/rapid-situation-interpreter/competitor-capability-evolution.md)
- [十年趋势评估](ideas/rapid-situation-interpreter/ten-year-trend-evaluation-2026-07-22.md)

### 城市兴趣与中国本地体验

- [城市兴趣体验与消费地图 Idea Brief](ideas/city-interest-experience-map/idea-brief.md)
- [市场数据研究](ideas/city-interest-experience-map/market-data-research-2026-07-22.md)
- [竞品定位选项](ideas/city-interest-experience-map/competitor-positioning-options-2026-07-22.md)
- [GitHub 仓库扫描](ideas/city-interest-experience-map/github-repo-landscape-2026-08-01.md)
- [中国城市日常沉浸体验 Idea Brief](ideas/china-local-life-experiences/idea-brief.md)
- [中国城市日常沉浸体验竞品定位](ideas/china-local-life-experiences/competitor-positioning-research-2026-07-22.md)

### 中国老年陪伴与助医陪诊

- [完整平台 PRD v0.1](ideas/elder-companion/prd-full-v0.1-2026-09-06.md)：手机网页、一对一社区陪伴撮合、三端流程与演进蓝图；草稿
- [交易 MVP PRD v0.1](ideas/elder-companion/prd-mvp-v0.1-2026-09-06.md)：人选浏览、预约、付款、履约与复约；范围、状态、验收与指标
- [市场研究总览](ideas/elder-companion/market-research-2026-09-05.md)
- [城市与全国人口数据](ideas/elder-companion/demographics.csv)
- [服务价格样本](ideas/elder-companion/service-prices.csv)
- [来源索引](ideas/elder-companion/source-index.md)
- 状态：研究包；助医陪诊 V2、纯非医疗陪伴 V1；未修改 roadmap 承诺
- 当前产品方向：用户已选择社区一对一陪伴撮合与手机网页；访谈暂停。以上两份 PRD 为当前设计入口，旧陪诊优先建议保留为历史，不作为本版范围；本产品仍 V1，尚无自有交易验证。

### 其他产品想法

- [健身房实时人数与拥挤度查询](ideas/gym-occupancy/idea-brief.md)：单店实验、必需会员入口、简洁首页与场地配置；V0，数据接入和拥挤阈值待核查
- [健身房产品功能与UI研究（2026-09-10）](ideas/gym-occupancy/product-feature-ui-research-2026-09-10.md)：11个相关产品／项目、科技公司赛事与开源许可；[来源证据卡](ideas/gym-occupancy/evidence-cards-2026-09-10.md)，新功能为建议、V0不变

- [AI 护理交班草稿器](ideas/ai-nursing-handoff-draft/idea-brief.md)
- [CTP 古籍阅读体验现代化](ideas/chinese-text-project-reading-experience/idea-brief.md)
- [工业设备报警分诊 Idea Brief](ideas/industrial-equipment-alert-triage/idea-brief.md)
- [工业设备协作框架](ideas/industrial-equipment-alert-triage/collaboration-framework.md)
- [工业设备 Discovery 访谈指南](ideas/industrial-equipment-alert-triage/discovery-interview-guide.md)
- [线条小狗跨端宠物](ideas/line-puppy-companion/idea-brief.md)

## 可复用参考

- [Dan Koe 参考入口](references/dan-koe/README.md)
- [一人公司 AI 中文决策框架](references/dan-koe/build-1m-one-person-business-ai-chinese-reference-framework.md)
- [一人公司 AI 英文时间线笔记](references/dan-koe/build-1m-one-person-business-ai-english-timeline-notes.md)
- [一人公司 AI 来源地图](references/dan-koe/build-1m-one-person-business-ai-source-map.md)
- [Don't Quit 中文决策框架](references/dan-koe/dont-quit-chinese-decision-framework.md)
- [Don't Quit 英文综合笔记](references/dan-koe/dont-quit-english-comprehensive-notes.md)

## 模板与操作入口

- [来源记录模板](templates/source-record.md)
- [决策记录模板](templates/decision-record.md)
- [PRD 模板](templates/prd.md)
- [周度产品 Loop](templates/weekly-product-loop.md)
- `$product-research`：新研究与 Evidence Cards。
- `$knowledge-loop ingest`：来源登记与长期写回。
- `$knowledge-loop query`：可追溯回答。
- `$knowledge-loop lint`：确定性与语义质量检查。
