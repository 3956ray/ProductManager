---
source_id: SRC-20260905-think-cp2-acquisition-tool-03
title: "提交 da9279a 第一方离线审查核心接口与限制"
source_url_or_path: "/Users/orderly_ray/Projects/think@da9279a411d990e4c37191e22be680b2c4bfcb07:tools/asr_review_offline_v2/"
publisher_or_author: "think repository"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: repository
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "README、REPORT、adapter/controller 接口明确把候选限制为 synthetic-only：只接受 project-synthetic 与 SyntheticAdapter，source_verdict 恒为 insufficient_evidence，没有真实 URL、HTTP、GitHub metadata 或获取入口。新增完整组件必须形成新候选并重新验收，不能在冻结阶段补代码。"
quoted_or_referenced_location: "README.md、REPORT.md、offline_review/__init__.py、adapter.py、policy.py、controller.py；README SHA-256 54a73fda6bc9bd0e29dc6cde10e1fcf0d03eea1c527376a5909047f889f957bb；REPORT SHA-256 b3c008c85547c0adac0292412369f568ce08ec24682642b1983e9cfb84abc12c；adapter.py SHA-256 5b04e61b8bfc2becfeb0151fd4b7f72c554812efb1a61df7d0e0af667ed15b9a；controller.py SHA-256 11d696dd879f9bde8db6e8922dd1badb8fedf714c9aeb44ccf46c35facd464f7"
supersedes: null
---

# 结论限制

tool_ready_for_freeze 只适用于离线核心/schema/合成证据候选。不能通过移除 synthetic 标记、包裹一次外部 fetch 或冻结时补代码，把该提交转成完整获取 release。
