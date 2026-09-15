# 决定：JNA 5.18.1 单AAR取得与有限静态审查

Owner: Product Lead
Last updated: 2026-09-09
Source: CP2-JNA-SCOPE-001完整合同及用户确认上下文；Leader CP2-JNA-AAR-NEXT-SCOPE.md；已验收元数据恢复报告和CER验收
Confidence: High（范围与已验收元数据）；Unknown（未取得AAR内容及真实运行）
Related decisions: [元数据恢复报告](cp2-vosk-dependency-license-metadata-resumed-2026-09-08.md)；[公开语料决定](cp2-public-chinese-corpus-test-decision-2026-09-09.md)；[简化分阶段决定](cp2-vosk-simplified-staged-review-decision-2026-09-08.md)；[PRD](prd-v0.1-2026-09-04.md)
Next review date: 2026-09-16
Research Quality: 88/100（沿用已验收元数据证据质量，不是新研究或安全评分）
Validation Level: V2（不变）
Next evidence: Leader验收本决定后，dev同单同步四文档并取得、有限静态审查唯一JNA AAR
Allowed next investment: CP2-JNA-AAR-STATIC-REVIEW-001，最多两小时；只固定一个包，预算如下
Pause/Kill condition: 权限／TLS／身份／资源失败或不支持、不安全结构立即停止；采用和运行门保持blocked

## RESULT与身份

**APPROVED：仅唯一 CP2-JNA-AAR-STATIC-REVIEW-001，范围为一个固定JNA AAR的取得与离线静态检查。**

本轮只离线对齐正式文档，实际GET=0、取得bytes=0、目标静态工具调用=0。不批准安装、构建、加载、运行或产品集成。开发下一单先同步四文档，再在新隔离目录取得和检查包；不用另开纯同步任务。

```json
{"task_id":"CP2-JNA-SCOPE-001","attempt_id":"0fdd9888-9aec-4540-b030-06b8ce0c5e7f","contract_sha256":"315ac3456a1c207811482d67dcfc097f1dcd75e67965fe4b456fcff21187719d","assigned_thread_id":"01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779","acknowledged":true,"result":"COMPLETE","decision":"APPROVED","next_task":"CP2-JNA-AAR-STATIC-REVIEW-001","adoption_gate":"blocked","runtime_admission":"blocked","product_changed":false}
```

## 用户确认与固定来源

Leader在明确询问是否批准[单AAR提案](/Users/orderly_ray/Leader/orchestration/reports/CP2-JNA-AAR-NEXT-SCOPE.md)之后，用户直接回复“继续工作”。当前合同将此记录为对该具体下载／静态检查范围的确认。本决定据此落地，不再次要求批准同一范围，不将一般“继续”外推到其他对象或执行。

提案开头“not dispatched or authorized”是用户回答前的历史状态；原提案保持只读，新确认记录于此。提案最后的文档同步时序在当前合同中明确为：PM先正式对齐，Leader验收并派发dev，dev同一单内先同步四文档后开始取得。无需在dev派发前另开同步单。

| 固定来源 | bytes | SHA-256 |
| --- | ---: | --- |
| Leader CP2-JNA-AAR-NEXT-SCOPE.md | 2523 | ec45c20efbdffd217a78e031b4e2b851f7636ff46bfdf73848d411f9f10d812a |
| [元数据恢复验收](/Users/orderly_ray/Leader/orchestration/reports/CP2-VOSK-METADATA-RESUME-001-verification.md) | 2442 | 715c9167524ad37b9b25ada3f2a0ba7519f5c5247f2a910792be52cdf0f337d3 |
| [CER验收](/Users/orderly_ray/Leader/orchestration/reports/CP2-CER-SCORER-001-verification.md) | 3141 | 82848639ef6d812653cad25294e1a126fe9d6ff2a51f963a194c59ab4d6e1443 |

contract_body按递归键排序、UTF-8紧凑JSON重算SHA，与四身份一致。来源hash为本轮实际计算，不是转述未经核对的值。旧Q01权限拒绝、后续文本恢复9GET、旧两包及公共语料5GET各自保留历史，不重置或混用预算；本次是新确认的单AAR任务。若执行工具实际仍拒绝，立即停止、不换渠道绕过。此前完成回调拒绝不重试，完整结果供Leader主动读取。

