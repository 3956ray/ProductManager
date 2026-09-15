# Vosk 官方身份准备就绪记录

Owner: Product Lead
Last updated: 2026-09-06
Source: `/Users/orderly_ray/Leader/orchestration/current-task.json`（CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001 及 resume_authority）；正式选择决定；`CP2-VOSK-SELECTION-DECISION-SYNC-001-acceptance.md`；R01/R02/R03/M01/M02 ledger 与三份成功官方说明／元数据响应
Confidence: High（来源及预算记录）；Medium（Android 精确制品绑定未核定）
Related decisions: `cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md`
Next review date: 2026-09-13
Research Quality: 82/100 · fail（续接；Android 精确版本绑定未闭合；首次 55 分与 R1 92 分均保留）
Validation Level: V2（无新增产品使用或付款证据）
Next evidence: Leader 验收本次官方证据，裁定 Android 精确版本／坐标绑定缺口；本任务不自行增加 runtime 预算
Allowed next investment: 本地收尾和等待验收；不形成阶段 B/C 授权
Pause/Kill condition: runtime 3/3 已用尽仍不能唯一指认精确 Android 制品；已停止，不挪用模型预算

## RESULT

**identity_insufficient**

当前为同任务获准渠道续接后的结果：已核定模型 `vosk-model-small-cn-0.22`、官方文件名／URL、`42M` 与 Apache 2.0 条目标识；已核定项目 release `v0.3.50` 和 Android 包名 `com.alphacephei:vosk-android`，但安装说明只给动态版本 `0.3.32+`，release 附件为空，不能证明该 tag 对应某一精确 Android 包。runtime 3/3 用尽后停止，总尝试 5/6、model 2/3。模型剩余预算不转用于 runtime，当前仍不得构造可生效的阶段 B 授权。

以下首次停止正文及 R01 原记录保留为历史；新证据和当前验收以文末“续接最终记录”为准。

## 首次结果（历史）

首次结果为 `identity_insufficient`，原因为服务额度阻塞：

唯一候选仍为 Vosk。运行库首个官方入口请求因 Firecrawl 服务额度不足失败，没有页面正文、链接、发行元数据、HTTP 状态或最终 URL 返回。模型页面未请求。无法固定 runtime 的精确 release／Android 坐标以及中文模型的名称／修订／对象，因此不具备提出可唯一指认对象的制品审查授权的身份条件。

这是获取渠道阻塞下的有界停止，不是 Vosk 不可用、不安全或许可证不合格，也不否定 R1 研究。没有构造生效授权、自动改选、购买额度、安装工具或切换获取渠道。

## 输入核对

- 当前合同由 Leader 派发至本 PM `01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779`；目标为最多 6 个端点，runtime/model 各最多 3。
- 正式决定路径：`/Users/orderly_ray/Projects/think/doc/cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md`；SHA-256 `d58d59a51a94afc92f55f4211bd273972fe6b516d2823108ba55c9d27f166176`，与 current-task 一致。
- 选择决定同步已由 Leader 验收，Think HEAD `92e5027852b8c2cb8476f7c2da684ef98f61ec82`；本轮开始检查为 clean。选择文档中的“尚待验收”是当时历史状态，本轮以同步验收和新下发合同为准，不修改已验收原件。
- R1 已登记仓库 `https://github.com/alphacep/vosk-api` 为官方入口；请求前据此确认来源，不通过名称猜测新域名。

## 访问 Ledger

访问日期为 2026-09-06，时区 Asia/Taipei（UTC+08）；下列请求未保存精确开始秒数，不用记录时间冒充请求时间。收尾记录时间为 `2026-09-06T20:32:27+08:00`。

