---
source_id: SRC-20260906-think-cp2-local-configuration-01
title: "CP2 v8 active dynamic_paths 的局部配置语义审查"
source_url_or_path: "/Users/orderly_ray/Leader/orchestration/reports/CP2-ASR-V8-ACTIVE-DYNAMIC-PATHS-STATIC-REVIEW-001-acceptance.json"
publisher_or_author: "Leader orchestration；think first-party repository"
published_or_event_date: 2026-09-06
accessed_date: 2026-09-06
source_class: B
source_type: internal
projects:
  - personal-thought-archive
storage_permission: user-owned
access_status: verified
summary: "Leader 已验收对同一 retained online-recognizer.h 的七个 occurrence 的局部静态审查，人工可见范围合计 55 行。一个 literal include 在获准查看的目标 directive 局部没有显示运行时操作，但未查看的同文件行与跨文件依赖未审；四个 hotwords_file occurrence 分别是公开配置字段、const-ref 参数与成员初始化，属于局部 policy-relevant 配置面；相邻文档说明 buffer/file 两种输入选择。这 55 行局部证据没有证明实际文件访问、selector 执行、运行时可达性、动态加载或未来业务 API 暴露。两处 comment bytes 仅在获准查看的局部上下文中不操作。原 active hard stop、comment pending、零 clearance 与路线暂停均未改变。"
quoted_or_referenced_location: "任务合同 /Users/orderly_ray/Leader/orchestration/tasks/CP2-ASR-V8-LOCAL-CONFIGURATION-ROUTE-DECISION-001.json，SHA-256 e891474ac5f847afe1dfbf1496e22fdd51a968026dca9f19eafc2f4776779f82；acceptance/review JSON/review MD/verification/semantic review SHA-256 431eb4d30511858cf298faec7da82d74d871fbb54db31d4075da94190925345d / f5d1f99d54084aec6757038f726ae455395e334ac0b120c5f254791c1bcbda8b / a6ec5534ed6b2bcd7b6ae41dd34576f3465ef7df2494c614755a00e809acd39b / 1812e5b8ef3384ebf82f7345c35865e5a7837ad39d84101bae14f8ebd24dcaac / 46d63124da6e24064fcc7c45b7e779c6d779cea151347fa7e06e0fd8623b4c8f"
supersedes: null
---

Owner: Product Lead
Last updated: 2026-09-06
Source: 上述五份第一方派生报告与现行产品决定
Confidence: High（对象身份、局部语法与审查边界已交叉验证）；Low（跨文件实现、实际 I/O 与业务可达性未取得证据）
Related decisions: ../ideas/personal-thought-archive/cp2-v8-hard-stop-next-step-decision-2026-09-06.md；../ideas/personal-thought-archive/cp2-v8-local-configuration-route-decision-2026-09-06.md
Next review date: 2026-09-13

# 来源边界

本卡只编译合同固定的第一方派生材料。产品经理没有读取 raw/private body、envelope、metadata、analysis archive 或 scanner context，没有运行脚本、候选、scanner、controller、第三方内容或网络，也没有修改 `think` 产品仓库。

# 可用于产品决定的事实

- 审查对象仍是固定 upstream commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`、tree `fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0` 下的 `sherpa-onnx/csrc/online-recognizer.h`，Git blob `a4559f413cae739f055509a01d5684879e4a626c`，body SHA-256 `382e6bcc6e26079419c0a0f972d89b6c48de5d9ecda49ceca592bd0786482836`，7,939 bytes。
- 行 15 的 `decoder` token 位于固定 include `online-ctc-fst-decoder-config.h`。本次获准查看的目标 directive 及其最小局部上下文中，没有看到运行时路径拼接、文件读取或动态加载；未查看的同文件行、被 include 类型及其跨文件下游行为均未审，不作断言。
- 行 110 的 `hotwords_file` 是 `OnlineRecognizerConfig` 上公开的 `std::string` 成员，是可由调用方提供的文件名配置槽。
- 行 143 的同名 token 是构造器 `const std::string &` 参数；行 156 两处 token 是成员初始化的目标与来源。若构造器被调用，值会在该局部数据流中被复制并保存；在本次获准查看的构造函数声明、成员初始化与空函数体中，没有看到实际文件读取调用。未查看的同文件行与跨文件实现均不作断言。
- 相邻文档说明 `hotwords_buf` 可用于 buffered input，并与 file-based loading 对比。该说明支持“存在 buffer/file 配置选择”的局部政策相关性，不证明 selector 在何处或是否执行。
- 行 64 与 132 的 comment bytes 在本文件局部不操作；其语义不能转移为字段、实现、依赖或运行时 clearance。
- 本轮输出是 `active_paths_review_complete_for_product_decision`，不是安全、不可达、无害或可采用结论。

# 产品解释

必须分开三层：上游配置表面、构建／运行实际需要的能力、未来 `think` 业务边界可达的能力。当前证据只触达第一层。`hotwords_file` 对个性词表需求有信息价值，但文件路径并不是达成该需求的唯一产品方案；优先验证能否只走 `hotwords_buf`／内存边界，符合既有窄 handle 架构。

# 限制

本次人工可见范围合计 55 行。没有证据证明或排除未查看的同文件行及跨文件实现中的实际文件打开、路径解析、selector 执行、动态加载、实现调用可达性、默认值传播、业务适配器是否能封死文件路径，也没有审查 `online-ctc-fst-decoder-config.h`。原 denylist hard stop、comment complete-set rejection、成功 adjudication 为 0、`fixed_point=false` 与 `source_verdict=insufficient_evidence` 全部不变。
