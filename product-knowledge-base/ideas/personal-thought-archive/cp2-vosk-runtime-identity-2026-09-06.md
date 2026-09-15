# Vosk Android runtime 身份记录

Owner: Product Lead
Last updated: 2026-09-06
Source: `CP2-VOSK-OFFICIAL-IDENTITY-INTAKE-001`；已验收 R1 `cp2-alternative-offline-chinese-asr-evidence-cards-2026-09-06.md` 的 E-VOSK-01/02/03；访问 ledger R01、R02、R03；官方安装说明与 release JSON（下方引用）
Confidence: Medium（官方项目发布和包名已知，精确 Android 制品绑定未核定）
Related decisions: `cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md`
Next review date: 2026-09-13
Research Quality: 82/100 · fail（续接身份准备；首次 55 分保留在就绪历史，不改变 R1 的 92 分）
Validation Level: V2（沿用产品行为证据，不升级）
Next evidence: Leader 裁定 Android 精确发行版本／坐标绑定缺口；runtime 3/3 预算已用尽，本任务不自行恢复
Allowed next investment: 本地证据整理及等待验收；无制品取得或执行权限
Pause/Kill condition: 精确运行库身份无法固定，停止并回产品门

## 当前摘要

续接已确认官方安装说明的 Android 包名 `com.alphacephei:vosk-android` 与项目 release `v0.3.50`，但两者之间没有精确版本绑定证据。不能把动态范围 `0.3.32+` 改写成固定 `0.3.32`，也不能把项目 tag 自动换算为 Android 包版本。当前仍未唯一指认精确 Android 制品，整体结果见[就绪记录](cp2-vosk-identity-readiness-2026-09-06.md)。

## 首次记录与证据边界（历史）

未能固定一个精确 Android runtime。官方仓库入口由已验收 R1 确认，2026-09-06 本轮尝试读取该入口失败；没有收到官方页面正文或元数据。服务错误不是 Vosk 项目、安全或许可证结论。

本页 `Observed（R1）` 仅表示已有已验收来源中的观察，不声称本轮重新访问成功。字段日期均为 2026-09-06；Unknown 是未核定，不是官方不存在。

| 字段 | 状态 | 值／限制 | 官方 URL 与访问日期 |
| --- | --- | --- | --- |
| 项目与维护者 | Observed（R1） | Vosk；Alpha Cephei；本轮未重新核实 | https://github.com/alphacep/vosk-api ，2026-09-06（R1；本轮失败） |
| 官方源码仓库身份 | Observed（R1） | `alphacep/vosk-api`，仅仓库归属，不含 commit 或源码身份 | https://github.com/alphacep/vosk-api ，2026-09-06（R1；本轮失败） |
| 精确 release／tag／version | Unknown | 没有返回发行元数据；不得猜版本 | https://github.com/alphacep/vosk-api ，2026-09-06（失败） |
| Android 发行坐标／精确分发入口 | Unknown | R1 只支持 Android API 能力，不固定 Maven 坐标或具体包；仓库首页不等于精确分发入口 | https://github.com/alphacep/vosk-api ，2026-09-06（失败） |
| runtime 许可证入口／范围 | Observed（R1）＋Unknown | R1 记录仓库 Apache-2.0 标识；精确 Android 包的许可证、依赖、notice 与适用范围未核定；未取得 LICENSE 正文 | https://github.com/alphacep/vosk-api ，2026-09-06（R1；本轮失败） |
| 官方 checksum／SHA-256 | Unknown | 未取得元数据；不能声称官方未发布，也无本地制品散列 | https://github.com/alphacep/vosk-api ，2026-09-06（失败） |
| 官方签名 | Unknown | 同上；未验证签名或签名者 | https://github.com/alphacep/vosk-api ，2026-09-06（失败） |
| 官方 SBOM | Unknown | 同上；未取得依赖清单 | https://github.com/alphacep/vosk-api ，2026-09-06（失败） |

## 访问与停止

