# MVP开发准备：证据卡与假设清单

Owner: Product Lead
Last updated: 2026-09-16
Source: 下列微信官方网页、已登记馆务产品与用户原始记录；[任务合同](../../raw/SRC-20260916-gym-mvp-task-01.md)
Confidence: High（官方平台规则）；Medium（推断）；Hypothesis（本店效果）
Related decisions: [MVP开发准备研究](mvp-readiness-research-2026-09-16.md)
Next review date: 2026-09-30

Research Quality: 90/100 · pass（独立只读文档与已取得官方原文复核；未联网重检或运行）
Validation Level: V0（本店）

微信7页属于同一官方证据线；Gymdesk、Gym Group用户评论、本店用户陈述分别独立。新官方网页直接取得，复用材料保留原访问日期，不将模型输出或搜索片段当原始证据。技术文档A类仅支持平台规则，不能验证MVP使用效果。任务范围来源与产品事实来源分开。

## M-01 · 小程序登录

[SRC记录](../../raw/SRC-20260916-gym-wechat-01.md)

```yaml
evidence_id: "M-01"
source_id: "SRC-20260916-gym-wechat-01"
claim: "wx.login取得临时code后由开发者服务端调用code2Session换身份，服务端据此生成业务登录态；code只能使用一次，session_key不应下发。"
label: "Fact"
source_title: "小程序登录"
source_url: "https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/login.html"
source_class: "A"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
scope: "微信小程序官方公开文档；实际项目账号能力未测试"
support: "full"
independence_group: "wechat-official"
limitations: "官方登录只能建立微信身份；不能由此证明本店会员资格。"
decision_relevance: "决定登录/隐私/网络/开发与发布边界；不支持本店运营效果"
confidence: "High"
```

## M-02 · 小程序登录凭证校验 code2Session

[SRC记录](../../raw/SRC-20260916-gym-wechat-02.md)

```yaml
evidence_id: "M-02"
source_id: "SRC-20260916-gym-wechat-02"
claim: "code2Session须在服务端调用，使用appid、secret、js_code等参数；返回openid、session_key、条件式unionid及错误状态。"
label: "Fact"
source_title: "小程序登录凭证校验 code2Session"
source_url: "https://developers.weixin.qq.com/miniprogram/dev/server/API/user-login/api_code2session"
source_class: "A"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
scope: "微信小程序官方公开文档；实际项目账号能力未测试"
support: "full"
independence_group: "wechat-official"
limitations: "接口支持事实不等于本项目已有AppID/AppSecret、服务器或账号能力。"
decision_relevance: "决定登录/隐私/网络/开发与发布边界；不支持本店运营效果"
confidence: "High"
```

## M-03 · 手机号快速验证组件

[SRC记录](../../raw/SRC-20260916-gym-wechat-03.md)

```yaml
evidence_id: "M-03"
source_id: "SRC-20260916-gym-wechat-03"
claim: "手机号快速验证须用户同意，面向符合资格且完成认证的非个人主体；不保证实时验证。手机号code与wx.login code不同，用户点击授权后由后台换号。"
label: "Fact"
source_title: "手机号快速验证组件"
source_url: "https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/getPhoneNumber.html"
source_class: "A"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
scope: "微信小程序官方公开文档；实际项目账号能力未测试"
support: "full"
independence_group: "wechat-official"
limitations: "文档还说明付费和境外主体限制；本轮不做费用预算或资格判断，不使用该能力作首版必要依赖。"
decision_relevance: "决定登录/隐私/网络/开发与发布边界；不支持本店运营效果"
confidence: "High"
```

## M-04 · 小程序隐私协议开发指南

[SRC记录](../../raw/SRC-20260916-gym-wechat-04.md)

```yaml
evidence_id: "M-04"
source_id: "SRC-20260916-gym-wechat-04"
claim: "隐私指引中声明的信息才可使用对应隐私接口/组件，还需同步用户同意；提供getPrivacySetting、openPrivacyContract、同意按钮及拒绝处理，相关API有基础库版本条件。"
label: "Fact"
source_title: "小程序隐私协议开发指南"
source_url: "https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/PrivacyAuthorize.html"
source_class: "A"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
scope: "微信小程序官方公开文档；实际项目账号能力未测试"
support: "full"
independence_group: "wechat-official"
limitations: "同意隐私指引不证明会员身份；平台接口授权不覆盖全部后端业务身份或数据处理安排。页面保留2023历史更新，采用后续更新口径，不沿用早期过渡开关。"
decision_relevance: "决定登录/隐私/网络/开发与发布边界；不支持本店运营效果"
confidence: "High"
```

