---
source_id: SRC-20260905-think-cp2-minimal-route-06
title: "最小源码部分快照 scanner Markdown 报告"
source_url_or_path: "/Users/orderly_ray/Projects/think/doc/security-reviews/sherpa-onnx-minimal-source-snapshot/2026-09-05/scan-report.md"
publisher_or_author: "scan-untrusted-code 1.1.2"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "Markdown scanner 报告与结构化报告一致：sandbox_only、40/100，命中 CMake 帮助文本中的 rm -rf build 和 logger 调试提示中的 gdb/python，均标记 unreachable；0 跳过、0 读取失败。"
quoted_or_referenced_location: "Summary、Findings、Scan statistics、Limitations"
supersedes: null
---

# 来源边界

此报告是 scanner 输出的可读视图，不证明快照闭合、可构建或安全，也不覆盖人工 manual_review 裁决。
