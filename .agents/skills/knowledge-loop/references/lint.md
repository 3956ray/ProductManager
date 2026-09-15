# Lint 协议

先运行确定性检查：

```bash
python3 .agents/skills/knowledge-loop/scripts/lint_knowledge.py product-knowledge-base
```

脚本检查长期文档元数据、失效内部链接、重复标题、过期复核日期、INDEX 遗漏、原始来源编号/URL重复、日期与枚举字段，以及把 `outputs/` 当来源的情况。

随后进行语义检查：

- 同一 claim 是否存在互相冲突的版本；
- 是否出现同义重复页面或孤立知识；
- 模型输出或二手摘要是否被自我引用成事实；
- 结论是否超过 Research Quality 或 Validation Level；
- 历史决策、人工复核内容或反证是否被覆盖；
- Git diff 中已提交的 `raw/` 是否被改写；确定性脚本不替代这项人工 append-only 检查；
- 来源是否已过期，适用地区、样本和时间窗是否改变。

试点期只输出问题和候选补丁，不自动修复。报告按 Error、Warning 排序，注明文件、问题、影响和建议动作；Lint 结果追加到 `LOG.md`。
