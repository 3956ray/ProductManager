# 决定：Android arm64无私密数据先行实验，执行暂缓

Owner: Product Lead
Last updated: 2026-09-09
Source: CP2-CONTROLLED-RUN-PLAN-001及用户仅确认制定方案的上下文；下列固定本地静态／验收报告；现行PRD
Confidence: High（已报告静态事实）；Medium（条件实验设计）；Unknown（环境和实际行为）
Related decisions: [JNA范围](cp2-jna-aar-static-review-decision-2026-09-09.md)；[元数据](cp2-vosk-dependency-license-metadata-resumed-2026-09-08.md)；[公共语料](cp2-public-chinese-corpus-test-decision-2026-09-09.md)；[PRD](prd-v0.1-2026-09-04.md)
Next review date: 2026-09-16
Research Quality: 86/100（复用已验收报告的方案完整性自评，不是安全认证或环境就绪评分）
Validation Level: V2（不变）
Next evidence: 一次现有Android arm64隔离环境及离线工具可用性只读核对；无合适环境就停止并报告
Allowed next investment: 当前只有方案交付；下一唯一解阻动作由Leader核定范围后处理，不安装、构建、启动模拟器或加载目标
Pause/Kill condition: 环境隔离／观测／离线构建或Owner残余风险处置未落实；禁止把方案确认作为执行许可

## RESULT

**PAUSE：方案已具体化，实际执行不准入。** Android arm64先行实验在所列条件成立时具有技术可行性；当前没有证据证明隔离目标、离线SDK构建闭包或足够观测能力已具备，也没有运行风险接受记录。用户在Leader提出制定受控方案后回复“可以”，只授权本轮方案，不授权设备修改、安装、加载或识别。

```json
{"task_id":"CP2-CONTROLLED-RUN-PLAN-001","attempt_id":"c803f612-e378-4fe6-9862-500bff19da86","contract_sha256":"ee5d01f3e1923fba14e94e651dd4481004b2fad1c2b9c9eb9cf17b433216a5ed","assigned_thread_id":"01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779","acknowledged":true,"result":"COMPLETE","decision":"PAUSE","plan_feasibility":"conditional","runtime_admission":"blocked","adoption_gate":"blocked","actual_asr_evaluation":"not_run","product_changed":false}
```

contract_body递归排序后重算摘要匹配。仅复用报告，没有重新扫描二进制、追源码、ADB操作、环境探测或实验执行。旧拒绝／旧裁决保留，本轮不派dev、不尝试回调。

## 固定报告与制品

以下是本轮实际读取并重算的报告摘要；它们支持历史观察，不构成执行授权。

