# 决策：Vosk 集成缺口归并与下一元数据批次

Owner: Product Lead
Last updated: 2026-09-08
Source: `CP2-VOSK-INTEGRATION-GAPS-DECISION-001`；Leader阶段2verification.md及review.json；固定attempt的stage2-static-review.md和license-dependency-gaps.md；正式阶段2决定与PRD
Confidence: High（静态事实及未覆盖）；Medium（运行准入和许可仍待证据）
Related decisions: `cp2-vosk-stage2-scope-decision-2026-09-08.md`；`cp2-vosk-simplified-staged-review-decision-2026-09-08.md`；`prd-v0.1-2026-09-04.md`
Next review date: 2026-09-15
Research Quality: 90/100（沿用已验收身份及静态证据，不是完整安全评分）
Validation Level: V2（保持，无新增产品使用验证）
Next evidence: 一个合并官方依赖／变体／许可来源元数据批次，之后归并裁定运行准入缺口
Allowed next investment: Leader同步下发后的最多12次公开说明／元数据请求；当前不联网，不新增二进制取得或执行权限
Pause/Kill condition: 来源／许可关键声明矛盾、预算耗尽仍不足、需新制品／实现源码或目标执行才能继续时停止；采用门保持blocked

## RESULT

**APPROVED：仅批准下一唯一 `CP2-VOSK-DEPENDENCY-LICENSE-METADATA-001` 合并元数据批次。**

该批次把原建议8次扩大为**12次总尝试**，额外预算用于主runtime及模型的官方许可／来源说明，不为每页创建审批。JNA固定5.18.1、Vosk固定0.3.75、模型固定small-cn-0.22，不比较新版本／候选，不重取现有包，不下载JNA AAR。它是新研究合同而非旧ledger预算重置；原2GET制品取得与先前失败记录不改。

本轮只读报告制定范围，未联网、读取归档／二进制、执行静态工具、修改Think或派dev。两个对象继续manual_review，adoption_gate=blocked；元数据完成不自动批准集成或阶段3。

## 已验收事实与限制

Leader阶段2verification SHA=`1b5078bacdeb39193468dca5cae2ba3246f20953bcd16ca3ca38f96cba06f969`；stage2-static-review SHA=`8ee29bea985c049f946ebdd2aa4d4221d2d1489119fffec66287ec89c2d78f10`。Leader核对63项manifest及23静态工具记录，50条覆盖／27成员完整读取，39813709B展开／副本，零网络；这不是动态目标执行证据。

- 14类字节码显示三个数组acceptWaveForm重载转native、close/free和JNA Native.register；支持设计内存PCM边界，不证明marshalling、下层不落盘或资源释放正确。
- StorageService含模型资产文件复制／删除／路径日志；不能据此认定原始录音已落盘，但未来私有音频不得经过这类文件helper。
- 四库ELF身份为machine183/40/3/62及64/32/32/64位，arm64成员SHA=`06965ebb4e5eb3a9e4a815755e178d9553392e3fe8d3d368ac46952ad3694173`。实际包ABI信息不等于小米15兼容或CPU-only证明。
- arm64导入popen/pclose及文件／日志API，DT_NEEDED为liblog/libm/libdl/libc。导入表示能力或依赖，**不是执行过命令或恶意证明**；未命中socket等选定符号也不是无网络证明。
- AAR外层和一层JAR均无LICENSE/NOTICE；模型外层无LICENSE/NOTICE，完整native许可与训练来源未建立。POM／目录Apache2声明不能替代义务核查。
- JNA5.18.1实际未取得，.module未读；缺build-ID不是篡改证明。异常POM主页不访问、不信任。静态证据没有关闭可复现来源、隐私、准确率及性能。

## 一次归并缺口与时点

