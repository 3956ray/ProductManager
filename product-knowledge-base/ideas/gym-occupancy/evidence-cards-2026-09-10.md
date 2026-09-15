# 健身房产品参考：来源与证据卡

Owner: Product Lead
Last updated: 2026-09-10
Source: 下列原始网页与对应SRC登记；非模型输出证据
Confidence: Medium
Related decisions: [单店研究建议](product-feature-ui-research-2026-09-10.md)；新增功能待验证
Next review date: 2026-10-10

Research Quality: 89/100（文档与登记证据映射复核；详见报告）
Validation Level: V0（本店）

所有网页于2026-09-10打开核查。官网功能属于厂商声明；界面取舍是本轮推断。来源只保留元数据、最小摘要及引用位置；同一产品官网与仓库不算独立需求证据。

## E-001 · 2024 winners and finalists — Apple Design Awards

[SRC登记](../../raw/SRC-20260910-gym-reference-01.md)

```yaml
evidence_id: "E-001"
source_id: "SRC-20260910-gym-reference-01"
claim: "Gentler Streak为2024 Apple Design Awards Social Impact类获奖应用；Apple评价其健康数据组织、温和设计及月度总结。"
label: "Fact"
source_title: "2024 winners and finalists — Apple Design Awards"
source_url: "https://developer.apple.com/design/awards/2024/"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "2024官方获奖身份及评审描述；非黑客松、非当前版本实测"
support: "full"
independence_group: "apple-awards"
limitations: "2024官方获奖身份及评审描述；非黑客松、非当前版本实测"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：官方奖项文字核验；产品官网截图另见gentler来源。

## E-002 · Celebrating innovation: Gemini API Developer Competition

[SRC登记](../../raw/SRC-20260910-gym-reference-02.md)

```yaml
evidence_id: "E-002"
source_id: "SRC-20260910-gym-reference-02"
claim: "AlphaFit被列入2024 Gemini API竞赛Honorable Mentions；Google描述其新手个性化训练、随进度调整难度、动作提示及休息时文字游戏。"
label: "Fact"
source_title: "Celebrating innovation: Gemini API Developer Competition"
source_url: "https://developers.googleblog.com/celebrating-innovation-gemini-api-developer-competition/"
source_class: "B"
published_or_event_date: "2024-12-19"
accessed_date: "2026-09-10"
scope: "官方特别提及，不是总冠军；未验证当前维护或训练建议效果"
support: "full"
independence_group: "google-competition"
limitations: "官方特别提及，不是总冠军；未验证当前维护或训练建议效果"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：未核验应用UI；只有文字描述。

## E-003 · 抖音AI创变者计划

[SRC登记](../../raw/SRC-20260910-gym-reference-03.md)

```yaml
evidence_id: "E-003"
source_id: "SRC-20260910-gym-reference-03"
claim: "2026赛事官网列出互动空间、内容重构、个性化瞬间和视觉搜索等赛道；历史项目展示Root Journey等，本轮页面未发现可直接核验的健身房UI作品。"
label: "Fact"
source_title: "抖音AI创变者计划"
source_url: "https://aiia.douyin.com/"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "赛事存在与本轮公开页面覆盖；不表示全部赛事没有健身作品"
support: "full"
independence_group: "douyin-aiia"
limitations: "赛事存在与本轮公开页面覆盖；不表示全部赛事没有健身作品"
decision_relevance: "说明本轮检索覆盖与缺口，不推断全部作品"
confidence: "High"
```

界面观察：赛事官网，非产品UI。

## E-004 · 看完小红书黑客松的59个热血团队，我们想推荐这6个

[SRC登记](../../raw/SRC-20260910-gym-reference-04.md)

```yaml
evidence_id: "E-004"
source_id: "SRC-20260910-gym-reference-04"
claim: "作者介绍2026小红书黑客松参赛项目Attune等，明确其推荐项目并非全部获奖；Attune尝试按注意力呈现操作并隐藏干扰。"
label: "Fact"
source_title: "看完小红书黑客松的59个热血团队，我们想推荐这6个"
source_url: "https://www.pingwest.com/a/312851"
source_class: "C"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "现场评审报道；非官方获奖名单，非健身产品；未核验可用演示"
support: "full"
independence_group: "pingwest-red-hackathon"
limitations: "现场评审报道；非官方获奖名单，非健身产品；未核验可用演示"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "Medium"
```

