# 原始来源记录模板

此模板用于创建 `raw/SRC-YYYYMMDD-slug-NN.md`。复制后替换所有占位符，不要在 `raw/` 保存第三方全文。

```yaml
source_id: SRC-YYYYMMDD-slug-NN
title: ""
source_url_or_path: ""
publisher_or_author: ""
published_or_event_date: unknown
accessed_date: YYYY-MM-DD
source_class: A
source_type: official
projects:
  - project-slug
storage_permission: metadata-and-short-excerpt
access_status: verified
summary: ""
quoted_or_referenced_location: ""
supersedes: null
```

## 使用边界

- 原始记录创建后不覆盖；修正时创建新编号并填写 `supersedes`。
- `summary` 只写来源直接支持的最小陈述。
- AI 回答、搜索摘要和 `outputs/` 不得登记为原始来源。

Owner: Product Lead
Last updated: 2026-08-23
Source: `.agents/skills/knowledge-loop/references/schema.md`
Confidence: High
Related decisions: `../decisions/one-person-pm-knowledge-loop-2026-08-23.md`
Next review date: 2026-09-30
