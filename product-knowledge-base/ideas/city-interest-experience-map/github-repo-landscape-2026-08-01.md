# 城市兴趣体验与消费地图：GitHub 相似仓库调研

Owner: Product Lead
Last updated: 2026-08-01
Source: GitHub Search、GitHub Repository API、仓库 README 与许可证文件
Confidence: Medium
Related decisions: 城市兴趣体验与消费地图首发切口（待决策）
Next review date: 2026-08-15

## 结论

GitHub 上已经存在大量地图、POI、活动发布、RSVP、票务、收藏、提醒和垂直兴趣工具，但没有发现一个成熟仓库同时覆盖「跨兴趣发现、新手门槛、实时可参加、门店与活动连接、线下转化」。

这不是“代码层面没有竞品”。相反，大部分基础功能已高度商品化；真正稀缺的是：

1. 某一城市中足够完整的兴趣地点与活动供给；
2. 新手友好、单人可参加、总费用、装备、水平要求等领域字段；
3. 对易过期数据的商户更新、用户纠错和可信度机制；
4. 从查看到报名、导航、到店与复购的数据闭环。

最接近本产品形态的是 **Pinball Map**：它用单一兴趣建立地点、设备库存、移动端、公开 API 和社区更新体系。它支持「先做一个垂直兴趣」的方向，不支持一开始做泛兴趣聚合。

## 调研口径

- 快照时间：2026-08-01。
- 搜索语言：中文与英文。
- 关键词覆盖：local events map、nearby activities、hobby map、fishing spots、tabletop events、game store locator、同城活动、钓鱼地图、卡牌店铺地图等。
- 指标来自 GitHub Repository API 或仓库页面。Star、Fork 和提交时间只能表示开发者关注与维护信号，不能代表真实用户数、收入或市场需求。
- 本次为方向性搜索，不是 GitHub 全量统计。私有仓库、未被索引仓库和托管在 GitLab/Framagit/Gitee 的项目不在完整覆盖范围内。

## 高相关仓库

