---
source_id: SRC-20260905-think-cp2-design-decision-05
title: "项目自有 handle 型窄运行时边界提案"
source_url_or_path: "/Users/orderly_ray/Projects/think@a57f643bac24edef5d6601b8a59baa77060f3d2c:doc/security-reviews/sherpa-onnx-narrow-runtime-boundary-design/2026-09-05/proposals/narrow-runtime-boundary.md"
publisher_or_author: "think repository security design review"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: repository
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "提案只向业务层暴露固定运行时／模型 handle、stream 生命周期、有界内存 PCM、decode、只读结果、版本和释放，并拒绝宽 API＋caller 规则作为最终架构；WAV、文件音频、ADSP/QNN/RKNN、TTS、自动下载、宽 JNI 与用户可控路径均在 denylist。"
quoted_or_referenced_location: "提交 a57f643bac24edef5d6601b8a59baa77060f3d2c；proposal SHA-256 257469cf982dafd0a0a6701090270ad54d4512fbdccf422afda0e8a2776e803e；Decision、Desired Invariants、Options、Validation Plan"
supersedes: null
---

# 限制

提案中的性能、内存与可靠性方向均非测量结果；窄公开 API 也不能证明未来 native 制品没有链接 dormant 禁止能力。
