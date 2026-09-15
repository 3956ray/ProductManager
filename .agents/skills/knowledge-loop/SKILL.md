---
name: knowledge-loop
description: 将已取得的公开或内部来源编译进产品知识库，并执行可追溯查询与一致性检查。用户要求摄取来源、把研究写回长期知识、追溯现有结论、检查知识库冲突/过期/重复时使用；不替代市场调研，也不把模型输出当作原始证据。
---

# 产品知识循环

把 `product-knowledge-base/raw/` 视为不可覆盖的证据层，把现有 `ideas/`、`references/`、`decisions/` 视为可维护的知识层。`BOARD.md` 管当前行动，`INDEX.md` 管知识导航，`LOG.md` 记录每次操作。

## 选择模式

- **Ingest**：用户提供新来源或要求把已核验研究写回时，读取 [references/ingest.md](references/ingest.md)。
- **Query**：用户要求基于知识库回答、追溯或综合问题时，读取 [references/query.md](references/query.md)。
- **Lint**：用户要求检查知识质量，或 Ingest 写回完成时，读取 [references/lint.md](references/lint.md)。

需要创建或解释 `SRC-*`、长期文档元数据、双轴评估字段时，读取 [references/schema.md](references/schema.md)。

## 不可破坏的边界

- 原始来源记录只追加，不覆盖；修正使用新的 `SRC-*` 并在 `LOG.md` 说明替代关系。
- 模型回答、`outputs/` 内容和搜索摘要不能作为原始证据；关键 claim 必须回到原始页面或获准保存的原始文件。
- 保留历史决策、人工修订、反证和互相冲突的版本，不替用户静默裁决。
- 来源收集可并行，知识写回串行；写回前先列出目标页面，写回后展示 diff。
- Research Quality 只评价研究质量；Validation Level 才决定允许投入，不得相互替代。
- 外部写入、定价、roadmap、上线、法律/合规和客户承诺仍按工作区审批规则处理。

## 交接

需要新检索、竞品分析或公开用户声音研究时，先使用 `product-research`；本 skill 只接收已核验 Evidence Cards、明确的来源缺口和冲突。`knowledge_curator_agent` 负责最终写回与 Lint，`product_manager_agent` 保持决策所有权。

## 维护元数据

- Owner: Product Lead
- Last updated: 2026-08-23
- Source: Product Lead 批准的一人公司 PM 工作流；本工作区运行规则
- Confidence: High
- Related decisions: `product-knowledge-base/decisions/one-person-pm-knowledge-loop-2026-08-23.md`
- Next review date: 2026-09-30
