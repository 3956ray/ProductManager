# ProductManager

产品团队知识库。thinkV2换机从[迁移恢复指南](product-knowledge-base/ideas/think-v2/migration-handoff-2026-09-17.md)开始；仓库已有其他项目与历史，不代表本次全部复核或迁移。

Owner: Product Lead
Last updated: 2026-09-17
Source: 用户经Leader转交的换机迁移要求；正式PM文档；指定ProductManager远端
Confidence: High（迁移内容与规则）；工程进度为Leader报告，非PM复测
Related decisions: [thinkV2迁移指南](product-knowledge-base/ideas/think-v2/migration-handoff-2026-09-17.md)
Next review date: 2026-09-24

## 正式入口

- [独立产品基线](product-knowledge-base/ideas/think-v2/product-baseline-decision-2026-09-16.md)
- [模拟器先行与完整工程顺序](product-knowledge-base/ideas/think-v2/emulator-first-full-engineering-addendum-2026-09-16.md)
- [SenseVoice有限评估与私人嵌入决定](product-knowledge-base/ideas/think-v2/sensevoice-int8-product-admission-decision-2026-09-16.md)
- [来源映射](product-knowledge-base/ideas/think-v2/sources/migration-source-map-2026-09-17.md)与[原文校验清单](product-knowledge-base/ideas/think-v2/migration-sha256.txt)
- [PM工作规则](AGENTS.md)、[知识地图](product-knowledge-base/INDEX.md)、[运行规则](product-knowledge-base/agents/operating-rules.md)

## 来源优先级

最新明确用户指令优先；当前正式范围决定覆盖它明确修订的旧条款；当前工程状态以Leader实际验收记录为准；开发者自报/测试输出不是Leader验收。模型摘要不充当原始来源。此迁移状态快照只更新交接进度，不改产品门槛；三份正式文档原字节保留，所以其旧时态和旧绝对路径需要结合来源映射解读。旧think代码、验收、制品或运行许可不继承到V2。

## 当前真实缺口

2026-09-17用户经Leader提供的状态：`88d3861`提醒UI交付仍在审查，尚未接受；先前notesUI `8a98e09`已接受。Voice002仍partial，SenseVoice最终私人嵌入仍PAUSE；AI `provider_verified=false`。小米15、家庭试用、自然重复提醒和TalkBack证据仍待补。以上短commit属于工程引用，不是本PM仓库commit，本次未独立复测。

先模拟器工程验证，完整开发后用户小米15及家庭验证的顺序保持；不能把迁移成功当产品验收。不得因换机重开研究、降低门槛或自动派dev。

## 仓库与隐私

当前迁移包仅本地可审查，尚未推送。2026-09-17 Leader转交：其公开推送因内部账本/历史证据/绝对路径/thread元数据风险被自动审批拒绝；本PM随即暂停同类公开写入，等待用户统一决定公开或私有。此包保留正式原文，含历史路径与任务身份，不应未经该决定直接公开。

- PM：[ProductManager](https://github.com/3956ray/ProductManager)
- 指挥/验收：[Leader](https://github.com/3956ray/Leader)
- 开发交接：[Developer](https://github.com/3956ray/Developer)

ProductManager在迁移前经GitHub元数据确认是public。本次仅新增选定正式文档、公开许可文本快照、必要技能和脱敏交接；不上传父亲真实记录、私人日历、私人实验全文、账号/密钥、全局聊天数据库、模型或APK。仓库既有历史本次不重写、不代表完成全历史敏感数据审计。

新电脑需新建并绑定PM/Leader/dev任务，旧thread ID只保留历史，不可作为新任务地址直接调用。操作步骤、认证条件和未迁移项见迁移指南。
