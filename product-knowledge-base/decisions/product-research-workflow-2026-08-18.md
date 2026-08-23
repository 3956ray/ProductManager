# 产品调研工作流标准化决策

Owner: Product Lead  
Last updated: 2026-08-18  
Source: Product Lead 明确批准；OpenAI Docs；GitHub 与产品管理社区调研  
Confidence: High  
Related decisions: 暂无  
Next review date: 2026-11-18

## 决策

将「决策定义 → 搜索计划 → 多来源证据收集 → Evidence Cards → 独立核查 → 决策综合 → 质量门 → 审批后写回 → 差异监控」纳入产品知识 loop。

仓库级 `.agents/skills/product-research/` 是该流程的规范入口。`product_manager_agent` 保持最终综合责任；specialist agents 作为受控工具提供证据收集、验证和 review，不自主修改 roadmap 或作最终优先级决定。

## 原因

- 当前知识库已有研究文档和 manager/specialist 分工，但缺少统一的来源分级、claim-to-source 结构、反证核查和可重复 eval。
- 市场、竞品、GitHub、Reddit/X 与内部资料的证据性质不同，需要明确限制，避免把热度或公司宣传误写成需求验证。
- 稳定结构可以支持后续定期刷新，报告「发生了什么变化」，而不是每次重做整份研究。

## 采用范围

- 产品想法初筛、市场与竞品研究、公开用户声音挖掘、趋势研究、定位和定价假设。
- PRD 前证据包、重大产品建议和研究刷新。
- 与当前项目相关的本地知识库写回。

## 不采用

- 不允许 agent 代替 Product Lead 作最终 roadmap、定价、上线或客户承诺。
- 不把公开社区讨论代替真实用户访谈、本产品指标或付费实验。
- 不直接复制或再分发第三方受限许可证 skill；仓库内流程采用原创中文实现并保留方法来源。
- 不因任务可以并行就默认增加多个 agent；只有证据线独立、职责契约不同且能降低上下文干扰时才使用。

## 质量标准

- 每个关键 claim 有原始链接、日期、范围、限制和置信度。
- 事实、推断和假设分开；冲突与反证保留。
- 研究质量总分至少 85/100，且来源覆盖与引用支持关系均达到单项最低线。
- 关键数字、法律/监管、医疗或价格 claim 无可核查来源时直接 Fail。

## 落地

1. 新增 `product-research` skill、来源政策和证据/eval 规范。
2. 在 agent roster 中新增 `source_scout_agent` 与 `evidence_verifier_agent`。
3. 更新 operating rules，使研究 gate 成为知识 loop 的正式环节。
4. 以「哎呀，早知道」现有研究做第一次回放 eval；试运行不改变已批准 PRD。

## 复核触发

- 连续两次研究低于 85 分。
- 发现高置信度结论引用错误或来源失效。
- 研究流程显著增加时间，却没有改善决策或减少返工。
- 数据源、模型或 agent orchestration 方式发生重大变化。
