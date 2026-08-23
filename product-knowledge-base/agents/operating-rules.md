# 产品 Agent 运行规则

Owner: Product Lead  
Last updated: 2026-08-18  
Source: 本工作区运行设计；OpenAI agent orchestration 与 eval 指南  
Confidence: High  
Related decisions: `../decisions/product-research-workflow-2026-08-18.md`  
Next review date: 2026-11-18

## 产品知识 Loop

1. Collect 收集
   收集用户反馈、指标、研究、会议纪要、销售记录、客服工单和 roadmap 变化。

2. Classify 分类
   把每条信息标成：反馈、指标信号、阻塞、决策、PRD 输入、研究信号或知识库维护事项。

3. Retrieve 检索
   在给建议前读取公告板、相关 PRD、历史决策、用户分层、指标定义和相关研究。

4. Scope 界定
   当任务涉及市场、竞品、用户问题、趋势、定位或定价假设时，调用 `.agents/skills/product-research/`，明确本次研究支持的决策、范围、非范围、交付物和停止条件。

5. Collect Evidence 收集证据
   按权威、产品、用户和内部证据线收集材料；把关键材料转换为 Evidence Cards。只有独立、只读的证据线适合并行 subagent。

6. Verify 核查
   打开原始来源，检查引用支持关系、时间、地区、样本、单位、来源独立性和反证。高风险、关键数字或冲突结论交给 `evidence_verifier_agent`。

7. Reason 判断
   区分事实、推断、假设和证据缺口，并明确标注置信度。公开社区热度不得替代用户访谈、产品指标或付费证据。

8. Propose 提议
   给出下一步建议：更新知识库、创建 PRD、提出待决策问题、加入 backlog、更新公告板、归档为不处理或进入更深调研。

9. Evaluate 评估
   重大产品研究由 `review_eval_agent` 按 100 分质量门检查；低于 85 分、关键引用不支持 claim 或存在直接 Fail 项时，先修订，不给高置信度 GO 建议。

10. Approve 审批
   外部写入、roadmap 变化、客户承诺、定价/法律表述、破坏性编辑或范围扩大之前，必须先问人。

11. Write Back 写回
   获得批准或确认是低风险后，更新对应长期文档，并交叉链接相关记录。

12. Monitor 监控
   需要持续跟踪时保存基线和 Next review date；后续刷新只报告变化、失效假设和新风险。

## Manager Agent 流程

使用 `product_manager_agent` 作为主编排者。

Manager 可以调用 specialist agents 做边界清楚的任务：

- `user_feedback_agent`：反馈聚类。
- `metrics_agent`：指标变化和异常。
- `research_agent`：市场或竞品综合。
- `source_scout_agent`：按单一证据线搜索并生成 Evidence Cards。
- `evidence_verifier_agent`：独立核查关键 claim、来源与反证。
- `prd_agent`：PRD 草拟。
- `knowledge_curator_agent`：文档维护。
- `decision_log_agent`：决策记录。
- `review_eval_agent`：最终质量检查。

Manager 负责最终综合，不能让 specialist agent 直接做最终 roadmap 或优先级决策。

产品调研优先使用 agents-as-tools：Manager 保持最终回答所有权，specialist 只返回边界清楚的结构化结果。只有 specialist 应完全接管下一段互动时才使用 handoff。

## Handoff 规则

默认优先使用 manager 控制下的 specialist 调用。只有当某个 specialist 应完全接管下一段互动时，才使用 handoff，例如：

- 产品问题已经确认后的 PRD 草拟。
- 用户只想做指标解释的 metrics deep dive。
- 完全聚焦市场或竞品问题的研究会话。

## 证据规则

每个建议都应该包括：

- 发生了什么变化
- 为什么重要
- 证据/来源
- 置信度
- 建议下一步
- 是否需要人类审批

每个产品调研关键 claim 还应该包括：

- 原始来源链接和访问日期
- 来源层级与独立性
- 适用地区、用户、样本和时间窗
- Fact、Inference 或 Assumption 标签
- 限制、反证和证据缺口

详细来源政策、Evidence Card 和 eval 结构见 `.agents/skills/product-research/references/`。

## 冲突规则

如果文档互相冲突：

1. 不要静默覆盖。
2. 记录双方来源。
3. 在公告板标记冲突，或创建待决策事项。
4. 请相关 Owner 或批准人解决。