## 已完成进度与剩余未知

元数据恢复已由Leader接受：Vosk0.3.75 API/runtime两个变体均显式选择JNA5.18.1 AAR并通配排除传递依赖；JNA默认POM打包jar不覆盖该选择器。固定POM声明Apache-2.0 OR LGPL-2.1-or-later；master许可文本只辅助核对，不能证明未来AAR全部捆绑组件许可。

CER已在提交3046f49344f4c3cd1c46836d0bf0b3060ac15bd6由Leader验收：20项测试、21个黄金用例、961组短字符串oracle比较通过，CLI合成结果摘要一致。这些为已读验收记录，不声称本PM重跑测试。真实公开语料识别NOT RUN，可信小test子集取得仍暂停。CER可用不代表真实引擎可用，不能再次派发CER准备工作。

固定JNA AAR实际存在性、bytes、本地SHA、官方制品SHA／签名、Java/native内容、ABI及完整第三方归属均Unknown。本次不联网补查、不读取旧二进制。已知URL可用于下一单精确GET，不能写成“对象已验证存在”。

## 下一单固定对象与预算

对象：`net.java.dev.jna:jna:5.18.1`，type=aar、extension=aar，无classifier。

唯一URL：`https://repo.maven.apache.org/maven2/net/java/dev/jna/jna/5.18.1/jna-5.18.1.aar`。

来源依据为已验收Vosk.module显式selector及Maven Central布局；不得改版本、替换jar、查询新POM/module、跟sidecar或取得第二依赖。实际取得后记录SHA，不称独立发布者认证，也不能把Vosk AAR的已知摘要套到JNA。

| 项目 | 原提案上限／规则，原样沿用 |
| --- | --- |
| 整单 | 最多两小时，包含文档同步、取得、静态检查和报告 |
| 网络 | 最多两次GET尝试；HTTPS only；无自动跳转或自动重试 |
| 单响应／总正文 | 64MiB／128MiB；失败或部分响应正文也记账 |
| 单次取得时间 | 最多180秒 |
| 第二次GET资格 | 仅暂时性传输失败可消耗；成功即不再取。权限、TLS、身份、资源失败不得重试；HTTP重定向不跟随，不猜新URL |
| 外层归档 | 最多10000成员 |
| 展开预算 | 总512MiB，单成员128MiB；声明值和实际展开均受限，外层及一层classes.jar共享总展开预算，不按层重置 |
| 嵌套范围 | 仅一层classes.jar；其他需深入结构记Unknown，必要时停止，不扩展 |
| 文本读取 | 单文件2MiB，累计32MiB |
| 静态工具 | 最多20次调用；每次120秒；输出每次16MiB、总128MiB |
| 保存与历史 | 新隔离attempt目录；原始包、请求响应、清单和报告可核，旧证据只读；包及展开产物不得进入产品目录或成为构建输入 |

开发可在`/private/tmp/think-jna-artifact-review/CP2-JNA-AAR-STATIC-REVIEW-001/<attempt_id>/`建立独立目录（本轮未建立取得目录）。不复用旧包目录覆盖文件，不将AAR放入Think libs／Gradle缓存或自动依赖解析路径。

取得阶段保留确切请求URL／方法／命令、实际时间、HTTP／类型／跳转字段、收到的bytes、SHA和错误；无HTTP响应则字段Unknown。类型或内容身份不符立即停止，HTML错误页不能冒充AAR。不必为实现本合同开发新传输器或扫描器，使用已安装且能落实上限的工具；不能实现某项既定保护则如实停止。

## 有限归档与静态检查

采用用户已确认的简化流程及现有标准归档、JDK／LLVM静态工具。解包前检查路径、链接、重复名、成员类型、声明资源限制，实际解包过程中同时约束真实展开量。禁止extractall，禁止执行归档附带程序；不支持或不安全结构停止。允许有界、安全路径的选定成员落地解包，不重启旧全内存解包／1GiB系统硬隔离或专用扫描器开发要求。

预算内至少分开报告以下问题与实际覆盖；未完成部分标Unknown，不能为补齐清单超时或扩对象：

