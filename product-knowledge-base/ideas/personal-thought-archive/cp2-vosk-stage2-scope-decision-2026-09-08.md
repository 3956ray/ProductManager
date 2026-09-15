# 决策：Vosk 阶段2包内静态审查范围

Owner: Product Lead
Last updated: 2026-09-08
Source: `CP2-VOSK-STAGE2-SCOPE-DECISION-001`；Leader阶段1verification.md及review.json；固定attempt的stage1-review.md与runtime/model-inventory.json；最新简化分阶段决定；PRD
Confidence: High（已验收取得／外层证据）；Medium（内部代码／许可／动态能力未知）
Related decisions: `cp2-vosk-simplified-staged-review-decision-2026-09-08.md`；`cp2-vosk-artifact-review-scope-decision-2026-09-06.md`；`prd-v0.1-2026-09-04.md`
Next review date: 2026-09-15
Research Quality: 90/100（沿用已验收来源身份；新增阶段1事实有Leader独立核验，不是安全评分）
Validation Level: V2（保持，尚无真实产品使用证据）
Next evidence: 同步本决定后执行一个固定SHA包内离线审查单；新对象仅列有界后续身份准备建议，不在本单取得
Allowed next investment: 一项最多一个工程工作日／8小时的现有包内静态审查，不联网、不安装、不加载目标，不实施通用扫描器
Pause/Kill condition: 输入身份不符、危险结构／资源硬停止或必须执行目标才能继续时停；外部依赖／许可缺口不阻止其他已授权包内核查，但继续阻止集成

## RESULT

**APPROVED：下一唯一任务 `CP2-VOSK-STAGE2-INPACKAGE-STATIC-REVIEW-001`，仅现有固定SHA包内离线审查。**

本决定依据用户已批准分阶段方向，具体化阶段2可用现有包完成的工作；Leader验收并同步下发后执行。当前PM只读reports制定范围，未读取归档／二进制、联网、下载、解析目标或改Think。没有重取旧对象、JNA/.module权限、阶段3执行或自动集成授权；adoption_gate始终blocked。

## 阶段1事实，不扩大结论

Leader review.json verdict=accepted；verification SHA-256 `4c013d1a4b36ad56d43c8080725f99f87e9574593b6bd961bd0d27840e43fa77`；stage1-review SHA-256 `f58b0d3a7b26463496f03d755d84d6238295559350e254f38a6d4d9f0e98eb95`。

| 对象 | 已取得实际bytes／SHA-256 | 已核查覆盖 |
| --- | --- | --- |
| AAR0.3.75 | 13472638；`ab2f8b91ac8051561aa325546b35fed9a68b36b8121bac5c6fb927525c4adfad` | 13外层成员／8普通文件，1个properties完整读156B并核CRC |
| small-cn-0.22 ZIP | 43898754；`3af8b0e7e0f835ae9d414ce5df580237a3cfb08d586c9fbbb0f7ff29ad5b14ba` | 20外层成员／14普通文件，5个选定文本完整读559B并核CRC |

共2个直接HTTP200 GET、57371392B，无retry／redirect，取得及初查130.165秒。所选文本合计715B；Leader另行重读715B为独立复核成本，不冒充开发者原 tally。两个unpacked未提取内容。其余二进制CRC、代码及动态行为未知。

两包**没有外层LICENSE/NOTICE条目**，不是“完整许可已缺失”或“无再分发义务”的证明；嵌套许可尚未知。AAR外层含Manifest、classes.jar及4个命名ABI目录的libvosk.so；目录名不证明实际ABI或可用性。模型声明16000Hz、README基准CER不等于小米15／专名90%验证。实收SHA固定bytes，不是独立发布者认证；同响应MD5/SHA1不是签名。

## 输入与输出固定边界

原attempt根：`/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/attempts/07a96480-78dd-4040-8d30-5bc8d44a7ed0/`。

- A输入：原根`artifacts/runtime-1-0.aar`，严格匹配上表bytes/SHA。
- B输入：原根`artifacts/model-1-0.zip`，严格匹配上表bytes/SHA。
- 证据输入：原根`reports/`及已验收Maven报告内POM／元数据、模型身份记录、最新PRD。不能读取其他历史制品、源码快照或私有语音数据。
- 输出：在原授权大根`attempts/`下独占创建Leader本次下发的UUID attempt子目录，`work/`与`reports/`分开；不写入原stage1 attempt。目录0700、普通文件0600、无执行位，不覆盖、不跟随链接。可按安全路径规则临时解包已授权成员，沿用用户简化允许，不重新要求全内存解包或1GiB硬隔离。
- 工作前后重新计算输入SHA，任何变化立即停止，不联网“修复”或重取；输出对象／成员SHA与输入链绑定。旧证据不删除、不改写、不在旧文件补签。

## 单批次检查顺序

