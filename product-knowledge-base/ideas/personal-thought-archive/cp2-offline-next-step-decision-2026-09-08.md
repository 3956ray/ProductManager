# 决策：CP2内存PCM会话契约与假ASR离线验证

Owner: Product Lead
Last updated: 2026-09-08
Source: CP2-OFFLINE-NEXT-TWO-DECISION-001；Leader command-path verification及原command-path-review；已验收stage2报告；当前PRD；用户继续两步且暂缓JNA/module查询的调度记录
Confidence: High（可做离线边界工程）；真实ASR安全及行为Unknown
Related decisions: `cp2-vosk-integration-gaps-decision-2026-09-08.md`；`cp2-vosk-stage2-scope-decision-2026-09-08.md`
Next review date: 2026-09-15
Research Quality: 90/100（沿用已验收静态证据，不是运行或需求验证）
Validation Level: V2（不升级）
Next evidence: 同一开发单先同步正式文档，再实现独立PCM会话模块并运行fake ASR合成测试
Allowed next investment: 一项最多6小时、5个工程文件的第一方离线产物；另4个正式同步文件，不构建产品
Pause/Kill condition: 需要新依赖／真实native加载／联网／产品构建或超出文件时间范围则BLOCKED；不为继续制造扫描工具或新文档循环

## RESULT

**APPROVED：唯一下一任务 `CP2-MEMORY-PCM-FAKE-ASR-CONTRACT-001`。**

用户要求的“两步”明确为：本PM裁定范围；Leader验收后dev在一个任务内完成必要同步及一个有实际测试的离线工程产物。不增加第三项自动任务、不只派纯文档同步、不恢复被拒metadata、不继续逐函数补证。本轮PM只修改知识库，不实施代码或改Think。

价值：在真实引擎尚未可采用时，先消除第一方调用边界的长度／状态／所有权／异常清理错误。接口可供以后适配真实引擎，但当前只绑定fake；不是实现真正语音识别，也不是CP3记录／搜索功能。

## 证据及未关闭事项

命令路径verification SHA `095bd961a9753a791696557f8790d63d3f64c657458749859fce2b534efc47db`；原报告SHA `a8b36e63bf677d164244e43aff633eff75d33b8c354c41e4a785e1e709c77f5f`。已验收静态审查定位PipeInput/Output::Open到popen，输入字符串去除首／尾管道符后传入；这是局部静态流，不是已执行攻击。Model下层ConfigureV1/V2/ReadDataFiles、grammar和音频传递到pipe的完整可达性仍Unknown。停止逐函数补证循环，本任务不再读二进制或跟进函数。

stage2已观察数组音频转发、close/free及StorageService资产文件路径，这些足以支持“窄内存接口＋显式生命周期”设计，不证明native内部不落盘或清零。仅过滤外层模型目录中的管道符不能证明所有配置派生路径安全；本fake模块不提供模型路径、grammar字符串、shell／文件API，因此不能声称解决真实native的命令路径问题。

用户暂停JNA/module的意图由当前合同及命令路径verification明确记载，原查询拒绝和0请求不变。许可／依赖／命令路径仍阻止真实加载，离线fake工程无需先假造这些已关闭。

## 下一dev完整合同

### 一项产物与允许文件

第一方独立Java标准库模块放在Think `tools/cp2-memory-pcm/`，不接入App源码或构建图。固定最多5个工程文件：

1. `MemoryPcmSession.java`：会话状态、窄backend接口、所有权和长度／结果边界。
2. `FakeAsrBackend.java`：只产生确定性假文本和计数，提供受控失败／延迟结果注入，不识别语音。
3. `MemoryPcmSessionTest.java`：无JUnit依赖的可执行断言测试入口。
4. `run-tests.sh`：用已有JDK直接编译这三个第一方文件到新临时目录并运行测试，清晰记录输出；不调用Gradle/Maven或App build。
5. `README.md`：接口契约、状态表、测试命令／结果、限制和未来适配注意；不是另造PRD。

必要同步另限4文件：把本决定及最新PRD原bytes复制到Think `doc/`对应文件；仅更新`AGENTS.md`、`doc/README.md`说明最新CP2准备范围、禁止真实加载／metadata恢复。总计最多9文件；先完成同步再同单实现／验证模块，不另派纯同步单。不改App/依赖文件/锁文件/数据库/其他功能。需路径适配时只能在这同一工具目录调整命名，最终报告说明，不扩大所有权边界。

最多6小时的一个开发批次。现有Android Studio JDK可直接用，但不得启动Android Studio项目／扩展或联网安装JDK；现有运行器不可用则报告具体阻塞，不改成开放式工具工程。编译和执行只针对以上第一方合成模块，明确不属于产品构建或真实Vosk/JNA执行。

### 可测契约