| 报告 | bytes | SHA256 |
| --- | ---: | --- |
| [CP2-JNA-AAR-STATIC-REVIEW-001-verification.md](/Users/orderly_ray/Leader/orchestration/reports/CP2-JNA-AAR-STATIC-REVIEW-001-verification.md) | 3362 | 53851dd3f696a72079a5955d2d2a09ec9be71cfb0c00617c4daa1d8f5b0add40 |
| [static-review.md](/private/tmp/think-jna-artifact-review/CP2-JNA-AAR-STATIC-REVIEW-001/152ecdef-f3ec-4dc8-8f36-f3de646bf2d8/static-review.md) | 16794 | 17e41e7f896564509091b718940311aac8b2757e26600398898755584d2040a1 |
| [stage2-static-review.md](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/attempts/7fb3904a-af73-4049-b4c8-0b5c3f9eaf00/reports/stage2-static-review.md) | 12668 | 8ee29bea985c049f946ebdd2aa4d4221d2d1489119fffec66287ec89c2d78f10 |
| [CP2-VOSK-ARM64-COMMAND-PATH-REVIEW-001-verification.md](/Users/orderly_ray/Leader/orchestration/reports/CP2-VOSK-ARM64-COMMAND-PATH-REVIEW-001-verification.md) | 2086 | 095bd961a9753a791696557f8790d63d3f64c657458749859fce2b534efc47db |
| [command-path-review.md](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/attempts/26b63ffe-ed33-46c3-a3e5-2cd46a2dd203/reports/command-path-review.md) | 9696 | a8b36e63bf677d164244e43aff633eff75d33b8c354c41e4a785e1e709c77f5f |
| [CP2-VOSK-METADATA-RESUME-001-verification.md](/Users/orderly_ray/Leader/orchestration/reports/CP2-VOSK-METADATA-RESUME-001-verification.md) | 2442 | 715c9167524ad37b9b25ada3f2a0ba7519f5c5247f2a910792be52cdf0f337d3 |
| [CP2-CER-SCORER-001-verification.md](/Users/orderly_ray/Leader/orchestration/reports/CP2-CER-SCORER-001-verification.md) | 3141 | 82848639ef6d812653cad25294e1a126fe9d6ff2a51f963a194c59ab4d6e1443 |
| [CP2-MEMORY-PCM-FAKE-ASR-CONTRACT-001-verification.md](/Users/orderly_ray/Leader/orchestration/reports/CP2-MEMORY-PCM-FAKE-ASR-CONTRACT-001-verification.md) | 3433 | b41027d987d06590e02a4ee771b019a0bf606437c73a1795c80cd9604eb3f05b |

三份实际输入在后续获准操作中须重新核对完整SHA，不能因本报告引用而假定临时路径仍存在或字节未变。本轮未读包，以下bytes/SHA来自已验收报告。

| 对象 | 已验收路径 | bytes／SHA256 |
| --- | --- | --- |
| Vosk Android 0.3.75 AAR | `/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/attempts/07a96480-78dd-4040-8d30-5bc8d44a7ed0/artifacts/runtime-1-0.aar` | 13472638／ab2f8b91ac8051561aa325546b35fed9a68b36b8121bac5c6fb927525c4adfad |
| vosk-model-small-cn-0.22 ZIP | `/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/attempts/07a96480-78dd-4040-8d30-5bc8d44a7ed0/artifacts/model-1-0.zip` | 43898754／3af8b0e7e0f835ae9d414ce5df580237a3cfb08d586c9fbbb0f7ff29ad5b14ba |
| JNA5.18.1 AAR | `/private/tmp/think-jna-artifact-review/CP2-JNA-AAR-STATIC-REVIEW-001/152ecdef-f3ec-4dc8-8f36-f3de646bf2d8/jna-5.18.1.aar` | 522677／7f053e3ec99e14dd71259c82c1c8a02738d64a13c31226b2acc170f3060951e0 |

仅打包已核arm64成员：Vosk `jni/arm64-v8a/libvosk.so` SHA06965ebb4e5eb3a9e4a815755e178d9553392e3fe8d3d368ac46952ad3694173；JNA对应arm64 ELF SHAabc26e994517bcaa3309acdb0a27373864086c7569c89d3087b8626fada9ef06。JNA成员实际basename及所有模型成员摘要从已有member清单冻结，不在本轮猜定未读字段。后续本地物化不许下载缺失包或替换ABI。模型先前只有5文本成员完整复核，其他模型数据CRC覆盖不足：完整ZIP SHA固定身份，但使用前安全物化时仍需检查全成员路径／CRC／实际展开及逐文件摘要，不宣称之前已完成。

JNA已取得并静态验收，仍manual_review；Vosk/model亦manual_review。JNA包内双许可与POM一致，libffi精确版本和独立归属未知。CER20测试／21黄金／961短字符串比较及PCM15组测试已验收，不再开发评分或准备工具；真实中文评测仍未运行。

## 唯一平台选择及当前缺口

先行选择：**一次性、无账号无私密数据的Android arm64-v8a模拟器实例，基于本机已经存在的可调试系统镜像，在独立临时数据目录冷启动。** Android原生ELF需要Android运行环境/Bionic，不能在macOS直接加载Android.so，也不替换为桌面库或x86包。既有Android Studio JDK/javap仅证明静态工具存在，不证明Android SDK平台、build-tools、构建插件缓存、模拟器可执行文件或arm64镜像已具备。