| 缺口 | 首次受控运行前必须具备 | 可留获准动态验证／残余风险 |
| --- | --- | --- |
| JNA／Gradle变体 | 固定实际需要的JNA坐标、类型、版本、变体约束及来源；若需新AAR，独立精确授权、取得身份与适当静态检查完成，不能让构建器自动下载 | 不要求本元数据批次闭合所有任意传递包；发现新增必要对象一次列清，未闭合则暂不运行 |
| runtime／模型许可 | 确定每对象适用许可声明、需要随包提供的notice／归属材料、与计划内部测试或分发用途的关系；关键权利冲突不得默认接受 | 不把没有LICENSE文件判违法；完整发布／再分发义务在分发前闭合。训练权利链若仍无证据，明确限制及必要Owner/法律处置，不模型自称法律批准 |
| native命令／文件／日志能力 | 固定受控入口和输入类型、模型路径／来源限制、禁止任意命令及原音频文件通道；针对popen可达性和影响输入给出有限证据或明确阻塞，不能靠符号无命中放行 | 日志实际内容、缓存、释放、文件／网络访问等在授权隔离动态实验中观察，不在静态阶段宣称通过 |
| JNA内存／生命周期 | 测试前明确数组长度边界、所有权、线程／close规则、模型数据与原始音频分离、错误处理方案及测试保护条件 | 正确marshalling、PCM全程内存、缓冲释放、重复close／竞态、异常恢复必须动态证据；无需先证明实验结果才能提出受控实验 |
| 来源／真实性 | 现有SHA固定对象，发布渠道可追溯，异常主页排除，关键来源冲突先解决；首次执行批准者明确已知来源局限 | 独立签名／可复现构建、缺build-ID、构建字符串可记录残余风险，不能据此自动要求无限源码闭包或称来源已认证 |
| CPU／准确率／性能 | 明确受控测试对象、设备、无原音频持久化边界及对应执行授权 | 普通话／父亲口音／词表专名90%、CPU-only、30秒P95／90秒／连续20次、耗电温升、飞行模式按PRD测试；未达标不能CP2通过 |

“可记录残余风险”不等于本PM已替用户接受全部风险：Owner／Leader后续运行准入决定需逐项注明可接受影响、限制和理由。不得接受原音频落盘／上传／日志等产品硬边界的违反，也不以一次授权把集成、受控验证和父亲Alpha合并。

## 下一唯一批次合同

任务ID：`CP2-VOSK-DEPENDENCY-LICENSE-METADATA-001`。目标：用官方公开说明／元数据输出一个依赖身份表、两个主对象许可来源处置表和剩余缺口清单，不取得任何新二进制或源码实现。

### 来源与固定范围

1. 已核官方Central root与布局、已有Vosk POM／报告作为本地起点。可按已核布局及固定字段确定性生成**JNA5.18.1 POM**；不读版本latest、不换版本。POM项目／组织／SCM是发布者声明，须与所发现官方说明交叉核对，不能把任何URL自动当可信。
2. Vosk0.3.75的`.module`只有原POM提示，精确路径须由已核官方Gradle／Central规范或页面直接链接建立后才请求；不得猜地址存在。只作有界JSON数据读取，不调用Gradle、依赖解析器或构建。记录variant、dependency、constraint、files摘要原值；摘要不是已下载对象校验，发现新对象只登记，不访问文件URL。
3. 主runtime许可来源仅`alphacep/vosk-api`官方README／LICENSE／NOTICE及官方发布说明；来源或版本关联明确写Observed/Unknown。若只能取得master的LICENSE，不外推为0.3.75具体二进制及全部捆绑Kaldi/FST许可。最多引用官方提供的组件说明，不追实现代码或层层依赖。
4. 模型只查Alpha Cephei已核官方模型目录及其直接提供的本模型许可／来源说明；不读zip、不重新校验下载、不找替代模型。通用Apache许可可以解释许可条款，但不能证明某模型权利链或把未发布说明补为事实。
5. 允许官方JNA项目／Gradle规范／Apache许可说明页的来源建立，先读公开关于／官方交叉链接，记录主体与域名；搜索仅导航、摘要不作最终证据。POM异常主页`alphacephei.com.com`绝不作为来源。无法核定官方归属则停止该分支并记录不足，不用镜像、论坛或名称相似替代。
6. 包括LICENSE／README的文档路径可以读取；源码实现、源码树遍历、AAR/JAR/ZIP、sidecar／签名／公钥、私有材料不在本批次对象内。仅允许上述元数据与文本说明；许可页若引导新的代码下载，不跟随。

### 一个预算，不逐页审批

- 总计最多12次请求尝试（搜索、失败、重试、显式跳转均计入）。计划JNA及来源3、.module及规范3、runtime/model许可4、恢复2；可在总额内调整，不变更对象和目标。
- 每请求正文1MiB、全批5MiB、每次30秒；失败／跳转正文也累计，无无限retry、自动分页或隐式依赖请求。必要恢复最多2次，仍占12次，TLS或权限拒绝不得绕过；来源未知则停止，不猜域名。
- 一份固定JNA POM、一个Vosk.module、最多一个必要直接父POM用于补身份／许可；不递归父链或依赖POM，不查第二版本。文本许可可以读取但不下载实现。
- XML拒绝DOCTYPE／ENTITY和外部schema加载；JSON只解析数据。每页保留实际URL／日期／HTTP／类型／bytes／来源链、完整关键metadata或必要短原文及SHA，未能读取字段Unknown。
- 成功即停，不为补可选字段耗尽预算；全批时间最多45分钟（含本地整理），达到边界就输出结果，不延长成新一轮自动研究。

