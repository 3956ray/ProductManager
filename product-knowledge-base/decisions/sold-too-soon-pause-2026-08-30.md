# 暂停「哎呀，早知道」项目

Owner: Product Lead
Last updated: 2026-08-30
Source: Product Lead 2026-08-30 明确指示暂停；`../raw/SRC-20260830-sold-too-soon-progress-01.md`
Confidence: High
Related decisions: `one-person-pm-knowledge-loop-2026-08-23.md`；`../ideas/sold-too-soon/prd-approval-decision-2026-08-07.md`
Next review date: 2026-09-30

## 状态

Approved

## 决策

自 2026-08-30 起暂停「哎呀，早知道」（`I Knew It`）的活跃 Build 状态，移入 Parking Lot，不再计入每周 Build 时间预算。释放出的 Build 名额不自动分配给其他候选项目，需由 Product Lead 另行决定。

## 背景

Product Lead 查看当前开发进度后明确要求暂停项目。暂停前，CP7 已完成 Agent 交易理解与自动行情验证流程，覆盖美股和台股原型路径，并通过任务记录中的完整开发验证。

暂停是优先级与 WIP 状态决定，不代表产品假设已被证伪，也不代表需求、分享、付费或留存已获得验证。

## 暂停时保留的资产

- 代码仓库：`/Users/orderly_ray/Projects/iknewit`。
- CP7：Agent 只提取交易事实、独立资产身份验证、历史与最新行情查询、确定性计算和 verifier、安全额度与 checkpoint 恢复规则。
- 验证记录：301/301 unit/flow、35/35 E2E、lint、typecheck、production build 和隔离安全容器通过。
- 现有产品策略、PRD、账号与图库、单输入体验、定价、计算、固定模板、结果文案、支付与退款决策文档。
- 当前代码尚未提交，未使用真实 API Key。

## 备选方案

| 选项 | 优点 | 缺点 | 备注 |
| --- | --- | --- | --- |
| 继续作为活跃 Build | 延续开发动量 | 持续占用一人公司的 Build 名额 | 不采用 |
| 暂停并保留全部资产 | 释放 WIP，同时保留恢复路径 | 未提交代码与原型依赖需要在恢复时重新核查 | 采用 |
| 终止并删除资产 | 减少维护面 | 破坏历史与已完成成果 | 不采用 |

## 理由

直接依据 Product Lead 的暂停指示执行。未补充推断暂停的市场或技术原因。

## 影响

- 活跃产品只保留 Family Chronicle 的 Discovery；当前没有活跃 Build。
- 「哎呀，早知道」的 Research Quality、Validation Level 与历史决策保持不变。
- 不删除、不覆盖、不提交 `iknewit` 仓库中的现有代码。
- 不启动真实 Agent、不接生产行情、不收款、不作外部发布承诺。

## Research Quality / Validation Level 影响

- Research Quality：保持 82 · revise。
- Validation Level：保持 V1。
- CP7 的工程完成度不能替代真实用户行为、付款或留存证据，因此不提升 Validation Level。

## 后续动作

1. 当前停止新增开发与验证投入。
2. 保留代码、checkpoint 文档、测试结果和产品知识文档。
3. 若未来恢复，先复核未提交工作树、依赖版本和当前测试基线。
4. 正式发布前必须替换 Yahoo 原型行情源、配置共享持久化 usage gate，并执行脱敏真实 Agent smoke eval。

## 复查触发条件

- Product Lead 明确重新排列 Build 优先级并决定恢复项目。
- 获得真实目标用户测试渠道，且能验证任务完成率、结果理解、模板裁切、保存或分享行为。
- 准备进入真实 Agent、生产行情、收款或公开发布阶段。