要求现有镜像可支持实验UID/进程及其子进程的文件、网络和exec观测；不要求为了本计划root、解锁手机或下载新镜像。若现有环境不支持，当前方案PAUSE，不临时降级为父亲手机、日常设备或未隔离host进程。小米15只留后续真实CP2阶段，本次不触碰其资料／设置。

隔离设置必须在任何目标类初始化前由获准执行者确认并记录：

- 模拟器无Google账号、无用户数据、无共享文件夹／剪贴板／相机／音频输入／USB透传；独立临时userdata，不加载个人快照。
- host侧对该模拟器进程限制所有外联和host服务访问，仅保留绑定本地的指定ADB控制端点；记录实际规则和测试结果，不臆造本平台防火墙命令。guest网络关闭作为第二层；无INTERNET权限／飞行模式不等于完整native沙箱，AF_UNIX/Binder、系统服务、OS或模拟器漏洞仍是残余风险。
- APK无INTERNET、RECORD_AUDIO、存储权限、备份／导出组件，仅固定测试入口；进程不与Think UID／数据共享。系统正常Android运行时文件访问另行冻结白名单，不能用“可读所有系统路径”掩盖未知加载。
- 可观测手段必须是已安装工具：从进程创建时覆盖库加载前、模型初始化、处理、释放的syscall文件访问、connect/send及execve/execveat，继承子进程；记录map/FD、进程树、限定UID日志和实验目录变化。只靠结束后的文件列表抓不到创建后删除的临时文件；只靠抓包看不到全部IPC。工具不支持、事件截断或UID/子进程漏覆盖即不具备先行通过条件。
- 跟踪使用控制进程/既有工具，不运行目标附带命令；观测不等于阻止。外部watchdog能够终止实验和模拟器；不能把native崩溃处理寄托于同进程finally。

镜像ID/API/build fingerprint/ABI、host能力、SDK/构建缓存、可用观测命令及权限、网络规则、精确ADB端点、恢复范围**全部待只读核对**，当前不声称已有可运行环境。

## 一次归并风险与处置

| 风险／依据 | 加载前必须落实 | 可留先行实验观测及结论边界 |
| --- | --- | --- |
| 许可／来源：JNA双许可，Vosk/model Apache2发布声明，libffi/Kaldi/FST归属与模型训练权利链不完整 | Owner逐项记录拟用Apache2选择、内部不分发用途、未知组件／训练来源、是否接受此次无私密数据实验残余风险及理由；不由PM勾选接受，不把缺NOTICE判违法。全部许可证材料随实验证据保留 | 可以验证包内材料与固定输入一致；实验不能证明权利链。正式分发义务、签名／可复现来源仍未闭合 |
| JNA类初始化即可能加载native；Android不受jna.nosys单独限制 | 所有路径／属性在首次引用Native/LibVosk前设定；固定类加载器仅含两固定JAR与第一方harness。native目录冻结两目标库及允许Android系统依赖，禁止可写目录优先、下载和用户可控搜索路径 | 捕获实际加载路径／映射／摘要，任何目标库来自未批准目录立即终止。不能靠设置属性就宣告加载安全 |
| JNA classpath提取／temp及路径日志；可能FFI可执行内存 | 默认不允许fallback提取；boot目录和Vosk搜索路径限定下节N，temp限定T用于检测。禁调试加载日志但保留受控UID观察。禁止任意NativeLibrary.getInstance／Pointer原始地址／callback／closure接口 | temp若出现任何提取、未列库加载、未知可执行文件映射即失败停止，不能当场放宽。JIT/ART合法匿名执行映射须与目标FFI迹象区分，无法区分就inconclusive；不把所有mmap都称恶意 |
| Vosk管道路径把去掉首尾竖线后的文本交给popen；完整可达性Unknown | 固定model目录、原始模型/config清单和摘要，不接受调用方路径／配置／grammar；禁StorageService、StreamService、麦克风及扩展API。仅检查外层目录无竖线不够；完整模型内部输入仍有解析风险，需Owner接受在隔离无私密实验中观察而非认定不可达 | 任意目标派生exec（包括shell）立即停止；不喂恶意grammar／命令字符串。观察没有exec只支持本次固定静音路径，不能证明所有输入不可达 |
| PCM／JNA marshalling和close无清零保证 | 第一方单线程、固定长度、无队列；只选short[]重载、计数单位为samples；使用已验收PCM所有权模式，实际同步adapter须review，无任意指针和手动FFI Memory分配 | Java私有副本finally清零、结果session隔离、exactly-once finish/close可测；JVM/JNI/native副本和物理擦除仍Unknown，Memory.close不等于clear |
| 新harness与离线构建可能引入未审对象 | 尚无已验收真实harness或APK；必须在未来获准同一实验内制作最小第一方harness并审阅、冻结SHA及有效manifest。已安装SDK、JDK和全部构建依赖闭包就绪；离线无自动下载，缺失即停止 | 构建／安装本身有影响，必须明确包含于将来的执行批准，不能用当前方案授权预先构建。不新增通用adapter/scanner平台 |
| 资源／终止与观测可用性 | 下述watchdog、输出／内存／磁盘限额和停止控制可实现，设备/host中断可操作 | 测量初始化/处理/释放时间、RSS和文件事件；模拟器成绩不外推小米15性能和CPU-only产品保证 |

