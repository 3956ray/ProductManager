# 决策：Vosk 简化分阶段审查

Owner: Product Lead
Last updated: 2026-09-08
Source: 用户决定 `/Users/orderly_ray/Leader/orchestration/decisions/2026-09-08-simplified-staged-review.md`；`CP2-SIMPLIFIED-STAGED-REVIEW-DECISION-001`；既有制品范围、零GET预检与PRD；已验收Maven元数据和模型目录身份
Confidence: High（用户范围决定）；Medium（首阶段执行和安全能力待证据）
Related decisions: `cp2-vosk-artifact-review-scope-decision-2026-09-06.md`；`cp2-vosk-tool-gap-decision-2026-09-08.md`；`prd-v0.1-2026-09-04.md`
Next review date: 2026-09-15
Research Quality: 90/100（沿用已验收元数据研究；不代表本次安全检查通过）
Validation Level: V2（保持）
Next evidence: Leader验收并同步本决定后，下发唯一首阶段取得与有限初查任务
Allowed next investment: 使用现有工具完成下述首阶段；不实施16小时adapter、不新建扫描平台、不自动进入集成或真机
Pause/Kill condition: 来源／结构／实际展开／时间边界触发或必须新增对象／执行目标时停止，已读与未读覆盖分别记录

## RESULT 与优先级

**APPROVED，落实用户已批准的简化、分阶段规则。** 用户原话“可以按照你的简化规则来进行 你记得同步给pm和dev 可以分阶段”，归档同时保存对应逐项简化。原两个精确对象授权与此次变更类别批准共同作为执行范围依据；不重复要求用户确认有限重试、核实HTTPS跳转、安全临时解包、新attempt目录或取消1GiB硬隔离前置。

本决定是未来执行的最新规则，优先于旧严格制品范围及工具缺口决定中冲突的要求。**`CP2-VOSK-BOUNDED-STATIC-ADAPTER-001` 不下发、不实施。** 原16小时提案、原每对象一次GET／零跳转／全内存解包／1GiB硬隔离规则及预检BLOCKED、零GET、两对象not_acquired均保留为历史，不改写原证据、不将旧失败改成通过。

当前PM仅写回决定及入口，无联网、下载、工具实现或Think修改。Leader同步正式文档和下发首阶段之后执行者才能工作；无需再开启逐页面或逐小步产品审批。环境自身权限拒绝仍须遵守，不绕过。

## 逐项变更

| 项目 | 处理 | 当前规则／残余风险 |
| --- | --- | --- |
| 对象、官方版本、TLS、实际bytes/SHA | 保留 | 只限两个原对象，官方SHA未知不编造；自行计算SHA只固定实收bytes |
| 每对象一次GET、任何跳转即停 | 简化 | 每对象最多2次尝试、每次最多2跳、总最多12个HTTP GET；仅下述核实来源、等价对象HTTPS规则；重试不证明内容可信 |
| 下载／读取／时间 | 保留且具体化 | 64MiB/响应、256MiB全单网络正文；每次尝试180秒，首阶段全单30分钟；旧精确header限额不再阻塞 |
| 必须全内存解包 | 简化 | 新attempt内先检查路径／链接／结构再按成员限额流式安全提取，禁止通用extractall或执行；解析器与文件系统残余风险披露 |
| 必须证明1GiB系统硬限额 | 简化 | 不作为首阶段前置；分块读、文件／展开上限、超时终止，优先已有沙箱；无强隔离不可称已隔离 |
| 高压缩比 | 简化 | 大于100:1记warning，不单凭比值判断恶意或失败；实际展开限额仍硬停止 |
| 归档路径、链接、损坏 | 保留 | 越界、绝对路径、链接、重复／冲突、加密、损坏等停止，不任意解包 |
| CRC | 分层 | 完整读到EOF的成员核CRC；未完整读成员Unknown，不能宣称全包CRC验证 |
| 嵌套JAR／Manifest／native深入审查 | 延期到阶段2 | 阶段1仅清单和可读许可／配置；未反编译／未读代码明确Unknown |
| 依赖许可、.module、来源可复现性 | 延期／保留风险 | JNA5.18.1与.module未审，不自动取得；不以主AAR初查替代完整闭包 |
| 旧目录存在即不能继续 | 简化 | 原授权根下创建不覆盖的新attempt子目录，旧报告／ledger原样保留；不删除旧根 |
| 运行、安装、集成、模型推理 | 不授权 | 阶段1禁止；后续阶段分别定义适用范围及授权 |
| CP1／CP2／CP3、隐私和专名90% | 保留 | 初查完成不是安全／采用通过，adoption_gate仍blocked |

