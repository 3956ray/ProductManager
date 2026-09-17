---
source_id: "SRC-20260916-gym-backend-code-01"
title: "gym-miniapp f22664d代码与CP5原生工具网络证据"
source_url_or_path: "/Users/orderly_ray/Projects/gym-miniapp/server/http.mjs"
publisher_or_author: "gym-miniapp工程仓库"
published_or_event_date: "2026-09-16"
accessed_date: "2026-09-16"
source_class: "B"
source_type: "repository"
projects: ["gym-occupancy"]
storage_permission: "user-owned"
access_status: "verified"
summary: "已有Node/SQLite领域服务及HTTP接口；test身份依赖fixture，原生客户端仍调用wx.login；loopback请求实际被合法域名校验阻断。"
quoted_or_referenced_location: "f22664d5f5b2320966df53c874eaaf120297be6b：server/*、miniprogram/lib/session.js、reports/cp5/tools-002/06-runtime-domain-error.txt"
supersedes: null
---

# 当前实现证据

Owner: Product Lead
Last updated: 2026-09-16
Source: 本地仓库提交 f22664d5f5b2320966df53c874eaaf120297be6b；[HTTP入口](/Users/orderly_ray/Projects/gym-miniapp/server/http.mjs)；[原生控制台记录](/Users/orderly_ray/Projects/gym-miniapp/reports/cp5/tools-002/06-runtime-domain-error.txt)
Confidence: High（所读源码及错误记录）；端到端效果待验证
Related decisions: GYM-MOCK-BACKEND-DECISION-001
Next review date: 2026-09-30

| Evidence | Fact及支持范围 | 原始位置与限制 |
| --- | --- | --- |
| E-M01 | 自有后端已有观察、会员、删除、课表、角色与会话服务；SQLite持久表已经存在 | server/http.mjs、server/migrations/001–005；代码存在不等于本轮执行通过 |
| E-M02 | test/store配置、身份模式及密钥/目录隔离；服务只监听127.0.0.1 | server/config.mjs；不能直接假定已经支持托管HTTPS test端点 |
| E-M03 | test adapter只接受预置摘要，客户端loginCode仍使用wx.login；没有可操作演示凭证发行流程 | server/wechat.mjs、server/identity.mjs、miniprogram/lib/session.js；测试替身不是微信验证 |
| E-M04 | 模拟器实际报127.0.0.1不在request合法域名列表 | reports/cp5/tools-002/06-runtime-domain-error.txt；错误证据不代表未来更改配置后仍失败或已经成功 |

工程94/94与官方工具编译通过为指挥者和已有开发报告的结果，本轮没有重跑。开发报告仅用于结果定位，源码/迁移和工具原始记录用于核查关键技术事实。无真实馆方数据库或真实身份交换的新证据。