界面观察：交互想法参考，不做UI质量排名。

## E-005 · wger-project/wger

[SRC登记](../../raw/SRC-20260910-gym-reference-05.md)

```yaml
evidence_id: "E-005"
source_id: "SRC-20260910-gym-reference-05"
claim: "README列出训练计划、进阶规则、饮食体重跟踪、动作Wiki、跨端、多用户基本馆务与REST API；代码AGPL-3.0-or-later，动作／食材条目各自CC许可，文档CC-BY-SA-4.0。"
label: "Fact"
source_title: "wger-project/wger"
source_url: "https://github.com/wger-project/wger"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "README声明；未运行／安全审计；代码与数据许可分开"
support: "full"
independence_group: "wger"
limitations: "README声明；未运行／安全审计；代码与数据许可分开"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：未查看运行界面；不评UI。

## E-006 · “开发者是AI时代的创作者”，小红书上独立开发者超5万

[SRC登记](../../raw/SRC-20260910-gym-reference-06.md)

```yaml
evidence_id: "E-006"
source_id: "SRC-20260910-gym-reference-06"
claim: "报道明确Peak Watch获2025小红书首届独立开发大赛宝藏APP奖项，并介绍其与Stress Watch团队关系。"
label: "Fact"
source_title: "“开发者是AI时代的创作者”，小红书上独立开发者超5万"
source_url: "https://jingji.cctv.com/2025/04/16/ARTIr4i1g313IU5WEySTYyMe250416.shtml"
source_class: "C"
published_or_event_date: "2025-04-16"
accessed_date: "2026-09-10"
scope: "媒体获奖报道，未取得主办方完整原始名单；不引用报道用户规模做需求证明"
support: "full"
independence_group: "red-contest-report"
limitations: "媒体获奖报道，未取得主办方完整原始名单；不引用报道用户规模做需求证明"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "Medium"
```

界面观察：不适用。

## E-007 · PeakWatch — Train Smarter, Recover Faster

[SRC登记](../../raw/SRC-20260910-gym-reference-07.md)

```yaml
evidence_id: "E-007"
source_id: "SRC-20260910-gym-reference-07"
claim: "官网列出恢复与训练负荷、压力与身体电量、睡眠、自定义训练、饮食记录、生活日志、Apple Watch与iOS小组件。"
label: "Fact"
source_title: "PeakWatch — Train Smarter, Recover Faster"
source_url: "https://www.peakwatch.co/"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "官网功能声明；恢复与营养效果未核验，不建议迁移健康判断到本项目"
support: "full"
independence_group: "peakwatch"
limitations: "官网功能声明；恢复与营养效果未核验，不建议迁移健康判断到本项目"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：已查看官网手机展示；深色数字、状态词和迷你图表卡片。

## E-008 · Gentler Streak: Workout Tracker That Puts Well-being First

[SRC登记](../../raw/SRC-20260910-gym-reference-08.md)

```yaml
evidence_id: "E-008"
source_id: "SRC-20260910-gym-reference-08"
claim: "官网展示Activity Path、每日训练／休息建议、Apple Watch记录、健康与睡眠数据、周月年总结；可切换休息、生病、受伤状态。"
label: "Fact"
source_title: "Gentler Streak: Workout Tracker That Puts Well-being First"
source_url: "https://gentlerstories.com/gentlerstreak"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "官网描述及截图，不验证健康效果；部分图片alt疑似混入The Outsiders，视觉判断以实际图像为准"
support: "full"
independence_group: "gentler"
limitations: "官网描述及截图，不验证健康效果；部分图片alt疑似混入The Outsiders，视觉判断以实际图像为准"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：已看首屏手机界面：先给一句状态解释，后给路径图和活动列表；橙绿点缀白底。

## E-009 · The Gym Group — Google Play

[SRC登记](../../raw/SRC-20260910-gym-reference-09.md)

```yaml
evidence_id: "E-009"
source_id: "SRC-20260910-gym-reference-09"
claim: "官方详情列出二维码入馆、实时人数及容量百分比、课程预约管理、训练库与动作视频、会员管理和可选Health Connect。"
label: "Fact"
source_title: "The Gym Group — Google Play"
source_url: "https://play.google.com/store/apps/details?id=com.netpulse.mobile.thegymgroup&hl=en_GB&gl=US"
source_class: "B"
published_or_event_date: "2026-09-07"
accessed_date: "2026-09-10"
scope: "官方功能与用户评论必须分开：官方B类；评论D类、两个自选择样本，2022旧评论不说明当前缺陷。Android英文页，更新2026-09-07，版本7.8.1；未登录实测。"
support: "full"
independence_group: "gymgroup-official"
limitations: "官方功能与用户评论必须分开：官方B类；评论D类、两个自选择样本，2022旧评论不说明当前缺陷。Android英文页，更新2026-09-07，版本7.8.1；未登录实测。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：仅文字核验，不做截图UI排名。

