# 中国城市日常沉浸体验：竞品与五套定位研究

Owner: Product Lead
Last updated: 2026-07-22
Source: ChatGPT 分享讨论、国际与中国竞品官网、OTA 在售页、政府公开统计与法规
Confidence: Medium
Related decisions: 暂无
Next review date: 2026-07-29

## 结论先行

这是一个**已有可购买替代品、但目标细分需求与溢价尚未验证**的市场。

- 赛道不空白。Withlocals、Airbnb Experiences、ToursByLocals、Showaround、GuruWalk 和各大 OTA 都在卖“local、authentic、hidden gems”。
- 中国也不缺英文食物团、胡同/弄堂路线、早市和私导。上海甚至已有几乎同名的 `Experience Shanghai Like a Native`。
- **待验证的差异化假设**是：在上海，能否用 **标准化日常场景 + Host 训练 + 跨文化解释 + 可靠履约**，在现有私导、本地人步行和食物团之外形成用户可感知的溢价。
- 最值得先测的不是开放式平台，而是 `After Work in Shanghai`：固定 2.5—4 小时、2—6 人、持证合作方履约的小团体验。
- 五套定位中，首次来华文化好奇者最适合作为第一验证人群；商务、重游者、创作者、家庭均可作为后续产品线，但不应同时首发。

## 研究口径

调研日期为 2026-07-22。竞品“仍在运营”以官网、官方帮助中心、近期在售库存或 2026 年评价为证据，不等于工商状态核验。

价格会随日期、人数、城市、币种和选项变化，仅用于测试价格带，不构成正式定价承诺。

## 竞品地图

### 一、全球直接竞品与平台