## 阶段1唯一执行合同

任务ID：`CP2-VOSK-STAGE1-ACQUISITION-INSPECTION-001`。

目标：串行取得原AAR和原模型ZIP，记录来源、实收bytes/SHA、外层目录、基本结构／路径和许可信息，输出明确覆盖及阶段2待办。只用现有curl、标准库、安全归档读取器等已可用组合，必要少量配置或本任务局部辅助代码可以直接在本单完成；不安装第三方、不改全局skill扫描器、不扩成通用平台。若基本限额无法落实则停止，不要求完成万能扫描器后才能进行有限初查。

### 对象与取得边界

| 对象 | 固定起始URL | 身份与限制 |
| --- | --- | --- |
| A：com.alphacephei:vosk-android:0.3.75 | `https://repo.maven.apache.org/maven2/com/alphacephei/vosk-android/0.3.75/vosk-android-0.3.75.aar` | 已核定Central＋布局＋POM派生；尚未请求，存在性／官方SHA／实际大小未知，Apache2仅POM声明 |
| B：vosk-model-small-cn-0.22 | `https://alphacephei.com/vosk/models/vosk-model-small-cn-0.22.zip` | 官方模型目录直接href，42M／Apache2仅目录声明；实际内容／SHA未知 |

先A后B，独立裁决。A仅因缺LICENSE／NOTICE、二进制未深读或来源未知需人工复核时可继续B；来源／身份／结构／资源硬停止时不再取得B。异常主页`alphacephei.com.com`不访问、不信任、不纠正。JNA5.18.1、.module、sidecar、公钥、SBOM、源码、模型替代品均不在本单网络对象内。不得HEAD／Range试探或自动解析依赖。

### 重试和跳转，一批定界

- 每对象最多2次完整取得尝试（首次＋1次恢复）；仅连接失败、连接中断或HTTP408/429/500/502/503/504可恢复。一次恢复最多等待10秒；Retry-After大于10秒则停止，不长时间挂起。不重试404、权限拒绝、TLS校验错误、类型／身份／结构异常或资源越限。
- 每次尝试最多2个HTTPS重定向，共最多3个GET；全单最多4次尝试／12个GET，所有跳转／失败／重试均记录并计入。不得开启无界自动-L／retry；每跳核验后请求，不需逐跳用户批准。
- 允许HTTP301/302/303/307/308的Location；仅HTTPS、默认443、无userinfo、无片段，不改变固定对象路径或增加查询参数。A只允许`repo.maven.apache.org`，B只允许`alphacephei.com`；相对Location按当前URL解析后仍须满足以上规则，循环停止。
- 这是“核实来源HTTPS跳转”的具体有限实现，不开放任意CDN／镜像。新host或对象路径变化没有现有证据可预先确认，记录Location后停止而非猜官方归属；该限制无需为已允许同源等价跳转再审批。
- 每响应正文64MiB，全单所有响应／失败残片累计256MiB；跳转错误正文也累计。每次尝试含跳转的墙钟180秒、连接等待最多15秒；单响应计时不得每块重置。到边界即停，不下载完再裁剪。Content-Length有则检查上限与实收一致性，无则实际流式计数。
- 使用TLS校验、官方URL及ZIP签名／结构交叉核对响应；预期ZIP或octet-stream等合理类型，HTTP非200最终结果、HTML登录／错误页、非ZIP、截断或异常类型停止。响应头记录所需字段，采用现有客户端正常限制，不为精确64KiB头限额另造工程；异常头或解析失败即停，并披露未单独证明精确头硬上限。
- 新attempt内每次尝试分别保存文件和ledger，重试不覆盖失败残片；中断文件标partial，不扫描成完整制品。成功后立即记录实际bytes和SHA，再进入有限初查。

