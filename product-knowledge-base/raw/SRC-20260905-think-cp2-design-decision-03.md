---
source_id: SRC-20260905-think-cp2-design-decision-03
title: "窄运行时边界设计返工：可复算输入集合"
source_url_or_path: "/Users/orderly_ray/Projects/think@a57f643bac24edef5d6601b8a59baa77060f3d2c:doc/security-reviews/sherpa-onnx-narrow-runtime-boundary-design/2026-09-05/context.md"
publisher_or_author: "think repository security design review"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: repository
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "返工将设计输入明确为 28 条 canonical record：固定证据目录 22 项、Leader 报告 1 项、正式产品文档 5 项，并给出可独立复算的集合摘要 c318c5a5…64d2；返工只修改 context.md 与 hardening.json。"
quoted_or_referenced_location: "提交 a57f643bac24edef5d6601b8a59baa77060f3d2c；最终设计 tree 31376c73f43caf3bbfd664d8316ffecdc589379d；context.md SHA-256 4d7fd8a0457cf6c59de2d42c9a67bba59087f4820dc3a68ef78bb3425b53f8b1；输入集合 SHA-256 c318c5a5f91d4af1d2759895ab9d5296c5784eaa214548b92f25fba4096764d2"
supersedes: null
---

# 限制

集合摘要绑定设计输入，不是第三方源码快照摘要；`sourceDrift=none` 只针对固定证据目录，不补足任何源码闭包或动态证据。
