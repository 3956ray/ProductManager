---
source_id: "SRC-20260916-gym-wechat-06"
title: "网络"
source_url_or_path: "https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html"
publisher_or_author: "微信开放文档／腾讯"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
source_class: "A"
source_type: "official"
projects: ["gym-occupancy"]
storage_permission: "metadata-and-short-excerpt"
access_status: "verified"
summary: "自建网络请求需事先配置通讯域名及有效HTTPS/WSS，AppSecret留后台；微信云托管特定调用有域名配置例外。后台请求受限；网络success不代表HTTP业务成功；跳过域名校验的调试结果不能代替正常客户端测试。"
quoted_or_referenced_location: "服务器域名配置、网络请求/使用限制/回调函数、跳过域名校验"
supersedes: null
---

# 网络（MVP平台证据）

Owner: Product Lead
Last updated: 2026-09-16
Source: https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html
Confidence: High（仅限官方文档规则）
Related decisions: [MVP开发准备研究](../ideas/gym-occupancy/mvp-readiness-research-2026-09-16.md)
Next review date: 2026-09-30

## 最小摘要

自建网络请求需事先配置通讯域名及有效HTTPS/WSS，AppSecret留后台；微信云托管特定调用有域名配置例外。后台请求受限；网络success不代表HTTP业务成功；跳过域名校验的调试结果不能代替正常客户端测试。

原文短摘录：

> 只要成功接收到服务器返回，无论 statusCode 是多少，都会进入 success 回调。

引用位置：服务器域名配置、网络请求/使用限制/回调函数、跳过域名校验。

限制：仅引用与方案相关规则；未核查具体账号、域名备案、证书或云资源，未开展真机测试。

取得方式：直接读取官方公开HTTPS页面；未登录，未使用任何AppSecret或用户资料。临时原始HTML SHA-256: `ec625026ea4737cfff2771769d443ae494dfedb32d1f49443b7f2a9540931a33`。临时读取文件不作为长期来源，原始网页仍是证据出处。