### 隔离目录与基本资源保护

在原根 `/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/` 下创建 `attempts/<Leader下发的attempt_id>/`，值只允许安全UUID字母数字和连字符，独占新建；原根既有不等于可覆盖。内部`artifacts/`、`unpacked/`、`reports/`各自分开，目录0700、文件0600，检查父路径无符号链接，旧预检文件只读。这项子目录变更已由用户批准，不重复询问，不删除旧证据“重来”。

- 每对象外层成员数最多10000，全单20000；含目录条目。先核归档目录大小与路径，使用实际输出流累计展开：每对象512MiB、全单1GiB、单成员128MiB。实际读取及重新读取成本都入账，不以内层／工具切换重置预算。
- 阶段1不递归解开JAR或模型嵌套归档：外层JAR作为普通文件列出，可安全提取但不执行；阶段2再按独立范围检查。不要把“未展开嵌套内容”当格式已安全。
- 许可／NOTICE／可读配置：每文件读取最多2MiB、全单文本32MiB；超过不强制全读，标部分覆盖，不能声称完整CRC或许可闭合。对选择完整读取的成员核CRC；其他成员列not_read／partial和原因。
- 安全提取先拒绝绝对路径、`..`、盘符／UNC、控制字符／NUL、规范化后或大小写碰撞、同名重复、符号／硬链接、设备、加密及不支持特殊类型；只创建目录和普通文件。逐成员确认最终路径位于新unpacked根，拒绝既有文件／链接，不保留执行位，不执行post-extract。不调用未核路径的通用extractall。
- 声明展开量超限、实际越限、CRC错误、中央目录／本地头不一致或异常结构停止；只有高压缩比本身记warning，实际展开和时间约束照常。声明不代表真实内容已验证，完整与未完整读取分别记录。
- 每对象有限初查墙钟最多10分钟，全单（取得、恢复、初查）最多30分钟，超时终止当前操作并保留结果，不自动续跑。用现有进程超时与分块读取，避免整包载入内存；优先已有沙箱，记录工具／配置与限制。不要求1GiB硬隔离证明，但必须报告未强制内存隔离的残余风险，内存／磁盘异常时停止。
- 不主动在静态阶段联网；若环境没有强制断网，不声称“已阻断所有网络”。不执行目标、导入目标、不启动构建器／IDE任务、不加载模型／native库，不上传公共扫描服务。任何工具对目标的执行需求都超出本单。

### 初查内容与交付

每对象记录完整外层清单（名称、压缩／展开声明、类型、实际读取bytes、CRC状态、SHA如已完整读、未覆盖原因）；检查顶层版本／名称线索、LICENSE／NOTICE／元数据声明、可见配置和可疑外部引用。存在脚本不等于运行过，出现网络字符串不等于实际上传；原文证据和推断分开。

报告独立标`basic_inventory_complete`、`manual_review`、`block`或`not_acquired`。`basic_inventory_complete`仅表示首阶段要求完成且未发现阻止继续记录的基本结构问题，不是安全合格；未审二进制、许可或来源仍可随其存在。路径逃逸／损坏／明确恶意结构为block，超预算或工具无法完成为manual_review＋hard_stop，均禁止自动继续B。

