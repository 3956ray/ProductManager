# 产品团队作战板

Owner: Product Lead
Last updated: 2026-08-18
Source: Manual setup；ChatGPT 分享讨论；外部公开数据调研
Confidence: Draft
Related decisions: 暂无
Next review date: 2026-08-31

## 当前进行中

| 项目 | Owner | 阶段 | 目标指标 | 状态 | 下一步 | 截止 |
| --- | --- | --- | --- | --- | --- | --- |
| 产品知识 loop | Product Lead | Setup | 团队运转清晰度 | Research workflow pilot complete | 首次 eval 为 82/100 · revise；补齐原型用户行为证据后复评 | 2026-08-25 |
| Rapid Situation Interpreter | Product Lead | Discovery | 验证问题强度和 MVP 切口 | Research complete | 产出访谈招募 screener 和 Wizard-of-Oz 音频测试评分表 | 2026-07-29 |
| 中国城市日常沉浸体验 | Product Lead | Discovery | 验证外国游客是否愿为普通城市日常付费 | Positioning proposed | 等待 Product Lead 决定是否测试 After Work in Shanghai | 2026-07-29 |
| 哎呀，早知道 | Product Lead | Prototype | 验证单输入、结果理解、图片分享与额度付费意愿 | PRD v0.1 approved | 设计手机网页交互原型与中英文「后悔账单」 | 2026-08-21 |

## 候选/下一步

| 候选事项 | 为什么现在做 | 证据 | Owner | 需要决策 |
| --- | --- | --- | --- | --- |
| 接入反馈来源 | 让知识库自动保持更新 | 待确认来源列表 | Product Lead | 先接 Slack、Notion、Drive、Linear/Jira 还是客服系统 |
| Rapid Situation Interpreter | 新产品 idea，已完成初步讨论 | ChatGPT 分享讨论 + 初步外部调研 | Product Lead | 选择第一验证人群和语言对 |
| 城市兴趣体验与消费地图 | 新产品 idea，已完成中美欧初步数据调研 | ChatGPT 分享讨论 + 政府/行业/公司公开数据 | Product Lead | 选择首发城市和首发品类；建议在卡牌/模型与钓鱼中二选一 |
| 中国城市日常沉浸体验 | 新产品 idea，竞品与五套定位已完成初步调研；定位与价格均未验证 | ChatGPT 分享讨论 + 国际/中国竞品 + 官方入境游数据 | Product Lead | 是否以 After Work in Shanghai 作为第一验证产品；未批准任何对外价格、渠道承诺或上线时间 |
| CTP 古籍阅读体验现代化 | CTP 内容与研究能力很强，但新读者、移动端和无障碍体验存在明显改进空间 | Product Lead 提议 + CTP 官方页面、API 与前端结构初步审计 | Product Lead | 是否先做《道德經》三章的高拟真阅读模式原型；未批准对外联络或完整改版承诺 |
| 工业设备报警上下文数据传输 | 工程师当前可能只收到报警、不同时收到判断所需的设备数据；“设备无数据”还是“通知不带数据”尚未核实 | Product Lead 口述需求；学长 2026-08-04 补充回答 | Product Lead | 取得一条真实报警和后续所查数据，确认数据来源、接口、时间窗与送达渠道；未批准生产接入、外部承诺或自动控制 |
| 女朋友专属跨端线条小狗宠物 | 私人礼物需要把角色喜好、算法开发工作节奏和伴侣留言结合成长期陪伴，而非普通循环动画 | Product Lead 口述想法 | Product Lead | 确认手机/电脑系统、可用素材来源，以及是否严格限于私人使用 |
| AI 护理交班草稿器「班安」 | 台湾不同层级与班别的护病比约为 1:6 至 1:15；交班与护理纪录已有明确节时案例，但同类方案不空白 | Product Lead 提议；卫福部政策与指引；台湾医院公开案例 | Product Lead | 是否先访谈 5–8 名区域／地区医院病房护理师，并用 20 个虚构／脱敏音档验证可追溯草稿 |
| 私人家庭史／家族编年网页 | 家庭史、口述回忆录和私人相册均有成熟需求信号，但「全家共建的跨人物编年史」持续使用尚未验证 | Product Lead 口述 idea；商业产品、Twile 历史与 GitHub 开源仓库调研 | Product Lead | 是否先为一个真实家庭完成 20–30 个事件的《家族纪事·第一卷》原型；先验证一次性成册还是长期网页 |