这些条件不要求重新完成无限源码闭包；对未证明可达性的风险，只有明确隔离、足够观测和Owner接受才能考虑限定先行运行。当前三者均未齐全，故不准入。

## 固定加载和路径合同（待实例化，空字段禁止执行）

未来实验包名固定为`org.think.cp2probe`，只在新模拟器使用；host输出根`/private/tmp/think-controlled-asr/<run_id>/`。路径由执行时实际ApplicationInfo生成并冻结，绝不猜Android随机安装段：

| 符号 | 允许路径和用途 |
| --- | --- |
| N | 该唯一已签名APK的实际canonical nativeLibraryDir（安装前为待定，安装后加载前绑定）；只两目标arm64库，其余依赖仅来自固定镜像的已列系统路径 |
| M | `/data/user/0/org.think.cp2probe/files/model/vosk-model-small-cn-0.22/`；固定ZIP安全物化后的全成员清单，禁止symlink和越界；初始化前后hash一致，逻辑只读 |
| T | `/data/user/0/org.think.cp2probe/cache/jna-probe/`；空目录、专用；用于发现不应发生的提取，不允许PCM或任意native文件写入 |
| R | `/data/user/0/org.think.cp2probe/files/probe-report/`；仅状态、计数、时间和错误码，由第一方报告器写；不保存PCM、dump或无限输出 |
| host evidence | 上述run_id根；APK/输入清单、允许系统路径、有限trace和摘要，全部本地，不上传 |

jna.boot.library.path与jna.library.path只指定N，java.io.tmpdir/jna.tmpdir指向T，关闭debug_load等调试选项；尝试禁止unpack/fallback的属性只是待验证配置，不作为强制沙箱的替代。LibVosk已知Native.register以名称vosk注册，因此要求加载前目录绑定＋全程观测＋映射核对；若无法保证只加载固定库，**不通过，不去修改JNA或换版本**。OS系统依赖路径/版本随镜像绑定；不能禁止Android本身必需的系统加载，也不能以其为由允许任意搜索。

M在普通app UID下chmod只读不能防止native自行chmod，因此必须观测写入/权限变化，并借一次性无私密guest降低影响；不能称不可写硬保证。宿主与guest允许文件变化范围先列明：安装及ART编译缓存属setup阶段，首次native加载前另取运行基线；此后未知文件写入、库提取、M变更或PCM落盘为停止条件。安全物化模型是固定已有包的准备，不允许新下载；展开最多512MiB／10000成员／128MiB单成员，一次；不足停止，不放大。

