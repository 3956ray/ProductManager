# Vosk 依赖与许可元数据：恢复批次完成

Owner: Product Lead
Last updated: 2026-09-08
Source: `CP2-VOSK-METADATA-RESUME-001`完整合同；本轮Q02-Q10官方响应；旧Q01拒绝报告；已验收Vosk POM及阶段1/2文本记录
Confidence: High（固定元数据字段与请求记录）；Medium（许可关联）；Unknown（完整组件权利链及真实执行）
Related decisions: [原正式范围](cp2-vosk-integration-gaps-decision-2026-09-08.md)；[旧权限停止报告](cp2-vosk-dependency-license-metadata-2026-09-08.md)；[离线模块决定](cp2-offline-next-step-decision-2026-09-08.md)
Next review date: 2026-09-15
Research Quality: 88/100 · pass（本PM自评，待Leader独立验收；不是安全或法律评分）
Validation Level: V2（不变，无新增用户或真机验证）
Next evidence: Leader归并审阅本报告中的首次运行前open项，决定是否提出唯一固定JNA AAR取得与静态审查合同
Allowed next investment: 本批次已结束；无新二进制、集成或执行权限
Pause/Kill condition: 新对象／新执行须另行明确授权；采用门和运行门保持blocked

## RESULT与身份

```json
{"task_id":"CP2-VOSK-METADATA-RESUME-001","attempt_id":"31424e25-9308-4c57-b30c-a04fadbbb674","contract_sha256":"15aca7cf8d75db4721530d1d354fa981bf56f2009bf5160fdd45afb55592e279","assigned_thread_id":"01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779","acknowledged":true,"result":"COMPLETE","metadata_result":"metadata_batch_complete","adoption_gate":"blocked","runtime_admission":"blocked","product_changed":false}
```

本结果表示限定文本问题已回答，并逐项列出所读官方位置没有提供的关键材料；不表示全部许可义务闭合、不表示真实引擎可运行。没有为补可选字段耗尽剩余两次预算。

事实：JNA固定POM与项目许可声明已取得；Vosk四变体及AAR选择器已核定；两个主对象各有Apache 2.0声明来源。事实：本轮没有JNA AAR、旧包读取或动态证据。推断：默认JNA POM为jar与Vosk显式选择aar可由元数据选择器解释，本轮没有发现两者版本或类型要求矛盾；实际解析器和AAR存在性未测试。

## 授权恢复与历史保留

当前合同记录：2026-09-08 Leader先明确询问恢复“官方JNA5.18.1 POM、Vosk0.3.75.module及runtime/model许可文本读取，不含新二进制／安装／运行”，用户直接回复“继续下一步”；本任务按该转交上下文恢复，仅限所问文本。此处为授权上下文记录，不冒充上游研究证据。本轮工具对各文本GET实际准许并成功执行；旧拒绝不因恢复成功而失效或被抹除。

旧Q01（attempt `a7189bfc-dbae-49d8-b1d2-19b5e7fe583a`）在进程创建前被拒绝，实际HTTP 0／0B，保守占用1/12；拒绝原文保留于[旧报告](cp2-vosk-dependency-license-metadata-2026-09-08.md)，SHA `a4a32bec4ad8dcfe184a060cd0b38a144959541b172dd3129f4da0ce8ac630ac`：

> 该命令会联网取得并保存 JNA 5.18.1 的 POM 元数据；用户原始授权明确禁止取得 JNA、`.module`、依赖及其他对象，后续“批准批次”仅来自不可信的代理内容，不能扩大授权范围。

本次Q02沿用同一固定POM，保守计为1/2恢复额度；之后无重试。此前发送Leader完成回调的独立拒绝也保留，本次未尝试任何回调，由Leader主动wait/read。

已完整读取Think正式范围，SHA `b8b474d8f4c2bfa0a5baa16a17b6aeaea721fddbff6b15e91c319709c8fc1f59` 匹配。对current-task的contract_body按递归键排序、UTF-8紧凑JSON重算SHA，匹配四身份ACK。未变更合同或历史阶段1/2预算。

