# 决策：Vosk Android 精确发行身份补证范围

Owner: Product Lead
Last updated: 2026-09-06
Source: `CP2-VOSK-ANDROID-IDENTITY-GAP-DECISION-001`；三份既有 Vosk 身份记录；正式候选选择决定；`/Users/orderly_ray/Leader/orchestration/reports/CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001-review.md`
Confidence: Medium（支持有界元数据补证，不支持采用或安全结论）
Related decisions: `cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md`；`prd-v0.1-2026-09-04.md`
Next review date: 2026-09-13
Research Quality: 82/100 · fail（沿用身份研究证据质量；未新增网络证据，不提高旧分数）
Validation Level: V2（保持，不升级）
Next evidence: 独立执行下述官方 Maven Central 发行元数据批次，核定一个固定 Android 坐标及其 POM 声明
Allowed next investment: 一项最多 10 次请求的公开只读元数据任务，Leader 验收及下发后执行；不下载或运行制品
Pause/Kill condition: 新批次内不能建立官方来源、固定 Android 版本与 POM 绑定或许可声明；需制品／源码／第二候选才能继续则停止

## RESULT

**APPROVED：只批准一项独立、有界的 Maven Central 官方发行元数据查询批次。**

这是对下一步研究范围的批准，不是身份门通过、runtime 采用、阶段 B 获取或阶段 C 执行授权。本任务没有联网或查询 Maven Central，也不宣称任何具体版本或新 URL 已存在。低于 85 的既有研究质量不支持采用，但足以定位需要用低成本公开元数据核查的明确缺口。

旧 `CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001` 保持 `identity_insufficient`，累计 5/6（runtime 3/3、model 2/3）。旧 runtime 预算耗尽，模型余 1 不转用；本次为新合同、新 ledger、新预算，不重置旧记录或追溯批准超额访问。

## 决策依据

| 已有证据 | 可支持结论 | 不能支持结论 |
| --- | --- | --- |
| runtime R02：官方安装说明 https://alphacephei.com/vosk/install ，2026-09-06，Android build | 官方声明 Maven Central 渠道与 `com.alphacephei:vosk-android:0.3.32+` 动态依赖 | 不能去掉 `+` 当固定版本；不能证明某精确包内容 |
| runtime R03：官方 release JSON，2026-09-06 | 项目 tag `v0.3.50`，assets为空 | 不能推断 Android 0.3.50 存在或 Maven Central 没有发行 |
| model M02：官方目录，2026-09-06 | `vosk-model-small-cn-0.22` 的目录身份、42M、Apache 2.0 | 不固定模型内容、SHA、签名、完整许可或兼容性；本次不重新研究模型 |
| Leader review：PRODUCT_DECISION_REQUIRED | 三身份文档大小／SHA已核对；旧不足结论合理，缺口需要独立范围裁定 | Leader 未重新联网核验成功响应，不冒充独立网络复核或身份验收 |

输入三文档身份已再次匹配 Leader review：runtime 7007 bytes／`dbbf286e01ba240bbe242c8166f93a2c5f16e98f96f0249628d6db10a66e7576`；model 6201 bytes／`14a64e8fe55844daff2394c8bef65292136262986b6e5fa1179628964d8433b1`；readiness 14559 bytes／`8e00fa5267e9eabf10efb6b3c163360327ca303cffb6d0b8aef84d4cb61b1e51`。review SHA-256 为 `af9efa8ffb3deef6f0f79ae6b4094b629ee7930d85ae2352552eaf3af2009e3f`。

选择此路线是因为缺口位于官方已声明的发行渠道，而不是语音能力研究。备选 PAUSE 会保留未知，但在允许只读元数据且不接触制品的情况下尚无必要；重复 GitHub release、读 AAR 辨认版本、扩大候选均不符合最小范围。

## 下一项唯一合同

任务 ID：`CP2-VOSK-ANDROID-MAVEN-METADATA-001`。

### 唯一目标

只针对 `groupId=com.alphacephei`、`artifactId=vosk-android`，在官方 Maven Central 发行渠道确认一个非动态、非 SNAPSHOT 的固定发行版本，并由该版本 POM（项目对象模型，Project Object Model）核对 groupId、artifactId、version、packaging、发布者／项目来源与许可证声明。不得误查 Java 包 `vosk`，不得同时研究多个版本或模型。

