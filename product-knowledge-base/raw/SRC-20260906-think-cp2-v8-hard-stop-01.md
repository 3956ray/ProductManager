---
source_id: SRC-20260906-think-cp2-v8-hard-stop-01
title: "CP2 v8 单次获取的 active dynamic_paths 硬停止"
source_url_or_path: "/Users/orderly_ray/Leader/orchestration/reports/CP2-ASR-NARROW-SOURCE-ACQUISITION-V8-001-acceptance.json"
publisher_or_author: "Leader orchestration；think first-party repository"
published_or_event_date: 2026-09-06
accessed_date: 2026-09-06
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "Leader 接受提交 393640b8 所记录的唯一 v8 获取尝试及其正确停止，不接受源码。该 run 只取得 LICENSE 与 online-recognizer.h，共 19,297 decoded bytes；头文件有 5 个 definite active dynamic_paths 命中和 4 个 comment，活动命中独立触发 denylist_capability，完整 comment 集合 4≠授权 2 又触发 manual_complete_matching。成功 adjudication 为 0、pending 未清、fixed_point=false、source_verdict=insufficient_evidence，run 永久结束。"
quoted_or_referenced_location: "任务合同 SHA-256 fb4fa094c656fe870e30e321aef7cf28fe9bedffb8c878a222c7ddc7dfb7c192；acceptance SHA-256 1613473a2c951b66dbc8605df1ee02e2f398ca530502f6e2365ef036f41eb8d3；REPORT/source-review/request-ledger/scanner-summary/semantic-review SHA-256 ec8978ef16f7162c59688503a2ea303708b7eeb22a53d3668482b1c6365085ab / 6bf0cbd564e4232d9a1c6114292d7d2e45c71b9da545578dbdf4565bf04e3fef / d19f8c8e012ff54821e625fe756cd18d054c4a6009c12cb9c3f24c6a57cf510f / 0e6fba99685377c6a5bf1eafefc8d1d435a20d48423f044cf7defe4ea880c2aa / 0b48e3c0f8d48e2ecef56e24fdbbf6f7aadea9a197b9c7db91d894c79ef1a4e2；用户批准 694c69bc465663cb2a8ba58e21c9757d131d6135956a92df00ed78f997979c81，绑定请求 JSON 2114259dc42837e96d938c65bce2b165ee47836623408c4377ffb8d11d5a392b"
supersedes: null
---

# 来源边界

本卡只编译合同指定的第一方派生报告、产品仓库治理／PRD 文档及已批准请求的权限条款。没有读取本次或历史 raw/private body、envelope、metadata、scanner context，也没有运行 reviewer、scanner、controller 或 transport。

# 可用于产品决定的事实

- 唯一 run 只请求固定 `LICENSE`（11,358 bytes）与 `online-recognizer.h`（7,939 bytes），共 19,297 decoded bytes；停止后无 successor、retry 或 resume。
- 5 个 active `dynamic_paths`：行 15 `[404,411)` 为 directive 内 definite string literal；行 110 `[3577,3590)`、行 143 `[4756,4769)`、行 156 `[5350,5363)` 与 `[5364,5377)` 为 definite code。
- 4 个 comment：原行 57／60 `websocket` 与新增行 64 `[2139,2146)`、行 132 `[4297,4310)` `dynamic_paths`。原授权只覆盖 2 个，故完整集合拒绝；即使未来补齐 comment，5 个 active 硬停止仍独立存在。
- 模式／identifier 命中不等于恶意、实际运行能力或可达性，但冻结规则当前必须 fail closed；不能从“可能误报”直接生成 clearance。
- 扫描原 verdict 保持 `manual_review`／32／4 medium；四项均被派生报告解释为保存的 SHA256 字符串内 `8086` 子串，但解释不把原 verdict 改成 PASS。
- 用户批准的一次获取请求 JSON 明确允许“新 retained bounded evidence 在固定门禁下独立静态审查”；一次性限制针对 acquisition attempt，当前 run 已永久消费，不能再获取或续跑。

# 限制

派生证据不能确定 5 个 active 命中的同文件局部语义、数据流用途或调用可达性，也不能替代对新增 comment 的精确语义审查。下一步若进行，只能由 Leader 在既有 post-acquisition review 权限内审查同一 retained object；产品经理不得自行读取。