## 最小先行实验（未授权、未执行）

只验证固定加载、模型构造、有界PCM处理及关闭的可观察行为，不进入真实中文识别。拟执行整单最多2小时（含同单harness实现／review／离线构建／安装／观察及清理）；native阶段最多5分钟、仅一次进程启动、一个Model、一个Recognizer、一个会话，不自动重试。

1. 在明确执行授权后，同单先复核三包SHA、模型全成员完整性，建立最多一个最小离线harness/APK并审阅。只依赖现有Android API、固定两AAR和第一方代码；只打arm64，冻结harness源码／APK SHA与有效manifest。不能启动目标类来“预检”。
2. 先创建已核一次性guest、落实断网／观测／watchdog，再安装一次APK。记录N/M/T/R实际值、APK与native成员hash、镜像身份和setup后文件基线；任何待定项未填则不加载。
3. 从首次Native初始化前启动外部观测；固定加载JNA和Vosk，核对目标映射。控制日志级别仅为降噪，不替代观察，初始化早期日志同样纳入。加载＋Model初始化合计最多120秒；任何异常即停，禁止调整路径重试。
4. 用普通无grammar构造器创建Recognizer，采样率16000；单线程生成全零short[320]帧，送50帧，总16000 samples即1秒PCM16 mono。没有WAV／麦克风／文件音频，累计32000逻辑音频bytes，只保留单帧私有副本。受控逐帧验证长度1..320；不向真实native传非法长度、关闭后指针或竞态来“测试安全”。
5. 处理阶段最多30秒，finish／final结果最多一次，随后Recognizer先close、Model后close；每个资源仅一次关闭尝试，Java工作帧finally清零。关闭合计最多30秒；部分初始化只释放已获得handle，保留主异常和清理状态，不再调用损坏native。OOM／崩溃／超时走外部终止，不依赖finally必达。
6. 比较映射、文件/网络/exec事件、M摘要、T内容、FD与进程结束状态，生成判定。静音产生空文本不是准确率成功；出现文字也只记录有限异常现象，不算CER。不得以静音N=0计算中文评分。

资源：guest最多4GiB RAM、2 vCPU、8GiB临时磁盘，host新工作目录最多2GiB；实验进程RSS达到1GiB或外部监控失效即停（采样监控非精确硬内存隔离，guest RAM为宿主影响边界）；证据累计64MiB、单日志/trace16MiB，临近上限即终止而非截断后报通过。harness最终状态/结果最多64KiB；不采集堆、core、完整内存dump，不输出PCM，即便全零也不保存音频。不得默认OS不会生成tombstone；受控guest可能产生，须登记为失败证据并受总量限制，非私密环境不证明未来不会泄漏。

失败清理：先外部终止实验进程及子进程，再停止该guest；仅清理本run_id创建的guest/userdata和指定新输出，保留有界报告及事件摘要。不要卸载其他包、wipe现有AVD、清空全局logcat或改全局SDK。需要强制杀进程/删除新guest的权限包含于最终执行草案，当前不实施。若隔离失效，停止guest并报告，禁止在同一实例继续。

## 实际判定表与后续阶段

| 实验结果 | 可报告的结论 | 不可报告 |
| --- | --- | --- |
| 前置缺失／未批准执行 | not_run／PAUSE及具体缺项 | 实验通过／真实ASR可用 |
| 崩溃、超限、异常映射/写入/网络/exec、关闭失败 | FAIL，停止且保留证据；逐项说明观察 | 自动重试、接受风险后继续本轮 |
| trace不完整、工具无权限、系统事件无法归属、模型完整性未知 | INCONCLUSIVE，不能准入下一阶段 | “没有发现问题所以安全” |
| 一次全流程完成、固定映射、观测完整且无越界 | bounded_silence_probe_pass：该实例/制品/输入范围加载处理关闭可行 | native无风险、物理擦除、中文CER／专名通过、CPU-only、小米15性能或CP2通过 |

