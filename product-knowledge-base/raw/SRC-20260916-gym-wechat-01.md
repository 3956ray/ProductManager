---
source_id: "SRC-20260916-gym-wechat-01"
title: "小程序登录"
source_url_or_path: "https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/login.html"
publisher_or_author: "微信开放文档／腾讯"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
source_class: "A"
source_type: "official"
projects: ["gym-occupancy"]
storage_permission: "metadata-and-short-excerpt"
access_status: "verified"
summary: "wx.login取得临时code后由开发者服务端调用code2Session换身份，服务端据此生成业务登录态；code只能使用一次，session_key不应下发。"
quoted_or_referenced_location: "登录流程时序、说明、注意事项"
supersedes: null
---

# 小程序登录（MVP平台证据）

Owner: Product Lead
Last updated: 2026-09-16
Source: https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/login.html
Confidence: High（仅限官方文档规则）
Related decisions: [MVP开发准备研究](../ideas/gym-occupancy/mvp-readiness-research-2026-09-16.md)
Next review date: 2026-09-30

## 最小摘要

wx.login取得临时code后由开发者服务端调用code2Session换身份，服务端据此生成业务登录态；code只能使用一次，session_key不应下发。

原文短摘录：

> 临时登录凭证 code 只能使用一次

引用位置：登录流程时序、说明、注意事项。

限制：官方登录只能建立微信身份；不能由此证明本店会员资格。

取得方式：直接读取官方公开HTTPS页面；未登录，未使用任何AppSecret或用户资料。临时原始HTML SHA-256: `34be791e2c5cec8e4a89046b8646f346f3b7bf939d1bd924dfae5490b7a99d8c`。临时读取文件不作为长期来源，原始网页仍是证据出处。
