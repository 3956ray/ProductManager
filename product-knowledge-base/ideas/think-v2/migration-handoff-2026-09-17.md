# thinkV2 PM换机恢复指南

Owner: Product Lead
Last updated: 2026-09-17
Source: 用户经Leader在本PM任务转交的迁移授权及状态；三份正式文档；ProductManager远端检查
Confidence: High（选定文档完整性）；Medium（Leader报告进度）；Unknown（新机环境、未提供工程原证据）
Related decisions: [基线](product-baseline-decision-2026-09-16.md)；[工程顺序](emulator-first-full-engineering-addendum-2026-09-16.md)；[模型准入](sensevoice-int8-product-admission-decision-2026-09-16.md)
Next review date: 2026-09-24
Research Quality: 85/100（沿用需求证据；不新增产品研究或安全评分）
Validation Level: V0（家庭需求行为验证未升级，迁移不是产品验证）

## 迁移边界与当前状态

迁移发布状态：LOCAL_ONLY / PUBLIC_PUSH_PAUSED。Leader转交其公开推送被自动审批拒绝，原因是内部历史证据、绝对路径和任务元数据公开风险；PM没有发生推送或另路重试。用户统一确认公开/私有后才处理远端写入。本地包保留原文及历史路径/thread身份以支持审查，不能将常见密钥模式未命中视为公开安全认证。

本次目标仅PM交接。基于远端main `6f294a57c0bd620ee2c7644a59d84fc7b08e3adf`独立克隆并建立`codex/thinkv2-pm-migration-20260917`分支，保留远端已有内容；不复制本地所有未提交项目，不force push，不替Leader/Developer推送。

Leader在2026-09-17转交：notesUI `8a98e09`已接受，提醒UI `88d3861`审查中未接受；Voice002 partial，embedding PAUSE，AI provider=false；小米15/家庭/自然提醒/TalkBack缺口保留。本次不读取实时Leader仓库或重新测试，恢复时须获取Leader最新验收原文，不能仅凭此快照接受88d3861。

三份正式文件保持既有SHA，见[清单](migration-sha256.txt)。原基线“当前文字单”及补充“当前提醒单”等描述是各自成文时状态，不能用于恢复旧在途任务。SenseVoice仅合成隔离评估APPROVED，私人嵌入PAUSE；不因模型可下载或迁移成功解除。声音准确率、性能、音频不落盘/上传、人工优先、恢复事务及真实证据要求保持。

## 新机恢复步骤

1. 克隆ProductManager，检出迁移分支或包含该提交的后续已合并分支。不要用本机旧目录整体覆盖远端。仓库公开可匿名读取；推送用新机自己的GitHub认证，不搬旧机token/钥匙串。
2. 在仓库根运行 `shasum -a 256 -c product-knowledge-base/ideas/think-v2/migration-sha256.txt`。清单路径相对仓库根；失败先查文件差异，不能重算摘要来冒充一致。
3. 阅读根README、AGENTS、本指南与三份正式文档；用来源映射解析旧绝对路径。迁移许可快照是旧审阅证据，不保证远端main未变，也不代表权利链或加载已通过。
4. 分别克隆用户指定Leader、Developer仓库，由各自恢复指南确认源码位置、分支、HEAD和证据。PM仓库不含App源码/构建/模型；不要假定Developer仓库根就是thinkV2源码根。
5. 新建PM、Leader、dev任务，并由用户/新Leader明确映射角色到新thread ID和新机checkout。旧PM `01a0768c-7ba7-7f11-bd4f-f5c2fd1fa779`、旧Leader `01a0a5ce-3e8b-75e1-92be-9eb89ef9ed37`、旧dev `01a0a5d3-8ec3-7071-82f6-a49f80ba7d1d`仅历史。不要自动发送历史回调、复活旧自动化或重复下发旧attempt。
6. 新Leader对照最后已接受commit、审查中提交和剩余证据，确认旧机任务已停止/无并发写入后，在新机重新绑定唯一在途任务。保留原task/attempt作为历史；新合同记录新环境及新的执行身份，不伪造旧ACK/验收。
7. 技能从仓库`.agents/skills`读取；模型路由名只是偏好，若新环境没有同名模型，应明确记录替代，不复制旧全局代理/供应商凭据。验证文档和授权后再依已授权顺序继续，不自动开始ASR、联网AI或真机操作。

## 必要技能与环境

仓库既有`product-research`、`knowledge-loop`及其references/agents配置保留；本次补入MIT标记的`karpathy-guidelines/SKILL.md`供代码工作优先读取。PM AGENTS保留原产品团队规则并补入最新最小改动要求及迁移入口；agent-roster与operating-rules来自既有远端，无需迁移任何全局账户。

`knowledge-loop/references/lint.md`提到的`scripts/lint_knowledge.py`在此次快照缺失，只有测试文件不能当作可用lint工具。不执行不完整脚本或宣称全库lint通过；必要时手动核对本次元数据/链接/差异。Git与SHA256工具是文档恢复所需；本任务机器没有gh，通过Git与GitHub只读API检查远端，gh不是恢复硬依赖。

旧文档中的`/Users/orderly_ray/...`、`/private/tmp/...`和Codex ID是溯源字符串，不是新机要创建的路径。新机用自身checkout路径，不创建指向旧home的软链接。私有实验源保持不迁移；许可文本在仓库有副本，按来源表重定位。

## 未迁移与恢复条件

未迁移父亲真实笔记/音频、私人日历/实验源全文、GitHub或AI凭据、全局Codex配置/聊天数据库/自动化、历史附件、临时审查工具、runtime/模型/tokens、APK、Android SDK/模拟器镜像、设备授权、App数据库。五份公开许可/模型卡文本只用于证据，不安装、不执行其中示例，也不授权网络子资源。

如需恢复私有来源，用户仅在新机本地自行提供并明确授权读取；不为消除链接缺失而上传GitHub。模型与必要依赖按后续精确范围核验，旧本地缓存不等于准入。AI真实服务须新机自行配置并明确发送范围；目前provider=false。最终小米15/家庭/自然提醒/TalkBack仍需真实证据。

本迁移不承诺上述运行条件已恢复，不把产品需求删除，也不要求重新批准已授权的产品方向。

## 本地核验限制

三份正式文档和五份许可来源副本的8项SHA核对通过；新写迁移文档作局部链接/元数据/差异检查。原模型卡有11处尾随空白，为保留来源原字节及SHA不清理；新写文件的空白检查单独通过。公开模型卡/README中的相对源码/图片链接仅作为来源原文，不抓取补齐，也不执行示例。未作仓库全历史隐私审计。
