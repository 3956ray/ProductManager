---
source_id: SRC-20260905-think-cp2-runtime-05
title: "Zipformer 14M 中文流式 INT8 四文件集人工安全复核"
source_url_or_path: "/Users/orderly_ray/Projects/think/doc/security-reviews/sherpa-onnx-model-zipformer-14m-int8/2026-09-05/manual-review.md"
publisher_or_author: "think security review"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "固定提交 204ad334e2e683fd295359930cc16fc0432a23ac 的 Zipformer 14M INT8 三个 ONNX 与 tokens 文件集最终裁决为 manual_review；同源 FP32 架构后门提示、量化继承可能性、来源/许可证和全 INT8 组合兼容性均未解决，禁止加载、推理、测试、打包或集成。"
quoted_or_referenced_location: "第 8–15 节"
supersedes: null
---

# 来源边界

此裁决不继承给 AAR、源码、Conformer 或其他模型组合，也不表示该模型已确认恶意；平台 safe 或 scanner low_indicators 不能替代人工门禁。
