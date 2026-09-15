# 项目上下文与续作入口

Owner: Product Lead
Last updated: 2026-09-05
Source: 任务「老年陪伴」`01a06cec-8b3e-7853-94ad-1c346bd16a7c`；项目已有研究包；本工作区配置
Confidence: Medium（历史记录，不代表当前重新核验）
Related decisions: `product-knowledge-base/decisions/one-person-pm-knowledge-loop-2026-08-23.md`
Next review date: 2026-10-05

## 已有意图

用户从 RentAFriend、国内地陪和实名信任机制讨论，转向中国老年人的真人陪伴。原始案例是在医院陪老人聊天、画画、做喜欢的事情；用户设想可能由 40–60 岁子女为 70–90 岁父母购买，且服务以陪伴为主。这些年龄和付款人判断仍是用户假设，不应把陪伴换成 AI 朋友、医疗护理或默认的陪诊平台。

研究范围曾包括全国、北上广深、杭州及二线城市老年人口、医院内老人、资质要求、抖音和小红书用户信号。RentAFriend、地陪可作机制对照，只有当前问题需要时才回读；不每轮扩展到旅游或青年社交市场。

## 知识位置

以下路径相对工作区根目录：

| 文件 | 用途 |
| --- | --- |
| `product-knowledge-base/ideas/elder-companion/market-research-2026-09-05.md` | 旧研究结论、假设与实验建议 |
| `product-knowledge-base/ideas/elder-companion/demographics.csv` | 人口记录、年份、单位、户籍／常住口径、来源 |
| `product-knowledge-base/ideas/elder-companion/service-prices.csv` | 服务范围、时长、价格依据、来源和核验状态 |
| `product-knowledge-base/ideas/elder-companion/source-index.md` | 21 条来源及访问限制 |
| `product-knowledge-base/raw/SRC-20260905-elder-companion-*.md` | 来源元数据与最小摘要；重要 claim 仍回到原始材料 |

从 INDEX 和项目目录确认有无更新版本。不要把本文变成另一份事实数据库；只按问题读取相关行与来源。继续旧会话时，可用任务读取工具查看最近用户决定，不重播其他旧任务。

## 已发现的待复核点

- 旧报告标注 Research Quality 89、助医陪诊 V2、纯非医疗陪伴 V1；旧报告不是独立原始证据，也不表示本项目已有自有订单。
- 旧报告建议“三城、10–20 名服务者、定金测试”，但未激活 BOARD 中的新项目。这些是建议，不是执行授权。当前 WIP 由最新 BOARD 和用户决定约束。
- 旧报告偏向助医陪诊，而用户原始兴趣偏纯陪伴。续作应比较两个方向的证据与代价，再提建议，不把旧推荐写成既定产品决策。
- 人口数据混有户籍／常住与不同年份；不能据此直接给城市机会排名。医院内老年人的占比也不能从城市老年人口占比推得。
- 视频来源 `13` 标记 partial，逐字稿未独立核验；来源 `14` 包含平台转录。小红书证据 `11` 来自媒体观察，不能写成自己已抽样原帖评论。
- 来源索引与 CSV 个别访问状态的粒度可能不同；按具体 claim 核查，不批量把 partial 改为 verified。EverCare 样本不是中国本地需求验证。
- 知识循环中存在 `test_lint_knowledge.py`，但本次盘点未找到它所对应的 `lint_knowledge.py`。未来写回先检查实际文件；脚本未运行不能报告 Lint 通过。

以上是截至本文件日期的检查线索，不是本轮修复任务；发现新证据时保留旧记录与替代关系。

## 现有调度的实际边界

`.codex/config.toml` 配置 subagent 开启、并发上限 4、默认 `gpt-5.6-terra`／`medium`。它没有设置本项目主会话默认模型。

`agent-roster.yaml` 中主控推荐 Terra／High，角色分工和升级条件属于工作流指导；`model-routing.md` 说明主控持有最终判断、专业 agent 返回材料。不能把 roster 中列出角色等同于运行时已经注册了同名可调用 agent。

本 skill 的 `agents/openai.yaml` 只提供 skill 的界面信息，不是 subagent 注册文件。运行时委派使用当前实际可用的工具；本 skill 不写入 `.codex` 或注册常驻团队。
