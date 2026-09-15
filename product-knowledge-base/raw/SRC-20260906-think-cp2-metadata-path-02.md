---
source_id: SRC-20260906-think-cp2-metadata-path-02
title: "CP2 冻结元数据预检报告"
source_url_or_path: "/Users/orderly_ray/Leader/orchestration/reports/CP2-ASR-FROZEN-METADATA-PREFLIGHT-001.md"
publisher_or_author: "Leader orchestration"
published_or_event_date: 2026-09-06
accessed_date: 2026-09-06
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "预检在正文请求前返回 BLOCKED：canonical input 与 commit 通过，tree 因 tree_path_or_duplicate 停止；8585 条记录无重复，171 个不兼容名称全部位于正文获取范围外。根因是第一方解析器把获取路径字符规则施加于整个惰性目录元数据。"
quoted_or_referenced_location: "全文，尤其‘冻结解析结果’和‘验收与下一步’；SHA-256 513cf687ba44a4e33c32ea56684947e91f302b4d6b640e6b23b2e856f911d06a"
supersedes: null
---

# 结论限制

预检实际网络事件与正文请求均为零。其 BLOCKED 是 metadata 兼容性结果，不是 sherpa-onnx 源码不可行、制品恶意或 CP2 结论。
