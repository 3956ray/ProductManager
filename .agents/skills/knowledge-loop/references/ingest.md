# Ingest 协议

1. 阅读 `BOARD.md`、`INDEX.md`、相关项目和历史决策。
2. 打开原始来源；若无法打开，标记 `access_status: unavailable`，不得引用搜索摘要补足事实。
   - 用户提供单一、明确来源时，Ingest 可完成来源核查并记录一个最小 claim、标签和限制。
   - 需要搜索新来源、比较多个竞品、判断市场或形成重大建议时，先交给 `product-research` 生成已核验 Evidence Cards。
3. 检查现有 `raw/` 编号后生成新的 `SRC-*`，按 schema 保存元数据、最小摘要和引用位置。
4. 写回前列出 impact plan：新建页面、更新页面、冲突页面、只登记不写回的来源。
5. 只更新 impact plan 中的页面；关键 claim 链接 `SRC-*`，并保留 Fact、Inference、Assumption、反证和证据缺口。
6. 评估是否需要更新 `INDEX.md`：只有新增长期页面、改变导航或现有入口无法找到该来源时才修改；否则在 `LOG.md` 记录“INDEX 无需变更”。一次来源只形成一条 Ingest 日志。
7. 运行 `python3 .agents/skills/knowledge-loop/scripts/lint_knowledge.py product-knowledge-base`。
8. 展示 Git status 与完整 diff。只有 Product Lead 对本次变更给出明确确认后才可提交，并在 `LOG.md` 记录确认；建议提交信息为 `knowledge: ingest SRC-...`。

修正原始来源时创建新记录，在新记录的 `supersedes` 指向旧编号，并在日志解释原因。禁止编辑旧记录来隐藏错误。
