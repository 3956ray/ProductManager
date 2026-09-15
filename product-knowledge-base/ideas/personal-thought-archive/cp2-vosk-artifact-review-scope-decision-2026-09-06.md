# 决策：Vosk 精确制品取得与静态审查范围

Owner: Product Lead
Last updated: 2026-09-06
Source: `CP2-VOSK-ARTIFACT-REVIEW-SCOPE-DECISION-001`；`cp2-vosk-android-maven-metadata-2026-09-06.md`；既有三身份记录；正式候选选择决定；Leader Maven metadata acceptance；本地 scan-untrusted-code 静态边界与风险模型
Confidence: Medium-High（可定义精确请求与静态边界；制品、安全、完整供应链及设备未验证）
Related decisions: `cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md`；`cp2-vosk-android-identity-gap-decision-2026-09-06.md`；`prd-v0.1-2026-09-04.md`
Next review date: 2026-09-13
Research Quality: 90/100 · pass（沿用已验收元数据研究，仅支持身份与本范围；不是安全评分）
Validation Level: V2（保持，不升级）
Next evidence: Leader验收范围、同步最新正式文档并取得用户对下述两个精确对象的明确授权后，才可下发唯一静态审查单
Allowed next investment: 当前仅文档收尾与授权准备；未来授权仅取得两个精确制品并静态审查，不采用、不执行
Pause/Kill condition: 未获精确授权／文档未同步／现有工具不能落实隔离与预算／来源类型身份冲突／结构风险或预算触发时停止；依赖与二进制来源缺口阻止采用

## RESULT

**APPROVED：批准下一项精确制品静态审查的范围及待用户确认授权请求，不批准实际取得。**

本轮不联网、不读新metadata／sidecar／源码、不下载、不安装、不构建、不修改Think。Leader验收研究或本范围不等于用户已批准制品请求。唯一下一任务为 `CP2-VOSK-ARTIFACT-STATIC-REVIEW-001`；执行前必须另有用户明确确认及正式文档同步，不由PM自行派发。

## 身份依据与两个对象

已验收Maven报告：18556 bytes，SHA-256 `f6e70fcbd52e4859f2cdae353eb4720545a135446c9c44206e64e4a0693c67c7`。Leader验收报告SHA为 `fa2ae324f9b9e5e9e034b065320572f6175c0ee4e9b776744c93ed0417717f4d`，只确认元数据身份；没有制品权限。模型身份文档6201 bytes，SHA为 `14a64e8fe55844daff2394c8bef65292136262986b6e5fa1179628964d8433b1`。

| ID | 精确对象／唯一允许GET URL | 已知来源与许可证声明 | 未验证 |
| --- | --- | --- | --- |
| A | `com.alphacephei:vosk-android:0.3.75`，文件 `vosk-android-0.3.75.aar`；`https://repo.maven.apache.org/maven2/com/alphacephei/vosk-android/0.3.75/vosk-android-0.3.75.aar` | 已核定Central root＋Apache布局＋同版本POM的aar声明；POM开发者Alpha Cephei Inc、SCM alphacep/vosk-api、Apache License 2.0 | 此地址是规范推导，未请求、存在性未验证；精确大小、官方制品SHA／签名、包内容、源码commit均Unknown |
| B | `vosk-model-small-cn-0.22`，文件 `vosk-model-small-cn-0.22.zip`；`https://alphacephei.com/vosk/models/vosk-model-small-cn-0.22.zip` | 官方模型目录直接href，原条目42M、Apache 2.0，Alpha Cephei官方发布入口 | 未请求；42M不是精确字节数；官方制品SHA／签名、完整包许可、训练来源／权利链Unknown |

不得把元数据XML的SHA当AAR SHA，也不得把下载后自行计算的SHA冒充官方预发布摘要或来源认证。下载只固定“此次收到的bytes”；没有独立签名／可复现来源证据，来源完整性仍需后续审查。

## 三个强制保留项