- 输入格式固定为PCM16、mono、16000Hz，使用short数组与validSamples；单帧最多320个sample（20ms），只处理声明有效区间。空／负长度／大于数组或320、格式不符拒绝，不把无效数据送backend。
- 会话累计最多1440000 sample（90秒）；计数用安全整数运算。刚好上限可完成，下一帧或一次跨界输入拒绝并终止该会话，不静默截断或接受第91秒。样本时长是本模块约束，不假称真实录音时钟或native性能。
- 单会话串行处理，不建立无限队列或整段录音缓存；只持有至多一个320-sample私有工作副本。公开写明调用者拥有原数组，本模块不清零调用者数组；模块复制有效范围，backend借用仅在调用期间有效，不得保留。finally清零自身副本，包括backend抛错路径。
- 所有权契约、fake验证只能证明被测第一方副本清理，不能证明JVM所有复制、JIT、系统／native缓存或物理内存已擦除；不做这种安全声明。
- 状态至少IDLE／ACTIVE／FINISHED／CANCELLED／FAILED／CLOSED；明确合法转换。重复close／cancel幂等；finish仅一次提交最终文本；终态后accept拒绝。关闭后不得重用已关闭backend；下一次开始必须新session标识／新backend，旧结果不得进入新会话。
- backend工厂只由受信第一方注入，模块不反射加载插件、不接受任意类名／库路径。测试只用fake，接口不依赖org.vosk/com.sun.jna/Android框架；禁止Native.register、System.load、dlopen、麦克风、文件流音频或网络输入。
- 明确串行调用／线程所有权；可以拒绝非owner线程而非实现复杂并发框架。结果以sessionId验证归属，取消／结束／替换后迟到结果无效；后台线程或真实音频线程集成不在本单。
- finish/cancel/异常确保backend关闭至多一次；失败清理不能吞掉原错误或把FAILED伪装成功。不得把原始PCM、数组内容、异常中的音频数据写日志／文件；测试报告只记录场景名／状态／计数与假文本，不保存PCM fixture到磁盘。
- fake输出显式标为fake测试文本，不根据音频内容生成识别结果；仅合成数组，不使用真实录音或父亲数据。不做UI／持久化／搜索／云端调用／提醒，保持CP2技术准备。

### 必须实际通过的测试

| 组 | 有意义的验收 |
| --- | --- |
| 基础与长度 | 正常多帧、有效区间、不足帧、所有非法长度／格式；拒绝项backend调用数为0 |
| 时长 | 刚好90秒可结束，跨界与边界后一帧拒绝，样本累计不溢出；不按真实90秒sleep测试 |
| 生命周期 | 各合法／非法状态、重复cancel/close、finish一次、错误后不提交结果；backend关闭次数准确 |
| 数据所有权 | 调用后原数组不变、工作副本不别名、fake仅为测试保留的借用引用在正常／异常返回后全零；validSamples以外不泄漏给backend |
| 失效结果 | 取消／终止／新session后注入旧session结果不被接收；正向匹配fake结果只接收一次 |
| 错误及线程 | accept/finish/close故障注入、原错误保留、幂等清理、跨线程按合同拒绝；不创建真实ASR线程 |
| 内存上界 | 高帧数循环中最大待处理副本／队列计数有界，无整段PCM留存；只证明代码级保留上界，不伪造OS内存隔离 |

不以测试条数凑通过。关键负例应能捕获删去长度校验、状态隔离或finally清零等回归。源码人工复核无目标包引用、无音频写盘／日志、无网络／native加载，并保留检查范围。运行脚本exit非0即失败；报告真实命令、JDK版本、全部测试结果及残余风险，不虚构覆盖率。

### 完成与停止

RESULT=COMPLETE须同步四文件身份正确、模块可独立编译测试、上述核心行为有证据，Git只在允许9文件范围内。最终报告列实际路径／bytes／SHA、diff、测试命令／结果、假实现范围和未验证；Leader独立验收。同单可以修复合成失败，不逐小步问用户。

需要联网、增加依赖、真实库加载、修改App、扩大CP3、超6小时或文件范围时BLOCKED，保存已有成果并报告唯一缺口。不为过测试删掉隐私或90秒标准，不用真实Vosk替代fake。完成后停止，不自动开始第三步、popen继续追踪或metadata查询。

## 未来真实运行前门槛

必须另行处理：固定实际JNA／.module及必要依赖和许可证据、适用的新增取得授权；主runtime/model完整许可／来源处置；固定模型／配置／输入路径、命令输入可达性和日志控制的运行准入论证；真实backend适配代码审查及对应受控执行权限。当前不申请或获得这些权限。

PCM marshalling、真实线程／close竞态、native缓冲／日志／文件／网络行为、模型grammar／专名90%、CPU／性能／飞行模式都留实际获准验证；不要求先证明未知测试结果才能做第一方设计，也不把fake测试当这些结果。adoption_gate和runtime admission继续blocked；CP2未过、CP3／父亲Alpha未批准，CP1人工恢复及Conformer／词表deferred规则保持。

## 本轮身份与检查

task_id=`CP2-OFFLINE-NEXT-TWO-DECISION-001`；attempt_id=`ad032b97-a1b6-47de-8ffb-8707dfec39c8`；contract_sha256=`7dd7da8a927b1a3687951d193c0680e0d649a731017e86a09fd6eda04021d7f5`；assigned_thread_id=`01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779`。

仅新决定及必要PRD／INDEX／LOG；旧reports和二进制不改不读，未联网/实施工具/改Think/提交。本地元数据／链接／日志前缀／差异检查，全库lint脚本缺失。完成报告等待Leader，回调拒绝不重试，不自行派开发。
