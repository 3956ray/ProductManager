# 产品团队 Agent 指南

这个工作区用于搭建一个可更新、可循环的产品团队知识库。

## 语言规则

默认使用中文工作。

- 面向人的说明、研究结论、公告板、PRD、决策记录、周报都用中文。
- 模型名、agent id、文件名、命令、配置字段保留英文。
- 引用英文来源时，用中文总结，保留原始链接。
- 如果必须保留英文术语，第一次出现时用「中文解释 + 英文原词」。

## 优先读取的上下文

做任何产品工作前，优先读取这些文件：

- `product-knowledge-base/BOARD.md`：当前项目、阻塞、待决策事项和新信号。
- `product-knowledge-base/INDEX.md`：项目、研究、来源与决策的知识地图。
- `product-knowledge-base/agents/agent-roster.yaml`：agent 分工、模型路由和升级规则。
- `product-knowledge-base/agents/operating-rules.md`：产品知识 loop 和审批边界。
- `.agents/skills/product-research/SKILL.md`：市场、竞品、公开用户声音、趋势和产品决策调研的证据流程。
- `.agents/skills/knowledge-loop/SKILL.md`：来源 Ingest、可追溯 Query、知识库 Lint 和长期写回规则。

## 工作原则

把知识库当作产品团队的当前工作记忆，而不是静态文档。只要决策、项目状态或已验证认知发生变化，就优先沉淀到对应的长期记录中。

涉及产品调研、市场扫描、竞品分析、公开用户声音、趋势、定位或定价假设时，使用仓库级 `product-research` skill。先定义研究支持的决策，再收集、核查和综合证据；不要把社区热度或 GitHub 热度当作需求验证。

新增来源、把研究写回长期知识、追溯现有结论或检查知识质量时，使用 `knowledge-loop`。`raw/` 只追加，模型输出不能作为原始来源，最终写回必须串行并通过 Git diff 复核。

所有产品判断同时记录 Research Quality 0–100 与 Validation Level V0–V5。Research Quality 合格不代表需求、付款或留存已经验证；投入上限由 Validation Level 决定。

## 审批边界

可以直接做的安全本地动作：

- 读取和总结当前工作区文件。
- 创建或更新范围内的知识库文档。
- 草拟 PRD、决策记录、周报、研究摘要、反馈摘要。
- 做非破坏性校验，例如检查链接、结构、元数据和文档一致性。

以下动作必须先获得人类明确批准：

- 向客户、合作伙伴、供应商或管理层发送外部消息。
- 在外部系统创建、调整优先级或关闭研发任务。
- 修改 roadmap 承诺、上线时间、定价、法律/合规表述、客户承诺。
- 删除或覆盖历史产品决策。
- 外部写入、破坏性变更、购买行为或明显扩大范围。

## Subagent 使用规则

适合用 subagent 的独立、偏读取任务：

- 按来源总结用户反馈。
- 检查知识库一致性。
- 分析指标记录中的异常。
- 比较竞品研究。
- 准备 PRD 证据包。

避免让多个 subagent 同时做写入型任务，除非文档或目录边界非常清楚。subagent 应返回提炼后的中文摘要，不要把原始日志塞回主线程。

默认性价比策略：

- 大多数 subagent 使用 `gpt-5.6-terra`。
- 高频分类、打标、提取使用 `gpt-5.6-luna`。
- 复杂综合、模糊优先级、战略判断、高风险 review 才使用 `gpt-5.6` / `gpt-5.6-sol`。

## 文档规则

每个长期知识文档都要包含：

- Owner
- Last updated
- Source
- Confidence
- Related decisions
- Next review date

证据弱时标为「假设」。文档冲突时保留双方来源，并创建待决策或待复核事项，不要静默覆盖。