| 记录 | 对象／目的 | 尝试 URL | 最终 URL／HTTP 状态 | 结果与可见证据 | 预算 |
| --- | --- | --- | --- | --- | --- |
| T00 | 既有工具预检 `firecrawl --status` | 无；本地命令 | 不适用 | `command not found: firecrawl`，exit 127；没有安装或 npx 拉取 | 不计官方端点 |
| R01 | runtime；读取已登记官方仓库首页 README／公开说明及链接，准备固定发行与许可证入口 | https://github.com/alphacep/vosk-api | Unknown；服务未返回最终 URL 或 HTTP 状态，不能声称已到达 GitHub | 已启用 Firecrawl MCP 的 scrape 返回 `Insufficient credits to perform this request`，`isError=true`，`error_code=INVALID_ARGUMENT`；没有官方正文、链接或元数据 | runtime 1/3，总计 1/6（失败也计入） |

R01 参数为 `formats=[markdown,links]`、`onlyMainContent=true`、`maxAge=0`；只请求一个已登记 URL，无搜索、爬取、浏览器动作或实现源码路径。CLI 不存在不是权限拒绝；调用的是已启用的同服务 MCP，并未安装新工具。MCP 明确报额度不足后立即停止，不重试或绕过。

统计：提交的官方 URL 尝试 1，runtime 1、model 0；成功页面 0；重试 0；可观察的官方最终 URL 0。服务是否向上游发出请求 Unknown。没有官方新增证据，不新增 `SRC-*` 或把错误文本登记成 Vosk 原始证据；工具返回只作为执行失败记录。

## 验收对照

| 验收项 | 结果 | 证据／限制 |
| --- | --- | --- |
| 唯一候选、总计及分对象预算 | PASS | Vosk；1/6，runtime 1/3，model 0/3；没有第二候选或重试 |
| 来源、尝试与最终 URL 可追溯 | PASS（失败记录） | R01 为 R1 已登记官方入口；最终 URL、上游状态与是否到达均明确 Unknown，不伪造成功 |
| runtime／模型字段与许可分开 | PASS（结构）；身份未就绪 | 两份身份表逐项标 Observed（R1）或 Unknown；未把仓库 Apache-2.0 继承到未指认制品 |
| 可唯一指认精确对象 | NOT MET | release／Android 坐标／模型名称与修订／官方对象入口未固定 |
| 无制品、无安装、无执行与产品改动 | PASS（本轮动作） | 仅本地合同／正式文件读取、一次官方页面服务请求和知识库写回；没有下载、扫描、构建、加载、推理、集成或设备测试 |
| 结论未越权 | PASS | 只得 identity_insufficient；阶段 B/C、CP2、CP3 与父亲 Alpha 未获批准 |

## 保持不变

- 三步录入／找回、按住说话、单段 90 秒、个性词表与专名 90% 门槛保持。
- 原始音频不落盘、不上传、不进入日志；只有转写文字可发送云端 AI；动态隐私未验证。
- CP1 父亲人工验证、Conformer 与词表实现仍 Deferred, not removed；CP1 人工须在任何 CP3 准入前恢复。
- 小米 15 的 ABI／CPU-only／JNI／PCM、30 秒 P95、90 秒与连续 20 次稳定性、飞行模式、RAM／耗电／温升、缓冲释放等均未验证。
- sherpa 终止链不恢复，不建立第二候选，不自动开始阶段 B/C，不通知开发者开工，不重试跨任务发送。

## 写回与检查

本轮只新增[运行库身份](cp2-vosk-runtime-identity-2026-09-06.md)、[模型身份](cp2-vosk-model-identity-2026-09-06.md)及本记录，并更新 INDEX、追加 LOG；原 R1、正式选择决定、PRD 和 Think 不修改，无 Git 提交。

三文档的六项元数据、身份字段、Observed/Unknown 区分、预算与停止边界进行本地检查；INDEX/LOG 与接管前副本做差异复核，LOG 保持原字节前缀。标准 `lint_knowledge.py` 缺失，不声称完整知识库自动 Lint 通过。