### 1. AAR Manifest与嵌套JAR

先按现有外层清单核安全路径，再完整读取Manifest和classes.jar，读完整成员核CRC／SHA。Manifest若为文本则安全XML解析，拒绝外部实体／schema获取；若二进制格式，使用现有可信解析工具，不能为此安装新包。记录package、minSdk等实际声明、组件／权限、资源引用；manifest声明不等于动态行为，也不把缺权限当绝无网络或文件访问。

仅进入**一层classes.jar**，列出完整条目、class名、包名、META-INF与许可。可用现有可信javap／反汇编／静态反编译工具读取class文件，目标仅作为数据，不把其加入可执行classpath、不反射／实例化，不调用gradle或目标类。优先回答：Vosk包装层公开入口、内存byte/short/float音频与文件路径接口、模型构造／释放、词表／grammar参数、日志／网络／临时文件／动态加载调用或引用。每条结论绑定类／方法／指令偏移及原文片段，区分声明、可见调用与未知下层行为。

包内出现其他嵌套归档只清单和大小，不递归追链；若无法覆盖classes.jar某类／方法，报告Unknown，不制造通用扫描平台。不调用工具自动拉依赖、反编译器更新或插件安装。

### 2. Native静态身份和有限能力

原清单四个libvosk.so分别为arm64-v8a、armeabi-v7a、x86、x86_64路径；先用实际文件头确认ELF class、machine、endianness，记录工具识别，不以目录推断。四库各自记录成员bytes/SHA、构建标识（如存在）、导出／导入符号、DT_NEEDED和可见来源／许可证线索。不能用ldd等可能执行加载的工具；可用现有readelf／llvm-readobj／安全静态工具组合，不dlopen、不调用JNI。

能力深入重点为arm64候选，但其他ABI身份不静默跳过。对文件操作、网络、日志、库加载、音频输入／缓冲释放等符号或字符串分类：只出现字符串标“字符串线索”，导入符号标“静态依赖”，若现有反汇编能建立局部调用则写局部关系及覆盖范围；不能宣称实际上传／落盘／内存释放正确、CPU-only完全证明或无隐蔽行为。DT_NEEDED缺库只登记，不下载。

不要求完整逆向4个库或证明全部机器码无害；被剥离符号／混淆／不支持格式留下明确覆盖缺口，必要时manual_review。发现危险结构或明确恶意执行链则block并停止，不把库含标准文件API自动判恶意。

### 3. 许可、模型来源及交叉表

- 在AAR已授权嵌套META-INF、Manifest／properties／可见native字符串查找LICENSE、NOTICE、作者及组件来源；保留实际内容和缺失位置，与已保存POM的Apache2声明对照。不能以网上通用Apache许可或POM一行代替包内和再分发义务。
- 模型使用既有报告及包内README／conf／已发现的普通文本线索补查来源、采样／路径声明及许可。只需有选择地读与来源／配置相关成员；不加载声学模型、图或ivector，不训练／转写，不为CRC全覆盖读取无关模型二进制。未读二进制的CRC和内容继续Unknown。
- 列包内已有组件与外部声明依赖的关系；JNA5.18.1是POM声明，未读.module可能补充变体／约束。包内如果包含同名组件也不能自动推定等于该坐标，必须依内容身份证据。
- 异常主页`alphacephei.com.com`保持不信任／不访问、不自行改错；签名真实性、模型训练权利、源码commit与可复现构建继续Unknown。许可／来源缺口单独列为集成阻塞，不因此阻止其他包内可完成检查。

## 预算、工具与停止

| 项目 | 本单上限与解释 |
| --- | --- |
| 网络／新增取得 | 0请求、0下载；无原对象重取、sidecar或许可网页 |
| 工程工作 | 最多8小时，一个审查批次；不是8小时工具开发；不得重开16小时adapter |
| 归档成员 | 外层及一层JAR合计最多10000条；各层同一计数，重复检查如实计成本 |
| 展开与提取 | 全单实际展开读取512MiB、单成员128MiB、磁盘工作副本256MiB；重复展开也累计，不只核声明；高压缩比warning、实际上限硬停 |
| 文本／工具输出 | 单文本2MiB、文本累计32MiB；单工具输出16MiB、报告／工具输出合计128MiB，截断明确partial，不伪完整 |
| 进程 | 每次静态工具调用最多120秒，单制品累计解析墙钟30分钟；超时终止、不自动重复同一失败命令；保留未覆盖 |
| 隔离 | 优先已有沙箱，分块读、有限输出、无目标执行；不强求未提供的1GiB系统硬限额，不把“不主动联网”写成系统禁网证明 |

路径越界／绝对路径／链接／重复和大小写冲突／加密／损坏或CRC错误、实收SHA不符时硬停；已读成员CRC与未读Unknown分开。安全解包逐成员检查最终路径在新work根内，拒绝覆盖和特殊文件，不通用extractall，不保留执行位。不提取到Think／依赖缓存／IDE目录，不上传外部扫描服务。