## E-010 · Download the free PureGym App

[SRC登记](../../raw/SRC-20260910-gym-reference-10.md)

```yaml
evidence_id: "E-010"
source_id: "SRC-20260910-gym-reference-10"
claim: "官方页面列出非接触入馆、课程预约、点播训练、实时到场人数、个性化训练计划与会员管理；官方展示人数加分时柱图。"
label: "Fact"
source_title: "Download the free PureGym App"
source_url: "https://www.puregym.com/app/"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "英国官网公开功能与截图；未登录会员端，精度未知"
support: "full"
independence_group: "puregym"
limitations: "英国官网公开功能与截图；未登录会员端，精度未知"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：2026-09-09已查看人数卡片；本轮重新核查官方页面。

## E-011 · Strong — Workout Tracker & Gym Log

[SRC登记](../../raw/SRC-20260910-gym-reference-11.md)

```yaml
evidence_id: "E-011"
source_id: "SRC-20260910-gym-reference-11"
claim: "官方列出训练记录、自定义动作、超级组、休息计时、RPE、进步图、CSV导出、Apple Health及Apple Watch。"
label: "Fact"
source_title: "Strong — Workout Tracker & Gym Log"
source_url: "https://www.strong.app/"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "官网功能声明；观察官方演示，不是安装实测，不引用注册量或评分证明需求。"
support: "full"
independence_group: "strong"
limitations: "官网功能声明；观察官方演示，不是安装实测，不引用注册量或评分证明需求。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：已观察官网训练记录演示；白底、对齐数字、蓝色主操作与轻列表。

## E-012 · Hevy — Workout Tracker & Planner Gym App

[SRC登记](../../raw/SRC-20260910-gym-reference-12.md)

```yaml
evidence_id: "E-012"
source_id: "SRC-20260910-gym-reference-12"
claim: "官网列出训练日志、计划、计时、笔记、进步图、动作视频、PR和历史，以及关注、点赞、评论与保存他人训练；支持Watch/WearOS。"
label: "Fact"
source_title: "Hevy — Workout Tracker & Planner Gym App"
source_url: "https://www.hevyapp.com/"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "公开功能与界面展示；未登录实测；功能齐全不代表适合本项目。"
support: "full"
independence_group: "hevy"
limitations: "公开功能与界面展示；未登录实测；功能齐全不代表适合本项目。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：已观察官方截图；蓝色操作、绿色完成标记、表格数字对齐。

## E-013 · Member Portal Guide

[SRC登记](../../raw/SRC-20260910-gym-reference-13.md)

```yaml
evidence_id: "E-013"
source_id: "SRC-20260910-gym-reference-13"
claim: "官方会员门户指南涵盖会员资料／条码、预约、签到、30天到店图、会员套餐、付款、按教练与项目筛课、历史和联系馆方。"
label: "Fact"
source_title: "Member Portal Guide"
source_url: "https://docs.gymdesk.com/en/help/docs/member-portal-guide"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "不同馆方配置可不同；未进入真实会员账号，不评UI优劣。"
support: "full"
independence_group: "gymdesk"
limitations: "不同馆方配置可不同；未进入真实会员账号，不评UI优劣。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：仅核查文档流程；不列为已实测优秀UI。

## E-014 · Workout.lol

[SRC登记](../../raw/SRC-20260910-gym-reference-14.md)