### 产物、结果与验收

下一单新增知识库`cp2-vosk-dependency-license-metadata-实际日期.md`及必要INDEX/LOG；保持旧静态reports、两个包与旧决定只读。正文包含完整ledger、JNA固定身份及所需新AAR精确授权准备字段、Vosk.module与已有POM差异表、runtime和model分别许可／NOTICE／来源表、事实/推断/未知、冲突及运行前处置清单。

RESULT只能为`metadata_batch_complete`或`metadata_insufficient`：前者要求请求范围完成，关键身份／变体／许可声明有来源或明确官方未提供位置及其阻塞影响；后者用于来源冲突、预算耗尽或关键字段无法核定。**两者都不代表许可完全闭合或运行准入**；每个缺口单列open/resolved及证据，不能用“批次完成”隐去不可运行状态。

新JNA AAR URL／官方摘要如有仅作为后续精确请求草案，不本单GET/HEAD/Range。未来取得仍须适用的精确用户授权，不能套用Vosk/模型授权。研究普通公开元数据已由本范围批准，不再逐页询问；本PM当前不执行任何查询。完整结果供Leader独立验收，然后一次归并下一步，不自动取得或集成。

## popen/pclose：后续有限包内核查建议

本元数据批次不能解决机器码可达性。为首次受控运行前提供论证，后续可由Leader单独下发固定已取得arm64成员的有限核查，不与当前唯一批次并行，不本轮读取二进制。

建议上限：只SHA `06965ebb4e5eb3a9e4a815755e178d9553392e3fe8d3d368ac46952ad3694173` 的libvosk.so及阶段2已有包装层输出，最多4小时、20次静态工具调用、每次120秒、单输出16MiB／总128MiB。先定位popen/pclose直接交叉引用，再从已经定位的模型构造／acceptWaveform／grammar受控入口核对关联；最多两层调用关系、最多12个有关函数。若直接引用或必要图超界则返回具体Unknown，不声称不存在、不得追新源码／第二库或恢复sherpa链。

核查问题限定为：调用位置与条件、命令字符串来源、外部模型路径／配置／grammar是否可能控制输入、受控测试可否以固定可信模型路径和受限API避开该路线。需区分直接调用、PLT／间接调用未解析、输入约束假设；没有完整证据时不得称不可达。可用现有LLVM静态工具，不加载目标、不执行shell、不下载源码。

未闭合命令输入风险时继续阻止运行；若只能在动态观察中验证，则须另立受控验证方案与执行授权，先限定合成音频、可信模型、无私密数据、无目标任意网络／文件写入边界。此处不代用户批准任何执行，不以需要动态验证为由放宽原音频隐私。

## 同步、历史与不变量

最小产品文档同步四项：本决定→Think `doc/cp2-vosk-integration-gaps-decision-2026-09-08.md`，最新PRD→`doc/prd-v0.1-2026-09-04.md`，`AGENTS.md`及`doc/README.md`入口注明阶段2已验收但manual_review、下一仅元数据批次、新AAR及运行未授权。不复制整库、不改变旧证据；Leader统一下发同步，PM不改Think。

原始音频不落盘／不上传／不进日志、云端只接收文字、三步／90秒、专名90%及PRD真机性能阈值均不变。CP1人工／Conformer／词表实现Deferred, not removed；CP1人工须在CP3前恢复。CP2未过、CP3／父亲Alpha未批准、阶段3执行未自动批准。缺LICENSE、build-ID、popen导入均按证据范围解释，不宣称恶意或安全。

## 身份绑定与本轮检查

task_id=`CP2-VOSK-INTEGRATION-GAPS-DECISION-001`；attempt_id=`8d5bc8f3-160a-4fa3-a054-fd41d4d17a68`；contract_sha256=`2cdf2d79235dc482729f8edaed41ac6327427504b91c5ad6d104e223617cccfb`；assigned_thread_id=`01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779`。

本轮只报告读取和四份知识文件写回，无新网络、二进制读取或工具解析目标、安装／构建／集成／产品修改／提交。元数据／本地链接／LOG前缀及差异核对；全库lint脚本仍缺失，不声称全库通过。阶段2静态受验收不提升Validation Level，采用保持blocked；完成极简回调实际拒绝不重试，完整原始结果留本PM最终答复。