## M-05 · 用户隐私保护指引填写说明

[SRC记录](../../raw/SRC-20260916-gym-wechat-05.md)

```yaml
evidence_id: "M-05"
source_id: "SRC-20260916-gym-wechat-05"
claim: "涉及处理用户个人信息的开发者需补充隐私保护指引；现网与提审版本的配置入口及生效规则有区别，审核/发布时需与实际接口使用一致。"
label: "Fact"
source_title: "用户隐私保护指引填写说明"
source_url: "https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/"
source_class: "A"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
scope: "微信小程序官方公开文档；实际项目账号能力未测试"
support: "full"
independence_group: "wechat-official"
limitations: "这是平台配置规则，不是对本项目作出法律合规或审核通过判断。"
decision_relevance: "决定登录/隐私/网络/开发与发布边界；不支持本店运营效果"
confidence: "High"
```

## M-06 · 网络

[SRC记录](../../raw/SRC-20260916-gym-wechat-06.md)

```yaml
evidence_id: "M-06"
source_id: "SRC-20260916-gym-wechat-06"
claim: "自建网络请求需事先配置通讯域名及有效HTTPS/WSS，AppSecret留后台；微信云托管特定调用有域名配置例外。后台请求受限；网络success不代表HTTP业务成功；跳过域名校验的调试结果不能代替正常客户端测试。"
label: "Fact"
source_title: "网络"
source_url: "https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html"
source_class: "A"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
scope: "微信小程序官方公开文档；实际项目账号能力未测试"
support: "full"
independence_group: "wechat-official"
limitations: "仅引用与方案相关规则；未核查具体账号、域名备案、证书或云资源，未开展真机测试。"
decision_relevance: "决定登录/隐私/网络/开发与发布边界；不支持本店运营效果"
confidence: "High"
```

## M-07 · 小程序协同工作和发布

[SRC记录](../../raw/SRC-20260916-gym-wechat-07.md)

```yaml
evidence_id: "M-07"
source_id: "SRC-20260916-gym-wechat-07"
claim: "微信区分项目成员与体验成员及开发/体验/审核/线上版本；预览会上传代码至微信服务器，审核通过后仍需发布操作。"
label: "Fact"
source_title: "小程序协同工作和发布"
source_url: "https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/release.html"
source_class: "A"
published_or_event_date: "unknown"
accessed_date: "2026-09-16"
scope: "微信小程序官方公开文档；实际项目账号能力未测试"
support: "full"
independence_group: "wechat-official"
limitations: "本轮只读文档，未执行预览上传审核发布；项目本身的主体、类目和备案要求仍须按实际账号核查。"
decision_relevance: "决定登录/隐私/网络/开发与发布边界；不支持本店运营效果"
confidence: "High"
```

## M-08 · Gymdesk会员门户指南

[原SRC记录](../../raw/SRC-20260910-gym-reference-13.md)

```yaml
evidence_id: "M-08"
source_id: "SRC-20260910-gym-reference-13"
claim: "Gymdesk公开会员门户包含会员资料、套餐、课表／预约、到店记录和联系馆方。"
label: "Fact"
source_title: "Gymdesk会员门户指南"
source_url: "https://docs.gymdesk.com/en/help/docs/member-portal-guide"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "复用已登记证据，本轮只核对本地原始记录"
support: "full"
independence_group: "gymdesk"
limitations: "官方产品能力声明，访问日期为2026-09-10，本轮复用；不验证本店需求或门店数据。"
decision_relevance: "确定会员/课表服务及可信度优先事项；不证明本店实际效果"
confidence: "High"
```

## M-09 · The Gym Group公开用户评论

[原SRC记录](../../raw/SRC-20260910-gym-reference-09.md)

```yaml
evidence_id: "M-09"
source_id: "SRC-20260910-gym-reference-09"
claim: "2026-06-18一条评论认为人数和课程还好，2022-10-03一条历史评论提到开门/人数更新异常。"
label: "Fact"
source_title: "The Gym Group公开用户评论"
source_url: "https://play.google.com/store/apps/details?id=com.netpulse.mobile.thegymgroup&hl=en_GB&gl=US"
source_class: "D"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "复用已登记证据，本轮只核对本地原始记录"
support: "full"
independence_group: "gymgroup-public-users"
limitations: "两个自选择评论n=2，分别为孤立体验；旧评论不证明当前故障，不估算频率。本轮复用9月10日记录，不冒充9月16日重读。"
decision_relevance: "确定会员/课表服务及可信度优先事项；不证明本店实际效果"
confidence: "Medium"
```

