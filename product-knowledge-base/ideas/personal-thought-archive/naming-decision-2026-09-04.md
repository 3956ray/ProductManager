# 决策记录：「思」／「think」产品命名

Owner: Product Lead
Last updated: 2026-09-04
Source: `../../raw/SRC-20260904-personal-thought-archive-10.md`
Confidence: High（Product Lead 直接确认）
Related decisions: `prd-v0.1-2026-09-04.md`
Next review date: 2026-10-04

## 状态

Approved

## 决策

- 中文产品名称：`思`
- 英文产品名称：`think`
- 英文品牌在产品界面中默认使用小写形式。
- `personal-thought-archive` 继续作为内部项目代号和文件路径，不作为面向用户的品牌。
- 「个人思想档案」或「思想档案」可以继续用于解释产品类别和长期价值，但不作为正式产品名称。

## 背景

PRD v0.1 原先使用「思想档案」作为临时产品名。Product Lead 在 2026-09-04 明确确认正式中英文名称，因此需要把品牌名称与产品描述分开。

## 备选方案

| 选项 | 优点 | 缺点 | 备注 |
| --- | --- | --- | --- |
| 思／think | 已由 Product Lead 明确确认；中英文简短 | 商标、搜索辨识度与应用商店重名尚未核查 | Approved |
| 思想档案／Thought Archive | 直接解释产品用途 | 名称较长；仅保留为描述语 | Superseded as display name |

## 理由

这是 Product Lead 的直接品牌决策，不是根据市场研究推导的命名结论。当前记录只负责保持 PRD、界面文案和未来开发的一致性。

## 影响

- Android App 中文界面显示「思」，英文界面显示「think」；
- PRD、原型、图标 brief、应用商店草稿和后续测试统一使用该名称；
- 内部代码目录、数据库命名和项目 slug 暂不重命名，避免无产品价值的迁移；
- 对外发布前仍需检查商标、应用商店重名、域名和用户理解度。

## Research Quality / Validation Level 影响

命名决策不改变当前 Research Quality 86 或 Validation Level V2，也不扩大允许投入范围。

## 后续动作

1. 在可点击原型中测试用户是否把「思」理解为记录思考的产品；
2. 设计图标与启动页时同时验证单字品牌在小尺寸下的辨识度；
3. 公开上架前完成中文与英文商标、应用商店名称和域名检查。

## 复查触发条件

- 商标或应用商店存在不可接受的冲突；
- 核心用户无法理解或记住名称；
- 英文用户持续把 `think` 误解为其他类别，影响搜索或分发。