```yaml
evidence_id: "E-014"
source_id: "SRC-20260910-gym-reference-14"
claim: "公开网页提供Equipment→Muscles→Exercises三步流程，本轮实际选择Dumbbell并进入肌肉选择页面。"
label: "Fact"
source_title: "Workout.lol"
source_url: "https://workout.lol/"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "仅操作前两步；没有完成动作生成、账户、持久化或移动端测试。"
support: "full"
independence_group: "workout-lol"
limitations: "仅操作前两步；没有完成动作生成、账户、持久化或移动端测试。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：实际网页操作；分步任务、留白、人体图；肌肉图仍需文字选项辅助。

## E-015 · workout-lol/workout-lol

[SRC登记](../../raw/SRC-20260910-gym-reference-15.md)

```yaml
evidence_id: "E-015"
source_id: "SRC-20260910-gym-reference-15"
claim: "README描述依可用器械与目标肌肉生成训练，支持自托管；仓库页面显示最近提交2024-09-27。"
label: "Fact"
source_title: "workout-lol/workout-lol"
source_url: "https://github.com/workout-lol/workout-lol"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "从Vincenius/workout-lol自动跳转规范仓库；时区tooltip显示次日，不评价活跃维护；未运行或审计。"
support: "full"
independence_group: "workout-lol"
limitations: "从Vincenius/workout-lol自动跳转规范仓库；时区tooltip显示次日，不评价活跃维护；未运行或审计。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：界面体验见官网来源。

## E-016 · aree6/LiftShift

[SRC登记](../../raw/SRC-20260910-gym-reference-16.md)

```yaml
evidence_id: "E-016"
source_id: "SRC-20260910-gym-reference-16"
claim: "README描述浏览器内导入Hevy／Strong等训练数据进行热图、PR、平台期、日期与一致性分析；页面最新提交2026-09-08，release v1.5.0日期2026-09-05。"
label: "Fact"
source_title: "aree6/LiftShift"
source_url: "https://github.com/aree6/LiftShift"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "README为作者能力声明，未验证浏览器本地处理及安全性；官网未成功访问。README另有归属要求表述，完整复用条件需结合文件复核。"
support: "full"
independence_group: "liftshift"
limitations: "README为作者能力声明，未验证浏览器本地处理及安全性；官网未成功访问。README另有归属要求表述，完整复用条件需结合文件复核。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：已看README截图；深色多图表，统计页参考。

## E-017 · Commits · wger-project/wger · master

[SRC登记](../../raw/SRC-20260910-gym-reference-17.md)

```yaml
evidence_id: "E-017"
source_id: "SRC-20260910-gym-reference-17"
claim: "截至访问日提交列表顶部为2026-09-06，提交83005f7d487c814833f3943784370bb0149fbaa8。"
label: "Fact"
source_title: "Commits · wger-project/wger · master"
source_url: "https://github.com/wger-project/wger/commits/master/"
source_class: "B"
published_or_event_date: "2026-09-06"
accessed_date: "2026-09-10"
scope: "提交日期仅为维护信号，不证明稳定、已发布或适合本项目。"
support: "full"
independence_group: "wger"
limitations: "提交日期仅为维护信号，不证明稳定、已发布或适合本项目。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：不适用。

## E-018 · wger LICENSE.txt

[SRC登记](../../raw/SRC-20260910-gym-reference-18.md)

```yaml
evidence_id: "E-018"
source_id: "SRC-20260910-gym-reference-18"
claim: "许可证文件是GNU Affero General Public License Version 3；项目README声明AGPL-3.0-or-later。"
label: "Fact"
source_title: "wger LICENSE.txt"
source_url: "https://github.com/wger-project/wger/blob/master/LICENSE.txt"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "仅登记可见许可文本与项目声明，不对商业使用作法律裁定；数据及文档许可单独列于README。"
support: "full"
independence_group: "wger"
limitations: "仅登记可见许可文本与项目声明，不对商业使用作法律裁定；数据及文档许可单独列于README。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：不适用。

## E-019 · Workout.lol LICENSE

[SRC登记](../../raw/SRC-20260910-gym-reference-19.md)

```yaml
evidence_id: "E-019"
source_id: "SRC-20260910-gym-reference-19"
claim: "LICENSE为MIT，Copyright (c) 2023 Vincent Will，并要求保留版权与许可声明。"
label: "Fact"
source_title: "Workout.lol LICENSE"
source_url: "https://github.com/workout-lol/workout-lol/blob/main/LICENSE"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "仅针对此代码许可文件；未核验动作数据、视频及第三方素材的许可。"
support: "full"
independence_group: "workout-lol"
limitations: "仅针对此代码许可文件；未核验动作数据、视频及第三方素材的许可。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：不适用。