单任务最终RESULT为COMPLETE（两个对象首阶段结果可核查）或BLOCKED（硬停止未完成）；同时必须保留`adoption_gate=blocked`。输出`acquisition-ledger.json`、`runtime-inventory.json`、`model-inventory.json`、`stage1-review.md`，附工具版本／请求与跳转链／累计预算／原许可摘录／coverage表及每对象实际SHA。未取得B时照实写not_acquired。汇总下一阶段需要检查的嵌套JAR、Manifest、native、JNA／.module、完整许可及来源未知，不获取它们。

合格证据：两对象身份与来源一致；实际次数／bytes／展开／时间不超界；新目录不覆盖；结构路径检查有结果；CRC覆盖如实；未知明确；零目标执行／依赖下载。少量必要辅助配置可用几个本地合成路径／超限／重定向策略案例验证，属于同一执行单，不重开16小时工具项目。完成后停止，不能自动安装或集成。

## 后续阶段，不在首阶段执行

| 阶段 | 责任与准入 | 证据要求／权限 |
| --- | --- | --- |
| 1 取得与有限初查 | Leader同步后下发dev；PM此刻仅落档 | 以上合同；原对象授权＋本次简化批准，无重复逐步产品审批 |
| 2 集成前静态审查 | Leader基于阶段1结果组织独立范围与审查，PM裁定覆盖缺口 | 使用现有工具分别检查嵌套JAR、Manifest／JNI／native、实际ABI／导入能力、依赖／变体／许可／NOTICE和来源风险。不要求一个万能扫描器；新增JNA／.module等取得仍需适当授权，首阶段不隐式覆盖。不得以未审二进制或无命中宣称安全；是否可集成须单独裁定 |
| 3 CP2实际产品验证 | 阶段2及对应执行授权满足后，dev执行、Leader独立验收 | 小米15、内存PCM、原音频不落盘／不上云／不进日志、释放／缓存、中文口音／专名90%、30秒P95／90秒及连续20次稳定性、RAM／耗电／温升、飞行模式和异常恢复；按当前PRD阈值，不在本决定新编性能数字 |

初查不要求证明二进制可复现，但来源／签名／完整许可风险必须留在采用评估中，不能默认为已闭合。CP1父亲人工、Conformer及词表实现仍Deferred, not removed；CP1人工须在任何CP3准入前恢复。三步录入／找回、按住说话、90秒、云端只接受文字及所有隐私和Checkpoint门槛不变。CP2未通过、CP3与父亲Alpha未批准，sherpa终止链不恢复。

## 最小正式同步清单

下一同步单由Leader派dev，PM不改Think：

1. 知识库本决定 → Think `doc/cp2-vosk-simplified-staged-review-decision-2026-09-08.md`，保持相同bytes/SHA。
2. 知识库最新 `prd-v0.1-2026-09-04.md` → Think `doc/prd-v0.1-2026-09-04.md`，保持相同bytes/SHA。
3. Think `AGENTS.md`、`doc/README.md` 必要入口更新：最新分阶段规则优先、adapter不下发、第一阶段不等于采用／CP2通过、原零GET保持历史。

INDEX／LOG留知识库，勿复制整库或删除旧决定。同步文档中的相对历史引用保持可追溯；若缺历史链接目标，仅记缺口或采用已有正式引用，不以同步为由扩范围拉取制品。Leader核验同步后可直接按用户已批准规则下发首阶段，不插入重复用户确认链。

## 本轮身份与检查

task_id=`CP2-SIMPLIFIED-STAGED-REVIEW-DECISION-001`；attempt_id=`0d005a32-4746-41cf-8051-d0f35fa713d1`；contract_sha256=`6ff0f899ee94b9214ac72e141f19f6319a3423882aa258b3e7408a90b7166d39`；assigned_thread_id=`01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779`。

本轮新决定＋PRD／INDEX／LOG，旧严格范围、工具提案、用户授权和零GET预检均只读；无下载、网络研究、工具实现、Think修改或Git提交。元数据／本地链接／LOG原前缀及差异检查；标准全库lint缺失，不声称全库自动通过。完成通知受实际工具权限约束，不将失败回调记成功；原始最终报告保留供Leader读取。
