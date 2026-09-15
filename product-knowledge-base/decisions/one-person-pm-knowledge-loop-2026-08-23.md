# 一人公司 PM 知识循环与 WIP 决策

Owner: Product Lead
Last updated: 2026-08-23
Source: Product Lead 明确批准的《一人公司 PM 工作流优化计划》；Karpathy LLM Wiki、Software 2.0/3.0 与 autoresearch 工作方式的内部研究综合
Confidence: High
Related decisions: `product-research-workflow-2026-08-18.md`
Next review date: 2026-09-30

## 状态

Approved

## 决策

1. 保留现有 `product-knowledge-base` 作为长期知识层，增量增加 `raw/`、`outputs/`、`INDEX.md` 与 `LOG.md`。
2. 使用单一 `knowledge-loop` skill 承担 Ingest、Query 与 Lint，不新增 agent；`knowledge_curator_agent` 负责串行写回。
3. 所有产品研究采用 Research Quality 0–100 与 Validation Level V0–V5 双轴评估。
4. 一人公司同时最多保留 1 个 Build 与 1 个 Discovery：Build 为「哎呀，早知道」，Discovery 为「私人家庭史／家族编年网页」。
5. Product Knowledge Loop 是内部基础设施，不占产品 WIP；Rapid Situation Interpreter 与中国城市日常沉浸体验进入 Parking Lot，资料保留。
6. 先手动完成 Family Chronicle 的 20 次 Ingest 与至少 3 次有效 Lint，再决定是否定时自动化。
7. 使用本地 Git 小提交和人工 diff 审核；本阶段不连接远程、不自动提交、不自动合并。

## 背景

团队实际是 one-person company，真人访谈和自有行为数据有限，主要依赖公开网页、官方披露、产品页、社区声音和开源项目。现有研究流程能控制来源质量，却缺少原始来源所有权、稳定知识编译、系统性 Lint 与投入上限，容易把研究完整度误读成市场验证。

## 备选方案

| 选项 | 优点 | 缺点 | 结论 |
| --- | --- | --- | --- |
| 保持现状 | 无迁移成本 | 来源与结论容易混合，缺少回溯和 WIP 约束 | 不采用 |
| 增量知识循环 | 保留现有成果，可逐步验证 | 需要维护来源编号与日志 | 采用 |
| 全量迁移到新 Wiki/数据库 | 结构统一 | 迁移和工具成本高，尚无真实使用数据证明必要 | 暂不采用 |

## 理由

- 文件、Markdown 与 Git 足以验证核心工作方式，不需要先引入向量数据库或知识图谱。
- 双轴评估能让公开研究继续产生价值，同时防止把社区热度、竞品存在或高研究分数当作真实需求。
- 1 Build + 1 Discovery 迫使有限创始人时间集中到交付和下一项证据。
- 先手动执行 20 次真实 Ingest，能在自动化前暴露来源冲突、维护成本和索引问题。

## 影响

- Build：哎呀，早知道；保持低成本交互原型范围。
- Discovery：Family Chronicle；以公开证据编译和第一卷验证为主。
- Parking Lot：RSI、中国城市日常沉浸体验及其他未激活机会。
- 历史研究评分和决策不覆盖；新版评估以补充记录方式加入。

## Research Quality / Validation Level 影响

- Research Quality 通过线为 85，评价研究本身。
- Validation Level 单独决定投入：V0 仅调研，V1 可逆原型，V2 原型测试/小范围发布，V3 有限开发，V4 视单位经济扩大，V5 才考虑规模化。
- 等级提升必须有新增行为证据，不能由研究分数自动推导。

## 后续动作

1. 完成结构、skill、Lint 和模板更新。
2. 对 Family Chronicle 摄取 20 个来源，每 5 个运行一次 Lint。
3. 执行 5 个可追溯 Query，完成双轴复评。
4. 记录耗时、人工修复、漏检、误报和冲突，再决定是否自动化。

## 复查触发条件

- 完成 20 次 Ingest 和至少 3 次有效 Lint。
- 发现原始来源丢失、历史决策被覆盖或模型自我引用。
- 手工维护成本高于所减少的返工。
- 准备加入定时任务、远程 Git、向量检索、知识图谱或无人值守写回。
