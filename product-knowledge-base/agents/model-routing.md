# 模型路由说明

Owner: Product Lead
Last updated: 2026-08-23
Source: OpenAI 官方模型与 agent 文档；本工作区 agent roster
Confidence: High
Related decisions: `../decisions/product-research-workflow-2026-08-18.md`；`../decisions/one-person-pm-knowledge-loop-2026-08-23.md`
Next review date: 2026-09-30

Last updated: 2026-07-22

## 推荐

产品团队 agent 默认使用 `gpt-5.6-terra`。这个工作区的大多数任务是综合、分类、草拟、检查一致性，不是每次都做最高难度战略判断，所以 `gpt-5.6-terra` 是更合适的性价比默认值。

高频、低风险任务使用 `gpt-5.6-luna`：

- 用户反馈打标
- 去重
- 字段提取
- 大量短记录摘要
- 第一轮聚类

高风险或复杂任务使用 `gpt-5.6` / `gpt-5.6-sol`：

- 重大 roadmap 取舍
- 战略叙事
- 复杂 PRD
- 证据互相冲突
- 面向管理层的总结
- 外部承诺前的最终 review

## Reasoning Effort

- `low`：快速检查、简单摘要、直接分类。
- `medium`：常规 subagent 默认值。
- `high`：manager 综合、指标解释、PRD 草拟、review。
- `xhigh` 或 `max`：只用于少数高难决策，且额外质量值得成本和延迟。

## Subagent Policy

默认 subagent 配置：

```toml
[agents]
enabled = true
max_concurrent_threads_per_session = 4
default_subagent_model = "gpt-5.6-terra"
default_subagent_reasoning_effort = "medium"
```

只有任务形态需要时才显式覆盖模型：

- `gpt-5.6-luna`：批量提取。
- `gpt-5.6-terra`：常规分析。
- `gpt-5.6`：复杂综合。

## 官方依据

OpenAI 模型文档当前说明：

- `gpt-5.6-sol` / `gpt-5.6` 是复杂推理和 coding 的旗舰选择。
- `gpt-5.6-terra` 平衡智能和成本。
- `gpt-5.6-luna` 面向成本敏感、高吞吐工作负载。

OpenAI Agents SDK 也描述了两种常见编排模式：

- Manager pattern：一个中心 agent 调用专业 agent，并负责最终综合。
- Handoffs：一个 agent 把任务交给另一个 specialist，由 specialist 接管后续交互。

这个产品团队工作区优先使用 Manager pattern。这样可以把最终产品判断集中在一个主 agent，同时让 specialist agents 做边界清楚的支持工作。
