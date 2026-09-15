# Vosk 依赖与许可元数据批次：权限前置停止

Owner: Product Lead
Last updated: 2026-09-08
Source: `CP2-VOSK-DEPENDENCY-LICENSE-METADATA-001`；固定formal_scope；Leader同步verification/review；本轮exec_command审批拒绝原文；既有元数据／阶段2报告
Confidence: High（拒绝与零网络事实）；Low（本批次待核元数据）
Related decisions: `cp2-vosk-integration-gaps-decision-2026-09-08.md`；`cp2-vosk-stage2-scope-decision-2026-09-08.md`
Next review date: 2026-09-15
Research Quality: 55/100 · fail（本批次未取得任何新官方证据，不覆盖先前研究评分）
Validation Level: V2（不变）
Next evidence: 用户直接确认仅官方JNA POM／Vosk.module及主对象许可说明的只读批次权限后，由Leader处理恢复；本次不重试
Allowed next investment: 当前仅停止报告及等待权限澄清；无网络、新二进制或目标执行
Pause/Kill condition: 实际自动审批拒绝，已停止全批，不换工具／渠道规避

## 身份与RESULT

```json
{"task_id":"CP2-VOSK-DEPENDENCY-LICENSE-METADATA-001","attempt_id":"a7189bfc-dbae-49d8-b1d2-19b5e7fe583a","contract_sha256":"4890e23aed783255c73910d55b902e803e36c7da6f96ad5c4837375fe164b849","assigned_thread_id":"01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779","acknowledged":true,"result":"BLOCKED","metadata_result":"metadata_insufficient"}
```

这是权限前置停止，不是JNA不存在、许可不合格或Vosk不可用。当前本批次没有任何官方响应正文、HTTP状态、重定向、版本／许可新观察；没有取得制品或读取现有二进制。

## 固定输入核对

- 正式范围 `/Users/orderly_ray/Projects/think/doc/cp2-vosk-integration-gaps-decision-2026-09-08.md` 已完整读取，SHA-256=`b8b474d8f4c2bfa0a5baa16a17b6aeaea721fddbff6b15e91c319709c8fc1f59`，匹配current-task。
- 已读取Leader `CP2-VOSK-INTEGRATION-GAPS-DOC-SYNC-001-verification.md` 与同前缀review.json：同步0cc8846b、四文件、两个固定源文件bytes/SHA一致，verdict=accepted。这里只转述已验收同步，不声称本PM重新查验commit或包。
- 合同允许的研究范围与工具审批认可的权限不同：前者已下发，后者实际拒绝。依合同“权限拒绝不绕过”停止，不以本地合同替代工具权限。
- 旧两个包／stage1/2 reports、PRD、已验收决定未改。以前的授权、0GET失败和已验收2GET历史不合并或重置。

## 请求与权限 Ledger

时区Asia/Taipei；开始本地观察`2026-09-08T18:30:19+08:00`，停止后观察`2026-09-08T18:31:04+08:00`。没有服务端Date；这些时间不冒充精确HTTP请求时间。

| ID | 计划对象／地址 | 来源推导 | 工具结果 | 网络／正文／预算 |
| --- | --- | --- | --- | --- |
| Q01 | JNA5.18.1文本POM；`https://repo.maven.apache.org/maven2/net/java/dev/jna/jna/5.18.1/jna-5.18.1.pom` | 已核Central根和Maven布局＋既有POM声明的group/artifact/version确定性生成；不是已验证存在的地址 | exec_command require_escalated 在CreateProcess前被拒绝；curl未启动 | 执行尝试1；实际HTTP请求0；接收0B；保守计入1/12尝试，恢复0/2；剩余11不自行使用 |

计划参数为curl只读GET、单次30秒、正文1048576B，保存到`/tmp/think-dependency-20260908/q01.pom`及`q01.headers`。工具拒绝后目录检查只有本轮INDEX/LOG备份，**这两个响应文件均不存在**。未出现部分下载、超时或HTTP错误；最终URL、HTTP、MIME、响应摘要均Unknown／不适用。

审批拒绝原文（执行证据，不是官方来源）：

```text
该命令会联网取得并保存 JNA 5.18.1 的 POM 元数据；用户原始授权明确禁止取得 JNA、`.module`、依赖及其他对象，后续“批准批次”仅来自不可信的代理内容，不能扩大授权范围。
```