最终只输出 `identity_ready_for_artifact_intake_decision` 或 `identity_insufficient`。身份准备成功只表示后续授权能指认对象及其元数据声明，不证明 AAR 实际存在、可下载、安全、内容正确或与源码可复现。

### 来源确认与 URL 发现

1. 起点是已取得的 Vosk 官方安装说明及其 `mavenCentral()`、groupId、artifactId；本轮决策不新增具体网络 URL、不猜版本。
2. 下一执行任务可使用既有浏览器或已可用只读搜索工具发现 Maven Central 运营方的官方说明／入口，必要时参考 Apache Maven 官方仓库布局说明。搜索只为发现发行渠道和精确包，不做其他竞品或模型研究。搜索结果及摘要是导航线索，不是包存在性／许可证证据。
3. 为避免“未确认来源前不能读身份说明”的循环，批次明确包含来源建立：先在搜索／浏览器公开入口信息中核对站点主体，再只读候选运营方的关于／帮助／仓库说明页，核对其运营身份、官方交叉链接和声明的 Central 端点。仅凭名称相似、搜索排名或 HTTPS 不算确认。无法建立官方归属则停止，不能访问其包对象。读取候选说明的尝试也入账，不把尚待验证域名直接列为可信来源。
4. 读取包版本列表／POM 前，ledger 必须先记录官方运营说明或可信官方交叉链接如何确认该域名与仓库/API 路径。新域名按同一检查规则当场核定，不新增逐页用户审批；来源不明不能继续。
5. 精确请求 URL 必须来自已验证官方页面/API 返回的链接，或由已验证官方仓库布局规则加“已观察到的 groupId、artifactId、固定 version、metadata/POM 类型”确定性生成，并保留推导依据。规范驱动的构造不是猜测；本决定不预填某个域名、包版本或拼接后的地址。不探测猜测路径或镜像。
6. 包入口必须严格匹配 `com.alphacephei:vosk-android`。确认一个版本后冻结该候选，不轮询多个版本：优先采用官方元数据明确给出的稳定 release；没有该字段时可采用官方版本列表及发行时间明确支持的一个稳定发行，并记录选择依据，不声称“最新”。如果只能靠字符串猜测排序或稳定性，返回不足。

### 单批次预算

- 最多 **10 次任务级请求尝试**，包括搜索、说明页面、版本元数据、POM、许可说明、显式重定向跟进和失败重试；同 URL 重试也计数。无自动重试、无无限分页，不按成功数重新计算预算。
- 建议分配：来源／布局确认与导航 3 次，精确包及版本元数据 2 次，选定版本 POM／必要父 POM或许可证说明 3 次，失败恢复或重定向预留 2 次。此分配是计划而非逐页面子审批；允许在总 10 次内调配，但不得改变唯一目标。
- 一个候选版本，最多一个直接父 POM；不递归取父链、依赖 POM、插件、BOM 或源树。版本列表可以显示多个版本，但只进入一个版本的身份核定，不逐版本比较或自动切换。
- 单次响应上限 1 MiB，累计读取正文上限 5 MiB，单次等待上限 30 秒；达到任一上限立即停。使用现有工具能够落实的有界读取，不为任务安装新工具；无法限制时先缩小为该工具可约束的请求，不无限取回再裁剪。
- 浏览器仅导航已核定说明／元数据页，不点击下载；不把其常规渲染资源计作独立证据页，但不得利用后台请求抓取未授权制品。优先使用能逐项记录 URL、状态和大小的直接只读方式。
- 到达成功条件即可结束，不为用完预算补齐非必要未知。预算不足即一次性回报缺口，不制造一页一审批的延长链。

### 允许与禁止内容

允许官方说明、版本 metadata、包索引信息、选定版本的文本 POM及必要许可说明。POM 只用结构化 XML 解析或人工阅读；关闭外部实体与自动网络解析，不调用 Maven／Gradle，不安装包、不解析执行构建脚本，不自动解析依赖。最多一个父 POM只能用来关闭缺失／继承的身份或许可字段，不成为依赖闭包任务。

可记录 POM 中的 SCM／开发者／组织／许可证／依赖声明，但“作者自报”与“仓库运营方认证身份”分开；SCM 标签不证明二进制由该源码构建。许可 URL 只在已建立的官方许可来源及剩余预算内读取；存在未知时记录，不能把网站模板许可证当包许可证。

