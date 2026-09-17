---
source_id: "SRC-20260917-gym-key-clarification-01"
title: "D2外部键可观测性问题及指挥者批准解释"
source_url_or_path: "codex://threads/01a0a64b-85f8-7790-88d9-fd1188ece566"
publisher_or_author: "指定dev提出；指定指挥者批准"
published_or_event_date: "2026-09-17"
accessed_date: "2026-09-17"
source_class: "D"
source_type: "internal"
projects: ["gym-occupancy"]
storage_permission: "user-owned"
access_status: "verified"
summary: "dev指出当前schema无法区分同键正常改课与实体回收；指挥者批准稳定映射、不做启发式检测的解释，并要求保持冻结文档不变。"
quoted_or_referenced_location: "本任务2026-09-17收到的dev问题及Leader批准两条codex_delegation"
supersedes: null
---

# 外部键解释批准来源

Owner: Product Lead
Last updated: 2026-09-17
Source: dev与[指挥者](codex://threads/01a0a64a-8f38-7503-a202-29ed08322b14)在本任务中的委派原文
Confidence: High（批准与范围）；非产品使用证据
Related decisions: GYM-DEMO-SCENARIOS-001；GYM-MOCK-BACKEND-DECISION-001
Next review date: 2026-09-30

dev原文摘录：“当前schema仅externalId/name/time/status，且允许同externalId改名改期，无法客观区分正常改课与外部把同键给新实体。”

指挥者批准原文：“现有字段确实无法观测实体回收，稳定映射且不做启发式检测符合最小实现。”并要求“明确解释而非扩范围，APPROVED解释”“不得新增字段/回收管理系统”“不得让dev因等待此记录停下其他已授权D2工作”。

本来源登记问题及明确批准，不将PM回复当作独立技术或市场证据。