1. POM异常主页 `http://www.alphacephei.com.com/vosk/` 不访问、不信任、不自动改为其他域名；只在报告中原样引用为异常。身份链使用已验收Central、固定坐标与匹配SCM，不因此宣称异常无害。
2. POM声明 `net.java.dev.jna:jna:5.18.1`、type=aar、scope=compile。它是未审依赖，不属于下述两个对象；**禁止隐式下载JNA、其POM或任何传递依赖**。若AAR内已捆绑其他组件，只审其已随授权AAR到达的bytes，另列来源／许可待核定，不自动等同外部JNA坐标。
3. POM的Gradle metadata提示不构成`.module`权限。`.module`、依赖变体／约束、sidecar、签名、公钥、SBOM和新源码均不在下一单网络白名单中，全部保留Unknown。主AAR静态扫描绝不等于整个Android依赖闭包通过。

## 下一单合同

### 前置条件与工具

- Leader先验收本决定，将本决定及最新PRD／元数据结论和入口同步到Think正式文档并复核身份；这是执行前置，**本PM不执行同步，也不自动创建开发任务**。
- 用户明确批准下方完整授权句或等价、同样精确的授权；执行合同记录确认来源、时间和两个对象。旧研究、旧sherpa授权、范围APPROVED、默认继续工作都不替代这次授权。
- 只使用现有、已审可用的下载与静态工具。执行者在接触制品前记录工具路径／版本／摘要、既有审查依据及实际可覆盖格式／资源限制；本决定没有认证任何尚未检查的工具。
- 工具必须能把AAR按ZIP数据处理、在不解压到文件系统的情况下检查成员／嵌套classes.jar，并限制解析资源。不能支持时返回`blocked`及工具缺口；不临时安装第三方、不以执行目标或普通解压作为替代。不强制新增专用工具工程或重复冻结链。

### 一单、串行、独立裁决

1. 新建隔离目录并确认不存在可覆盖的旧run；记录授权及输入身份，先处理AAR A。
2. A完整取得后立即记录实际bytes与SHA，网络关闭，完成A的结构检查及有界静态审查并给出独立裁决。
3. A出现获取／结构／预算硬停止或`block`时，**不再请求模型B**。A为`manual_review`且原因仅是完整许可、二进制来源、未审依赖、能力覆盖等已记录非结构未知时，才可在同一授权单内继续B；继续不等于解除A的门禁。
4. B以自身来源、实际SHA、结构、许可、模型文件清单与证据独立审查；不能继承A的许可、安全或格式结论。
5. 汇总两对象状态、未执行步骤及整体依赖／来源缺口；报告后停止，不同时派两个任务，不开始采用或阶段C。

### 网络、类型与保存边界

- 仅表中两个HTTPS URL，各最多**1次GET**，全单最多**2次GET**；不预做HEAD／Range／metadata或sidecar请求，不自动retry／redirect。重定向无论同域或跨域均停止并记录Location，不跟随、不修改URL继续。
- 校验证书及host/path，禁止降级HTTP／忽略TLS错误／登录／额外条款／第三方镜像。只接受目标HTTP200与ZIP类响应：`application/zip`、`application/x-zip-compressed`、`application/java-archive`或`application/octet-stream`；同时核对ZIP魔数及完整中央目录，不能只凭MIME放行。HTML/XML错误页、类型不符、截断、长度不一致或畸形内容即停；未知类型回报，不自行扩白名单。
- 每个响应正文最多**64 MiB**，累计最多**128 MiB**，单GET最多**120秒**，响应头各最多**64 KiB**。这些是设计的止损上限，不是官方实际大小声明；模型42M仅为目录量级，不要求与64MiB相等。下载实现须在流读取时限额，不能下载完才裁剪。
- 若Content-Length存在则先检查上限、完整响应后比对实收长度；缺失时仍流式计数和强制截断停止。到达上限、超时、错误或网络权限拒绝立即结束本单，不再请求另一对象。失败残片标`partial`，不当完整制品进入扫描；保留其bytes／SHA及停止证据，不自动删除或重取。
- 保存根目录固定为 `/private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/`，子目录`artifacts/`、`reports/`；新目录0700、制品0600，不覆盖既有路径，不允许链接指向仓库／家目录其他位置。该目录不加入Git、不置于App资产／依赖缓存／IDE项目、不云同步或上传公共恶意软件扫描服务。
- 默认不具可执行权限；从可信工具目录启动静态工具，不在目标目录运行Git、Maven、Gradle、Python项目或安装器；不导入目标、不dlopen、不加载模型、不做推理。网络仅在两个获准GET的取得窗口开放，静态阶段离线。