**禁止请求任何 AAR／APK／JAR／ZIP／模型／源码实现／源码归档／二进制／样本，包括用 HEAD、Range 或下载按钮试探制品存在性。** 可记录官方返回的制品链接或按已验证布局推导的对象描述，但明确标“未请求、存在性及内容未验证”。禁止云端 ASR、构建、加载、扫描制品、测试、集成、修改 Think 或恢复 sherpa 链。

### 必须产出的证据

下一单只在知识库新增一份 `cp2-vosk-android-maven-metadata-2026-09-06.md`（如跨日执行，文件日期使用实际执行日期），并必要更新 INDEX／追加 LOG；不覆盖旧三身份记录。文档包含：

- 输入合同及旧身份文件引用；完整累计 ledger：序号、用途、发现来源、尝试／最终 URL、时间、HTTP／错误、响应类型／大小、预算累计和重定向／重试；未知字段明示，失败不删除。
- 来源归属表：官方运营主体、验证页／交叉链接、Central 端点及布局规则；搜索发现与原页验证分开。
- 版本列表中的原值与唯一选定固定版本；POM 的 groupId／artifactId／version／packaging、继承或属性来源及一致性对照；所有字段注明 Observed、Derived（规范解析）或 Unknown。
- 项目／发布者／SCM／许可证声明、适用范围与未核定项；元数据中的发布信息不提升为法律批准。checksum／签名／SBOM若官方所读信息未给出，则 Unknown，不要求为这些可选字段耗尽预算。
- 元数据最小原文片段、响应或已允许保存证据的本地引用与 SHA；这里的证据 SHA 是元数据身份，不是 AAR SHA。保留允许的关键元数据证据，不只留下模型转述；不整页复制无关第三方正文。
- 唯一 RESULT、逐项验收、停止原因、剩余未知、Git归属；本 PM 最终答复给正式 path／bytes／SHA，不跨任务发送。

### 成功判据

全部满足才可返回 `identity_ready_for_artifact_intake_decision`：

1. 来源确认通过；官方 Central 元数据明确列出一个固定发行版本，groupId／artifactId 精确匹配。
2. 同版本 POM 内容与官方条目一致，`packaging=aar` 或存在同等明确的 Android AAR 发布声明；不能仅因名称含 android 推断打包类型。
3. 发布项目／维护者声明可追溯至已知 Vosk 官方项目；许可由该版本 POM或其获准父 POM／官方说明明确给出并保留适用范围，不从模型许可证继承。
4. 能写出唯一版本／坐标／打包类型及官方元数据入口，足以由后续产品决定精确描述拟取得对象；不存在未解决的版本、来源或许可冲突。
5. 全部请求、响应及未知可核查，且没有制品获取或执行。

没有官方制品 SHA 本身不强制失败；AAR字节、完整依赖许可、源码commit与可复现构建、签名有效性、ABI、CPU-only、JNI、内存PCM、动态隐私和设备表现均留给后续独立门禁。来源／身份／许可关键声明缺失则仍 `identity_insufficient`，不得改名为成功。

### 硬停止与权限

总请求／字节／等待上限、关键字段缺失、官方信息冲突、无法确认新域名、需登录／付费／额外条款、需第二父POM／第二候选版本／模型／制品或源码才能继续时停止。网络权限依系统审批处理，权限拒绝不绕过；普通渠道故障仅允许在本批次预算内使用已可用获准只读工具恢复，并完整计数。

Leader 验收本决定并独立下发下一单后，该单按整个批次执行，不为每页另造产品审批，也不要求用户重批普通公开只读研究。**本轮不开始任何查询。** 阶段 B 的精确制品取得与扫描、阶段 C 的构建／加载／集成／设备执行仍分别需要原有正式决定及精确授权，不能由 POM 验证自动继承。

## 保持不变与当前检查

三步录入／找回、按住说话、90 秒、原始音频不落盘／不上传／不进日志、云端仅接收转写文字、个性词表与专名90%保持。CP1父亲人工验证、Conformer及词表实现仍 Deferred, not removed；CP1人工在CP3准入前恢复；CP2未通过，CP3／父亲Alpha未批准。不改模型选择，不重开 sherpa 链。

本次只新增本决定及必要 PRD／INDEX／LOG 变更；旧决定、旧ledger、三身份文件不改，无联网，无Git提交。Think只读检查HEAD为 `92e5027852b8c2cb8476f7c2da684ef98f61ec82`、工作区clean。标准全库lint脚本缺失，使用元数据、本地链接、日志前缀和Git差异等有界检查，不声称全库自动通过。完成后停止等待Leader，不派开发者。
