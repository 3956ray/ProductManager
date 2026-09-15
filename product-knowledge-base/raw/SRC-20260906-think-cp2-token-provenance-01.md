---
source_id: SRC-20260906-think-cp2-token-provenance-01
title: "CP2 两处人工审查 occurrence 的原 token 来源缺口"
source_url_or_path: "/Users/orderly_ray/Leader/orchestration/reports/CP2-ASR-REVIEW-TOKEN-PROVENANCE-AUDIT-001-report.json"
publisher_or_author: "Leader orchestration；think first-party repository"
published_or_event_date: 2026-09-06
accessed_date: 2026-09-06
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "v8 C=1fe8574 已通过 Leader 两轮各 174 tests／1338 outcomes／0 skip；随后 K 正确停止，因为原 7051-byte R 和 3067-byte verification 只保存规则、行哈希与绝对区间，没有保存两个区间内的原 9-byte token。历史第一方脚本也先 lower() 再 index/count，无法恢复原大小写。原用户批准明确绑定同一 retained envelope/header 和两处命中，且没有一次性读取限制。"
quoted_or_referenced_location: "任务合同 SHA-256 b26bdb99957b0f0e96936b4725680acb97880d7e72a8cf77fd0b789c34288401；审计 SHA-256 b871d25ccb825a093f03e42d27a808dceaa254096a89afad295869c9365df12c；v8 acceptance SHA-256 141c9b5655cbde45dc7761e65658fd6fe2801c2b5252fc6b12810371b430dbeb；原 review request/approval SHA-256 c66a9fe77a77e15ca6dfa8f958f47ac1de4e1816de52779add3b9eee497163c7 / df26a4884e47a63c3cdbd0e2afc118e4a4f70f4ef7db9a267d6307e01b4aa9c2；原 R/verification/script SHA-256 0d8b34a06960a2c82a07effc376b60efe3c06aea1c968fb5a83b160c0d0519e6 / ca492d93813eb41dc589dbf868c49a8d423c8611d8ee180265c388ed3cf7c102 / 923d0669081f5ad7d2d6c35dace85c5c34b8ce3fbf5443a777f0292179fbe3e9；v8 SCHEMA/manual.py SHA-256 f0b19b5f25653b6f7cdfc4b7f5db2178ca0a5d7bf7c47e6dbb7c592808376107 / 8af6f8f931dd7194b134b58e9410eb8a2af7cb9e8ced1183b761b560e2e2a5c9"
supersedes: null
---

# 来源边界

本卡只编译任务合同、Leader 派生审计／验收、既有用户授权记录、原第一方 R／verification 和已接受 v8 schema。历史验证脚本只做静态阅读，没有执行或导入。没有读取 private envelope、header/body、metadata、LICENSE、API、raw scanner context 或任何第三方原文。

# 可用于产品决定的事实

- v8 `occurrence_id` 必须包含 `raw_token`；其长度必须等于 `token_end-token_start`，未来 controller 还会从当前已验证 body 的同区间重新构造并逐项匹配。
- 原 R 和 verification 已固定两个互不替代的区间：行 57 为 `[1893,1902)`、行 60 为 `[1972,1981)`，各 9 bytes；双行 hash、body SHA、Git blob、path、commit/tree 与 decision 已固定，但没有原 token bytes。
- 原验证脚本第 23 行对 segment 执行 `lower().index/count(b'websocket')`，第 24 行只保存区间和规则。大小写映射是非单射的，不能用规则名、聊天摘要或脚本反推原字节。
- 原用户授权允许在严格身份／权限检查后读取同一 8579-byte retained envelope 和 7939-byte header、检查同一两处命中，并记录原始 byte ranges；批准记录没有一次性读取或到期条款。它明确禁止的是新获取、联网和扩大到其他材料。
- 本次审计未读真实 body、未联网、未创建 K，且没有修改原 R、pending 或 v8。

# 限制

本卡不知道也不声明两个原 token 的具体大小写。只有后续单独获准的 Leader 补录任务可从已授权同一对象的固定区间读取并形成新 provenance；若对象身份、权限或范围不匹配，必须停止。
