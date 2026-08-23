# 城市兴趣体验与消费地图：中美欧初步市场数据调研

Owner: Product Lead
Last updated: 2026-08-01
Source: ChatGPT 分享讨论、政府统计、行业协会、上市公司披露、GitHub 公开仓库
Confidence: Medium
Related decisions: 暂无
Next review date: 2026-08-15

## TL;DR

数据支持继续 Discovery，但不支持直接开发一个泛兴趣地图 App。

- 中国、美国、欧洲都有足够大的城市人口、休闲消费和线下兴趣参与基础。
- 钓鱼在三地都有可量化的大规模参与人群；集换式卡牌/桌游则更符合「地点 + 活动 + 持续消费」的产品结构。
- 短视频适合获客，但内容浏览不是产品壁垒。中国短视频用户规模约 10.40 亿；美国 18—34 岁成人中 56% 使用 TikTok；欧盟 16—29 岁人群中 88% 使用社交网络。
- 最大竞争不是另一款同名产品，而是美团/大众点评、Google Maps、Eventbrite、Meetup、短视频和垂直社群的组合。
- 最值得验证的差异化是：用「当前可参加、新手友好、费用、预约要求、一个人是否适合、最近活动」等字段，把发现转化为导航、报名或到店。
- 第一轮应选择一个城市和一个主品类。中国与欧美不能共用同一份地点数据、分类、规则或合规逻辑。
- GitHub 已存在成熟的地图、票务和垂直兴趣实现，说明基础功能不是壁垒；未发现同时解决跨兴趣、新手门槛、实时可参加和线下转化的成熟仓库。最接近的产品样板是 Pinball Map。

## 研究口径

本报告把中国、美国、欧洲分开。欧洲主要使用欧盟 27 国数据；个别行业数据覆盖更广泛的欧洲，已单独注明。

这些数字用于判断行为和供给是否存在，不直接相加为 TAM。不同来源对「用户」「参与者」「消费」「市场规模」的定义不同，尤其不能把体育参与人数、短视频用户和平台交易用户去重相加。

## 区域对比

| 维度 | 中国 | 美国 | 欧洲 |
| --- | --- | --- | --- |
| 城市人口基础 | 2024 年城镇常住人口 9.435 亿，城镇化率 67.0% | 2020 年城市地区人口 2.651 亿，占 80.0% | 2021 年 EU 人口中 38.9% 居住在城市、35.9% 在城镇和郊区，合计 74.8% |
| 休闲消费 | 2024 年居民人均文化娱乐消费 955 元；教育文化娱乐支出 3,189 元，占 11.3% | 2024 年每个消费单元平均娱乐支出 3,609 美元，占总支出 4.6% | 2021 年 recreation and culture 占家庭支出 8.0%；2021—2023 年 recreation, sport and culture 实际支出增长 23.5% |
| 线下参与信号 | 2025 年经常锻炼比例 38.52%；19—59 岁人均体育消费 2,428 元，服务型体育消费占 48.5% | 2023 年户外活动参与者 1.758 亿，占 6 岁以上人口 57.3% | 2022 年 38% 至少每周运动一次，45% 从不运动；国家差异很大 |
| 钓鱼品类 | 2024 年约 1.5 亿爱好者；2024-06 至 2025-05 各类赛事超过 7,000 场 | 2023 年 5,770 万参与者，占人口 19%；2024 年 boating/fishing 贡献 384 亿美元增加值 | 欧洲约 2,500 万钓鱼者，社会经济价值约 200 亿欧元；为行业协会估算 |
| 内容获客 | 2024-12 短视频用户约 10.40 亿 | 18—34 岁成人中 56% 使用 TikTok（2023 调查） | 2024 年 16—29 岁人群中 88% 使用社交网络，97% 每日上网 |
| 强替代方案 | 美团/大众点评、高德、百度、小红书、抖音、微信群 | Google Maps、Yelp、Eventbrite、Meetup、TikTok、Reddit、Discord、垂直 App | Google Maps、Eventbrite、Meetup、TikTok/Instagram、国家级活动平台与垂直社群 |
| 初步判断 | 本地生活竞争最强；适合小程序/网页先验证 | 户外和活动经济成熟，但垂直工具很多；必须窄切口 | 语言、国家和法规高度分散；应按单个国家/城市启动 |

## 中国市场

