---
source_id: SRC-20260905-think-cp2-boundary-route-03
title: "sherpa-onnx 静态闭包发现四态裁决"
source_url_or_path: "/Users/orderly_ray/Projects/think@0ded8eb54e5d4d529759b46c62b9b5eb10722fbb:doc/security-reviews/sherpa-onnx-static-closure-discovery/2026-09-05/security-verdict.json"
publisher_or_author: "think repository security review"
published_or_event_date: 2026-09-05
accessed_date: 2026-09-05
source_class: B
source_type: repository
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "结构化裁决为 TASK RESULT=BLOCKED、artifact_verdict=manual_review、fixed_point=false；阻塞原因同时记录 Leader 停止造成的两条未完成边，以及 WAV 路径写入、ADSP/QNN/RKNN 与无法证明 CPU-only ASR-only/TTS 排除的独立边界缺陷。"
quoted_or_referenced_location: "提交 0ded8eb；security-verdict.json 全文；SHA-256 8b0a87846101fe01f51aa1c6d4b6c560838e8b74724ac00f50305ea3af4673e0"
supersedes: null
---

# 非继承

该裁决只适用于固定提交、固定停止状态的静态发现材料，不转移给未来快照、构建输入、AAR、模型、依赖、集成或 checkpoint 决定。