本轮评分分项：决策对齐 15/15、来源质量与覆盖 4/20、引用支持关系 3/20、事实／推断分离 15/15、反证与冲突处理 5/10、决策价值 5/10、可维护性 8/10，共 55/100。低分反映身份核定没有成功证据，不代表失败记录不可信；R1 的 92/100 与 V2 不受影响。

## 同任务续接授权记录

2026-09-06：Leader 的 current-task 已记录用户渠道选择“不一定要使用 Firecrawl 进行搜寻”，resume_authority 时间为 `2026-09-06T21:17:23+08:00`。现在恢复同一 `CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001`，允许现有浏览器或其他已可用只读工具直接读取同一获准官方来源；不安装工具、不付费、不绕过权限拒绝，不扩大来源或候选。

先前 R01 服务额度失败、首次 `identity_insufficient` 和 55/100 评分均保留为历史，不冒充首次成功。续接开始已用总计 1/6、runtime 1/3、model 0/3；剩余总计 5、runtime 2、model 3，每次尝试继续累计。上述“不换渠道／不自行恢复”描述第一次停止动作，现由明确渠道续接授权更新；阶段 B/C 仍未获授权。续接结果将在下方追加，首次记录不删除。

## 续接最终记录

### 累计访问 Ledger

访问日期均为 2026-09-06，任务时区 Asia/Taipei。成功请求的下列时间是服务器响应 `Date`，不是假定客户端开始时间；本次收尾本地记录时间为 `2026-09-06T21:21:04+08:00`。

| 顺序／ID | 对象／目的 | 尝试 URL | 最终 URL／HTTP／可见证据 | 累计预算（总／runtime／model） |
| --- | --- | --- | --- | --- |
| 1 R01（原失败） | runtime；官方仓库说明 | https://github.com/alphacep/vosk-api | 最终 URL／HTTP Unknown；Firecrawl Insufficient credits，无页面 | 1/6；1/3；0/3 |
| 2 M01 | model；官方目录 | https://alphacephei.com/vosk/models | 无官方最终 URL／HTTP；curl exit 7，连接沙箱内 `127.0.0.1:7897` 代理失败，无页面；失败也计数 | 2/6；1/3；1/3 |
| 3 M02 | model；同目录授权网络重试 | https://alphacephei.com/vosk/models | 同 URL，HTTP 200；Date=`Sun, 06 Sep 2026 13:19:30 GMT`；text/html，Content-Length=43888；Chinese 小模型名称／href／42M／Apache 2.0 | 3/6；1/3；2/3 |
| 4 R02 | runtime；官方 Android 发行说明 | https://alphacephei.com/vosk/install | 同 URL，HTTP 200；Date=`Sun, 06 Sep 2026 13:20:00 GMT`；text/html，Content-Length=15095；Android build 的 Maven Central／动态版本坐标 | 4/6；2/3；2/3 |
| 5 R03 | runtime；官方项目 release 元数据 | https://api.github.com/repos/alphacep/vosk-api/releases/latest | 同 URL，HTTP 200；Date=`Sun, 06 Sep 2026 13:20:36 GMT`；application/json，Content-Length=2224；v0.3.50／id152196573／author nshmyrev／assets=[] | 5/6；3/3；2/3 |

全部尝试为 5 次、4 个不同 URL，成功读取 3 个官方页面／元数据端点。模型同 URL 的失败及授权重试各占一次，不重置 R01，不把失败排除预算。剩余总 1、runtime 0、model 1；不挪用分对象预算。

### 渠道、来源与证据保全

