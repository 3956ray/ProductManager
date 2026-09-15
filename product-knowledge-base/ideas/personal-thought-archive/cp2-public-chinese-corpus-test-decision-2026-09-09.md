# 决定：公开中文语料测试边界与有限CER工具

Owner: Product Lead
Last updated: 2026-09-09
Source: 用户2026-09-09公开中文数据测试要求；Leader CP2-CHINESE-CORPUS-001-intake；本轮Q01-Q05文本响应；现行PRD；Leader元数据恢复批次验收
Confidence: High（官方目录字段、请求及边界）；Low（小子集可取得性）；Unknown（真实识别效果）
Related decisions: [PRD](prd-v0.1-2026-09-04.md)；[元数据恢复报告](cp2-vosk-dependency-license-metadata-resumed-2026-09-08.md)；[离线PCM决定](cp2-offline-next-step-decision-2026-09-08.md)
Next review date: 2026-09-16
Research Quality: 78/100 · revise（来源入口可信，小子集／划分／固定包许可未补齐；不对真实测试给GO）
Validation Level: V2（不变）
Next evidence: 一次交付可运行的离线CER评分CLI、合成黄金测试与数据缺口清单；真实测试仍需可核语料和ASR准入
Allowed next investment: Leader验收后唯一CP2-CER-SCORER-001，最多4小时、5工程＋4同步文件；现有Python标准库，无音频／网络／新依赖／真实native
Pause/Kill condition: 小子集入口或许可不明则不取得；不得以公开语料授权扩大JNA或真实ASR执行；工具完成后仍缺真实前置则明确暂停，不续发准备链

## RESULT和身份

**APPROVED：落实公共工程fixture与私密录音的边界，并批准下一单有限文本CER评分工具。公开音频取得暂不下发；真实ASR测试继续blocked。**

这是工具开发范围决定，不是研究质量通过、公开数据已下载或CP2通过。优先候选为AISHELL-1官方test划分；THCHS-30为本次已核备选，不并行取得。两者都没有在本次所读可信页面建立独立小子集入口，不编造样本ID、文件URL、大小或哈希。

```json
{"task_id":"CP2-CHINESE-CORPUS-001","attempt_id":"af861510-8a44-4376-8c7a-000a1e8bb0af","contract_sha256":"6b1b9a5eb3599a366bd1191ade64dbbddf5fc5cc05d2b8bebd9fec35530ba5ae","assigned_thread_id":"01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779","acknowledged":true,"result":"COMPLETE","decision":"APPROVED","corpus_acquisition":"PAUSE","real_asr_test":"blocked","product_changed":false}
```

合同contract_body递归排序后重算SHA匹配；已在本任务输出四身份ACK。读取[Leader intake](/Users/orderly_ray/Leader/orchestration/reports/CP2-CHINESE-CORPUS-001-intake.md)、[最新元数据验收](/Users/orderly_ray/Leader/orchestration/reports/CP2-VOSK-METADATA-RESUME-001-verification.md)及现行PRD。用户原话“可以 你可以先去搜索公开的 中文数据家来进行测试 然后继续工作”支持此处公共测试方向，不授权JNA AAR、真实native或私密录音保存。旧拒绝和历史静态结果保留，本次未回调或派dev。

## 公开语料与私密录音的边界

| 数据 | 允许保存范围 | 禁止／验收 |
| --- | --- | --- |
| 公开且许可用途明确的语音、原始标注、许可／归属文本 | 未来取得合同选定后，保存在工程专用fixture根目录；标记public-licensed、来源、版本、split、ID、原始SHA、许可依据和取得时间。与产品数据库、麦克风采集、用户备份隔离；不随产品APK发布 | 不能用“网上能访问”替代许可；未取得数据不写已验证。未来任何再分发先核许可副本／修改和归属义务；不向第三方ASR／扫描服务上传。公共fixture本身不能被当作私密音频泄漏 |
| 父亲／其他用户的麦克风、聊天或日历附带录音 | 只在内存用于获准本地转写；完成、取消、异常后释放 | 绝不写磁盘、临时文件、缓存、日志、崩溃报告、网络或备份；不能因改名为test／匿名化／用户同意测试而自动套用公共fixture例外 |
| 项目自建合成文本与评分黄金用例 | 第一方工具目录中保存，明确project-synthetic | 不是公开语料转写，更不是真实ASR输出；评分测试通过不得写成识别成功 |
| 未来真实引擎对公共fixture的输出 | 仅在另行准入的工程实验中，保存与固定输入／模型／运行版本绑定的报告 | 只支持该固定集合回归；不得进入用户档案，不拿报告替代CP2私密音频不落盘／小米15证据 |

