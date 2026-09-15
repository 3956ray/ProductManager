# 老年陪伴研究来源索引

Owner: Product Lead  
Last updated: 2026-09-05  
Source: `product-knowledge-base/raw/SRC-20260905-elder-companion-01`–`21`  
Confidence: Medium-High  
Related decisions: `../../decisions/one-person-pm-knowledge-loop-2026-08-23.md`  
Next review date: 2026-10-05

## 使用说明

原始来源只保留元数据和短摘要；网页、社交平台和商家页面可能动态变化。A 为官方／一手公共来源，B 为商家自报，C 为媒体或个人公开样本，D 为平台转录或二手内容。A/B/C/D 是来源等级，不是结论可信度；研究综合中的推断必须回到本索引和 raw 文件。

| Source ID | 来源与类型 | 主要用途 | 访问状态 | 主要限制 |
| --- | --- | --- | --- | --- |
| [SRC-01](../../raw/SRC-20260905-elder-companion-01.md) | 国家统计局，官方人口 | 全国 60+/65+ 基线 | verified | 年末全国口径，不能直接代表可付费人群 |
| [SRC-02](../../raw/SRC-20260905-elder-companion-02.md) | 北京市民政局，官方统计 | 北京城市规模 | verified | 常住人口；与其他城市户籍口径不同 |
| [SRC-03](../../raw/SRC-20260905-elder-companion-03.md) | 上海市政府，官方统计 | 上海 60+/80+、纯老家庭、独居 | verified | 户籍人口 |
| [SRC-04](../../raw/SRC-20260905-elder-companion-04.md) | 广州市政府，官方统计 | 广州户籍与非户籍老人 | verified | 户籍与居住登记口径需分开 |
| [SRC-05](../../raw/SRC-20260905-elder-companion-05.md) | 杭州网／官方发布，统计 | 杭州 60+/65+/80+ | verified | 户籍人口 |
| [SRC-06](../../raw/SRC-20260905-elder-companion-06.md) | 南京市民政局，统计 | 南京 60+/65+/80+ | verified | 户籍人口 |
| [SRC-07](../../raw/SRC-20260905-elder-companion-07.md) | 武汉市医保局，统计引用 | 武汉 60+/65+ | verified | 户籍人口，来源为政府答复引用 |
| [SRC-08](../../raw/SRC-20260905-elder-companion-08.md) | 西安市民政局，官方统计 | 西安常住与户籍 60+/65+ | verified | 常住与户籍口径需分开 |
| [SRC-09](../../raw/SRC-20260905-elder-companion-09.md) | 上海市民政／卫健／人社／消保，政策 | 服务定义、培训、合同、保险、隐私 | verified | 上海地方方案，不自动适用于全国 |
| [SRC-10](../../raw/SRC-20260905-elder-companion-10.md) | 浦东新区政府，试点与价格 | 2,480 人调研、1,600 人次、满意度、198–280 元 | verified | 单区试点；满意度为项目口径 |
| [SRC-11](../../raw/SRC-20260905-elder-companion-11.md) | 解放日报，医院与社交平台样本 | 医院流程、XHS 个人价格、平台内容 | verified | 个案和媒体报道，不是平台全量 |
| [SRC-12](../../raw/SRC-20260905-elder-companion-12.md) | HansPub 学术调查 | 82 位上海老人功能需求 | verified | 小样本、单城市、横截面 |
| [SRC-13](../../raw/SRC-20260905-elder-companion-13.md) | 用户提供抖音视频 | 95 岁老人陪伴案例与内容 | partial | 页面摘要可读，视频逐字稿未独立核验 |
| [SRC-14](../../raw/SRC-20260905-elder-companion-14.md) | 抖音公开账号／话题 | 地方供给、粉丝和价格讨论 | partial | 页面动态、部分为 AI／平台转录 |
| [SRC-15](../../raw/SRC-20260905-elder-companion-15.md) | 陪诊呗官网 | 服务形态、起价、认证自报 | partial | 商家自报，规模和认证未第三方验证 |
| [SRC-16](../../raw/SRC-20260905-elder-companion-16.md) | 99 陪诊杭州页 | 杭州 2h/4h/全天价格 | partial | 商家自报，价格会变动 |
| [SRC-17](../../raw/SRC-20260905-elder-companion-17.md) | EverCare 官网 | 长期陪伴套餐形态 | partial | 页面抽取不稳定，非中国本地验证 |
| [SRC-18](../../raw/SRC-20260905-elder-companion-18.md) | 人社部，养老护理员职业标准 | 养老护理职业边界 | verified | 不等同于纯陪伴或陪诊执照 |
| [SRC-19](../../raw/SRC-20260905-elder-companion-19.md) | 南方都市报，深圳统计整理 | 深圳时间序列 | partial | 2024 公开数据不完整；含媒体转述 |
| [SRC-20](../../raw/SRC-20260905-elder-companion-20.md) | 广州市民政局转载，老年网民统计 | 老年网民触达线索 | partial | 网民规模不是老年人口；二手引用 |
| [SRC-21](../../raw/SRC-20260905-elder-companion-21.md) | 国家医保局，广东免陪照护指导 | 住院照护价格参照 | verified | 医疗照护，不应与纯陪伴／陪诊混价 |

## 结构化表之间的关系

- `demographics.csv`：只放人口和相关结构化指标，保留人口口径。
- `service-prices.csv`：只放可观察价格样本，保留服务范围、价格类型、来源等级和验证状态。
- `market-research-2026-09-05.md`：只做可追溯综合、推断、假设、验证计划，不把模型判断伪装成原始事实。
