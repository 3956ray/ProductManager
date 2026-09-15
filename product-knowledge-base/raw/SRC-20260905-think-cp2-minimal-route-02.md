---
source_id: SRC-20260905-think-cp2-minimal-route-02
title: "最小源码快照依赖与许可证静态复核"
source_url_or_path: "/Users/orderly_ray/Projects/think/doc/security-reviews/sherpa-onnx-minimal-source-snapshot/2026-09-05/dependency-license-review.md"
publisher_or_author: "think security review"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "在提交 6952167795d1243534a93fa59a18372fb0d192e8 中，依赖闭包未闭合：首批 50 个正文文件引用 5 个冻结清单外仓库内头文件，其中 offline-tts-frontend.h 跨入明确排除的 TTS 能力；上游统一 sources、默认功能和 CMake 自动下载也不满足 ASR-only、依赖预门禁要求。101 个文件、JNI/Kotlin 和外部依赖仍未验证。"
quoted_or_referenced_location: "结论；仓库内闭包缺口；构建元数据边界；未验证项"
supersedes: null
---

# 来源边界

此报告只支持“本次 151 项清单未闭合且不能用于构建”的结论；它不批准任何依赖、源码裁剪方案、构建描述或运行时产物。