### 归档与静态资源上限

在不落地解压成员的前提下先枚举元数据，再决定是否读取成员。总成员数最多**10000**（含嵌套JAR），累计实际解压读取最多**512 MiB**、单成员最多**128 MiB**、单成员声明压缩比最多**100:1**。AAR仅允许**一层嵌套JAR**读取，例如classes.jar或libs/*.jar；模型ZIP不递归读取嵌套归档。所有嵌套成员复用同一预算，不能在内层重置。

文本／配置扫描单成员最多**2 MiB**、累计文本最多**32 MiB**；静态审查每对象最多**10分钟**、进程可用内存最多**1 GiB**。这些是执行防护配置，须由已审工具或现有隔离环境实际限制；无法落实则前置blocked，不一边取得一边扩大工具范围。

中央目录声明超限、实际流量超限、重复／规范化或大小写冲突路径、绝对路径、`..`越界、符号／硬链接、设备文件、加密归档、异常ZIP结构或CRC失败触发硬停止。越界／恶意结构明确为block；仅压缩比／格式能力／资源上限不足且无恶意证据时为manual_review并`hard_stop=true`，不得为了覆盖而提高预算或提取后继续。

更深嵌套、未知二进制格式或无法读取的成员明确列入未覆盖表，不执行／解压绕过。不得把“跳过大文件或二进制”写成已完整扫描；格式安全与文本命中少不代表二进制安全。

### 静态证据内容

| 面向对象 | 必须记录 | 解释边界 |
| --- | --- | --- |
| 每个制品 | 请求／最终URL、HTTP／MIME／时间、bytes、实际SHA、授权引用、工具清单、原归档目录与成员大小／类型／覆盖表 | SHA只固定此次对象；没有官方摘要的对照不能假装验证通过 |
| 归档安全 | 路径／链接／重复条目、嵌套、压缩／展开上限、加密／截断／CRC等静态检查 | 不解压到文件系统，不执行成员，异常按硬停止处理 |
| AAR许可与来源 | 包内LICENSE／NOTICE／元数据原文及位置，与既有POM声明对照；bundled组件、native库来源、构建标识／可见版本 | 缺LICENSE／NOTICE或二进制来源时manual_review；不将未核notice义务当“未发现所以不需要” |
| AAR能力 | AndroidManifest、classes.jar及可见JNI/native清单；ABI标识、导入符号／字符串中网络、文件、动态加载、日志、音频入口线索；声明依赖与内含组件区分 | 仅使用支持内存／归档读取的已审静态解析；字符串／符号不是调用可达或真实行为，未覆盖的方法／二进制明确Unknown |
| 模型 | 顶层目录与声学模型／图／配置／词表文件清单，LICENSE／NOTICE／作者和训练来源声明，异常脚本／外部路径引用 | 文件名与格式只作结构证据，不加载模型、不证明中文准确率、CPU或与runtime兼容；训练权利链未知不隐去 |
| 总体 | 异常主页、JNA5.18.1、未读.module、完整依赖及源码可复现性缺口 | 不查询这些外部对象，不自动下载或继承本单许可，不声明全供应链通过 |

使用`scan-untrusted-code`时保留其原始JSON／Markdown裁决及命中上下文。其通用规则不做二进制来源认证、签名验证、反编译或动态分析，不能以exit0替代覆盖清单。CI、文档、样本命令与可执行行为区分；只有明确风险链或结构越界才作block，不以术语出现次数认定恶意。

### 交付与可判定状态

交付在隔离`reports/`中至少包括：`acquisition-ledger.json`、`runtime-static-review.md`、`model-static-review.md`、`artifact-review-summary.md`，以及工具原始报告和完整成员／覆盖清单。未到达B时模型报告记`not_acquired`并引用停止原因，不伪造空扫描。正式摘要随后由获准执行者按任务合同写回，不自动拷贝制品进Think。

每对象给出且区分：

- `low_indicators`：在列明静态覆盖内没有配置规则的高风险迹象，**不叫safe／采用通过**。
- `manual_review`：许可／来源／二进制／跳过项／依赖等证据不足，说明具体缺口与是否hard_stop。
- `block`：确认的结构越界、关键来源冲突或可执行恶意链；停止且不得执行。
- `not_acquired`：未授权、前置失败或前项停止后未取得，不能算扫描结果。

全单任务完成状态为`complete`（两个对象有可核查审查结果及限制）或`blocked`（前置／取得／资源／结构硬停止使合同未完成）；**complete可以伴随manual_review，不是安全通过**。若工具产生`sandbox_only`，保留原值但执行权限仍为禁止，不启动沙箱运行。

主AAR存在未审JNA／.module、签名和二进制可复现来源缺口，因此即使通用扫描为low_indicators，runtime采用门至少仍为manual_review；**整体`adoption_gate=blocked`固定不解除**。模型许可／来源亦单独判断。下一单的合理成功是固定实际bytes并产出可信静态证据与缺口，不是闭合全部供应链。之后如需依赖／源码／元数据／动态验证，回新范围决定，不自行获取。

## 待用户确认的精确授权句

下列文本已经填好精确对象与边界，**目前只是授权请求草案，未获得用户确认**；引用或生成它本身不使权限生效。

> 我授权唯一任务 CP2-VOSK-ARTIFACT-STATIC-REVIEW-001，在Leader验收范围并同步最新正式文档后，仅按该合同串行取得和静态审查两个对象：Vosk Android com.alphacephei:vosk-android:0.3.75 的 vosk-android-0.3.75.aar，URL https://repo.maven.apache.org/maven2/com/alphacephei/vosk-android/0.3.75/vosk-android-0.3.75.aar；中文模型 vosk-model-small-cn-0.22 的 vosk-model-small-cn-0.22.zip，URL https://alphacephei.com/vosk/models/vosk-model-small-cn-0.22.zip。我知悉AAR地址为规范推导且未验证存在，两对象官方制品SHA当前Unknown；取得后记录实际bytes和SHA但不得称为官方校验通过。每对象仅1次GET、最多64MiB和120秒，总计最多2次GET／128MiB，任何重定向、类型或身份不符、资源上限及合同硬停止均立即停止；AAR硬停止后不得再取得模型。只保存到 /private/tmp/think-vosk-artifact-review/CP2-VOSK-ARTIFACT-STATIC-REVIEW-001/，遵守归档不落地解压和有界离线静态检查。禁止取得JNA、.module、sidecar、签名公钥、依赖、源码或其他对象；不访问异常主页，不安装、不导入、不构建、不加载、不运行、不推理、不集成、不做真机测试、不上传外部扫描服务。采用门继续blocked，任何执行和后续对象另行明确授权。

该句只覆盖下一单两个对象；用户未确认前网络和制品动作均禁止。若对象、版本、URL、预算或工具范围需改变，停止回Leader，不用这一句覆盖新内容。

## 保持不变与本轮核对

三步录入／找回、按住说话、单段90秒、原始音频不落盘／不上传／不进日志、云端仅文字、个性词表与专名90%不变。CP1父亲人工、Conformer、词表实现仍Deferred, not removed；CP1人工必须在任何CP3准入前恢复。CP2未通过，CP3和父亲Alpha未批准；小米15的ABI／CPU／PCM／隐私／性能／稳定性／飞行模式均待独立证据；不恢复sherpa链。

本轮仅新增本决定及必要PRD／INDEX／LOG，不改变旧研究和身份报告，无联网／实际审查／制品取得／工具安装／Git提交或Think修改。Think只读HEAD为 `92e5027852b8c2cb8476f7c2da684ef98f61ec82`、clean。本地核对输入SHA、元数据、链接、日志前缀、差异与权限语义；全库lint脚本缺失，不宣称全库自动通过。完成只在本PM最终答复留证据，停止待Leader，不派开发者。