## 阻塞

| 阻塞 | 影响 | 需要谁处理 | Owner | 提出日期 |
| --- | --- | --- | --- | --- |
| 未选择来源系统 | Agent 还不能持续摄取真实反馈 | Product/ops | Product Lead | 2026-07-22 |

## 待决策

| 决策 | 选项 | 建议方 | 批准人 | 截止 |
| --- | --- | --- | --- | --- |
| 第一个接入来源 | Slack、Notion、Google Drive、Linear/Jira、客服工具 | Product Manager Agent | Product Lead | TBD |
| Rapid Situation Interpreter 的第一版 MVP 方向 | 第三方倾听理解、实时现场态势理解、事后跨语言事件时间线、创作者漫画工作流 | Product Manager Agent | Product Lead | 2026-07-29 |
| 第一目标人群 | 在日本/韩国生活的中文留学生/新移民、短期游客、家庭旅行决策者、内容创作者 | Research Agent | Product Lead | 2026-07-29 |
| 城市兴趣体验与消费地图首发切口 | 单一城市的卡牌/模型、单一城市的钓鱼 | Research Agent | Product Lead | 2026-07-29 |
| 中国城市日常沉浸体验第一定位 | 首次来华文化好奇者、商务短停留者、城市深度探索者、内容创作者、亲子家庭 | Research Agent | Product Lead | 2026-07-29 |
| 城市兴趣体验与消费地图定位 | 新手第一次、实时兴趣场次、单一兴趣专业地图、周末兴趣方案、兴趣门店增长工具 | Research Agent | Product Lead | 2026-07-29 |
| CTP 第一验证产物 | 《道德經》三章阅读模式原型、全站 UX 审计、直接联系维护者 | Product Manager Agent | Product Lead | 2026-08-10 |
| 工业设备告警项目协作架构 | 飞书作为业务协作主入口、GitHub 作为研发主入口、Codex 知识库作为分析记忆；是否同时创建远程仓库 | Product Manager Agent | Product Lead | 2026-08-11 |
| 卖飞之后首发切口 | 普通散户的平行持仓档案、财经创作者内容工具、媒体/社区嵌入组件 | Product Manager Agent | Product Lead | 2026-08-18 |
| 卖飞之后第一市场 | A 股、台股、美股、加密资产 | Product Manager Agent | Product Lead | 2026-08-18 |
| 家庭史第一验证形态 | 私人编年网页＋PDF／实体书、个人口述回忆录礼物、传统家谱研究工具 | Product Manager Agent | Product Lead | 2026-08-31 |

## 新信号