### 城市人口与消费

2024 年末中国城镇常住人口为 9.435 亿，城镇化率 67.00%。这是地图型本地产品的基础人口池，但不是本产品可触达用户数。来源：[国家统计局人口解读](https://www.stats.gov.cn/sj/sjjd/202501/t20250117_1958337.html)。

2024 年全国居民人均教育文化娱乐支出为 3,189 元，同比增长 9.8%，占人均消费支出的 11.3%。其中更窄的文化娱乐消费为 955 元，比 2020 年增长 67.8%。两个口径不能混用：前者包含教育。来源：[国家统计局居民收入和消费支出](https://www.stats.gov.cn/sj/zxfb/202501/t20250117_1958325.html)、[“十四五”社会民生统计报告](https://www.stats.gov.cn/sj/zxfb/202509/t20250928_1961404.html)。

### 从买装备转向买体验

2025 年全民健身调查覆盖 141,145 个样本。经常参加体育锻炼的比例为 38.52%；19—59 岁居民人均体育消费为 2,428 元；服务型体育消费占比升至 48.5%；39.4% 的 19 岁以上居民参加过体育健身组织，45.1% 参加过群众体育赛事活动。来源：[国家体育总局《2025年全民健身活动状况调查公报》](https://www.sport.gov.cn/n20001280/n20745751/c29327174/content.html)。

这支持「地点 + 活动 + 报名」而不是单纯商品目录，但体育数据不能代表卡牌、模型等非体育兴趣。

### 钓鱼是规模最大的可量化候选品类

国家体育总局发布的产业报告称，2024 年全国钓鱼爱好者约 1.5 亿；2024 年 6 月至 2025 年 5 月各类赛事活动超过 7,000 次。来源：[国家体育总局《中国户外运动产业发展报告（2024-2025）》摘要](https://www.sport.gov.cn/n20001280/n20067608/n20067635/c29144955/content.html)。

钓场、装备店、赛事、规则、季节、新手指导和预约天然需要结构化；但水域规则、安全、天气、禁钓期和地点真实性使数据维护明显更难。

### 卡牌与模型符合 A+B 交叉，但市场口径混乱

中国玩具和婴童用品协会披露，2023 年国内玩具零售额为 906.9 亿元，但明确不含潮流和收藏玩具，且主要不是成年兴趣消费口径。来源：[《2024中国玩具和婴童用品行业发展白皮书》发布信息](https://www.china-kids-fair.com/media_center/16673)。

公开研究对 2024 年中国集换式卡牌市场给出约 140 亿元到 263 亿元不等的估算，差异来自是否包含收藏卡、集换式游戏卡、泛娱乐卡牌和二级交易。该区间只能标为假设，不能用于正式 TAM。更应统计首发城市中的门店数、每周活动数、支持品类、新手场次和报名方式。

### 获客容易，独立产品分发很难

CNNIC 第 55 次报告显示，2024 年 12 月中国短视频用户规模约 10.40 亿。短视频可以成为兴趣灵感和地图入口，但不应抓取或复制内容。来源：[CNNIC 第55次《中国互联网络发展状况统计报告》](https://www.cnnic.net.cn/NMediaFile/2025/0428/MAIN17458061595875K4FP1NEUO.pdf)。

美团 2024 年交易用户超过 7.7 亿，活跃商户达到 1,450 万，到店业务订单量同比增长超过 65%。来源：[美团 2024 年财报摘要](https://www.meituan.com/news/NN250321082001991)。新产品必须提供大众点评没有稳定结构化的兴趣信息，而不是重复 POI。

## 美国市场

### 城市和娱乐消费

美国 2020 年有 2.651 亿人居住在城市地区，占全国人口 80.0%。来源：[U.S. Census 2020 Urban Areas Facts](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural/2020-ua-facts.html)。

2024 年每个消费单元平均娱乐支出为 3,609 美元，占总支出 4.6%。这是全体家庭/消费单元口径，不等同于 22—35 岁男性。来源：[U.S. Bureau of Labor Statistics Consumer Expenditures 2024](https://www.bls.gov/news.release/cesan.htm)。

### 户外兴趣是成熟经济

美国经济分析局估算，2024 年户外休闲经济增加值为 6,967 亿美元，占 GDP 2.4%；其中 boating/fishing 是最大的传统户外活动，增加值 384 亿美元。来源：[U.S. BEA Outdoor Recreation Economic Statistics 2024](https://www.bea.gov/index.php/news/2026/outdoor-recreation-economic-statistics-us-and-states-2024)。

2023 年户外活动参与者为 1.758 亿，占 6 岁以上人口 57.3%。来源：[Outdoor Industry Association 2024 Participation Trends](https://outdoorindustry.org/press-release/outdoor-participation-hits-record-levels-for-ninth-consecutive-year/)。

### 钓鱼有高参与，但已有成熟垂直生态

2023 年有 5,770 万美国人钓鱼，占人口 19%，为报告记录中的最高水平。来源：[Recreational Boating & Fishing Foundation 2024 Report](https://www.takemefishing.org/corporate/resource-center/research/fishing-boating-research/)。

机会是新手入口、许可证、季节、地点、租赁、向导和活动；风险是 Fishbrain、州政府许可网站、Google Maps、钓具零售商和本地论坛已经覆盖部分需求。

### 卡牌/桌游的「门店 + 活动 + 消费」模型已被证明

Hasbro 披露，Magic: The Gathering 2024 年收入约 10.8 亿美元；其桌面玩家平均年龄约 30 岁，Wizards Play Network 约有 7,500 家门店。来源：[Hasbro Magic investor page](https://investor.hasbro.com/magic-gathering)、[Hasbro 2024 results](https://newsroom.hasbro.com/news-releases/news-release-details/hasbro-reports-fourth-quarter-and-full-year-2024-financial)。

这些是单一品牌和全球门店网络数据，不是美国 TCG 市场规模，但直接支持首发用户年龄、线下门店网络和持续活动机制与本 idea 匹配。

### 短视频获客有效，活动平台竞争强

Pew 2023 年调查显示，56% 的美国 18—34 岁成人使用 TikTok；美国全体成人使用率为 33%。来源：[Pew Research Center](https://www.pewresearch.org/internet/2024/02/22/how-u-s-adults-use-tiktok/)。

Eventbrite 2024 年全球口径有 8,900 万月均用户、470 万场活动和 8,300 万张付费票；Meetup 对外称有 6,000 万注册用户和 33 万个群组。来源：[Eventbrite 2024 at a Glance](https://www.eventbrite.com/about/investors/)、[Meetup press material](https://www.meetup.com/marketing-assets/PDF/Press%20Release%20Member%20Connections.pdf)。两组数据只能证明替代平台强，不能作为美国市场规模。

## 欧洲市场

### 必须按国家和城市启动

Eurostat 2021 数据显示，EU 人口中 38.9% 居住在城市，35.9% 居住在城镇和郊区，合计 74.8%；25.2% 居住在农村。来源：[Eurostat Urban-rural Europe](https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/112336.pdf)。

人口密集不代表可用同一产品覆盖欧盟。语言、支付、商户平台、活动习惯、钓鱼许可和酒类/枪械规则均按国家变化，第一版不应做「欧洲地图」。

### 休闲支出恢复，但运动参与分化明显

EU 家庭 2021 年将 8.0% 支出用于 recreation and culture；2021—2023 年 recreation, sport and culture 的实际支出增长 23.5%。来源：[Eurostat household spending 2021](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20230104-1)、[Eurostat household spending 2023](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20241128-1)。

2022 年 Eurobarometer 显示，38% 的欧洲受访者至少每周运动一次，45% 从不运动；各国参与率差异显著。来源：[Eurobarometer Sport and Physical Activity](https://europa.eu/eurobarometer/surveys/detail/2668)。不能把 EU 平均值直接套到首发城市。

### 钓鱼是明确机会，但法规和地点数据碎片化

European Fishing Tackle Trade Association 估算，欧洲有超过 2,500 万钓鱼者，社会经济价值约 200 亿欧元。来源：[EFTTA 2024 lobbying brief](https://www.eftta.com/fileadmin/IMG_Lobby_Projects/EFTTA_LOBBY_LEAFLET_2024_v4.pdf)。这是行业协会估算，置信度低于官方人口调查。

### 桌游和卡牌的线下独立店很关键

Asmodee 引用的 Arthur D. Little 研究把欧洲和北美合并估算为：约 2.5 亿休闲玩家、5 亿家庭玩家和 6,000 万核心爱好者；核心爱好者以 16—35 岁为主。该数据没有拆分欧洲与北美，只能用作跨市场方向信号。来源：[Asmodee Capital Markets Day 2024](https://cdn.svc.asmodee.net/production-payload-corporate/Asmodee_Capital_Markets_Day_2024%20Dec.pdf)。

S&P Global 对 Asmodee 的分析称，hobby and independent stores 约占桌游销售的 35%—40%，并且是高频、高消费玩家和新品的重要渠道。来源：[S&P Global Ratings on Asmodee](https://www.spglobal.com/ratings/es/regulatory/article/-/view/type/HTML/id/3291174)。这强化了「门店详情 + 店内活动 + 新品/库存情报」结构。

### 社交网络适合分发，但不是差异化

2024 年 EU 16—29 岁人群中 97% 每日使用互联网，88% 参与社交网络活动。来源：[Eurostat young people in the digital world](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/edn-20250715-1)。

## 品类优先级

评分是产品适配判断，不是市场规模排名。

| 品类 | A 体验需求 | B 消费需求 | 地点/活动结构 | 数据维护 | 合规风险 | 初步结论 |
| --- | --- | --- | --- | --- | --- | --- |
| 卡牌、桌游、模型 | 高 | 高 | 门店、比赛、课程清晰 | 中高，活动和库存易过期 | 低 | 最适合验证 A+B 飞轮 |
| 钓鱼 | 高 | 高 | 钓场、商店、向导、赛事清晰 | 高，受天气、季节和规则影响 | 中 | 规模最大，但应做垂直版本 |
| 篮球等大众运动 | 高 | 中低 | 场馆清晰 | 中 | 低 | 获客可行，商业化较弱 |
| 汽车活动/卡丁车 | 高 | 高 | 活动和场地存在 | 高 | 中高 | 合作和安全成本较高 |
| 酒类 | 高 | 高 | 商户密集 | 中 | 高 | 与点评平台重叠，首发不利 |
| 枪械 | 中 | 高 | 地区差异大 | 高 | 极高 | 不进入第一阶段 |

区域倾向：

- 中国：卡牌/模型最适合先验证产品飞轮；钓鱼最适合验证大规模垂直需求。
- 美国：钓鱼经济与数据更成熟，但竞争也更垂直；卡牌门店活动适合做小而清晰的 MVP。
- 欧洲：卡牌/桌游在城市中更容易低风险启动；钓鱼必须按国家法规设计。

## 不能从现有数据得出的结论

1. 不能证明 22—35 岁男性愿意安装一个独立 App。
2. 不能证明不同兴趣可以放在同一个首页。
3. 不能证明用户会从短视频点击到地图，再到店消费。
4. 不能证明商户愿意更新活动、价格和库存。
5. 不能证明「男孩子的快乐」这个品牌会提高转化且不排斥女性用户。
6. 不能用上述人口与行业数字直接计算 TAM；缺少首发城市的目标年龄、兴趣渗透、地点供给和行动转化数据。

## 下一步数据工作

### 城市级 POI 供给审计

为每个候选城市统计：目标品类门店/场地数、过去 30 天活动数、有价格/新手信息/预约入口的比例、现有地图信息完整度，以及可公开使用或经商户授权的数据比例。

### 目标用户访谈

访谈 15—20 名最近 60 天实际参加过卡牌、模型、钓鱼或同类线下活动的人。要求回忆最近一次发现、比较和到店过程，重点问替代方案和信息缺口，不问「你喜不喜欢这个 idea」。

### 无 App 原型

一个城市、一个主品类、80—120 个地点，用网页或小程序验证：查看至少 3 个地点的比例、收藏率、导航/报名/预约/联系点击率、7 天回访率和错误信息率。

初始成功阈值可暂设为：20% 查看至少 3 个地点、10% 收藏、5% 产生高意图动作、15% 七天回访。它们是内部实验门槛，不是行业基准。

## 当前建议

保持 Discovery，不进入 PRD。

先决定「首发城市 + 首发品类」，再做城市级供给审计。若结构化地点信息没有显著提高导航、报名或到店意图，应停止扩展地图和推荐算法。

## 相关 GitHub 调研

- [GitHub 相似仓库调研（2026-08-01）](</Users/orderly_ray/Documents/Products Manager/product-knowledge-base/ideas/city-interest-experience-map/github-repo-landscape-2026-08-01.md>)
