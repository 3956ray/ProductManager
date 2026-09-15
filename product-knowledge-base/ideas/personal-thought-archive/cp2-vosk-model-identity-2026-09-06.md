# Vosk 中文小模型身份记录

Owner: Product Lead
Last updated: 2026-09-06
Source: `CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001`；已验收 R1 `cp2-alternative-offline-chinese-asr-evidence-cards-2026-09-06.md` 的 E-VOSK-02；续接 M01/M02 ledger；https://alphacephei.com/vosk/models 的 Chinese 小模型行
Confidence: Medium-High（模型目录身份已核定；制品内容、完整许可与签名未知）
Related decisions: `cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md`
Next review date: 2026-09-13
Research Quality: 82/100 · fail（整体续接身份准备，缺口在 Android 精确制品；首次 55 分保留为历史）
Validation Level: V2（沿用，不升级）
Next evidence: Leader 验收模型目录身份及整体运行库缺口；任何模型制品取得仍需独立授权
Allowed next investment: 本地证据整理及等待验收；不得请求模型文件辨认身份
Pause/Kill condition: 整体运行库精确制品未核定且 runtime 预算耗尽，停止并回产品门

## 当前摘要

续接 M02 成功读取官方模型目录，唯一模型固定为 `vosk-model-small-cn-0.22`，官方对象 `vosk-model-small-cn-0.22.zip`，条目标注 `42M`、`Apache 2.0`。名称与版本化下载入口已足以指认目录对象，但未请求该 ZIP，模型 SHA-256、签名、完整许可和实际内容均未知。整体仍因 Android runtime 精确版本绑定不足而停止。

## 首次身份字段（历史）

`Observed（R1）` 是历史已验收观察，非本轮官方访问结果。运行库首个请求失败后停止，没有发出模型目录请求；以下官方 URL 是 R1 已登记来源，并非已发生的本轮访问。

| 字段 | 状态 | 值／限制 | 官方 URL 与访问日期 |
| --- | --- | --- | --- |
| 精确模型名称与官方条目 | Unknown | R1 只记录中文小模型条目概述，本轮未核定精确名称 | https://alphacephei.com/vosk/models ，R1 2026-09-06；本轮未访问 |
| 版本／发布日期／修订身份 | Unknown | 不由体积或候选名称推断版本 | https://alphacephei.com/vosk/models ，R1 2026-09-06；本轮未访问 |
| 官方文件名／下载 URL | Unknown | 未取得可唯一指认的对象链接；不猜路径、不请求模型 | https://alphacephei.com/vosk/models ，R1 2026-09-06；本轮未访问 |
| 官方声明大小 | Observed（R1） | 约 42 MB 的中文小模型条目；非精确字节数，不能作为制品身份 | https://alphacephei.com/vosk/models ，R1 2026-09-06；本轮未访问 |
| 模型发布者与来源 | Observed（R1）＋Unknown | Alpha Cephei 官方目录；所选精确模型的发布者／修订尚未核定 | https://alphacephei.com/vosk/models ，R1 2026-09-06；本轮未访问 |
| 模型许可证入口与范围 | Observed（R1）＋Unknown | R1 中文小模型条目标 Apache-2.0；未核定精确制品完整许可／notice／再分发义务，不从 runtime 继承 | https://alphacephei.com/vosk/models ，R1 2026-09-06；本轮未访问 |
| 官方 checksum／SHA-256 | Unknown | 未查询到不是“官方没有”；没有模型本体散列 | https://alphacephei.com/vosk/models ，R1 2026-09-06；本轮未访问 |
| 官方签名 | Unknown | 未核定，不推断签名是否存在 | https://alphacephei.com/vosk/models ，R1 2026-09-06；本轮未访问 |

## 停止与限制

模型端点尝试 0/3，成功页面 0。完整原因见[身份就绪记录](cp2-vosk-identity-readiness-2026-09-06.md#访问-ledger)。不把未使用预算转为自动继续许可，不推进第二候选。

模型是否适用于所选 Android runtime、中文／口音／噪声准确率、专名 90%、词表机制、内存／CPU／性能／隐私和法律义务均未验证。未下载、加载或测试模型。

## 续接身份字段（2026-09-06）

下列字段仅据同一官方目录 M02：`https://alphacephei.com/vosk/models`，访问日期均为 2026-09-06；无需访问 ZIP。目录包含其他语言和大模型，但没有选择、比较或跟进这些对象。

| 字段 | 状态 | 当前证据与限制 | 官方 URL／日期 |
| --- | --- | --- | --- |
| 精确名称／条目 | Observed | Chinese 下 `vosk-model-small-cn-0.22`；说明为 `Lightweight model for Android and RPi` | https://alphacephei.com/vosk/models ，2026-09-06 |
| 版本／可区分修订 | Observed＋Unknown | 名称中版本 `0.22`；独立模型发布日期、不可变修订摘要 Unknown；网页 Last-Modified 不是模型发布日期 | https://alphacephei.com/vosk/models ，2026-09-06 |
| 官方对象文件名／下载入口 | Observed | `vosk-model-small-cn-0.22.zip`；`https://alphacephei.com/vosk/models/vosk-model-small-cn-0.22.zip`（只记录 href，未请求） | https://alphacephei.com/vosk/models ，2026-09-06 |
| 官方大小 | Observed | 原表写 `42M`，不换算为精确 bytes，非下载实测 | https://alphacephei.com/vosk/models ，2026-09-06 |
| 发布入口／来源 | Observed | Alpha Cephei Vosk 官方目录，同域托管对象；具体训练作者与权利链未核定 | https://alphacephei.com/vosk/models ，2026-09-06 |
| 模型许可证入口／范围 | Observed＋Unknown | 该模型同一行 License 列 `Apache 2.0`，不是由 runtime 推断；ZIP 内完整 LICENSE、notice、第三方权利与再分发审查未知 | https://alphacephei.com/vosk/models ，2026-09-06 |
| 官方 checksum／SHA-256 | Unknown | 该行未列 checksum；未查询所有官方来源，不能声称官方没有；未计算制品散列 | https://alphacephei.com/vosk/models ，2026-09-06 |
| 官方签名 | Unknown | 该行未列签名，未获取或验证签名 | https://alphacephei.com/vosk/models ，2026-09-06 |

必要短摘录：`vosk-model-small-cn-0.22 | 42M | Lightweight model for Android and RPi | Apache 2.0`（仅引用身份相关列）。目录的基准误差率、通用内存估计及“大多数小模型可重配词表”不是本产品专名 90% 或真机验证，未升级相关能力结论。

模型累计尝试 2/3：M01 沙箱代理连接失败，M02 经网络权限批准后成功读取同一 URL；两次均计入预算。剩余 1 次不挪给 runtime，也不为用完预算读取不必要页面。