| 信号 | 来源 | 摘要 | 置信度 | 建议动作 |
| --- | --- | --- | --- | --- |
| 需要当前项目可视化 | 团队设计讨论 | 把作战板作为知识库首页 | High | 保持 `BOARD.md` 为第一个上下文文件 |
| 产品调研流程标准化 | Product Lead 2026-08-18 明确批准；OpenAI Docs；GitHub 与社区调研 | 已把决策定义、来源分级、Evidence Cards、独立核查、100 分质量门、审批后写回和差异监控纳入知识 loop | High | 在第二个不同类型项目上测试通用性；累计两次后复核 skill |
| 产品调研首次回放 eval | `product-research` 只读前向测试；「哎呀，早知道」现有 PRD 与决策记录 | 结论收缩为「可进入低风险原型验证」，未误判为需求或付费已验证；82/100，因缺少真实用户行为与模板测试标为 revise | High | 完成首轮原型任务、理解度与裁切测试后重新评分；第二个不同类型项目再测通用性 |
| 产品 idea：Rapid Situation Interpreter | ChatGPT 分享讨论 | 更强切口是「现场态势理解」，不是泛翻译或漫画生成 | Medium | 先做用户验证，再进入 PRD |
| 翻译市场拥挤 | 外部调研 | Google、Apple、Papago、Samsung、Microsoft、Timekettle 已覆盖实时对话翻译 | High | 用事件解释、相关性、不确定性和证据链做差异化 |
| 工作区应中文优先 | 用户反馈 | 中文母语者读中文更快，英文会降低产品团队运转速度 | High | 将知识库正文和模板改为中文优先 |
| RSI 十年趋势评估完成 | Subagent 调研 + 外部资料 | 2016-2026 数据支持继续 Discovery，但不支持立即进入 PRD；第一验证人群建议为在日中文留学生，首发语言对日语 -> 中文 | Medium-High | 进入访谈招募和音频 Wizard-of-Oz 设计 |
| RSI 核心场景澄清 | 产品负责人反馈 | 绝大多数情况下用户是第三方倾听者，不参与对话；核心需求是理解他人聊天、现场讲话或广播内容，而不是判断自己是否需要行动 | High | 把 MVP 输出改为「内容大意/脉络/关键原话/不确定性」优先 |
| 新 idea：城市兴趣体验与消费地图 | ChatGPT 分享讨论 | 原始「男孩子的快乐」更可行的切口是帮助用户发现附近可实际体验、购买或报名的兴趣地点与活动，而不是兴趣短视频聚合 | Medium | 保持 Discovery；先做一个城市、一个品类的 POI 供给审计与无 App 原型 |
| 中美欧休闲与兴趣数据 | 政府统计、行业协会、公司披露 | 三地均有较大线下兴趣参与和消费基础；钓鱼规模可量化，卡牌/桌游更符合「地点 + 活动 + 消费」飞轮；区域数据不可直接混算 | Medium | 中国、美国、欧洲分别建数据和规则；不以宏观人数直接估算 TAM |
| 新 idea：中国城市日常沉浸体验 | ChatGPT 分享讨论 | 核心不是景点或攻略，而是由可信本地人提供 Access、Context、Connection，帮助外国游客理解普通中国城市生活 | Medium | 保持 Discovery；先验证一个固定主题小团，不先做开放式 marketplace |
| 本地体验赛道已拥挤 | 国内外竞品调研 | Withlocals、Airbnb Experiences、ToursByLocals、Showaround、GuruWalk、食物团和中国本地生活路线均已覆盖 local/authentic/hidden gems 心智；建议的差异化尚未验证 | High | 测试可信 Host + 普通日常 + 跨文化解释 + 可靠履约能否形成可感知溢价 |
| 上海入境需求上行 | 官方统计 | 2025 年上海接待约 936 万入境游客，其中外国游客约 714 万；但人次不能直接推算订单 TAM | High | 若批准上海首测，使用 US$79 真实全额付款转化与明确退订规则判断需求 |
| Host marketplace 有较高合规与安全成本 | 中国法规与产品分析 | 改称 Host 不会自动规避导游、旅行社、在线旅游经营、保险和平台核验责任 | Medium-High | 首轮与持证旅行社/导游合作，实验前进行本地法律与主管部门核验 |
| 兴趣地图竞品定位分析 | 竞品官方产品页和公司披露 | 通用地图、活动票务、垂直工具和品牌官方 App 已覆盖地点、活动或专业数据；较清晰的空白是帮助新手完成第一次行动 | Medium | 优先验证「新手第一次」，用「实时兴趣场次」作为对照定位 |
| 兴趣地图 GitHub 仓库扫描 | GitHub Search、Repository API、仓库 README/License | 基础地图、RSVP、票务和垂直工具已有开源实现；Pinball Map 是最接近的垂直样板，但未发现成熟的跨兴趣新手行动地图 | Medium | 地图和票务优先集成；把研发重点放在垂直数据模型、更新机制和新手字段 |
| 新增 Dan Koe 创作者商业框架 | Dan Koe YouTube 视频、官方书面版、英文自动字幕 | 可将「痛点—表达—分发—Offer—行为反馈—放大信号—建立世界」作为 creator-led idea 的辅助评审框架；互动不等于需求，需保留支付、留存与产品证据 | Medium-High | 涉及个人品牌、内容分发、知识产品或创始人驱动增长时，调用 `references/dan-koe/dont-quit-chinese-decision-framework.md` |
| 新增 Dan Koe AI 一人公司与金额框架 | Dan Koe YouTube、官方书面版、公开 Eden 模板、英文时间字幕与影片画面 | 商业基本方程未因 AI 改变；应以 Brand–Content–Offer、收入/成本方程、人工质量标准和真实反馈判断 AI 是否创造价值。US$1M 为教学拆解，不是 forecast | Medium-High | 涉及 AI agent、一人公司、服务/产品选择、定价或收入目标时，调用 `references/dan-koe/build-1m-one-person-business-ai-chinese-reference-framework.md` |
| 新 idea：CTP 古籍阅读体验现代化 | Product Lead 提议；CTP 官方页面、FAQ、API 与公开前端结构 | CTP 拥有强大的结构化古籍、检索、版本、影印本和协作能力；机会是增加现代阅读体验层，而不是重建资料库。项目目前由 Dr. Donald Sturgeon 主编维护，不宜先称为“协会” | Medium | 保持 Discovery；先验证维护者需求，并以《道德經》三章原型证明阅读、来源与研究工具可以更清楚地结合 |
| 新 idea：工业设备智能告警与维修分诊 | Product Lead 口述需求；学长与现场老板的初步交流 | 可能的核心价值不是直接预测故障，而是把大量信号聚合为可解释、可分派、可回写结果的风险事件；历史数据是否能关联到真实故障和维修结果尚未确认 | Low-Medium | 保持 Discovery；先访谈老板与工程师，并对单站点/单机型做数据—告警—工单可追溯性审计 |
| 工业设备告警项目需要跨系统协作 | Product Lead 协作设想；飞书与 GitHub 官方能力 | 飞书适合承载需求、工作流和人类审批，GitHub 适合代码、Issues 和 Pull Request；需要避免 PRD 多份可编辑副本 | Medium-High | 先以链接和唯一 Requirement ID 手动串联一条完整流程，再决定是否自动同步 |
| 工业设备需求收敛为“报警 + 数据送达” | 学长 2026-08-04 回答 | 当前主要价值可能是让工程师收到报警时同时取得设备数据，而不是预测；仍需区分“通知不带数据”和“现场没有数据通道” | Medium | 查看一条真实报警，列出工程师随后查找的数据；据此决定做软件消息卡片还是单设备采集/传输验证 |
| 新 idea：卖飞之后/平行持仓档案 | Product Lead 口述灵感；高度相似竞品公开页面 | 「计算少赚多少 + 分享图」已有直接竞品；更可取的差异化是持续追踪售出资产、双向呈现卖飞与避险，并以创作者工具优先验证付费 | Medium | 保持 Discovery；先选择一个市场与一个用户群，验证真实记录完成率、分享率、保存率和创作者付费意愿 |
| 卖飞之后交互收敛为单输入框 | Product Lead 产品方向确认；Web Share API 与 Snap Creative Kit 官方能力 | 首发只暴露自然语言文本输入；AI 免费解析与资料确认在登录和额度之前；确定性引擎负责计算；第一版只支持做多股票、ETF 与现货加密 | High | 按已批准流程设计交互原型，并验证登录草稿恢复 |
| 卖飞之后首发采用图片额度定价 | Product Lead 定价与付费时机决定 | US$1/2 张、US$2/5 张、US$3/10 张；AI 免费解析与卖飞资格判断后才登录和使用额度；成功保存才扣额度；不提供付费前最终数字 | High | 原型使用模拟额度；真实收款前确定支付渠道与商户地区 |
| 卖飞之后生成图自动进入私人账户 | Product Lead 产品方向确认 | 成功图片自动保存到用户账户，可重复下载和分享；购买与永久额度绑定账户；首发不接收交易截图 | High | 定义用户删除图片、交易摘要和整个账号时的数据删除规则 |
| 卖飞之后品牌方向 | Product Lead 命名决定；英文公开搜索 | 中文正式品牌采用「哎呀，早知道」，英文采用 `I Knew It`；网页副标题建议 `What if you never sold?`；应用商店已有近似同名非金融应用 | High | 原型统一使用中英文正式品牌；正式发布前核查商标、域名、应用商店和社交账号 |
| 卖飞结果图片主文案确认 | Product Lead 明确确认 | 中文保留「不然」的人类口语表达；英文采用 `Ugh… I knew ... was gonna take off. If I’d held, I’d be up another ... right now.`；其中金额必须是相对实际卖出额外错过的收益 | High | 定义下跌、清算、零收益和估算结果的对应文案 |
| 卖飞之后计算口径确认 | Product Lead 明确确认 | 使用实时价格与当前汇率；默认不计股息，用户明确要求时才触发；自动处理拆股；不计税费和手续费；不追踪卖出资金用途；不支持分批交易；AI 解析错误免费重算 | High | 定义复杂杠杆、期货、永续与期权公式；确认股息是否再投资及行情中断降级策略 |
| 卖飞之后账号、额度与退款规则确认 | Product Lead 明确确认；支付渠道官方资料 | 首发仅 email、微信或手机号登录；删除截图识别；额度与图片绑定账号且永久有效；成功保存才扣额度；系统失败自动返还；整包未使用可退款 | High | 确认收款主体注册地；据此在 Stripe Checkout 与商户记录方方案间选择 |
| 微支付固定费用风险 | Lemon Squeezy、Paddle、PayPal 官方定价 | Lemon Squeezy 与 Paddle 标准价为 5% + US$0.50；PayPal 美国普通 Checkout 固定费为 US$0.49。US$1 套餐可能被固定费用吞噬大部分收入 | High | 支付渠道确定后测算三档真实贡献毛利；若 US$1 档为负，作为限量获客档或测试小额支付费率 |
| 卖飞之后首发固定模板 | Product Lead 明确确认 | 首发固定模板采用「后悔账单」；默认显示错过的金额，可切换百分比；始终隐藏本金、卖出所得与数量；AI 只做文字结构化提取，图片由程序渲染 | High | 设计中英文共用模板，并用超长资产名、大额数字和五个平台裁切做压力测试 |
| 卖飞之后退款与 Stripe 方向确认 | Product Lead 明确确认 | 整包完全未使用可在购买后 7 天内全额退款；不做部分退款；系统失败返还额度。Stripe Checkout 保留为后续方向，不阻塞当前原型 | High | 先完成原型与核心流程验证；真实收款前再确认商户注册地、Stripe 资格、税务与各地支付方式 |
| 卖飞之后金额与百分比共用额度 | Product Lead 明确确认 | 同一笔交易的金额版与百分比版属于同一个图片故事，共同消耗 1 张额度；生成后切换、下载和分享不重复扣费 | High | 在固定模板中验证金额与百分比两种状态的排版和理解度 |
| 卖飞之后首发资产与价格口径确认 | Product Lead 明确确认 | 第一版只支持无杠杆股票、ETF 与现货加密资产；使用生成时最新可用价格，休市股票使用最近收盘价，价格不可用则停止生成并返还额度 | High | 选择覆盖目标市场且允许结果图展示的行情与企业行动数据源 |
| 卖飞之后登录保留输入 | Product Lead 明确确认 | 登录前保存匿名草稿；email、微信或手机号登录成功、取消或失败后都返回原步骤，并恢复原始文本、AI 解析资料与用户修改内容 | High | 在交互原型中测试同标签、新标签 magic link、取消登录与支付失败四条恢复路径 |
| 哎呀，早知道 PRD 获批 | Product Lead 2026-08-07 明确回复「全部按建议」 | PRD v0.1 三个阻塞项已批准：AI 免费解析在登录与额度前；非卖飞不出图不扣额度；百分比采用卖出后涨幅口径 | High | 进入手机网页交互原型和中英文固定模板设计 |
| 新 idea：女朋友专属跨端线条小狗宠物 | Product Lead 想为喜欢线条小狗、从事算法开发的女朋友制作手机与电脑专用宠物 | 电脑端应承载常驻陪伴与专注互动，手机端先用小组件和留言延伸；IP 素材、设备组合和是否公开发行尚未确认 | Medium | 先确认设备与素材；以私用、离线优先的电脑端原型验证手感，不先做账号和云同步 |
| 新 idea：AI 护理交班草稿器「班安」 | Product Lead 希望用一个小型 AI 产品缓解台湾医护人力压力；官方护病比依层级与班别为 1:6 至 1:15，并非统一 1:8 | 台湾已有多家医院公开语音护理纪录与交班摘要的节时成果，证明问题真实；但大型医院多有自研或整合方案，市场差异化尚未验证 | Medium | 保持 Discovery；先访谈 5–8 名区域／地区医院病房护理师，再用虚构／脱敏音档验证「口述→可追溯草稿→人工确认」能否节省至少 30% 时间且不增加关键事实错误 |
| 新 idea：私人家庭史／家族编年网页 | Product Lead 希望为一个家庭建立类似家族史书的长期网页 | Ancestry、Storyworth、Remento 与 FamilyAlbum 证明寻根、成书和家庭照片有付费／规模信号；最接近互动时间线的 Twile 被收购后仍消失；GitHub 的成熟能力集中在家谱和媒体管理 | Medium | 采用「编年体主线＋人物列传＋事件多视角＋档案证据＋定期成册」；先做一个家庭、一个主题、20–30 个事件的第一卷，不先做完整平台 |
| 父母／祖辈个人回忆录市场 | US$59–149 自助／语音成书与高价真人采访两端均已形成产品带；华语市场已有 ¥888 AI 回忆录、¥5,999 访谈成书及人民币 2–8 万元代写服务 | Storyworth、Remento、Storii、Meminto、LifeBook、LifeBio、HereAfter 与华语产品／行业报道 | Medium-High | 下一轮用同一段故事实测 4 个代表产品；重点判断语音完成率、子女参与、华语渠道和原始素材可导出性，不把标准功能误当差异化 |

