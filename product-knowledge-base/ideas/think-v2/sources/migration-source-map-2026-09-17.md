# thinkV2正式来源映射

Owner: Product Lead
Last updated: 2026-09-17
Source: 三份正式PM文件既有Source与SHA；用户经Leader转交迁移/状态要求；已读本地公开许可快照
Confidence: High（原文副本）；Medium（指挥官状态）；私人行为结果Unknown
Related decisions: [迁移指南](../migration-handoff-2026-09-17.md)
Next review date: 2026-09-24

## 需求来源

私人《父亲笔记App交付验证》为原基线指定实验来源，源SHA256 `0539a1b2c9c28629e4d6eb18eb4f859a1173c4d36ee92b988f7db2bc04298a7d`。原文不上传，旧绝对路径仅在原基线中保留溯源。可迁移的必要摘要：目标为记录→重复提醒→找回→备份恢复，分类可纠正，观察父亲需要帮助的步骤；实验proposed，实际试用结果Unknown。该摘要是派生需求记录，不充当原始访谈或成功证据，不复制私人记录。

用户经当前Leader明确从零thinkV2、不继承旧代码/验收；后续明确先模拟器验证、全部开发后自己用小米15。这些会话指令已在原基线和模拟器补充中记录；全球聊天库与原始会话未迁移。新机如需争议复核，由用户/新Leader提供必要授权消息，不从模型摘要推导新的权限。

## 正式文件映射

| 旧工作区来源 | 新仓库位置 | 处理 |
| --- | --- | --- |
| product-knowledge-base/ideas/think-v2/product-baseline-decision-2026-09-16.md | 同相对路径 | 原字节保留，完整SHA见migration-sha256.txt |
| product-knowledge-base/ideas/think-v2/emulator-first-full-engineering-addendum-2026-09-16.md | 同相对路径 | 原字节保留，明确补充优先的范围 |
| product-knowledge-base/ideas/think-v2/sensevoice-int8-product-admission-decision-2026-09-16.md | 同相对路径 | 原字节保留，有限评估与embedding PAUSE分开 |
| /private/tmp/thinkv2-voice-002-review/model-LICENSE | sources/license-snapshots/model-LICENSE | 一行转引，不当成独立完整许可 |
| /private/tmp/thinkv2-voice-002-review/sensevoice-model-card.md | sources/license-snapshots/sensevoice-model-card.md | 原模型卡license other及模型许可链接 |
| /private/tmp/thinkv2-voice-002-review/FunASR-MODEL_LICENSE | sources/license-snapshots/FunASR-MODEL_LICENSE | 模型协议v1.1；保留中英文和原署名 |
| /private/tmp/thinkv2-voice-002-review/FunASR-README.md | sources/license-snapshots/FunASR-README.md | 工具代码与模型许可分离的说明 |
| /private/tmp/thinkv2-voice-002-review/SenseVoice-LICENSE | sources/license-snapshots/SenseVoice-LICENSE | MIT代码许可文本，不覆盖模型权重 |

表中sources路径相对think-v2目录。原模型卡链接为 https://huggingface.co/FunAudioLLM/SenseVoiceSmall/raw/main/README.md ，模型协议链接为 https://github.com/modelscope/FunASR/blob/main/MODEL_LICENSE 。本次不重新抓取，五份快照SHA与原准入决定一致；未证明main历史不可变或固定转换权重完整权利链。原仓库根MIT不能将这些第三方文本/模型重新许可为MIT，须保留各自来源和条款。

## 工程与权限证据

原准入决定绑定的Leader合同/attempt及制品身份保留在正式文件；合同本体/运行报告由Leader与Developer迁移，PM未复制或独立验收。模型SHA是当时待核对目标，不是本次实收模型SHA。2026-09-17最新进度来自迁移指令：88d3861审查中未接受、8a98e09已接受、Voice002 partial/embedding PAUSE、AI provider=false，最终设备与家庭证据未完成。对应原测试与验收缺失时保持待核，不因本表升级结论。

本表不是重新研究；不承诺官方许可认证、法律效力、加载安全或当前远端条款未变。