完整尝试、预算、错误及最终 URL 限制见[身份就绪记录](cp2-vosk-identity-readiness-2026-09-06.md#访问-ledger)。运行库计入 1/3 个端点尝试，成功页面 0；没有重试、遍历源码树、请求实现源码或制品。

Android ABI、CPU-only、JNI、内存 PCM、音频不落盘、不上传、不进入日志、缓存与 buffer 生命周期、个性词表专名 90%、小米 15 性能与稳定性均未验证。阶段 B/C 未获授权。

## 续接身份字段（2026-09-06）

| 字段 | 状态 | 当前证据与限制 | 官方 URL／访问日期 |
| --- | --- | --- | --- |
| 官方项目／维护者 | Observed | Alpha Cephei 官方站直接指向 `alphacep/vosk-api`；R03 的 release author 为 `nshmyrev`，仅指该 release 发布账号，不推定独占维护或法律权利 | https://alphacephei.com/vosk/install ；https://api.github.com/repos/alphacep/vosk-api/releases/latest ，2026-09-06 |
| 项目精确 release／tag | Observed | `v0.3.50`，release id `152196573`；published_at=`2024-04-22T13:02:41Z`；draft=false，prerelease=false，immutable=false | https://api.github.com/repos/alphacep/vosk-api/releases/latest ，2026-09-06 |
| 固定 release 页面指针 | Observed | JSON 的 html_url 为 `https://github.com/alphacep/vosk-api/releases/tag/v0.3.50`；只记录未访问 | https://api.github.com/repos/alphacep/vosk-api/releases/latest ，2026-09-06 |
| Android 坐标／分发渠道 | Observed（部分） | `com.alphacephei:vosk-android:0.3.32+`，官方要求 `mavenCentral()`；这是动态范围，不是精确版本。Java 段另列 `com.alphacephei:vosk`，不得混同 Android 包 | https://alphacephei.com/vosk/install ，2026-09-06，Android build 段 |
| Android 精确版本／AAR 对象 URL | Unknown | 未得到固定坐标；R03 的 `assets=[]`，不能用项目 v0.3.50 推断 Android 0.3.50 已发布，也不能推断 Maven Central 没有包 | https://alphacephei.com/vosk/install ；https://api.github.com/repos/alphacep/vosk-api/releases/latest ，2026-09-06 |
| 源码仓库身份／commit | Observed＋Unknown | 仓库 `alphacep/vosk-api`；target_commitish=`master` 是分支字符串，不是不可变 commit；tag 对应完整 commit 未核定 | https://api.github.com/repos/alphacep/vosk-api/releases/latest ，2026-09-06 |
| runtime 许可证入口／范围 | Observed（R1）＋Unknown | R1 记录官方仓库 Apache-2.0 标识；续接安装说明和 release JSON 没有关闭精确 Android 包许可。LICENSE 正文、包内 notice、依赖许可及再分发范围未核定，不从模型许可继承 | https://github.com/alphacep/vosk-api （R1 2026-09-06）；R02/R03 2026-09-06 |
| 官方 checksum／签名／SBOM | Unknown | 所读安装说明与无附件 release 未给出可绑定目标 Android 制品的字段；不等于官方全站没有发布。响应 ETag 不是制品 SHA／签名 | https://alphacephei.com/vosk/install ；https://api.github.com/repos/alphacep/vosk-api/releases/latest ，2026-09-06 |

必要短摘录：R02 Android build 写 `implementation group: 'com.alphacephei', name: 'vosk-android', version: '0.3.32+'`；R03 JSON 写 `"tag_name": "v0.3.50"`、`"assets": []`。二者都是官方观察，但“该 tag 对应哪个 Android 包”仍 Unknown。

R03 JSON 中 tarball_url、zipball_url 和其他 API 链接均未请求。runtime 累计 3/3（R01 失败、R02/R03 成功），立即停止运行库读取，不挪用模型预算；未获取任何 AAR、源码归档或实现正文。
