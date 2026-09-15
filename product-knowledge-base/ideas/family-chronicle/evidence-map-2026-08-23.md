# Family Chronicle 公开证据地图

Owner: Product Lead
Last updated: 2026-08-23
Source: `../../raw/SRC-20260823-family-chronicle-01.md` 至 `../../raw/SRC-20260823-family-chronicle-20.md`
Confidence: Medium-High
Related decisions: `../../decisions/one-person-pm-knowledge-loop-2026-08-23.md`
Next review date: 2026-09-06

## 支持的决策

公开证据是否足以支持把 Family Chronicle 保持在 Discovery，并投入一个可逆的「真实家庭第一卷」原型；不决定正式定价、长期订阅、公开发布或规模化开发。

## 证据覆盖

| 证据线 | 来源 | 能支持什么 | 不能支持什么 |
| --- | --- | --- | --- |
| 大型家族史商业信号 | [SRC-01](../../raw/SRC-20260823-family-chronicle-01.md)、[SRC-02](../../raw/SRC-20260823-family-chronicle-02.md) | 寻根、历史记录和家谱存在大规模用户与付费 | 跨人物编年网页的留存和付费 |
| 成书与低摩擦采集 | [SRC-03](../../raw/SRC-20260823-family-chronicle-03.md) 至 [SRC-06](../../raw/SRC-20260823-family-chronicle-06.md) | 用户可购买提示、口述整理和实体书结果；语音/电话是已存在形态 | 本项目的渠道、完成率或单位经济 |
| 家庭媒体与保存 | [SRC-07](../../raw/SRC-20260823-family-chronicle-07.md) 至 [SRC-10](../../raw/SRC-20260823-family-chronicle-10.md) | 家庭媒体分享、私密档案和长期导出是相邻需求 | 用户愿持续共同撰写家史 |
| 开源能力 | [SRC-11](../../raw/SRC-20260823-family-chronicle-11.md) 至 [SRC-15](../../raw/SRC-20260823-family-chronicle-15.md) | 家谱、协作、权限、GEDCOM、媒体和可视化已有成熟底座 | GitHub 热度不能证明市场需求；GPL/AGPL 不能未经审查进入闭源服务 |
| 直接时间线案例 | [SRC-16](../../raw/SRC-20260823-family-chronicle-16.md)、[SRC-17](../../raw/SRC-20260823-family-chronicle-17.md) | Twile 曾以家族时间线、协作和订阅定位，并被收购 | 没有可靠数据说明其实际付费、留存或后续停止原因 |
| 公开用户声音 | [SRC-18](../../raw/SRC-20260823-family-chronicle-18.md)、[SRC-19](../../raw/SRC-20260823-family-chronicle-19.md) | 长周期写作常被体验成作业，也有完成后高度珍视的反例 | Reddit 样本不能估算总体完成率或购买率 |
| 存续风险 | [SRC-20](../../raw/SRC-20260823-family-chronicle-20.md) | 平台停止与素材导出是必须提前设计的风险 | 竞品整理且原官方页失效，不能单独确认关闭全过程 |

## 已确认事实

1. **Fact**：大型家族史平台证明寻根、历史记录与家谱可以形成规模业务，但价值核心偏「发现未知资料」。证据：SRC-01、SRC-02。
2. **Fact**：Storyworth、Remento 与 Storii 均把采集故事和得到书册作为清楚结果，其中 Remento/Storii 明确降低写作或设备门槛。证据：SRC-03 至 SRC-06。
3. **Fact**：家庭相册、记忆保存和数字档案已有不同商业或非营利实现。证据：SRC-07 至 SRC-10。
4. **Fact**：家谱数据、协作、权限、关系视图和媒体管理已有成熟开源实现。证据：SRC-11 至 SRC-15。
5. **Fact**：Twile 曾直接提供互动家族时间线并发生收购。证据：SRC-16、SRC-17。

## 推断

1. **Inference**：较可信的切口不是再做一棵家谱树，而是把低摩擦采访、跨人物事件、多版本记忆、原始档案和阶段性成册组合起来。依据：产品线、开源线和用户线共同指向。
2. **Inference**：网页更适合作为持续浏览和修订载体，书册更适合作为完成感与购买结果；第一卷应同时拥有二者，不先押注纯订阅。
3. **Inference**：数据导出、来源、授权和冲突并列不是后台能力，而是核心信任设计；否则平台停止或家庭意见冲突会破坏长期价值。

## 假设

- 除发起人外，至少部分亲属愿意主动讲述、纠正、补充或回来浏览。
- 编年主线比相册、微信群、人物回忆录或一次性书册更容易理解家族关系。
- 家庭愿意接受清楚的 Owner、Contributor、Viewer 权限和敏感内容边界。
- 一次性第一卷能成为后续服务、订阅或自托管产品的有效入口。

## 冲突与反证

- 写作提示对部分家庭是珍贵的完成框架，对另一些家庭是高压力作业；不能只展示成功案例。
- Twile 的获奖、用户计划与收购证明关注和战略价值，不证明可持续独立商业模式。
- HereAfter 停止信息来自竞品整理，官方页面当前不可访问；只保留为存续风险信号。
- 开源项目成熟降低研发门槛，也说明技术底座不是主要差异化；许可证边界仍需正式审查。

## 证据缺口

- 一个真实家庭中非发起人的贡献率、纠错率、再次浏览率。
- 整理每个事件所需的人力时间，以及 concierge 模式能否被一人公司承担。
- 一次性网页＋书、订阅、采访成书服务三种价值捕获方式的真实承诺。
- 华语家庭的隐私冲突、代际设备习惯和语音完成率。

## 双轴评估

```yaml
eval_status: pass
research_quality: 91
validation_level: V1
critical_failures: []
weak_claims:
  - HereAfter 停止信息缺少可访问的一手公告
  - Twile 收购后留存与停止原因不可核实
missing_sources:
  - 自有家庭行为数据
  - 华语用户完成率与价值承诺
recommended_repairs:
  - 用一个真实家庭的第一卷原型取得 V2 所需行为代理
  - 对任何开源复用先做许可证审查
next_evidence: 非发起亲属的主动讲述、纠正、补充、再次浏览或索取成册行为
allowed_next_investment: 公开研究、素材准备、一个家庭的可逆 concierge 第一卷原型
pause_or_kill_condition: 只有发起人维护；时间线不优于相册或书；隐私无法达成；整理成本超出一人公司承受范围
reviewer: review_eval_agent
reviewed_at: 2026-08-23
```

分项：决策对齐 15/15；来源质量与覆盖 18/20；引用支持关系 18/20；事实/推断/假设分离 15/15；反证与冲突处理 9/10；决策价值 9/10；可维护性 7/10。可维护性待用下一次来源刷新验证。

## 当前结论

Research Quality 通过，但 Validation Level 仍为 V1。允许进入一个真实家庭、一个主题、20–30 个事件的可逆第一卷原型；不得宣称需求、长期协作、订阅或付费已经验证，也不进入完整平台开发。
