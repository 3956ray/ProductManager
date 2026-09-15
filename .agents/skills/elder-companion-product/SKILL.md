---
name: elder-companion-product
description: 继续 Products Manager 工作区“中国老年陪伴”项目的调研、服务设计、验证实验和 PRD 草拟。适用于子女为父母购买真人陪伴、医院内兴趣陪伴、社区或居家陪伴，以及与助医陪诊的比较；复用 product-research 与 knowledge-loop，不用于其他 PM 项目或泛养老医疗咨询。
---

# 老年陪伴调研与产品设计

帮助 Product Lead 判断谁在什么场景需要真人陪伴、谁愿意付款、怎样履约，再设计与证据等级相称的服务和产品。默认中文工作。

## 接入现有 PM 工作流

这是项目领域 skill，不是新的主控 agent 或运行时配置。保留 `product_manager_agent` 的最终综合所有权；不修改 `.codex/config.toml`、`AGENTS.md`、既有 skill、agent roster 或全局模型设置。下列模型分工仅适用于本 skill 中确有需要的子任务，不会切换当前会话模型。

先读取工作区要求的 BOARD、INDEX、agent-roster 与 operating-rules；在同一任务已读且未变化时复用。路径均相对 Products Manager 工作区根目录；skill 内的 Markdown 链接相对本 skill 目录。

- 首次继续本项目：读 [references/project-context.md](references/project-context.md)，再读最新项目研究与来源索引。该参考是导航和历史提醒，当前用户指令与最新决策优先。
- 做新调研：使用 [product-research](../product-research/SKILL.md)，继承其来源、独立核查与质量门；本 skill 只补领域判断。
- 做服务设计、实验或 PRD：读 [references/research-design.md](references/research-design.md) 对应部分，复用 `product-knowledge-base/templates/prd.md`，不重新发明通用 PRD 模板。
- 追溯或长期写回：使用 [knowledge-loop](../knowledge-loop/SKILL.md) 的 Query／Ingest／Lint。若其确定性 Lint 工具缺失，记录未执行和原因，做可执行的检查，不宣称全部通过，也不顺手修改公共 skill。

## 每轮只推进一个明确决策

用一句话说明本轮支持的决策和所需产物。例如“比较医院内非医疗陪伴与社区兴趣陪伴，形成一个场景的服务蓝图”。用户只说“继续”时，先从最新材料找出最影响下一步的证据缺口，给出有限范围并继续；不默认重跑全部人口和竞品研究。

保留“纯陪伴”这一原始方向。医院是地点，陪诊是服务类型；在医院聊天、画画不自动等于挂号、取药或医疗护理。选择方向时比较非医疗陪伴、助医陪诊及组合服务，证据不足时允许“不做／保持现状”。用户已选定纯陪伴做原型时，围绕该场景设计并说明证据限制；不能仅因邻近陪诊证据较多，就强行把陪伴降为附加功能。

始终分别记录老人、付款子女、服务者、机构四方的目标和约束。子女付款不等于老人同意，也不等于有权无限查看病历、照片和谈话内容。年龄段、城市、套餐、频次和“陪伴比保姆便宜”均是待验证条件，不写成固定事实。

## 证据到设计的交接

1. 复用相关 CSV 行、`SRC-*` 与原始链接；旧报告中的 `verified`、89 分、V1／V2 是历史记录，不能代替本轮核查或评分。只刷新影响本轮决策的易变事实。
2. 用父 skill 的 Evidence Cards 建立关键 claim 的支持与反证。人口口径、服务范围、公开报价与成交、政府补贴与自费、媒体转述与原帖分别处理。
3. 为每个候选场景明确：触发事件、实际替代方案、付款动机、老人接受条件、供给条件、尚缺证据。需要产品建议时，按既有量表给出本轮 Research Quality 0–100、Validation Level V0–V5、置信度及限制；若只有局部离线材料，评分标为暂评并解释缺口，不沿用旧分数。仅能读取 raw 摘要而非原始正文时，明确标为“材料级暂评”，列出评分依据，不表述为独立核验后的研究评分。
4. 每条关键设计需求连接到 claim／source 或标记为假设，并给出可观察的验收结果。不把高级模型同意、界面精美、第三方订单或公开报价当作自有产品付款与留存验证。
5. 用户只要分析时在会话交付；要求文件时在本项目目录新增带日期的草稿。正式写回按 knowledge-loop 串行执行。用差异复核确认没有覆盖历史决策或其他任务修改。

BOARD 的 WIP 与既有审批继续有效。可做获准的本地研究和可逆设计；不要因为旧报告写有“三城试点”就自动激活项目、招募、联系服务者、收定金、发布价格或上线。真正需要扩大投入时，先完成研究、设计与实验草案，说明具体待批准动作；已有明确授权不重复询问。

## 有限的模型分工

小任务由当前会话直接完成。只有独立子任务能与主控的有效工作并行时才委派；通常同时 1–2 个，最大不超过工作区与当前工具限制中更小者。不为了凑齐模型而启动四个 agent。

| 工作 | 优先模型／推理强度 | 沿用角色与交付 |
| --- | --- | --- |
| 已取得材料的批量提取、评论分类 | `gpt-5.6-luna`／`medium` | `user_feedback_agent`：带原文定位的标签、反例、模糊项；不做最终推荐 |
| 常规来源核查、竞品比较、PRD 子模块 | `gpt-5.6-terra`／`medium` | `research_agent`／`prd_agent`：证据、选项、缺口或有边界的草稿 |
| 冲突证据、模糊服务定位、复杂服务蓝图 | `gpt-5.6-sol`／`high` | `research_agent`／`evidence_verifier_agent`：取舍依据、反证、需人判断的内容 |
| 经 Sol 仍未解决且会改变重大投入的跨领域判断 | `gpt-6-astra`／`high` | `review_eval_agent`：一次聚焦复核，指出阻断项、依据和最低修复；不自动扩展成全项目研究 |

模型分工是本项目的成本假设，尚无四模型任务对照评测。只使用当前工具声明可用的准确 model id 与推理档位；不可用时采用已有合适模型并说明，不编辑共享配置、不猜测别名。只有当前环境允许时才覆盖子任务模型；不为此强制 Max／Ultra。

委派时提供：一个问题、相关材料路径或原始证据、完成标准、停止条件、只读边界和期望输出。核查者应能检查关键原始材料，不能只接收上一模型的摘要。每个子任务返回中文结论、证据定位、反证、缺口；主控负责最终综合，共享文件只由一个写入者更新。

信息不足优先补来源、收窄问题或设计验证，不把逐级升级模型当作补证据。模型消耗、耗时或修订次数不可得时写未知；有实际任务记录后再调整路由建议。

## 维护元数据

- Owner: Product Lead
- Last updated: 2026-09-05
- Source: 用户在本任务的专用 skill 请求；任务「老年陪伴」`01a06cec-8b3e-7853-94ad-1c346bd16a7c`；本工作区 agent 配置与运行规则；[OpenAI 模型说明](https://learn.chatgpt.com/docs/models)
- Confidence: Medium（已核对工作区；模型路由收益需实际任务验证）
- Related decisions: `product-knowledge-base/decisions/product-research-workflow-2026-08-18.md`；`product-knowledge-base/decisions/one-person-pm-knowledge-loop-2026-08-23.md`
- Next review date: 2026-10-05
