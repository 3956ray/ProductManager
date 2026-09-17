---
source_id: "SRC-20260916-gym-mock-decision-01"
title: "用户决定使用自有动态mock后端及指挥者增量合同"
source_url_or_path: "codex://threads/01a0a64a-8f38-7503-a202-29ed08322b14"
publisher_or_author: "用户；指定指挥者转达"
published_or_event_date: "2026-09-16"
accessed_date: "2026-09-16"
source_class: "D"
source_type: "internal"
projects: ["gym-occupancy"]
storage_permission: "user-owned"
access_status: "verified"
summary: "用户要求自有后端驱动动态模拟、持久存储及未来数据适配；馆方真实后端不再是演示MVP前置。"
quoted_or_referenced_location: "本任务收到的codex_delegation；GYM-MOCK-BACKEND-DECISION-001 current-task.json"
supersedes: null
---

# 自有动态演示后端授权

Owner: Product Lead
Last updated: 2026-09-16
Source: 本任务用户提供的指挥者委派原文；[任务合同](/Users/orderly_ray/Leader/projects/gym-miniapp/orchestration/current-task.json)
Confidence: High（授权与约束）；不代表真实使用验证
Related decisions: GYM-MOCK-BACKEND-DECISION-001；GYM-MVP-PRD-001
Next review date: 2026-09-30

转达的用户原话：

> 真实后端是没有的…只能自己mock这个数据动态的过程…知道数据怎么存储…设计成可扩展的…随时接入他们数据库…有自己的后端进行mock

指挥者要求：基于既有实现形成正式版本化补充决定、PRD/AC/Checkpoint增量；演示身份与官方身份分开；mock不解决域名校验；需要用户确认的工具安全开关单列；报告路径/hash后停止，不派dev。

此来源确认需求与本地方案编制授权，不证明馆方数据库结构、网络可用性或商业需求。current-task会变化，读取时hash保存在本次交付清单；本摘录不覆盖旧批准记录。