## M-10 · 用户确认单店与会员入口

[原SRC记录](../../raw/SRC-20260909-gym-single-store-01.md)

```yaml
evidence_id: "M-10"
source_id: "SRC-20260909-gym-single-store-01"
claim: "用户确定先做好单店、会员入口必需；只进门刷脸，出门有效计数未知。"
label: "Fact"
source_title: "用户确认单店与会员入口"
source_url: "codex://threads/01a08198-b2ec-7b11-9bc3-89ed40433df5"
source_class: "D"
published_or_event_date: "2026-09-09"
accessed_date: "2026-09-09"
scope: "复用已登记证据，本轮只核对本地原始记录"
support: "full"
independence_group: "gym-user-owner"
limitations: "用户方向不等于馆方承诺；V0未改变。"
decision_relevance: "确定会员/课表服务及可信度优先事项；不证明本店实际效果"
confidence: "Medium"
```

## M-11 · 用户确认有瑜伽课表

[原SRC记录](../../raw/SRC-20260910-gym-yoga-schedule-01.md)

```yaml
evidence_id: "M-11"
source_id: "SRC-20260910-gym-yoga-schedule-01"
claim: "用户确认瑜伽室有课程表，未提供具体内容。"
label: "Fact"
source_title: "用户确认有瑜伽课表"
source_url: "codex://threads/01a08198-b2ec-7b11-9bc3-89ed40433df5"
source_class: "D"
published_or_event_date: "2026-09-10"
accessed_date: "2026-09-10"
scope: "复用已登记证据，本轮只核对本地原始记录"
support: "full"
independence_group: "gym-user-owner"
limitations: "无实际课表、更新人、取消规则或现场使用记录。"
decision_relevance: "确定会员/课表服务及可信度优先事项；不证明本店实际效果"
confidence: "Medium"
```

## 推断、假设与验证关系

| ID | 陈述 | 标签 | 支持／局限 | 下一验证 |
| --- | --- | --- | --- | --- |
| H-01 | 无出场事件可先人工发布现场忙闲等级 | Inference | M-09/M-10说明可信度问题与数据缺口；人工观测可独立产生记录是设计推导，非竞品效果证明 | 真实值班更新和独立观察对照 |
| H-02 | 15分钟TTL、10分钟更新、60秒前台刷新足够 | Assumption | 无来源规定这些数值；仅为可测试默认值 | 试点覆盖率、变化速度、误导和维护耗时 |
| H-03 | 微信登录＋前台核验配对可建立会员关联 | Inference | M-01/M-02只证明微信登录能力；线下核验是本方案业务信任来源 | operator核验实际原系统会员，测试错绑/重放/撤销 |
| H-04 | 8位码、10分钟有效、每10分钟5次错误查询为可实施起点 | Assumption | 本轮工程设计参数，非微信标准；仍需随机生成/碰撞检查、会话与操作员权限及限流 | 并发、过期、重放、枚举边界测试 |
| H-05 | 公共课表和个人会员状态提供最小用户价值 | Inference | M-08/M-10/M-11；产品功能存在与需求表述不等于持续使用 | 真实会员查询状态与今日课表的任务观察 |
| H-06 | 7天试点、30次抽查、80%有效覆盖、误导不超过10%可用于下一步判断 | Assumption | 本轮拟定的小样本探索判据，不是统计显著性或行业基准 | 记录分母、覆盖窗口与反例，不宣传普遍效果 |
| H-07 | 观察30天、审计90天等默认保留期 | Assumption | 工程起点，非法律规定或对外承诺 | PRD细化必要字段、删除/备份周期，与实际用途一致 |

## 已尝试渠道与缺口

Firecrawl scrape登录官方页返回额度不足；浏览器首次导航超时；随后curl直读同一官方公开域名及页面所链接的6个官方文档，取得中文正文并核对。没有绕过登录、验证码或访问限制，没有使用或请求凭证。未开展额外泛竞品搜索。

未取得：真实门禁/API、馆方操作员/合作、会员记录、实际课表、真实AppID主体及平台账号资格、服务器/域名/云资源、真机或试点结果。缺口按主报告分阶段限制，不用合成数据替代。