## Agent 备注

| Agent | 备注 | 动作 |
| --- | --- | --- |
| Product Manager Agent | 产品调研采用 manager-as-tools；`source_scout_agent` 只收集证据，`evidence_verifier_agent` 独立核查，最终建议仍由 Manager 综合。 | 查看 `.agents/skills/product-research/SKILL.md` 与 `decisions/product-research-workflow-2026-08-18.md` |
| Product Manager Agent | 使用 manager-style loop 和边界清楚的 specialist agents。 | 查看 `agents/agent-roster.yaml` |
| Research Agent | Rapid Situation Interpreter 在获得真实音频和目标用户证据前，应保持 Discovery。 | 查看 `ideas/rapid-situation-interpreter/research-brief.md` |
| Product Manager Agent | RSI 的差异化不是翻译，而是「第三方倾听理解 + 证据 + 不确定性」。 | 查看 `ideas/rapid-situation-interpreter/ten-year-trend-evaluation-2026-07-22.md` |
| Research Agent | 城市兴趣体验与消费地图的数据支持继续 Discovery，但不足以证明独立 App 或泛兴趣聚合成立。 | 查看 `ideas/city-interest-experience-map/market-data-research-2026-07-22.md` |
| Research Agent | 待验证的差异化假设不是 hidden gems，而是能否把可信 Host、普通日常、跨文化解释和履约保障同时产品化，并形成可感知溢价。 | 查看 `ideas/china-local-life-experiences/competitor-positioning-research-2026-07-22.md` |
| Research Agent | 城市兴趣体验与消费地图首选定位为「新手第一次」，定价均为待验证假设，不能视为正式价格。 | 查看 `ideas/city-interest-experience-map/competitor-positioning-options-2026-07-22.md` |
| Research Agent | GitHub 扫描说明代码不是主要壁垒；Pinball Map 值得拆解，但 GPL/AGPL、独立数据许可和无许可证仓库都不能未经审查进入商业代码。 | 查看 `ideas/city-interest-experience-map/github-repo-landscape-2026-08-01.md` |
| Research Agent | 家庭史市场已验证的是史料发现、低摩擦口述和实体成果，不是纯时间线订阅；第一验证产物应是一卷可浏览、可导出、可成册的真实家庭样本。 | 查看 `ideas/family-chronicle/idea-brief.md` |
| Research Agent | 父母／祖辈回忆录已形成从低价自助成书到高价真人代写的完整价格带；最大未解问题是完成率，“一年 52 个问题”常把礼物变成作业。互动数字人格产品 HereAfter 已停止服务，原始素材导出与平台存续必须成为基础要求。 | 查看 `ideas/family-chronicle/elder-memoir-market-research-2026-08-17.md` |
| Product Manager Agent | AI 无法直接补足护理人力；最小且相对低风险的切口是只整理护理师已口述事实的交班草稿。正式临床测试前必须经过院方风险、个资、资安与临床流程审批。 | 查看 `ideas/ai-nursing-handoff-draft/idea-brief.md` |