1. 外层及允许一层classes.jar的成员清单，Java/native分布、大小、SHA和已读／未读范围。
2. native各ABI的ELF身份（位数、machine、对应包路径），结合已有JDK/LLVM静态输出核对；名字含arm64不等于身份已证。记录依赖与相关静态能力线索，不运行native。
3. 包内LICENSE／NOTICE／第三方归属材料，与已验收JNA POM双许可声明交叉核对；缺失文件不自动推定违法，也不等于义务不存在。
4. native加载入口、JNI相关声明及相关内存API签名：Java到native的边界、可见加载／提取行为、内存长度／所有权／释放接口。只读字节码／符号／必要有限静态输出；不调用类初始化、反射加载、JNI或测试目标方法。
5. 记录读取工具、参数、退出状态、时间、输出bytes／SHA、覆盖范围和未解析依赖。scanner如使用只为补充，不替代JNI／ELF／许可人工审阅；不作穷尽调用图、源码闭包或新scanner工程。

静态导入和接口只证明能力或声明，不证明实际发生文件／网络操作、恶意行为、PCM内存正确或可达性安全。有限检查到预算就形成具体剩余问题，不能追加“只再追一个函数”的链。

## 停止、交付与裁决

权限／TLS／身份／资源失败、不安全或不支持归档结构立即停止；不请求下一对象或改通道。暂时传输故障仅可按两次总额使用一次人工控制的恢复；失败、部分下载与本地检查均保留真实记录，不能补造HTTP／bytes／来源认证。404等存在性失败不是暂时传输故障，不能用第二次GET猜另一路径。

下一单交付：请求／响应原文及摘要、实际AAR bytes／SHA、归档清单、受限静态证据及覆盖、许可／ABI／加载与内存API发现、单对象裁决和运行准入缺口。未取得则明确not_acquired／原因；危险或身份问题可block，证据有限可manual_review。静态完成不要求强行给通过，不继承Vosk或模型对象的裁决。Leader独立复核后才能接受结果，接受静态工作也不自动放行采用。

已知运行前缺口继续单列：JNA实际包身份／内容（本单可能补）；完整runtime/model/JNA许可归属及Owner处置；native命令输入／文件／日志限制；真实marshalling、生命周期、PCM隐私；小米15性能／CPU／稳定性、父亲口音／专名准确率；公共语料来源和训练重叠未知。不要求本单证明所有动态结果，也不替用户接受残余风险。

## 同单同步与禁止范围

Leader验收本PM决定后，下发唯一dev任务CP2-JNA-AAR-STATIC-REVIEW-001。dev同一单内先同步并核对下列四文件，再开始取得；不复制整个知识库：

- 本决定→Think `doc/cp2-jna-aar-static-review-decision-2026-09-09.md`；
- 最新PRD→Think `doc/prd-v0.1-2026-09-04.md`；
- Think `AGENTS.md`的当前任务／门禁入口；
- Think `doc/README.md`的文档入口。

同步记录源／目标bytes与SHA相同，入口注明“单包取得／静态检查已确认，采用／执行未批准”。本PM不修改Think，不派dev；同步后包及静态产物只在隔离目录。任务报告留原执行任务，由Leader主动核验；旧回调拒绝不重试。

禁止安装、Gradle/Maven构建、自动依赖取得、目标native加载、麦克风、真机执行、产品集成、新源码／sidecar／第二依赖或旧包重取。不继续公共语料搜索，不训练模型，不恢复sherpa链，不新增扫描器。原始私密录音不落盘／上传／日志、云端仅文字、90秒／专名90%、CP1人工恢复、CP2未过、CP3与父亲Alpha未批准保持；公共fixture隔离边界不变。

## 本轮验证

仅新建本决定及必要PRD／INDEX／LOG更新，LOG只追加，其他项目及旧证据保持。本轮GET=0、对象取得=0、二进制读取=0、目标执行=0、Think修改=0、派dev／回调=0。按product-research复用已验收证据、knowledge-loop串行写回；不重新研究或引用模型输出作为原始来源。

核对合同SHA、三份源bytes/SHA、提案各项预算及权限一一对应、六元数据／本地链接、PRD最新状态、LOG原始前缀及Git局部差异。标准全库lint脚本若仍缺失仅报告范围校验，不声称全库自动通过；本单无产品或目标测试。
