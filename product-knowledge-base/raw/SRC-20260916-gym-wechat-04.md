---
source_id: "SRC-20260916-gym-wechat-04"
title: "小程序隐私协议开发指南"
source_url_or_path: "https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/PrivacyAuthorize.html"
publisher_or_author: "微信开放文档／腾讯"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
source_class: "A"
source_type: "official"
projects: ["gym-occupancy"]
storage_permission: "metadata-and-short-excerpt"
access_status: "verified"
summary: "隐私指引中声明的信息才可使用对应隐私接口/组件，还需同步用户同意；提供getPrivacySetting、openPrivacyContract、同意按钮及拒绝处理，相关API有基础库版本条件。"
quoted_or_referenced_location: "接入流程1/2/3、常见错误、官方隐私弹窗功能说明"
supersedes: null
---

# 小程序隐私协议开发指南（MVP平台证据）

Owner: Product Lead
Last updated: 2026-09-16
Source: https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/PrivacyAuthorize.html
Confidence: High（仅限官方文档规则）
Related decisions: [MVP开发准备研究](../ideas/gym-occupancy/mvp-readiness-research-2026-09-16.md)
Next review date: 2026-09-30

## 最小摘要

隐私指引中声明的信息才可使用对应隐私接口/组件，还需同步用户同意；提供getPrivacySetting、openPrivacyContract、同意按钮及拒绝处理，相关API有基础库版本条件。

原文短摘录：

> 若未声明，对应接口或组件将直接禁用。

引用位置：接入流程1/2/3、常见错误、官方隐私弹窗功能说明。

限制：同意隐私指引不证明会员身份；平台接口授权不覆盖全部后端业务身份或数据处理安排。页面保留2023历史更新，采用后续更新口径，不沿用早期过渡开关。

取得方式：直接读取官方公开HTTPS页面；未登录，未使用任何AppSecret或用户资料。临时原始HTML SHA-256: `a8bba8b74940189125b1eda3f0325e117bf06e8beae97cc96a6dc6efce7e9363`。临时读取文件不作为长期来源，原始网页仍是证据出处。