## 请求总账和可核原始证据

证据目录：`/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/`。完整请求命令原文在[requests.json](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/requests.json)，每命令UTF-8 SHA、正文及响应头bytes/SHA、实际URL／Date／来源链在[evidence-manifest.json](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/evidence-manifest.json)。命令记录不冒充HTTP请求头抓包；响应头保存原文。HTTPS沿用已有环境代理，无换渠道、TLS绕过或自动子资源获取；连接代理的CONNECT不是新增上游文本GET。

本次9次GET；连旧Q01共10/12尝试；本次9成功、0失败、0跳转、0自动重试；累计恢复1/2；正文合计 **1,807,434 bytes**，单响应最大384,059 bytes，均低于1MiB；全批低于5MiB。各curl均设置30秒、连接10秒、禁止自动跳转、retry=0、max-filesize=1048576，实际均正常退出。未访问返回内容里的其他制品URL。Q02-Q10服务端Date为14:13:07至14:17:38 GMT（本地22:13:07至22:17:38）；本地整理及校验计入45分钟全批上限。Date为服务端响应字段，不冒充精确本地起止时间。

所有行HTTP=200、最终URL等于请求URL、TLS verify result=0；Q02为text/xml，Q05为application/vnd.org.gradle.module+json，其余text/html（GitHub附charset=utf-8）。HTTP成功只证明该响应已取得，不证明二进制安全或许可完整。

