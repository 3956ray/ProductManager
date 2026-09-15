# 决策记录：CP0 延后但不阻塞可逆开发

Owner: Product Lead
Last updated: 2026-09-05
Source: `../../raw/SRC-20260905-personal-thought-archive-01.md`
Confidence: High（Product Lead 直接确认）
Related decisions: `prd-v0.1-2026-09-04.md`；`naming-decision-2026-09-04.md`
Next review date: 2026-09-19

## 状态

Approved

## 决策

1. `prd-v0.1-2026-09-04.md` 继续作为「思（think）」当前产品范围基线。
2. 小米 15 是 Product Lead 本人持有、可随时用于后续验证的设备。
3. 现在不要求先完成完整实机审计，可以直接开始 PRD 范围内的可逆开发。
4. CP0 完整实机审计属于延后，不是删除。
5. 需要形成 ASR、权限、提醒的通过结论，或进入父亲 Alpha 时，仍必须用小米 15 提供真实设备证据。
6. 现有 Android Studio Empty Project 安全审查文档已获 Product Lead 批准提交；此批准不等于安全审查中的工程整改项自动通过。

最小解释：

> CP0 完整实机审计不再阻塞开发启动，但属于延后而不是删除；需要验证 ASR、权限、提醒或进入父亲 Alpha 时，仍用小米 15 提供证据。

## 保持不变

- 当前 PRD 的产品目标与 P0/P1；
- 正常录入三步、正常找回三步；
- 原始录音不落盘、不上传；
- 本地 `sherpa-onnx` 语音识别路线；
- 不扩大到账号、同步、支付、Flutter、KMP、公开发布或云端语音识别；
- 当前 Research Quality 86 与 Validation Level V2；
- `/Users/orderly_ray/Projects/think` 仍由开发工作流管理，本次产品同步不修改该仓库。

## 允许立即开始的可逆开发

- Compose 页面骨架与三步交互原型；
- 使用 fake 数据的录入、搜索、模块与记录详情流程；
- Room／FTS 的本地数据骨架与自动测试；
- `AsrEngine`、`CalendarSource`、`ReminderScheduler`、`AiClassificationClient` 接口边界；
- 安全审查已指出的模板基线修正与相应文档同步。

以上工作不能声称 ASR、日历权限、后台提醒或父亲实际使用已经通过验证。

## 延后的 CP0 证据

在以下任一节点前，补齐对应的小米 15 实测，而非一次性阻塞所有开发：

| 节点 | 必须补齐的证据 |
| --- | --- |
| 宣布 ASR 门禁通过 | Android/API、ABI、内存、存储、模型包体、30/90 秒延迟、发热、OOM、飞行模式与音频不落盘 |
| 宣布日历权限／导入通过 | Calendar Provider 可见日历、只读权限、字段完整度、Outlook 可见性与重复导入 |
| 宣布提醒门禁通过 | 通知权限、后台／被划掉／重启／省电模式的到达和 deep link |
| 进入父亲 Alpha | 可安装测试 APK、核心权限状态、ASR 与提醒基础门禁、父亲所需的脱敏真实样本与同意 |

## 安全审查提交批准的解释

开发仓库只读检查显示，安全审查文档已经位于本地提交 `1019963 docs: add Android project security review`，当前 `main` 相对 `origin/main` 领先 3 个提交。本决定确认这些现有安全审查文档可以提交，但不授权本任务 push、修改开发仓库或忽略审查中列出的 Wrapper、依赖校验、自动备份、包名和版本等整改项。

## Research Quality / Validation Level 影响

- Research Quality：保持 86，不因调整顺序增加研究质量。
- Validation Level：保持 V2；开始写可逆代码不是自有产品真实使用证据。
- Allowed next investment：仍仅限 Android 技术样机、可点击原型和父亲单用户 Alpha。

## 风险与控制

| 风险 | 控制 |
| --- | --- |
| 开发先行后忘记 CP0 | 把实机证据绑定到 ASR、权限、提醒和 Alpha 的通过门，而非绑定到开发第一天 |
| 模拟器结果被当作真机结论 | Checkpoint 报告必须标明设备；通过结论必须包含小米 15 证据 |
| “允许开发”被误解为范围扩张 | 本决策逐项重申不允许的账号、同步、支付、跨平台、公开发布和云端 ASR |
| 安全文档已提交被误解为风险已修复 | 保留原审查结论；整改项仍需各自验证后关闭 |

## 后续动作

1. 开发侧把本决策同步到 PRD 快照、开发指南与文档索引；
2. 直接从可逆的 Compose 交互／本地数据骨架开始；
3. 在首次宣告 ASR、权限或提醒通过前，安排小米 15 对应实测；
4. 进入父亲 Alpha 前完成所需 CP0 子集并保存证据。

## 复查触发条件

- 开发需要宣布任一真机相关 checkpoint 通过；
- 准备进入父亲 Alpha；
- 目标设备不再是小米 15，或 Android／HyperOS 环境发生重大变化；
- 出现任何要求扩大 PRD 范围的提议。