公共数据工程目录应排除云同步和用户备份；只读输入与输出分目录。隐私检测未来须区分“预先登记的公共源音频”和“本轮引擎新写出的音频”：对获准入口仍要求音频内容经内存PCM传入，不允许以公共文件测试掩盖引擎额外落盘。私密数据路径完全不得进入公共评测工具。保留实际输入文件sha和实验前后文件变化证据；不能靠文件名白名单放过私密录音。

## 有界来源核查与取得缺口

复用Leader已经核查的两个候选，不做市场／模型大范围搜索。为保存可核文本并检查直接后继入口，本次实际5次GET（含失败和显式跳转），无自动重试／分页／子资源；每次30秒、正文2MiB、总8MiB、全单20分钟。实际正文**9,726 bytes**；2次200、1次502、1次301、1次429；显式跟随跳转1次，剩余1次不使用。HTTP失败不是权限拒绝，也不是数据不存在；未换工具或绕过限流。

原始正文与headers位于`/private/tmp/think-chinese-corpus-af861510-8a44-4376-8c7a-000a1e8bb0af/`；[证据总账](/private/tmp/think-chinese-corpus-af861510-8a44-4376-8c7a-000a1e8bb0af/ledger.json)记录各文件bytes/SHA、实际URL、来源链和状态。下列bytes为收到的正文，不是语料包大小；Q01空正文SHA只固定空响应，不形成任何数据集负证据。未取得音频、tgz、资源包、代码或sidecar；没有HEAD／Range去探测归档。