使用已有可信静态工具组合和少量本任务局部命令／配置即可；工具先记录版本／来源，不运行目标提供的程序。工具某项不可用时可改用已可用等价工具；仍不足则记录具体未覆盖，完成其他独立包内工作，无安装或开放式工具工程。资源／结构硬停止后不继续消耗目标；只是外部许可／依赖不足不作为阻止本单其余静态检查的借口。

## 新对象与未来权限，不在本单执行

现有包内字节审查由本阶段范围明确允许；首阶段网络授权不能继承为任何新增取得。报告仅产出以下**后续准备建议**，不是同时下发第二任务：

1. 若集成需要JNA5.18.1和对应Gradle变体，提出一个合并的官方发行身份／许可元数据批次，最多8次只读请求、单响应1MiB、总5MiB／30秒；只核`net.java.dev.jna:jna:5.18.1`与既有Vosk0.3.75的.module，不查其他版本／依赖树。具体域名／URL需按官方证据核定，不能在本轮猜造；这批次须Leader以后正式下发，当前0请求。
2. 即使元数据身份核定，JNA AAR等新制品仍须精确对象授权后才能取得；不能借“只读研究”下载库。许可网页／新源码／公钥不在首阶段或本单权限中，后续应明确限定官方来源及字段，不无界扩链。
3. 源码可复现性、模型来源权利是否需要进一步证据，由Leader／产品根据本单缺口一次归并裁定，不逐符号／逐页审批，也不无条件要求先闭合未知未来对象才读现有classes.jar。

## 交付和验收

输出`stage2-static-review.md`、`coverage.json`、`license-dependency-gaps.md`、`evidence-manifest.json`及有界原工具输出；绑定每个输入包SHA和具体成员SHA、来源报告、工具／命令／时间／返回码、类方法或符号位置、CRC状态、实际预算与未知。最小记录包含：

- 已检查什么、未检查什么及原因，不把文件名、字符串或声明升级为运行行为。
- classes.jar／Manifest覆盖，四native身份及arm64有限能力证据，模型文本来源与许可交叉表。
- 缺LICENSE／NOTICE证据的范围，以及JNA/.module、训练来源／签名／二进制出处等集成阻塞清单。
- 每对象`manual_review`或`block`等限定静态结论；未命中只能`low_indicators_in_covered_scope`，不能safe。采用门固定blocked。

任务RESULT=COMPLETE表示已完成可执行包内批次并交付覆盖／未知，不要求消除外部依赖许可缺口；若必要输入无法读取、关键结构风险、资源触发或核心包内项完全无法核查则BLOCKED，明确已完成部分。无论哪种，Leader独立验收后才能决定下一范围，不能自动集成或执行。

验收逐项：两个输入SHA一致且未重取；nested／Manifest／native与许可有原证据或具体不可用项；观察／推断／动态未知分离；所有工具不执行目标且无新网络对象；目录不覆盖、预算／CRC覆盖可核查；集成缺口与新授权需求明确。不得因扫描分数或一个native无命中声称供应链全通过。

## 同步清单与产品不变量

Leader下一同步单最少四文件：本决定原字节复制到Think `doc/cp2-vosk-stage2-scope-decision-2026-09-08.md`；最新PRD复制到`doc/prd-v0.1-2026-09-04.md`；`AGENTS.md`与`doc/README.md`只更新阶段1已验收、阶段2包内范围、禁止新增取得／自动集成入口。INDEX／LOG不复制；旧决定和预检不改写。本PM不派dev、不修改Think。

原音频不落盘／不上云／不进日志、云端仅文字、三步路径／90秒、专名90%、小米15 PCM／准确率／性能／稳定性／飞行模式等仍按PRD独立验证。CP1父亲人工／Conformer／词表实现仍Deferred, not removed；CP1人工须在CP3准入前恢复。阶段3执行未授权、CP2未过、CP3与父亲Alpha未批准，sherpa链不恢复。

## 本轮身份与核对

task_id=`CP2-VOSK-STAGE2-SCOPE-DECISION-001`；attempt_id=`c74bc093-5656-4a8e-99b6-726bd59dccdf`；contract_sha256=`8b335bd2ee7187e8f7552e893c702ddf3ff84841b244530f31fb9784b5c85288`；assigned_thread_id=`01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779`。

本轮只读阶段1reports及正式规则，不读取输入包或实施静态工具。新决定＋PRD／INDEX／LOG，旧研究／对象／reports只读，无网络／下载／Think修改／提交。元数据、本地链接、LOG前缀和差异检查；全库lint脚本缺失，不声称全库自动通过。回调仅极简完成通知，实际失败则停止不重试，原始最终报告保留供Leader核验。
