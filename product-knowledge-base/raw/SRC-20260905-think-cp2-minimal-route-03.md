---
source_id: SRC-20260905-think-cp2-minimal-route-03
title: "最小源码快照冻结 allowlist"
source_url_or_path: "/Users/orderly_ray/Projects/think/doc/security-reviews/sherpa-onnx-minimal-source-snapshot/2026-09-05/frozen-allowlist.json"
publisher_or_author: "think security review"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "提交 6952167795d1243534a93fa59a18372fb0d192e8 中的冻结清单固定 sherpa-onnx commit 917bed95... 与 tree fd2c4e97...，共 151 个唯一 Git blob、887,313 声明字节，正文获取前冻结；不含 mode 120000。其选择声明排除 TTS 等能力，但后续正文证明清单并未形成真实 include 闭包。"
quoted_or_referenced_location: "顶层元数据、excluded_capabilities、entries"
supersedes: null
---

# 来源边界

清单冻结顺序和逐项身份正确，不等于清单完整、安全或可构建；它不得被静默增补、重冻或当作最终快照输入。
