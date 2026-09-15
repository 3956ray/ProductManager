# 产品知识库

Owner: Product Lead  
Last updated: 2026-08-23
Source: 本工作区运行设计；产品调研工作流标准化决策；一人公司 PM 知识循环决策
Confidence: High  
Related decisions: `decisions/product-research-workflow-2026-08-18.md`；`decisions/one-person-pm-knowledge-loop-2026-08-23.md`
Next review date: 2026-09-30

这个目录是产品团队的「工作操作系统」。

它有三个用途：

- 作为当前状态板，让团队知道现在在做什么、卡在哪里、谁需要决策。
- 作为长期知识库，沉淀用户、市场、产品决策、PRD、指标和实验结果。
- 作为 agent loop 的入口和出口：收集信号、综合判断、需要时请求审批、确认后写回。

## 核心文件

- `BOARD.md`：当前产品作战板。
- `INDEX.md`：项目、知识、来源和决策的稳定导航入口。
- `LOG.md`：Ingest、Query、Lint 与人工决策的追加式操作记录。
- `raw/`：不可覆盖的来源元数据和合规短摘录。
- `outputs/`：一次性交付物；不能作为后续研究的原始来源。
- `agents/agent-roster.yaml`：agent 分工、推荐模型、reasoning effort 和升级规则。
- `agents/operating-rules.md`：产品知识 loop 如何运行，哪些地方需要人类审批。
- `agents/model-routing.md`：基于 OpenAI 官方资料整理的模型选择逻辑。
- `.agents/skills/product-research/`：产品、市场、竞品和公开用户声音调研的证据流程与质量门。
- `.agents/skills/knowledge-loop/`：把已核验来源编译成长期知识，并执行可追溯 Query 与 Lint。
- `templates/`：PRD、决策记录、周度复盘和 Codex 配置模板。
- `references/`：可在多个 idea 讨论中复用的外部思考框架、来源笔记与适用边界。

## 推荐节奏

- 每日：处理新反馈、阻塞、指标异常和紧急决策。
- 每周：刷新公告板，总结信号，更新项目状态，提出下一步建议。
- 按需：在产品或市场判断前运行 `product-research`，形成 Evidence Cards、反证和待验证假设。
- 每次新来源：运行 `knowledge-loop ingest`；写回后更新 `INDEX.md`、追加 `LOG.md` 并检查 diff。
- 每个 Sprint：把已确认机会转成 PRD、验收标准和交付任务。
- 每月：检查过期知识、未解决决策、roadmap 匹配度和产品假设；对需持续关注的竞品或市场只记录相对基线的变化。

当前一人公司 WIP 上限为 1 个 Build 与 1 个 Discovery。内部知识系统维护不占产品名额；重新激活 Parking Lot 项目前必须先释放名额。