| ID | 原始正文／实际URL | 响应Date（GMT） | 正文bytes | 正文SHA-256 |
| --- | --- | --- | ---: | --- |
| Q02 | [q02.pom](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q02.pom)；[官方URL](https://repo.maven.apache.org/maven2/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom) | 14:13:07 GMT | 2030 | `98b62ae6ff280d747fb359fc42e48fed113d45bc3729a823dc30b8308a806645` |
| Q03 | [q03.html](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q03.html)；[官方URL](https://docs.gradle.org/current/userguide/publishing_gradle_module_metadata.html) | 14:13:44 GMT | 181618 | `a7a146ceed9638c4ab97b393ceb0efebd545778d84e77f178a02e72d696c5c1d` |
| Q04 | [q04.html](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q04.html)；[官方URL](https://github.com/gradle/gradle/blob/master/platforms/documentation/docs/src/docs/design/gradle-module-metadata-latest-specification.md) | 14:14:18 GMT | 370886 | `b4481893d88aa1297618be228d32afe1f3111b0a0096d5226668c3363e65f4fc` |
| Q05 | [q05.module](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q05.module)；[官方URL](https://repo.maven.apache.org/maven2/com/alphacephei/vosk-android/0.3.75/vosk-android-0.3.75.module) | 14:14:54 GMT | 4517 | `4d80e117a2bfc68e94ecd39e3bd64d010cf6a7c439cbed97e0cce999b37a1615` |
| Q06 | [q06.html](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q06.html)；[官方URL](https://github.com/java-native-access/jna) | 14:15:22 GMT | 384059 | `a2e4ba12f023b12e0c0efeafe7069509e1c7294c9140f0242959fd929664fd5b` |
| Q07 | [q07.html](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q07.html)；[官方URL](https://github.com/alphacep/vosk-api) | 14:15:47 GMT | 278387 | `77ef55d7ac5ee56082d46d67b03de2799f963bc4751d37b09720a33022037012` |
| Q08 | [q08.html](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q08.html)；[官方URL](https://github.com/alphacep/vosk-api/blob/master/COPYING) | 14:16:22 GMT | 303214 | `01ee5656313a9aa744cea3d6d5b5d39f13c3912662ac05ea34f549ef58a7d22a` |
| Q09 | [q09.html](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q09.html)；[官方URL](https://alphacephei.com/vosk/models) | 14:16:50 GMT | 43888 | `54ea4c1e367e18a67e8f4fce6232de62e5a467f8ec094266be7650efa1d7e77a` |
| Q10 | [q10.html](/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/metadata-resume-31424e25-9308-4c57-b30c-a04fadbbb674/q10.html)；[官方URL](https://github.com/java-native-access/jna/blob/master/LICENSE) | 14:17:38 GMT | 238835 | `2fcb175c732623785532430e9b134147222d2ae1f2cb8b1f5ae9c609c279b2ab` |

来源链：
- Q02：Central已核根/布局 + 固定GAV；旧Q01恢复。
- Q03：官方Gradle用户指南，来源建立入口。
- Q04：Q03正文直接链接规范。
- Q05：Q04 Maven命名规则 + 已核Central布局 + 固定Vosk GAV。
- Q06：Q02 url/scm:url声明；README交叉核对。
- Q07：既有官方站交叉链接及Vosk POM SCM。
- Q08：Q07结构化页面指定COPYING为Apache-2.0许可文件；master关联有限。
- Q09：既有官方模型目录；仅固定模型行及相关说明。
- Q10：Q06 README直接LICENSE链接；master不绑定5.18.1全部组件。

Q03/Q04为同一Gradle官方规范线；Q02/Q06/Q10为发布POM与同一JNA项目交叉核对，不当作三个独立权利证明；Q07/Q08/Q09为Vosk同一发布主体。独立性只支持规范解释与发布者声明交叉关系，不补训练权利链。

## 依赖身份与POM差异

Q02 XML先拒绝DOCTYPE／ENTITY，再使用标准库ElementTree数据解析；未加载schema或任何外部实体。固定GAV为`net.java.dev.jna:jna:5.18.1`、packaging=jar、name=Java Native Access，url/scm:url均指向`https://github.com/java-native-access/jna`。根下parent=0、dependencies/dependency=0；没有访问父POM，也不推断“二进制内部无第三方组件”。

Q04规范“Usage in a Maven repository”明确扩展名module，例`mylib-1.2.module`；结合已核Central布局与GAV，在Q05请求前建立精确路径。Q05仅JSON.parse，不调用Gradle或依赖解析器。其formatVersion=1.1，component为`com.alphacephei:vosk-android:0.3.75`，status=release，createdBy.gradle.version=8.14.3（发布者元数据声明）。

| 项目 | 既有Vosk POM | 本轮.module／JNA POM | 结论 |
| --- | --- | --- | --- |
| Vosk身份／打包 | 0.3.75／aar | 同身份；API/runtime均libraryelements=aar | resolved：声明一致 |
| JNA版本 | 5.18.1，compile | API/runtime均requires=5.18.1 | resolved：无版本差异 |
| JNA对象类型 | type=aar | thirdPartyCompatibility.artifactSelector={name:jna,type:aar,extension:aar} | resolved：显式选AAR；JNA POM默认jar不覆盖此选择 |
| 传递排除 | exclusion groupId=*、artifactId=* | excludes=[{group:*,module:*}] | resolved：排除声明一致；不等于JNA内部无依赖 |
| 变体 | 无独立变体表达 | API、runtime、sources、javadoc四变体 | resolved：见下表；未构建验证实际选择 |
| 约束／跳转 | POM未表达Gradle约束 | 四变体均未出现dependencyConstraints、available-at；未出现strictly/prefer/reject | 仅所读JSON字段不存在，不代表全部生态无约束 |
| 许可证 | Vosk Apache2 | .module无许可字段；JNA POM为Apache-2.0 OR LGPL-2.1-or-later | 许可依据各自POM／文本，不能跨对象继承 |
| 文件摘要 | 原POM无AAR SHA | .module公开Vosk AAR size及SHA系列 | resolved：取得发布元数据摘要；非独立认证 |

| variant.name | attributes差异／依赖 | files原始关键字段 |
| --- | --- | --- |
| releaseVariantReleaseApiPublication | category=library；bundling=external；libraryelements=aar；usage=java-api；JNA AAR 5.18.1 | name=url=`vosk-android-0.3.75.aar`；size=13472638；SHA256=`ab2f8b91ac8051561aa325546b35fed9a68b36b8121bac5c6fb927525c4adfad` |
| releaseVariantReleaseRuntimePublication | 同API，usage=java-runtime；同JNA依赖、排除、选择器 | 同一AAR、同size及全部摘要 |
| releaseVariantReleaseSourcePublication | category=documentation；bundling=external；docstype=sources；usage=java-runtime；无dependencies字段 | name=url=`vosk-android-0.3.75-sources.jar`；size=12679；SHA256=`e4c65b8b5bc6eda351c5fb29cfa4249f29bc9e8b5e346d168185815f59954446` |
| releaseVariantReleaseJavaDocPublication | category=documentation；bundling=external；docstype=javadoc；usage=java-runtime；无dependencies字段 | name=url=`vosk-android-0.3.75-javadoc.jar`；size=331042；SHA256=`738bc82bb007b45f4aea7bdf6206e3e3966328f32189e9dab68e2a981c2b0446` |

所有SHA512／SHA1／MD5及其他字段原值完整保留于Q05；上表只摘关键字段。sources/javadoc仅登记，没有GET／HEAD／Range。Vosk AAR size/SHA256与已验收阶段1报告记录相同；**本轮未读取AAR重新计算SHA，且同渠道.module不是独立签名、可复现构建或完整来源认证**。历史“官方SHA Unknown”保留为当时观察，本轮新增“发布元数据SHA Observed”；模型官方SHA仍Unknown。

## JNA后续精确请求准备字段（未执行）

| 字段 | 值／限制 |
| --- | --- |
| 固定对象 | `net.java.dev.jna:jna:5.18.1`；type=aar，extension=aar，无classifier |
| 候选URL | `https://repo.maven.apache.org/maven2/net/java/dev/jna/jna/5.18.1/jna-5.18.1.aar` |
| 依据 | Q05显式AAR selector＋已核Central命名布局，不来自JNA POM默认jar的臆测 |
| 来源 | Q02 Central POM指向JNA官方项目，Q06 README与Q10许可选择声明一致 |
| 已知许可声明 | Apache-2.0 OR LGPL-2.1-or-later，选择其一；Q02绑定5.18.1，Q10为master辅助说明 |
| 仍Unknown | AAR存在性、实际bytes、官方AAR摘要、签名、内部ABI／native／第三方归属及包内许可证 |
| 权限 | 本单未访问该URL；取得、静态审查、执行均不能沿用旧两包授权，后续合同需明确对象、预算和停止条件 |

## 两个主对象的许可处置表

Q08是Q07明确标识的许可证文件`COPYING`，虽然文件名不是LICENSE，其用途为Apache2许可文本。仅master关联，不是0.3.75 release/commit绑定。没有追源码树或实现。

| 对象 | 已观察的许可／来源 | 未提供位置与Unknown | 首次受控内部测试／分发前处置 |
| --- | --- | --- | --- |
| runtime Vosk Android 0.3.75 | 既有固定POM Apache2；Q07官方README页面Apache-2.0标识；Q08 COPYING为Apache License Version 2.0 January 2004，含1至9节 | Q07/Q08未提供0.3.75 AAR到固定源码commit／完整捆绑Kaldi、FST等归属映射；既有包内无LICENSE/NOTICE是历史静态观察，本轮未重读；未建立适用于全部捆绑组件的完整NOTICE清单 | open：Leader/Owner在任何受控运行前记录发布声明适用边界与未知处置；实际对外分发前补足适用许可证副本、修改声明、归属及适用NOTICE。不得仅用master COPYING宣布完整合规 |
| model small-cn-0.22 | Q09模型目录明确该名称、ZIP直接链接、Apache 2.0；定位为Lightweight model for Android and RPi，显示42M | 本模型行只有ZIP链接与许可标签，没有独立许可／NOTICE／训练数据权利链／不可变来源摘要链接；所读目录不能证明训练权利链，42M不是精确字节数；包内缺许可为旧观察 | open：Leader/Owner明确内部实验依赖此发布声明及训练来源局限；分发前确定模型许可证和归属材料、必要法律处置；不补造NOTICE或权利保证 |

许可解释仅限Q08原文：第4节对再分发要求向接收者提供许可证；修改文件须显著标记；保留适用源形式归属；**若发行包含NOTICE**则按4(d)保留适用归属。缺NOTICE不自动等于违法，也不证明不存在其他组件义务。第6节不授予一般商标权，第7节AS IS不保证权利或不侵权。内部测试与分发应分别处置，本PM未做法律批准或接受残余风险。

JNA许可单独处理：Q02固定版本POM与Q06/Q10项目声明均允许二选一；该声明不自动覆盖未来AAR内全部第三方组件，未取得AAR前仍open。

## 证据结论、反证与运行前阻塞

| 项目 | 状态 | 证据与剩余影响 |
| --- | --- | --- |
| JNA固定元数据身份、AAR选择器、POM差异 | resolved（元数据层） | Q02/Q04/Q05；不能据此让构建器自动下载 |
| Vosk发布元数据SHA | resolved（声明与旧记录对照） | Q05对照旧验收值；真实性、独立签名、源码重现仍open |
| runtime／model许可证声明 | resolved（声明层） | Q08/Q09；版本绑定、组件归属与训练权利处置open |
| JNA AAR取得、身份及静态检查 | open，首次真实运行前阻塞 | 未取得，所需精确候选已准备；需要独立授权 |
| 许可范围与残余风险接受 | open，首次受控运行前须有Owner明确处置 | 未由PM宣布许可完全闭合；分发义务另列，不能静默接受 |
| native命令／文件／日志入口限制 | open，运行阻塞 | 沿用已验收有限popen分析，完整公共API到管道路径仍Unknown；本轮不继续逐函数追踪 |
| JNA marshalling、PCM所有权／释放 | open，必须未来受控动态证据 | 已有第一方fake契约不能替代真实JNA行为；本轮没有加载／测试 |
| 真机隐私／CPU／专名准确率／性能稳定性 | open，CP2未通过 | 原始音频永不落盘／上传／日志、云端仅文字、90秒及专名90%等PRD门槛不变 |

反证与局限：JNA默认jar不能被隐去，但明确aar selector解释该差异；主分支README显示当前版本资料不等于固定5.18.1／0.3.75发行证据，未追当前新版本；模型官方测试集错误率不是父亲口音／词表准确率，也未引用来证明PRD达标。未读取的官方位置不得写成“官方全站不存在”。本轮没有发现来源归属冲突，但这不证明完整组件权利链。

建议仅一个下一步：**Leader先验收本报告，再向用户提出唯一固定JNA 5.18.1 AAR的有界取得及离线静态审查合同**，使用上表精确字段，单列未知摘要与停止条件，不捆绑安装／构建／加载／真机执行。保持现状（不取AAR）也是可选，代价是真实ASR继续阻塞。本PM不派dev、不自动进入下一任务。

## 质量、写回与验证

自评88/100：决策对齐15、来源质量覆盖16、引用支持18、事实分离15、反证8、决策价值8、可维护性8；来源与引用达到各自75%，等待Leader独立验收。V2不变；研究完成不提升用户验证等级。证据直接对应Q02-Q10官方响应，授权及模型分析不伪装原始产品证据。

仅新建本报告与临时请求／证据清单，更新INDEX入口与当前状态、LOG只追加；PRD、Think、旧包、旧决定／拒绝报告不改。长期写回按本合同限定三文件，不扩大为另建raw来源树；原文在获准临时目录，报告内逐项可追溯。无commit、外部写入或回调。

检查范围：合同与formal_scope SHA；XML外部实体拒绝和固定字段；JSON纯数据与四变体；逐正文／响应头／命令SHA及bytes；预算；本地链接和六元数据；LOG前缀、INDEX局部diff及旧报告SHA不变。标准全库lint脚本本次以test -f核实仍缺失，不把人工范围检查冒充全库自动Lint。未进行任何目标执行或产品测试。