- 使用系统已有 curl 只读请求，不安装工具、不购买额度。M01 为网络连接失败而非审批拒绝；随后按沙箱规则请求并获准网络访问，M02 才成功。R02/R03 亦通过明确网络权限审批；没有绕过拒绝。
- curl 设置 30 秒上限，响应大小上限依次 500000／200000／300000 bytes；没有自动重试、没有 `-L` 自动跟随重定向。三个成功响应均直接 200，最终 URL 等于请求 URL；代理 CONNECT 的 200 与目标 HTTP 200 区分记录。
- 模型目录来自原合同；其导航直接给出相对 `install` 链接，经同域解析为 R02。R03 属于原合同明确允许的 `alphacep/vosk-api` 官方 release 元数据，官方站同时直接链接该仓库；无新候选或来源猜测。
- 只取 HTML／JSON，未执行页面脚本或请求 CSS／图片／iframe／下载链接；目录中其他模型、安装页中的命令、源码链接及 R03 的归档 URL 都没有执行或访问。端点响应的 Content-Length 是说明／元数据字节数，不是模型／AAR 大小；ETag 不作为制品 SHA。
- 成功内容保留为工具会话响应；身份文档保存必要字段、官方 URL、日期、引用位置和最小摘录，不将完整网页写入 raw。本合同限定三文档及 INDEX/LOG，故本轮不另建 raw/SRC 文件；不覆盖既有来源。

### 新证据与身份缺口

| 证据 | 直接观察 | 限制／不能推导 |
| --- | --- | --- |
| E-M02：官方目录 Chinese 行 | `vosk-model-small-cn-0.22`；对应同域 `.zip` href；`42M`；`Apache 2.0`；Android/RPi 说明 | 只确认目录身份，不固定模型 bytes、签名、完整许可或实测能力；未请求 ZIP |
| E-R02：Android build | `com.alphacephei:vosk-android:0.3.32+`，使用 Maven Central | `+` 是动态范围，不是可复现固定版本；Java 段的 `vosk` 不等于 Android 包 |
| E-R03：release JSON | `tag_name=v0.3.50`、id=152196573、author=nshmyrev、published_at=2024-04-22T13:02:41Z、assets=[]、immutable=false | 项目 tag 不证明 Android 0.3.50 包存在；master 不固定 commit；无附件不代表其他发行渠道无包 |

checksum 缺失本身不是本合同的必然失败原因。本次失败项是 Android 精确版本与发行对象绑定尚无证据；不能依赖“0.3.32+ + v0.3.50”自行拼接坐标。runtime 精确包的完整许可证、notice、依赖闭包，以及两对象的 SHA／签名／SBOM 仍 Unknown，不能声称官方全站没有发布。模型发布时点、训练作者／权利链、实际内容和 Android 兼容未核定。

### 当前验收与停止

| 条件 | 结果 | 证据 |
| --- | --- | --- |
| 6 总／3+3 分对象及原失败保留 | PASS | 上表 5/6、3/3、2/3，含全部失败及授权重试 |
| 获准官方来源和身份字段可追溯 | PASS（字段记录） | 三成功响应及两身份表；Observed／Unknown 分开，许可不跨对象继承 |
| 两个精确制品均可唯一指认 | NOT MET | 模型目录身份已指认；Android 固定版本／对象未闭合，runtime 预算耗尽 |
| 无制品取得／执行／产品修改 | PASS（本轮动作） | 只读官方说明和 JSON；无安装／源码实现／归档／模型／AAR 获取或构建、加载、测试 |
| 状态不外推、符合停止边界 | PASS | 当前 identity_insufficient；无阶段 B/C 授权，不启动新任务或通知开发者 |

本次只更新既有三身份文件、INDEX 与追加 LOG；历史失败、首次结果和新授权续接过程保留，其他未提交修改不动，无 commit。Think 开始和结束均为 clean，HEAD `92e5027852b8c2cb8476f7c2da684ef98f61ec82`。保留前述三步、音频隐私、专名90%、CP1／Conformer／词表 deferred、CP2未过、CP3及父亲Alpha未批准；所有接口、安全与真机能力未验证。

续接评分：决策对齐15、来源质量与覆盖14、引用支持关系18、事实／推断分离15、反证与冲突处理8、决策价值5、可维护性7，共82/100；Android精确身份缺口使研究质量未过85门槛，Validation Level仍V2。首轮55分及已验收R1的92分不覆盖。等待Leader验收，不使用模型剩余预算补运行库，不自行为阶段B/C构造生效授权。
