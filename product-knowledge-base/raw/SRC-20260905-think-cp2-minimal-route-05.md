---
source_id: SRC-20260905-think-cp2-minimal-route-05
title: "最小源码部分快照 scanner 结构化报告"
source_url_or_path: "/Users/orderly_ray/Projects/think/doc/security-reviews/sherpa-onnx-minimal-source-snapshot/2026-09-05/scan-report.json"
publisher_or_author: "scan-untrusted-code 1.1.2"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "结构化 scanner 报告记录部分快照 verdict=sandbox_only、40/100、2 个不可达 high、0 block signal，50 candidates 且无 skipped/unreadable；报告同时声明静态检查不能证明制品安全。最终人工门禁因闭包失败为 manual_review。"
quoted_or_referenced_location: "verdict、score_breakdown、findings、stats、limitations"
supersedes: null
---

# 来源边界

scanner 的机械裁决不替代人工闭包、能力、来源和许可证判断；两项命中被解释为不可达字符串，也不能把未完成快照提升为安全批准。
