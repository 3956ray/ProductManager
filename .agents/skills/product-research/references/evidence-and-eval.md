# 证据结构与产品调研质量门

Owner: Product Lead  
Last updated: 2026-08-18  
Source: OpenAI agent eval guidance；本工作区知识 loop  
Confidence: High  
Related decisions: `product-knowledge-base/decisions/product-research-workflow-2026-08-18.md`  
Next review date: 2026-11-18

## Evidence Card

每条会影响结论的证据使用一张卡：

```yaml
evidence_id: E-001
claim: "来源直接支持的最小完整陈述"
label: Fact | Inference | Assumption
source_title: "原始页面标题"
source_url: "https://..."
source_class: A | B | C | D | E
published_or_event_date: YYYY-MM-DD | unknown
accessed_date: YYYY-MM-DD
scope: "地区、用户、产品、样本、时间窗"
support: full | partial | contextual
independence_group: "相同底层数据或新闻稿使用同一组名"
limitations: "偏差、缺口或不能推出的内容"
decision_relevance: "支持或反对哪个选项"
confidence: High | Medium | Low | Hypothesis
```

原则：一张卡只表达一个可核查 claim；二手来源能找到原始来源时，卡片链接原始来源。

## 产品调研决策简报

长期研究文档按以下顺序输出：

1. 元数据：Owner、Last updated、Source、Confidence、Related decisions、Next review date。
2. 待做决策：谁在何时需要决定什么。
3. 范围与非范围：用户、地区、时间、产品边界。
4. 结论：3–7 条按重要性排序的结论，分别标记事实、推断或假设。
5. 关键证据：Evidence Cards 或 claim-to-source 表。
6. 反证与冲突：哪些材料不支持主结论，如何解释或留待决策。
7. 选项与权衡：至少包含保持现状或不做。
8. 建议：说明置信度、可逆性和适用条件。
9. 验证计划：下一次访谈、原型、数据检查或付费实验。
10. 证据缺口：明确当前不知道什么。
11. 审批与写回：哪些动作可直接做，哪些必须由谁批准。

## 100 分质量门

| 维度 | 分值 | 通过标准 |
| --- | ---: | --- |
| 决策对齐 | 15 | 明确支持的决策、范围、截止和停止条件 |
| 来源质量与覆盖 | 20 | 关键 claim 有合适的一手来源，多条独立证据线 |
| 引用支持关系 | 20 | 链接可打开，来源确实支持 claim，口径和日期准确 |
| 事实/推断/假设分离 | 15 | 未把推断写成事实，假设进入验证计划 |
| 反证与冲突处理 | 10 | 主动寻找反例，冲突不被静默抹平 |
| 决策价值 | 10 | 明确选项、权衡、建议条件和下一步 |
| 可维护性 | 10 | 元数据完整、结构稳定、能与下一次运行比较 |

通过线：总分至少 85，且「来源质量与覆盖」「引用支持关系」均不得低于各自分值的 75%。

以下任一项直接 Fail：

- 关键数字、价格、法律/监管或医学 claim 没有可核查来源。
- 引用不支持陈述，或只支持陈述的一部分却标记为完整支持。
- 把 Reddit/X 热度、GitHub stars 或单一公司宣传当成市场需求证明。
- 忽略已发现的重大反证或文档冲突。
- 在没有人类批准时改变 roadmap、定价、上线、法律/合规或客户承诺。

## Eval 记录

每次重大研究至少记录：

```yaml
eval_status: pass | revise | fail
score: 0-100
critical_failures: []
weak_claims: []
missing_sources: []
recommended_repairs: []
reviewer: review_eval_agent | human
reviewed_at: YYYY-MM-DD
```

优先修复会改变建议方向的 claim；不要为了提高总分而补充与决策无关的材料。
