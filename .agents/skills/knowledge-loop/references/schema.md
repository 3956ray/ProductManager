# 知识循环结构

## 来源编号与记录

文件名与 `source_id` 使用 `SRC-YYYYMMDD-slug-NN`。同一天相同 slug 的序号从 `01` 递增。

```yaml
source_id: SRC-YYYYMMDD-slug-NN
title: "原始标题"
source_url_or_path: "https://... | 本地路径"
publisher_or_author: "发布者或作者"
published_or_event_date: YYYY-MM-DD | unknown
accessed_date: YYYY-MM-DD
source_class: A | B | C | D | E
source_type: official | product | user_voice | independent | repository | internal
projects:
  - project-slug
storage_permission: metadata-and-short-excerpt | full-copy-permitted | user-owned
access_status: verified | partial | unavailable
summary: "来源直接支持的最小摘要"
quoted_or_referenced_location: "章节、段落、行号或页面区域"
supersedes: null | SRC-...
```

非自有网页默认使用 `metadata-and-short-excerpt`。不得把整篇第三方内容复制进 `raw/`。

## 长期文档元数据

所有长期知识文档包含：Owner、Last updated、Source、Confidence、Related decisions、Next review date。

被人工复核的文档可增加 `Human reviewed: YYYY-MM-DD`。后续 agent 只能提出局部 diff，不能整页重写。

## 双轴评估

```yaml
research_quality: 0-100 | pending
validation_level: V0 | V1 | V2 | V3 | V4 | V5
confidence: High | Medium | Low | Hypothesis
next_evidence: "下一条必须取得的证据"
allowed_next_investment: "当前允许的可逆投入"
pause_or_kill_condition: "暂停或终止条件"
```

| 等级 | 可确认的证据 | 投资上限 |
| --- | --- | --- |
| V0 | 创始人假设 | 仅调研 |
| V1 | 可靠公开证据 | 可逆、低成本原型 |
| V2 | workaround、主动求助或持续成本等行为代理 | 原型测试或小范围发布 |
| V3 | 自有产品真实使用 | 有限开发 |
| V4 | 付款或其他高成本承诺 | 单位经济成立时扩大 |
| V5 | 留存或目标结果 | 考虑规模化 |

Research Quality 达到 85 只表示研究合格，不能自动提高 Validation Level。