之后真实中文评测是**另一个条件阶段**：先行通过不自动开始；需要可信公开小test语料、冻结标注/许可/ID与训练重叠声明、实际backend和设备绑定、明确执行授权，使用既有CER工具。父亲30段27段无需重录、专名90%、30秒P95、90秒20次、飞行模式、真实私密音频保护以及CP1人工恢复仍独立，不纳入本静音试验的通过标准；CP3/Alpha不变。

## PAUSE唯一解阻动作

由Leader处理一次 **现有环境可用性只读核对**，不建立新工具或依次派出多轮准备任务：让用户指认已有可用于本实验的无私密Android arm64环境；核对现有host/SDK平台/build-tools/构建依赖缓存/arm64可调试镜像的本地身份、已安装观察工具及其支持范围，记录是否能实现上述隔离和清理。该动作应有单次20分钟上限，零网络、零安装/构建、零目标加载、零启动或修改设备；静态清单不足以证明动态隔离时保留待执行前验证项。

本单没有执行这个核对，也没有假定“可以制定方案”涵盖ADB。只读核对若需设备连接/ADB只读查询，须明确用户指定设备与该操作范围后由Leader处理；不因缺镜像而下载，不因缺观测而新开发工具。不具备就结束为环境不足，向用户报告唯一环境缺项，不自动进入下一准备链。Owner风险接受和最终执行批准仍必须在加载前完成，环境核对本身不代替两者。

## 面向用户的执行授权草案（当前不可直接执行）

> 我批准一次CP2无私密数据静音先行实验，仅在已核定的一次性Android arm64环境【镜像ID/API/fingerprint/host/ADB端点待填】进行。允许在新隔离目录使用现有离线工具制作、审阅和冻结一个最小第一方harness/APK【源码及APK SHA待同单加载前记录】，安全物化并打包本决定固定SHA的Vosk0.3.75、small-cn-0.22与JNA5.18.1已有对象，安装一次，完成一个1秒内存全零PCM会话及关闭；允许限定观测、失败终止和仅本次新guest的清理。整单2小时、native阶段5分钟、一次启动/一会话、资源和证据限制按本决定；任何前置不满足、超限或异常即停，不重试。
>
> 我已审阅并对本次内部实验逐项处置【JNA/libffi及Vosk/Kaldi/FST归属、模型训练来源、独立来源认证、命令可达性、temp/FFI及native内存未知：Owner选择与理由待填】。这些风险未被静态扫描消除；隔离与观测不能保证无OS/模拟器漏洞或所有native行为可见。该处置不接受私密音频泄漏，不是分发法律许可或产品采用批准。
>
> 不允许网络或新依赖下载、macOS直接加载Android库、父亲/日常手机操作、麦克风或真实音频、中文准确率评测、训练、产品集成、CP3或Alpha。任何待填身份／路径／Owner处置仍空白时不得开始目标加载；harness/APK和实际N/M/T/R必须在加载前被Leader核对，不能由构建器自动补依赖。

这是一份审阅草案，不是用户已经作出的批准。本次停止于方案交付；不给出可误触发加载的现成命令，不替用户勾选残余风险。

## 本轮验证与限制

仅新决定、PRD／INDEX／LOG串行写回；零网络／包读取／安装／构建／设备操作／运行／派dev／回调。复用product-research和knowledge-loop，不调用扫描skill启动新审查。报告摘要、合同身份、路径文字来源、预算、六元数据／链接及LOG前缀/局部diff检查；标准全库lint缺失则不声称自动通过。

本轮完成的是范围与PAUSE裁定；环境、harness、OS观察、许可Owner接受均未验证，真实实验次数=0。未知集中在本决定，不派发新工具、不恢复旧源码或公共语料研究链。