| 竞品 | 核心承诺与模式 | 已验证信号 | 与本 idea 的重叠 | 可利用的空白 |
| --- | --- | --- | --- | --- |
| [Withlocals](https://www.withlocals.com/become-a-host/) | 私人、本地视角、个性化城市体验；既有 Host 原创，也有平台策划的 `Originals` | 官方称服务超过 100 万旅行者；[申请条件](https://helpcenter.withlocals.com/en/articles/633904-eligibility-check)包括英语、城市居住时间、既有带团评价和可投入时间；另有[入职培训与 Stripe 身份验证](https://helpcenter.withlocals.com/en/articles/627960-what-is-withlocals-for-hosts)；当前 Host 服务费为 32% | 本地人、非大团、个性化、真实连接，重叠最高 | 是否能用更深的中国日常解释形成垂直溢价，仍需与同城产品实测 |
| [Airbnb Experiences](https://www.airbnb.com/host/experiences) | 当地人主持的活动、课程、饮食与文化体验 | 2025 年重新设计后在 650 个城市上线；Host 成交服务费 20%，并提供审核、支付和最高 100 万美元责任保障 | 全球流量、Host 心智、评论与支付基础设施强 | 中国供给与当前可用性需逐城核验；普通本地人日常不一定符合其专业背景审核和规模化逻辑 |
| [ToursByLocals](https://www.toursbylocals.com/tours/china/shanghai) | 筛选本地导游、私人定制、行前沟通 | 上海当前展示 109 条路线；常见 4—8 小时私人团约 US$154—550/组 | 信任、定制、英语和私人服务成熟 | 仍以导游和景点为中心；本 idea 可用“时间切片+共同参与”替代景点清单 |
| [Showaround](https://www.showaround.com/locals/jenny-shanghai-china-9512165) | 按小时雇当地人陪同，自由协商路线 | 上海仍有可访问的本地人档案；但整体活跃度只可标中等置信度 | “普通本地人而非专业导游”与 idea 高度接近 | 自由撮合带来质量、安全和解释深度不稳定；可用标准化场景包和训练补足 |
| [GuruWalk](https://www.guruwalk.com/shanghai) | 免费预订、结束后自愿付费的城市步行团 | 上海展示 14 条路线；既有地标团，也有小团、本地食物和生活方式产品；官方建议小费最低约 US$15 / €15/人 | 低门槛、英语、城市故事和本地生活供给，属于直接价格与内容替代 | 首轮前需逐条审计 14 个上海产品的人数、语言、解释深度、退改、持证状态、真实场景和近期评价，不能仅按平台类型排除 |
| [GetYourGuide](https://www.getyourguide.com/c/about) / [Viator](https://supplier.viator.com/sign-up-info?m=66029) | 海量活动 OTA，提供评论、退改、客服和全球分发 | GetYourGuide 称覆盖 12,000+ 城市、150,000+ 体验；Viator 称 400,000+ 体验 | 用户会直接在 OTA 搜索“local life”“food tour”“private guide” | 它们是渠道而非差异化；本项目可把 OTA 当分销，不应把“更多路线”当壁垒 |
| [Eatwith](https://www.eatwith.com/zh-CN/how-it-works) | 本地人家宴、烹饪课、菜市场和美食团 | 覆盖 130+ 国家 Host 社群；平台对客人价格加 30% 佣金 | 证明“进入私人生活空间+食物+故事”可以付费 | 垂直食物；可把共同用餐嵌入通勤、家庭分工和邻里关系，而不是只做餐饮 |
| [Context Travel](https://www.contexttravel.com/) | 专家带领的小团和私享深度文化体验 | 1,200+ 专家；3 小时小团常见 US$140—229/人，私享约 US$469—902/组 | 证明“理解城市如何运作”可支撑高客单 | 专家/文化遗产导向强；本 idea 应保留平等交流和普通生活，而不是做中国版学术讲解团 |

### 二、中国和来华入境游直接/半直接竞品

| 竞品 | 当前产品与价格样本 | 强项 | 仍未解决的空白 |
| --- | --- | --- | --- |
| [Shanghai Pathways](https://www.shanghaipathways.com/backstreets-walk-in-southern-city-tour) | 2 小时上海旧城背街、市场和居民叙事；1 人 RMB2,000，每增 1 人 RMB500 | 非主流街区、英语、私人定制、可能触达居民和家中空间 | 高价且偏历史/旧城；居民同意、互动持续性和规模化不透明 |
| [UnTour Food Tours](https://untourfoodtours.com/product/shanghai-night-eats-tour/) | 上海夜食团 3 小时、15+ 品尝、最多 10 人，RMB640/成人 | 双语导游、商户关系、标准化和强口碑 | 游客仍主要跟团吃喝；普通人关系和非饮食日常没有被产品化 |
| [Lost Plate Food Tours](https://lostplate.com/beijing-food-tours/) | 北京晚餐 US$75/3.5 小时，早餐 US$39/3 小时；另覆盖成都、西安 | “避开游客陷阱”的英文叙事成熟，可复制 | 锚点仍是食物；跨场景日常和 Host 匹配不足 |
| [Chengdu Food Tours](https://chengdufoodtours.com/services/) | 湿市场、家庭式餐厅和老街区；约 RMB350—500/人 | 本地垂直团队，食物与街区结合 | 主理人筛选、居民共创和非饮食生活场景不清晰 |
| [The Hutong](https://thehutong.com/beijing-breakfast-stroll-savor-the-hutongs-2/) | 北京胡同早餐、菜市场、烹饪课；约 RMB350—380/人 | 实体文化中心、可参与技能、陌生人社交 | 特定路线当前档期需再次确认；公开供给更像课程/美食活动 |
| [Free Tours China](https://www.viator.com/tours/Shanghai/Shanghai-City-Free-Walking-Tour/d325-122769P2) | 上海约 4 小时英语城市概览，Viator 预订价 US$5 起/小费型，最多 30 人 | 极低门槛、英语口碑、地标覆盖 | 大团、地标、低价；无法稳定交付私密和深度日常 |
| [Lokafy 上海私人本地人步行](https://www.getyourguide.com/shanghai-l178/shanghai-like-a-local-customized-guided-tour-t94266/) | 2—6 小时、最多 6 人；2026-07-22 访问前后页面曾显示 2 小时 US$35/人起，实际价格随查询条件变化 | 最接近“本地朋友+个性化+真实故事” | 它已承诺真实连接、私人和无固定路线；本项目能否靠场景标准与解释训练胜出，必须直接对比测试 |
| [Experience Shanghai Like a Native](https://www.getyourguide.com/en-au/shanghai-l178/experience-shanghai-like-a-native-a-day-in-local-life-t976381/) | 6 小时、英语私人组；2026-07-22 页面显示促销价 US$77、原价 US$85；市场、社区食堂、交通、西岸等 | 和本 idea 的商品描述几乎直接重叠，且已有 2026 年评价 | 产品仍混合寺庙、法租界等旅游内容；“更纯粹的日常”是否提高转化或价格，尚未验证 |
| [Klook 西安早市路线](https://www.klook.com/en-GB/activity/17262-wet-food-antique-market-morning-tour-xian/) | 约 4.5 小时、英文/中文、早市+早餐+公园，约 S$54.75/人 | 真实日常切口、国际支付、退改和 100+ 预订 | 同一早市已在多个 OTA 同质化；用户更记住平台和地点，不记住体验品牌 |

### 待核验线索

[Take Me 原型](https://www.reddit.com/r/shanghai/comments/1i9yeal/) 于 2025-01-25 在 Reddit 发帖测试“本地人发布日常活动、游客选择同行”。它与本 idea 结构几乎一致，但只找到早期发帖，没有可核验的当前在售页、规模或持续运营证据，Confidence: Low，不参与竞品强弱结论。

## 用户真正的替代方案

用户不会只在“买这个产品”和“什么都不做”之间选择。他们会拼接：

- 传统私人导游：信任、英语和履约强，但客单高、景点化。
- 酒店礼宾或商务接待：省心，但通常推荐合作供应商，真实性和选择有限。
- 食物团或 free walking tour：价格和价值很清晰；其中也有小团与生活方式产品，具体深度需逐条比较。
- Meetup、语言交换、Reddit/微信群或中国朋友：真实性高，安全、语言和履约不稳定。
- TikTok、YouTube、小红书、Google Maps、Trip.com 自助：控制权高、成本低，但用户仍要自行翻译、判断和完成。

因此缺口必须同时交付：**可信陌生人关系、双语解释、非景点化日常、可预订可退款的履约，以及用户保有选择权。**

## 五套不同定位

下面的价格仅为验证假设，尚未获得人类批准，也不是对外承诺。

### 1. `After Work in Shanghai`：第一次来华文化好奇者

- **面向谁**：25—45 岁英语自由行游客；第一次来上海，经典景点已安排，但还有一个普通工作日晚间空闲。
- **核心承诺**：3 小时读懂一个上海上班族怎样通勤、吃饭、消费、社交和结束一天。
- **差异化角度**：按“真实时间切片”设计，不按景点清单设计；每个场景都回答“为什么本地人这样生活”。
- **一句话 slogan**：`Don't just visit Shanghai. Live one ordinary evening in it.`（别只看上海，过一个上海人的普通夜晚。）
- **适合的定价方式**：固定小团按人收费。第一轮先用 US$79 单一完整结算价；确认有人真实付款后，再测 US$59/79/89 三档。私享底价不得低于同一时段 4 个公开席位总价；以 US$79 为例，可从 US$320/组（最多 4 人）起。页面需写清是否含简餐、公共交通、税费和持证合作方分成。
- **当前判断**：第一验证假设，Confidence: Medium。问题清楚、商品容易理解，但“普通日常”是否有独立溢价尚未证明。

### 2. `China Between Meetings`：商务短暂停留者

- **面向谁**：来华参加展会、会议、公司访问，只剩 2—3 小时的商务旅客或小型客户团。
- **核心承诺**：在一个准时可控的晚上，让用户看到机场、酒店、办公室之外的中国城市生活。
- **差异化角度**：固定时长、明确集合/结束地点、英文项目经理、无购物、备用 Host 和企业发票；卖的是确定性，不是“探索感”。
- **一句话 slogan**：`See the city between the meetings.`（在会议之间，看见这座城市。）
- **适合的定价方式**：按私享团或企业项目收费，基础项目费 + 人头变动费；消费端测试 US$220—450/组，企业端询价。
- **当前判断**：第二顺位。客单高，但酒店、会展、企业差旅渠道难度更高，且准时和备用履约成本高。

### 3. `China City Decode`：重游者与城市深度探索者

- **面向谁**：第二次来华、曾在中国生活，或对城市、社会、建筑和公共生活有强兴趣的人。
- **核心承诺**：不是重看景点，而是用一个主题读懂城市如何变化，以及变化怎样进入普通人的生活。
- **差异化角度**：由城市研究者、记者、建筑师、社区工作者或长期居民共同设计主题；强调证据、争议和多方视角。
- **一句话 slogan**：`Skip the sights. Read the city.`（不看景点，读懂城市。）
- **适合的定价方式**：专家溢价的小团/私享定价；按主题和专家资历分级，测试 US$120—220/人或 US$400—800/组。
- **当前判断**：第三顺位。规模较小，但口碑和高端产品潜力好；需避免夸张社会解释和单一叙事。

### 4. `Local Story Access`：内容创作者

- **面向谁**：YouTube、TikTok、Instagram、小红书国际内容创作者，以及小型媒体团队。
- **核心承诺**：获得可拍、可解释、有故事线的中国日常场景，而不是到现场才发现不能拍或没有叙事。
- **差异化角度**：把拍摄边界、场地主体同意、人物授权、翻译、故事研究和现场协调做成服务；不承诺“随便拍”。
- **一句话 slogan**：`Film the China tourists usually miss.`（拍到游客通常错过的中国。）
- **适合的定价方式**：半日/全日制作支持费 + 场地/人物授权和交通实报实销；在完成旅行社、保险、授权、翻译、场地和陪同成本表前，不设公开美元区间，复杂项目询价。
- **当前判断**：后续独立产品线，不是首轮同一 SKU。传播价值高，但最容易破坏真实性，也有隐私、肖像、社区关系和敏感场景风险。

### 5. `China Life Mission`：亲子教育型家庭

- **面向谁**：带 8—18 岁孩子来华的国际家庭、华裔家庭和教育旅行者。
- **核心承诺**：让孩子亲手完成一次本地生活任务，而不是听完一场成人式文化讲解。
- **差异化角度**：围绕安全、可操作的任务设计，例如公共交通、买早餐、识别食材、观察公共空间、用简单中文完成交流；有年龄分级和家长共同行程。
- **一句话 slogan**：`Learn China by living one small part of it.`（用一次真实生活任务认识中国。）
- **适合的定价方式**：按家庭包收费，而不是按每个儿童单独收费；在完成未成年人保险、持证陪同、食品、授权和场地成本模型前，不设公开美元区间；超出基础家庭人数再加价。
- **当前判断**：后续独立产品线，不是首轮同一 SKU。教育和客单潜力可能较高，但食品、未成年人、节奏、卫生和安全要求最高。

## 定位优先级

| 定位 | 需求清晰度 | 支付潜力 | 获客难度 | 履约/合规难度 | 证据状态 | 建议 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| After Work in Shanghai | 假设：高 | 中 | 中 | 中 | 待交易验证 | **先验证** |
| China Between Meetings | 假设：中高 | 高 | 中高 | 中高 | 待渠道与交易验证 | 第二阶段 |
| China City Decode | 假设：高 | 中高 | 高 | 高 | 待访谈与专家供给验证 | 主题化高端产品 |
| Local Story Access | 假设：中高 | 中高 | 中 | 很高 | 待定制试单 | 仅定制试单 |
| China Life Mission | 假设：中高 | 高 | 高 | 很高 | 待家庭访谈与合规验证 | 暂缓 |

上表是产品判断，不是已验证的用户需求排序；五个定位都需访谈或交易测试。

## 推荐的首轮验证

### 产品

上海、白天或早晚但不进入深夜、2—6 人、2.5—4 小时、公共场所、无 Host 私家车载客、无私宅、无未许可餐饮，由持证旅行社/导游合作履约。

产品页只写清：

- 和谁一起；
- 进入哪些生活场景；
- 会理解哪些问题；
- 哪些地方可以/不可以拍摄；
- 费用、取消和备用 Host；
- 不含什么，以及风险边界。

### 测试设计

1. 第一轮先向 20 名正在规划未来 90 天来华或已在上海旅行的非熟人目标用户展示同一个 US$79 完整结算价。
2. 要求用户真实支付完整价格，并提供清晰的体验前 72 小时退订规则；分别记录付款、取消和实际到场，不用低额订金替代支付意愿。
3. 若至少 5/20 付款，再扩大样本并随机展示 `US$59 / US$79 / US$89`，每位用户只看到一个价格；小样本只用于方向判断，不据此宣布最优价格。
4. 连续测试 4 个周末，记录完成率、取消率、NPS/评分、Host 复约率、居民/场地方投诉、每单履约毛利和主动分享率。
5. 若少于 5/20 付款，只能判断当前证据不足：暂不扩张，先迭代一次产品/获客后复测；不能宣称需求不存在。若转化持续依赖“含很多食物”或“必须去知名景点”，则“普通日常可独立形成溢价”的假设受到反证。

## 合规边界

以下不是法律意见，只是必须在实验前核验的产品前置条件：

- `Host` 命名不能代替导游、旅行社或在线旅游经营所需的许可与责任。
- 平台可能需要核验经营者身份、许可、质量信息，并承担投诉、安全、合同、保险和应急处置责任。
- 首发不使用 Host 私家车收费载客，不以私宅餐饮为核心 SKU，不进入学校、住宅、宗教或敏感场所，不做一对一深夜陌生人匹配。
- 上线前应让本地持牌旅行社和中国旅游/数据律师按实际流程复核，并尽可能取得当地文旅主管部门的书面意见。

## 关键来源

- [国家统计局 2025 年统计公报](https://www.stats.gov.cn/sj/zxfbhjd/202602/t20260228_1962662.html)
- [2025 年上海入境游客与消费](https://english.shanghai.gov.cn/en-Latest-WhatsNew/20260128/1c81e7eb8f9e4f199893e55ab0b98f36.html)
- [Airbnb 2025 Summer Release](https://news.airbnb.com/en-uk/2025-summer-release-now-you-can-airbnb-more-than-an-airbnb/)
- [Airbnb Experience Host 与 20% 服务费](https://www.airbnb.com/host/experiences)
- [Withlocals Host 模式与 32% 服务费](https://www.withlocals.com/become-a-host/)
- [GuruWalk 价格说明](https://support.guruwalk.com/portal/en/kb/articles/how-much-does-a-guruwalk-cost)
- [ToursByLocals 上海在售页](https://www.toursbylocals.com/tours/china/shanghai)
- [GetYourGuide 上海本地生活一日体验](https://www.getyourguide.com/en-au/shanghai-l178/experience-shanghai-like-a-native-a-day-in-local-life-t976381/)
- [在线旅游经营服务管理暂行规定](https://zwgk.mct.gov.cn/zfxxgkml/zcfg/bmgz/202012/t20201204_905349.html)
- [中华人民共和国旅游法](https://www.npc.gov.cn/WZWSREL2MyL2MxMjQzNS8yMDE5MDUvdDIwMTkwNTIxXzI3NjYxMi5odG1s)