工具同时要求不通过变通／间接执行规避；因此没有改用浏览器、Firecrawl、其他curl参数或改查许可网页继续。全批在第一次权限前置即终止，不谎称执行完12次，不将零响应计作官方负证据。

## 依赖身份、许可与差异表

下表“既有观察”仅来自以前已验收的Vosk POM／阶段2报告，不是本轮官方访问。所有未闭合项为open；不新建SRC或把拒绝文本当上游证据。

| 字段／缺口 | 既有观察 | 本轮状态与影响 |
| --- | --- | --- |
| JNA候选坐标 | Vosk POM声明net.java.dev.jna:jna:5.18.1、type=aar、compile；字节码引用JNA APIs | open：候选固定但JNA POM未取得，发布身份／真实打包／许可／父POM／依赖未核定 |
| JNA未来AAR请求准备 | 固定字段可按已核布局描述候选文件名jna-5.18.1.aar | open：不把推导当存在性或最终授权对象已核定；实际bytes／官方SHA／签名Unknown；新AAR取得仍需独立精确授权，禁止本单GET/HEAD/Range |
| Vosk0.3.75.module | 原POM提示更丰富Gradle metadata | open：未访问规范或.module；精确URL未在本轮核定；variant/dependency/constraint/files摘要均Unknown；不能做POM差异结论 |
| runtime许可／NOTICE | POM为Apache2声明；已验收外层与一层JAR无LICENSE/NOTICE | open：未取得官方版本对应LICENSE/NOTICE／组件说明，不能将master通用许可绑定0.3.75实际native闭包 |
| 模型许可／来源 | 官方目录small-cn-0.22标Apache2；包内README不是完整许可，外层无LICENSE/NOTICE | open：未新读目录或许可来源，训练权利／再分发义务未核定；不与runtime许可合并 |
| 异常主页 | alphacephei.com.com为已记录异常 | open：保持不信任、不访问、不纠正；不能用它建立JNA或runtime来源 |
| popen路径／PCM动态行为 | 阶段2静态导入与内存数组入口已知 | open且非本批次执行范围：未做包内可达性追踪，未执行或实测；仍待未来限定证据与适当权限 |

本轮resolved仅限任务身份与固定scope匹配、同步验收已存在、实际权限拒绝被正确记录；**没有依赖／变体／许可缺口被resolved**。原元数据身份ready不等于此批次或运行准入通过。

## 后续权限澄清的最小范围

需要用户本人直接确认的只是本次官方文本／元数据读取范围：固定JNA5.18.1 POM、Vosk0.3.75.module与必要官方规范、主runtime／模型许可来源说明，按原最多12次（保留Q01记录）、1MiB/响应、5MiB总、30秒/请求、45分钟全批执行。不包含JNA AAR、任何新二进制／源码实现／签名sidecar、已有包重取或目标执行，不重批已取得两个包。

本报告不是授权句生效，也不以剩余预算作为恢复许可。Leader应先处理这项实际权限差异，再恢复相同范围；不得自动执行popen核查、集成或阶段3。若用户明确不授权该读取，保持metadata_insufficient和采用blocked。

## 验收、写回及产品边界

- 已核对四身份与formal_scope，保留唯一尝试／实际0请求／0B／拒绝原文；来源／版本／许可未知没有猜补。
- 未安装／构建／运行／解析目标、未新读旧包、未改Think／PRD或原reports。只新增本文及必要INDEX/LOG；无提交，其余已有改动保留。
- 本地检查元数据、链接、日志前缀和Git差异；全库lint脚本仍缺失，完整自动Lint未运行。没有新官方原文可保存或计算SHA，不用虚构XML填充。
- Research Quality55分仅反映本批次未取得证据：决策15、来源4、引用3、分层15、反证5、决策价值5、维护8；V2不升级。
- 两对象仍manual_review，adoption_gate=blocked。原音频不落盘／不上传／不进日志、仅文字上云、三步／90秒、专名90%、CP1恢复／Conformer／词表deferred和CP2/CP3/Alpha门槛不变。
- 完整结果留本PM最终报告；回调如被拒不重试。此次查询拒绝不冒充回调拒绝，不声称已向Leader送达。
