---
source_id: "SRC-20260916-gym-wechat-02"
title: "小程序登录凭证校验 code2Session"
source_url_or_path: "https://developers.weixin.qq.com/miniprogram/dev/server/API/user-login/api_code2session"
publisher_or_author: "微信开放文档／腾讯"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
source_class: "A"
source_type: "official"
projects: ["gym-occupancy"]
storage_permission: "metadata-and-short-excerpt"
access_status: "verified"
summary: "code2Session须在服务端调用，使用appid、secret、js_code等参数；返回openid、session_key、条件式unionid及错误状态。"
quoted_or_referenced_location: "调用方式、请求/返回参数、错误码"
supersedes: null
---

# 小程序登录凭证校验 code2Session（MVP平台证据）

Owner: Product Lead
Last updated: 2026-09-16
Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-login/api_code2session
Confidence: High（仅限官方文档规则）
Related decisions: [MVP开发准备研究](../ideas/gym-occupancy/mvp-readiness-research-2026-09-16.md)
Next review date: 2026-09-30

## 最小摘要

code2Session须在服务端调用，使用appid、secret、js_code等参数；返回openid、session_key、条件式unionid及错误状态。

原文短摘录：

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用

引用位置：调用方式、请求/返回参数、错误码。

限制：接口支持事实不等于本项目已有AppID/AppSecret、服务器或账号能力。

取得方式：直接读取官方公开HTTPS页面；未登录，未使用任何AppSecret或用户资料。临时原始HTML SHA-256: `25a9f8cd440ac9e96dbcb8f639f6e77d8af9f4e8b274b8d9b9682ac552e93f9b`。临时读取文件不作为长期来源，原始网页仍是证据出处。