## E-020 · LiftShift LICENSE

[SRC登记](../../raw/SRC-20260910-gym-reference-20.md)

```yaml
evidence_id: "E-020"
source_id: "SRC-20260910-gym-reference-20"
claim: "LICENSE显式SPDX-License-Identifier: AGPL-3.0-only，并链接AGPL全文、说明修改后网络交互的对应源码要求。"
label: "Fact"
source_title: "LiftShift LICENSE"
source_url: "https://github.com/aree6/LiftShift/blob/main/LICENSE"
source_class: "B"
published_or_event_date: "unknown"
accessed_date: "2026-09-10"
scope: "LICENSE为12行声明而非完整AGPL全文；README归属表述需一并复核；不推断可以直接闭源商用。"
support: "full"
independence_group: "liftshift"
limitations: "LICENSE为12行声明而非完整AGPL全文；README归属表述需一并复核；不推断可以直接闭源商用。"
decision_relevance: "能力／设计参考；不证明本店需求"
confidence: "High"
```

界面观察：不适用。

## E-021 · 用户评论 2026-06-18

[共用页面SRC登记](../../raw/SRC-20260910-gym-reference-09.md)

```yaml
evidence_id: "E-021"
source_id: "SRC-20260910-gym-reference-09"
claim: "一条评论认为查人数与课程还好，但查找训练器械记录繁琐，并建议在器械上贴二维码。"
label: "Fact"
source_title: "The Gym Group Google Play用户评论"
source_url: "https://play.google.com/store/apps/details?id=com.netpulse.mobile.thegymgroup&hl=en_GB&gl=US"
source_class: "D"
published_or_event_date: "2026-06-18"
accessed_date: "2026-09-10"
scope: "一条公开自选择评论，账号身份与使用情况未独立验证"
support: "full"
independence_group: "gymgroup-public-users"
limitations: "每项n=1，无代表性，不估算问题频率；历史评论不代表当前版本"
decision_relevance: "形成器械目录／扫码说明的访谈假设"
confidence: "Medium"
```

## E-022 · 用户评论 2022-10-03

[共用页面SRC登记](../../raw/SRC-20260910-gym-reference-09.md)

```yaml
evidence_id: "E-022"
source_id: "SRC-20260910-gym-reference-09"
claim: "一条历史评论报告二维码开门偶发失效、人数更新异常。"
label: "Fact"
source_title: "The Gym Group Google Play用户评论"
source_url: "https://play.google.com/store/apps/details?id=com.netpulse.mobile.thegymgroup&hl=en_GB&gl=US"
source_class: "D"
published_or_event_date: "2022-10-03"
accessed_date: "2026-09-10"
scope: "一条公开自选择评论，账号身份与使用情况未独立验证"
support: "full"
independence_group: "gymgroup-public-users"
limitations: "每项n=1，无代表性，不估算问题频率；历史评论不代表当前版本"
decision_relevance: "提示可靠性优先；不能指称当前版本仍有相同故障"
confidence: "Medium"
```

## 推断与假设对应关系

| 判断 | 标签 | 对应证据 | 待验证跳跃 |
| --- | --- | --- | --- |
| 人数＋会员＋课表是首店较小且完整的组合 | Inference | E-009、E-010、E-013、已确认需求 | 海外功能样板能否帮助本店会员 |
| 器械目录／扫码说明值得追加 | Assumption | E-014、E-021 | 查训练记录的抱怨能否迁移到本店找器械场景 |
| 扫码报修有价值 | Assumption | 本店器械场景＋E-021作背景 | 评论未直接要求报修；馆方接收处理意愿未知 |
| 简洁列表＋状态解释适合首页 | Inference | E-008、E-010、E-011、E-014 | 无可用性任务数据；图片观察不能证明完成率 |
| 增加卡片可改善信息层级 | Inference | E-007 | 需控制卡片数量并测试中文理解度 |