| 仓库 | 截至 2026-08-01 的信号 | 已有能力 | 与本产品的关系 | 建议 |
| --- | --- | --- | --- | --- |
| [pinballmap/pbm](https://github.com/pinballmap/pbm) | 138 Stars、30 Forks；2026-07-30 有代码更新；5,868 次提交 | 弹球机地点、具体机器库存、公开 API、社区数据 | **最接近的产品样板**：兴趣对象不是普通 POI 属性，而是会变化的“店内有什么” | 深度拆解数据模型、纠错与贡献流程；不直接复制代码或数据 |
| [pinballmap/pbm-react](https://github.com/pinballmap/pbm-react) | 45 Stars、12 Forks；2026-07-29 有代码更新；2026-07 有连续版本 | React Native 移动端、附近地点、机器过滤、活动距离、收藏/生命周期记录 | 证明垂直兴趣地图可形成长期移动产品，而不是一次性网页 | 参考筛选、地点详情和近期变化体验 |
| [cgeo/cgeo](https://github.com/cgeo/cgeo) | 约 1.5k Stars、594 Forks；20,376 次提交 | 地理寻宝、多数据源、离线使用、地图与兴趣任务结合 | 成熟的「地图即兴趣体验」案例 | 参考离线、收藏、任务状态和多数据源架构 |
| [WatWowMap/ReactMap](https://github.com/WatWowMap/ReactMap) | 157 Stars、86 Forks；MIT | Pokémon GO 地图、实时对象、Raid、天气、精细过滤、Discord/Telegram 登录和提醒 | 与「实时兴趣场次雷达」相似 | 参考过滤和提醒；游戏数据来源与平台条款风险使其不适合作为业务模板 |
| [itskovacs/trip](https://github.com/itskovacs/trip) | 约 1.7k Stars、103 Forks；2026-05-30 发布 v1.45.2；MIT | POI 管理、行程、协作分享、自托管 | 与无 App 原型和周末方案相近，但没有实时兴趣供给 | 可评估为原型参考；先验证需求再决定是否复用 |
| [polaroi8d/cactoide](https://github.com/polaroi8d/cactoide) | 389 Stars、21 Forks；最后代码推送为 2025-12-08；AGPL-3.0 | 无需注册的活动创建、链接分享、RSVP、容量、日历和联邦发现 | 可降低小型兴趣活动发布门槛 | 参考无账号 RSVP；活跃度与许可证使其不宜直接作为闭源产品底座 |
| [HiEventsDev/Hi.Events](https://github.com/HiEventsDev/Hi.Events) | 约 3.9k Stars、692 Forks；2026-07-30 有代码更新 | 票种、支付、容量、退款、QR 核销、营销、报表、REST API | 说明通用票务和商户活动后台已非常成熟 | 不自研完整票务；优先外链或集成。许可证含 AGPL-3.0 附加条款，商用复用前必须审查 |
| [organicmaps/organicmaps](https://github.com/organicmaps/organicmaps) | 约 14.9k Stars、1.5k Forks；2026-08-01 有代码更新；Apache-2.0 代码、地图数据另有许可 | 跨平台离线地图、导航、POI、搜索、收藏、轨迹 | 地图基础设施完整，但远超 MVP 需要 | 不建议 Fork 整套产品；地图数据、署名和白标需单独核验 |

## 小型或直接命中概念的仓库

| 仓库 | 信号 | 判断 |
| --- | --- | --- |
| [EmpyreanMist/Fishing-Diary](https://github.com/EmpyreanMist/Fishing-Diary) | 2 Stars、0 Fork；2026-03-06 更新；未检测到许可证 | 已实现钓获日志、照片、天气、水况、地图和常用钓点。适合验证数据字段，不适合直接复用代码；无许可证默认不应复制。 |
| [seasensedev/seasense](https://github.com/seasensedev/seasense) | 5 Stars、3 Forks；2025-01-30 最后推送；MIT | “钓点＋天气＋鱼类行为”概念明确，但采用度和维护信号弱，只能作为功能参考。 |
| [JinhaKimGH/Basketball-Court-Finder](https://github.com/JinhaKimGH/Basketball-Court-Finder) | 1 Star、1 Fork；2025-06-06 最后推送；README 声明 MIT | 使用 OpenStreetMap/Nominatim 查找附近篮球场、评价和维护场地属性；在线站点已不可用。说明普通“附近场地＋评论”容易实现，也容易缺少持续运营。 |
| [r-community/event-explorer](https://github.com/r-community/event-explorer) | 13 Stars、0 Fork；2022-01-27 最后推送；未检测到许可证 | 全球 R 活动的日历、地图和图表，已明显停止更新；只适合参考聚合展示。 |
| [justgamer6472/TCG-Store-Locator-name-pending-](https://github.com/justgamer6472/TCG-Store-Locator-name-pending-) | 0 Star、0 Fork；2026-07-24 创建/推送；未检测到许可证 | 名称和目标与 TCG 店铺地图直接重合，但没有采用度证据，也没有可安全复用的许可证。它是概念撞车信号，不是成熟竞品。 |

## 对产品定位的影响

### 1. “兴趣地图”本身不是差异化

TRIP、Organic Maps、篮球场 Finder 等仓库说明地图、附近搜索、POI 详情、收藏和评论都能快速拼装。把这些功能组合起来不会自动形成产品壁垒。

### 2. 垂直数据比泛兴趣更可能形成飞轮

Pinball Map 的核心不是地图，而是「某地点当前有哪些具体机器」；c:geo 的核心也不是地图，而是地理任务和完成状态。对应到本产品，应先定义卡牌/模型或钓鱼中独有、会持续更新且影响行动的对象。

### 3. 通用活动和票务应集成，不应重造

Hi.Events、Cactoide 等已经覆盖发布、容量、RSVP、票务、核销和通知。第一版可外链商户现有报名渠道；除非验证商户更新与成交显著受阻，否则不做完整票务系统。

### 4. “新手第一次”仍然是更清晰的空白

已发现的成熟仓库大多服务已有兴趣用户、组织者或地图用户，没有把「第一次需要知道什么」作为统一的数据模型。这加强了当前首选定位，但仍需用户实验验证，不能由 GitHub 搜索直接证明需求。

### 5. 中国与欧美的代码可共用，数据和地图规则不能直接共用

开源前后端可以作为技术参考，但中国上线仍需单独核验地图服务、坐标体系、数据授权和相关合规要求。OpenStreetMap 或欧美仓库中的地点数据不能默认直接用于中国商业产品。

## 可复用性与许可证判断

| 类型 | 可采取的动作 | 风险 |
| --- | --- | --- |
| MIT / Apache-2.0 | 可评估复用组件或设计模式，并保留许可证与署名 | 仍需检查第三方依赖、地图数据、商标和 API 条款 |
| GPL-3.0 / AGPL-3.0 | 可研究和运行原型；若分发修改版或提供网络服务，可能触发源码开放义务 | 商业闭源产品使用前必须做许可证审查；Hi.Events 还有附加条款 |
| 无许可证 | 只阅读、学习产品思路 | 默认没有复制、修改和分发授权，不应把代码带入产品 |
| 开放代码＋独立数据许可 | 分别审查代码和数据 | Pinball Map、Organic Maps 都明确区分代码与数据许可，不能只看仓库主许可证 |

以上不是法律意见；在决定 Fork、嵌入或商用前需要正式许可证审查。

## 技术与产品建议

### MVP

- 不 Fork Organic Maps、Hi.Events 或 Pinball Map 整套系统。
- 用轻量 Web/PWA 实现地图、列表、筛选、详情、收藏与外链报名。
- 数据模型优先于 UI：新手友好、单人参加、完整费用、装备、水平、最近场次、最后核验时间、来源和可信度。
- 报名先外链，导航调用本地地图，活动更新先用商户表单和人工审核。

### 若进入开发

1. 拆解 Pinball Map 的地点—兴趣对象—贡献—纠错模型。
2. 借鉴 Cactoide 的无账号 RSVP，验证小活动是否需要站内报名。
3. 若票务成为阻塞，再比较 Hi.Events 集成、商业许可或自建最小订单模块。
4. 中国和欧美使用同一领域模型，但分别实现地图供应商、地点源、坐标和合规适配。

## 当前判断

GitHub 调研没有发现可以直接拿来即用、且已经验证本产品定位的仓库；也没有发现需要因此放弃 idea 的强信号。

它带来的主要修正是：

- 进一步降低“地图功能”的战略权重；
- 提高垂直兴趣数据、实时更新和新手字段的权重；
- 把 Pinball Map 设为首要产品参考；
- 把开源项目视为原型与架构参考，不视为市场需求证据。