| ID | 实际URL与来源 | HTTP／正文bytes | 正文SHA256 |
| --- | --- | --- | --- |
| Q01 | [THCHS README](http://data.cslt.org/thchs30/README.html)，intake明确官方链接，Q03亦直接指向 | 502／0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| Q02 | [OpenSLR SLR33](https://www.openslr.org/33/)，已有官方候选 | 200／4011 | 072e77c5f5a401eca59f7ba0c6608a4c6720f6c67227ab53c37f5745d7b019d9 |
| Q03 | [OpenSLR SLR18](https://www.openslr.org/18/)，已有官方候选 | 200／5261 | 4cb5506d18858d06221da017b4472dacd6db63b188d0fb06b2e919a5cf891935 |
| Q04 | [AISHELL公司说明](http://www.aishelltech.com/kysjcp)，Q02直接链接 | 301／262，Location为同主机同路径HTTPS | 4555de589ff9b307e20c708d6f112bc47bb377df29ff0a5914f8fb0932926887 |
| Q05 | [AISHELL HTTPS说明](https://www.aishelltech.com/kysjcp)，仅按Q04实际Location | 429／192，停止该分支 | 96acedd05fd81f12e8d92c4248592dcd1b2b96a3e49a504baed66f60935b2f89 |

| 候选 | 页面直接支持的事实 | 页面未提供／本轮未取得 | 本次处置 |
| --- | --- | --- | --- |
| AISHELL-1／SLR33 | 北京希尔贝壳发布；400位来自不同口音区域的录音人、安静室内、降采样16kHz；页面声明人工标注准确度>95%；License字段Apache License v.2.0 | data_aishell.tgz标15G，包含speech/transcripts；resource_aishell.tgz标1.2M，仅词典／说话人资料，不能冒充小音频测试集。没有独立test小包链接、test ID清单／说话人划分、逐文件时长／摘要；公司详情429 | 优先候选，仅冻结选样规则；不取得15G或资源包充数 |
| THCHS-30／SLR18 | 清华CSLT发布，License字段Apache License v.2.0；data_thchs30.tgz标6.4G；test-noise.tgz标1.9G、标准0dB噪声测试；resource.tgz标24M、词典和噪声样本 | 24M资源包不是clean test集。未见独立小clean-test入口；原始README 502，标注格式／划分详情Unknown；精确单文件大小与hash Unknown | 本次备选，不改查网盘／第三方重打包；不下载6.4G |

Q02/Q03同时有“free for academic use／totally free to academic users”介绍和Apache2许可字段。两者原文均保留：这句话没有明说academic-only，不能自行增加“仅限学术”限制；但页面标签也不能替代固定包内许可／第三方归属核查，更不能由PM给出法律保证。本轮只支持候选筛选和明确缺口，任何未来保存的fixture必须能绑定实际取得对象与适用许可，分发用途另核。

事实与推断分开：优先AISHELL-1是工程取舍（官方明确16kHz、人工标注）；不是其识别效果优于THCHS的证据。Vosk small-cn-0.22已有官方THCHS成绩声明（见旧元数据响应），不能从“评测过”推断“训练过”；两个数据集与Vosk训练／调参重叠仍Unknown。公开朗读语料不能代表父亲自发口述、环境噪声或私人专名。

## 固定选样与参考转写规范

以下是未来取得可核官方test成员后的冻结规则，不是本轮已选出的样本：

1. 只用一个固定版本的官方clean test划分；test归属必须由官方manifest／说明直接证明。不得把train/dev改名test，或从整包猜ID。参考转写和说话人信息必须能对应相同utterance_id；冻结前保存原始split清单与来源SHA。
2. 按speaker_id字节序排序；每位内部按utterance_id字节序排序，循环每位取一个，直到30条。只预先按有对应参考文本、单声道16kHz PCM16、时长1至30秒筛选；不能按识别成功／文本简单程度筛选。总时长不超过600秒、原始音频总大小不超过32MiB。无法凑够时返回实际数量和所有排除原因，标incomplete，不从其他划分补齐；不自动转码。
3. 在任何识别前冻结完整ID列表、speaker_id、split、原始来源URL／包成员、音频bytes/SHA256、reference原文及SHA256、采样参数、时长、许可出处、selection_version。当前这些精确ID和音频SHA全为Unknown，不生成伪manifest。
4. 原始reference逐字节保留；去除文件格式中的ID字段和记录行终止符只属于字段解析，不修改文本。保留原始字段文本和规范化后的文本；不得用ASR结果改写reference。若确需人工纠错，创建新版本并保留旧结果，不能回填原基线。
5. 主指标normalization-v1：Unicode NFC；仅ASCII A-Z转小写；移除Unicode空白与类别P*标点；保留数字、英文、符号、汉字。无繁简转换、数字读法折叠、同音替换、热词补写、分词或拼音化。另报raw-CER（原始字段Unicode码点序列，保留空格和标点）供复核；raw与normalized不可混写。

该规则是回归用小样本，不是统计代表性抽样。若官方split或原始编码无法核定，实际语料取得停止；不会为实现规则而追加多GB下载或猜镜像地址。

## CER口径与失败处理

字符错误率（Character Error Rate，CER）以Unicode码点序列的最小编辑距离定义，操作成本均为1。每条输出S替换、D删除、I插入和reference长度N；等价最优路径的分解按“匹配优先，然后替换、删除、插入”固定回溯顺序。汇总为**sum(S+D+I)/sum(N)**，不是逐条百分比平均；插入可使CER超过100%，不得截断。不把1-CER称作CP2专名准确率。

没有候选结果／超时／识别错误：该条仍计入计划分母，主口径按空hypothesis计D=N，并单独报失败类别、完成率；可附“仅成功条目CER”，但不能取代全计划CER。空reference（含规范化后空）、重复ID、未知额外ID、非法编码、未标记数据来源必须使输入验证失败，不能悄悄跳过。明确status=success且空hypothesis是有效全删除结果，不等于缺记录。

报告需包含expected/completed/failed数量、总参考字符、S/D/I、raw及normalized CER、失败分布、规范化版本、输入SHA、工具版本和每条结果。只读现有候选转写，**不生成hypothesis，不把reference复制为识别结果**。合成用例固定标记synthetic，不产生“模型得分”；未有获准真实运行记录时actual_asr_evaluation=not_run。

30／90秒延迟、P95、连续20次、内存／温升／耗电／CPU-only、飞行模式及音频不落盘是另一组真实运行验收；不得用CER工具执行时间替代。父亲30段至少27段无需重录、专名90%、CP1人工恢复及CP3准入不变。

## 唯一实际下一任务：CP2-CER-SCORER-001

Leader验收后下发给dev，**一次最多4小时**，实现可用的独立离线CLI和黄金测试，同时完成文档同步；不再派一个仅整理评分说明的任务。允许现有Python3标准库运行第一方工具及合成单测；无pip／Gradle／Maven／网络／目标模型或第三方代码加载。

最多5个工程文件，限定Think `tools/cp2-cer/`：

- `score.py`：本地manifest＋hypotheses JSONL输入校验、normalization-v1、确定性编辑距离及汇总JSON输出。
- `test_score.py`：黄金计数、字符加权、Unicode及错误输入测试。
- `synthetic-cases.json`：第一方手工构造的输入与独立预期计数；明确不是公开语料。
- `README.md`：精确CLI、schema、评分口径和真实评测未运行状态。
- `synthetic-validation.json`：实际运行工具／测试后生成的有界验证结果，不包含真实识别成绩。

另最多4个同步文件：本决定→Think同名doc，最新PRD→Think doc，必要Think AGENTS.md和doc/README.md入口。总最多9个文件。PM本单只改知识库，不改Think或派dev。

CLI合同：`python3 tools/cp2-cer/score.py --manifest <local.jsonl> --hypotheses <local.jsonl> --output <new.json>`。输入限定工程根内非符号链接的普通文件；manifest每行至少id、source_kind（project-synthetic/public-licensed）、reference；public还须dataset/version/split/speaker_id/audio_sha256/reference_sha256/license_source及来源字段，CLI只校验格式，不打开音频或访问URL，也不能自称来源字段已被外部认证。hypotheses每行id、status、text（成功时必填），错误行只保留错误码，不带堆栈或私密正文。工具不接受private／microphone来源；元数据标签只是防误用，不能证明输入实际公开。

上限：每输入1MiB，最多100条，单文本最多2000 Unicode码点；逐条DP、内存有界，超限／链接穿越／重复／额外ID即失败，输出路径已存在则拒绝覆盖。错误信息只含ID／错误码，不写输入正文到终端或日志。合成结果和显式工程评分文件可落盘，工具没有麦克风、音频读取、上传或ASR适配功能。

必要验收：S/D/I单操作与组合；不同长度样本的字符加权；CER>100%；raw/normalized差异；NFC组合字符／补充平面字符／ASCII大小写；保留数字和繁简差异；缺hypothesis计全删除和完成率；空reference／重复／额外ID／无source_kind／越界与输出覆盖拒绝；等成本路径固定分解；重复运行结果语义一致。运行测试还要以CLI实际生成synthetic-validation.json，不能只写测试不执行。

完成定义是“评分工具可用、合成黄金验算通过、文档同步”，不是“公开音频测试完成”。这一单之后**不自动续发工具／准备任务**：若可信小语料仍不可得或JNA／native未准入，直接报告实际阻塞供用户／Leader决定。用户目标中的真实识别评测目前尚未完成，这是明确缺口，不隐瞒为研究完成。

## 验证、局限与写回

本单只做5次文本GET、只读整理和4个知识文件写回，无音频／归档／新依赖／实现源码下载，无Vosk/JNA执行、模型训练、真实测试或外部回调。研究评分78（决策15、来源13、引用16、事实15、反证7、价值7、维护5）未过85门，下一工具仅依赖已明确的算术和合成数据，不依赖未核语料主张；不据此给真实ASR GO。

检查合同SHA、请求正文及headers bytes/SHA、6查询和8MiB预算、六元数据／本地链接、PRD隐私限定与CP2门槛、INDEX局部变更、LOG原始前缀及旧证据保留。标准全库lint脚本缺失时仅声明范围检查，不冒充全库自动通过。该决定／PRD／INDEX／LOG串行写回，不覆盖其他项目修改，不自动提交。

所需真实前置集中为两项：可信官方小test子集及固定标注／许可；真实ASR的JNA依赖、许可处置、命令输入边界与执行准入。取得公共语料也不会自动解决第二项。
