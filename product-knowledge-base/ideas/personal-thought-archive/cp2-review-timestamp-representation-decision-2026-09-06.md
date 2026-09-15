# 决策记录：CP2 人工审查时间的无损表示

Owner: Product Lead
Last updated: 2026-09-06
Source: ../../raw/SRC-20260906-think-cp2-review-timestamp-01.md
Confidence: High（时间不可表示原因、v7 验收身份和 K 未创建状态均由 Leader 派生报告与第一方 schema 交叉确认）；Medium（v8 尚未实现、验收或用于真实映射）
Related decisions: prd-v0.1-2026-09-04.md；cp2-manual-capability-evidence-decision-2026-09-06.md；cp2-source-semantics-readiness-decision-2026-09-06.md
Next review date: 2026-09-13

Research Quality: 94 · pass
Validation Level: V2
Next evidence: 独立 v8 第一方离线候选以自建 fixture 完成严格日期／时间解析、6 位以内小数秒与明确 offset 的无损转换、表示与时刻双域哈希、防篡改／等时异串／no-successor 矩阵，并由 Leader 双跑全部 167 基线方法和 1210 既有 outcomes 后独立复算
Allowed next investment: 一个独立新目录中的最小第一方离线时间表示修订；仅 Python 标准库、自建 fixture 与既有已接受 v7 必要第一方代码/schema，不读取真实 R/body，不创建实际 K/F/M/A/T/N
Pause/Kill condition: 必须截断精度、改写旧报告、使用新 K 时间冒充 review 时间、依赖真实报告作 fixture、放宽其他 authority／隐私／权限／checkpoint，或无法使篡改与等时异串确定性 fail closed

## RESULT

**APPROVED — 只批准一个独立 v8 第一方离线候选中的最小时间表示修订。它只解决未来证据接收合同如何无损绑定合法小数秒与明确时区，不批准真实 R 的转换或映射，不批准现有／新第三方源码、制品、构建、模型、集成、CP2、CP3 或父亲 Alpha。**

## 已确认事实

1. v7 R1 候选 `C=443bbb5dc73e52dc11610ba766fdda23a0923b80`、bundle `198c24c66a3e82117828e9eacfa333b4dde8eb19949c7425b8a81b839399553e` 已获 Leader 接受；两轮各 167 tests／1210 outcomes，原 158 基线与 1154 个旧 v7 outcomes 保留。
2. v7 的 `reviewed_at` 只接受整秒 UTC `YYYY-MM-DDTHH:MM:SSZ`。真实人工报告时间原值为 `2026-09-06T06:48:22.579140+08:00`，无损 UTC 为 `2026-09-05T22:48:22.579140Z`；截断到整秒会丢失 `579140` 微秒。
3. 保存报告 SHA-256 只能绑定原始字节，不能让错误或有损的规范时间变得准确。也不能新造一个 K 建立时间来替代原审查时间。
4. K 前置检查没有读取真实正文或 private body，`K/F/M/A/T/N` 均未创建。这个表示阻塞不推翻 v7 的自建离线验证，但 v7 也不能用于真实 R 映射。

## 产品判断

这是一个局部、第一方、可逆且可以完全用自建时间 fixture 验证的表示缺口；不需要放宽安全、隐私或 authority DAG。直接暂停会放弃已接受的 v7 证据接收边界，而截断或改写会破坏审计身份。故批准独立 v8，只修订时间表示和相关哈希绑定；如果实现必须触碰其他边界，则立即暂停。

## v8 时间表示合同

### 接受的原始语法

`reviewed_at_raw` 必须是 ASCII、长度受既有 128 bytes 上限约束，并严格符合以下 RFC 3339 子集：

`YYYY-MM-DDTHH:MM:SS[.ffffff](Z|±HH:MM)`

- 年为 `0001..9999`；月份、日期必须是有效公历日期并正确处理闰年。
- 小时 `00..23`、分钟 `00..59`、秒 `00..59`；不接受 `24:00`、闰秒 `:60`、空格、命名时区、缺失时区、小写 `t/z` 或多余字符。
- 小数秒可缺省；存在时必须为 1..6 位十进制数字。6 位足以无损表示当前真实值；遇到超过 6 位的未来输入必须停止并回到产品决策，不能舍入或截断。
- offset 必须是 `Z` 或 `±HH:MM`；范围不超过 `±14:00`，`14` 小时时分钟必须为 `00`。`-00:00` 表示未知本地偏移，拒绝；`+00:00` 合法但不得被当作与原始 `Z` 字符串相同。

### 原值、无损 UTC 与精度

每条 representation 必须同时保存并绑定：

- `reviewed_at_raw`：输入的原始合法字符串，逐 ASCII byte 保留，不修剪、不改写；
- `reviewed_at_utc`：按公历和 offset 无损换算成 UTC，使用大写 `T/Z`，并保留与 raw 相同的小数位数；没有小数则仍为整秒；
- `fraction_digits`：严格整数 `0..6`；
- `offset_minutes`：原始明确 offset 的带符号分钟数，`Z` 与 `+00:00` 都是数值 0，但原始字符串仍不同；
- `instant_microseconds`：以 proleptic Gregorian（前推公历）的 `1970-01-01T00:00:00Z` 为 epoch 的带符号 UTC 微秒整数，只用于判定是否同一时刻，不替代任何表示身份；可表示范围必须与已接受的 `0001..9999` 日期域完全一致并在 schema 中冻结上下界。

当前值必须得到：

- raw：`2026-09-06T06:48:22.579140+08:00`
- UTC：`2026-09-05T22:48:22.579140Z`
- `fraction_digits=6`
- `offset_minutes=480`

不得把 `2026-09-05T22:48:22Z`、K 建立时间或任何重新格式化的近似值当作该审查时间。

### 两个互不替代的身份域

1. **时刻等价域**：`instant_microseconds` 只用于判断两个合法字符串是否表示同一物理时刻；例如 `Z` 与 `+00:00`、`.1` 与 `.100000` 可能等时。
2. **表示身份域**：`reviewed_at` 在 v8 中成为一个严格对象，domain 为 `think-review-timestamp-v1`。它必须包含 raw、UTC、`fraction_digits`、`offset_minutes`、epoch/instant，以及 raw/UTC 精确 ASCII bytes 的独立 SHA-256。raw 与 UTC 的 hash domain 分别固定为 `sha256-reviewed-at-raw-ascii-v1` 和 `sha256-reviewed-at-utc-ascii-v1`；禁止跨域替换。

时间对象和外层 representation 都继续使用 v7 的 sorted-key、compact ASCII、no-nonfinite、exactly-one-LF canonical JSON 规则。外层 representation 升为 `think-manual-representation-v2`；受其 schema 影响的未来 `K/F/M/A/T/N` 使用新的 v8 domain/version，防止 v7 对象与 v8 对象互换。`H` 和原始报告 R 的既有字节／摘要保持不变；升级 domain/version 只隔离新合同，不增加 authority 或 clearance。representation digest 对整个 v2 canonical 对象计算；只要原 offset、精度或字符串形式不同，表示身份就不同，即使时刻等价。

K、M、T 和新 adjudication 必须绑定精确 representation digest 及原始报告 R digest；不得只按时刻等价接受另一字符串，不得只绑定 UTC 而丢失原 offset／精度，也不得让 untrusted input 或 runtime 自行选择转换结果。`map_schema` 必须绑定 v8 时间合同版本。

### 完整性与 fail closed

- 解析、日期有效性、offset 换算和 canonical bytes 必须由第一方标准库实现并独立复算；不接受平台宽松解析器的自动纠错。
- raw、UTC、精度、offset、instant、任一 hash、R binding 或 representation digest 被篡改，均在 successor 前停止。
- 两个字符串只有时刻等价但表示不同，若 K 承诺的是其中一个，另一个必须 fail closed；禁止 normalization collision。
- v7 C、旧 run/freeze/report/evidence 保持原字节只读。v8 是新的 C 候选与新 hash，不原地修补 v7，不修改真实 R。
- 全部非时间规则保持：`H/R/C/K/F/M/A/T/N` 非循环 DAG、原报告与 representation 双域、逐 occurrence 完整匹配、硬停止优先级、预算、角色、权限、隐私和 no-successor。

## 下一项唯一任务

任务名：`CP2-ASR-REVIEW-TIMESTAMP-REPRESENTATION-OFFLINE-001`。

### 唯一目标

在独立 `tools/asr_review_acquisition_v8/` 形成最小第一方离线候选，只把上述时间合同加入已接受 v7 的证据接收机制。输出只能是 `timestamp_representation_candidate_ready_for_acceptance` 或 `timestamp_representation_candidate_blocked`。

### 允许输入与变更

- 只读复制 `443bbb5…` 中必要的第一方 v7 code/schema/tests/recalculator，记录 v7→v8 provenance/diff；v7 提交和全部既有 evidence 保持只读。
- 只修改 schema/version/domain、时间解析／转换／canonicalization、representation/K/M/adjudication 的时间哈希绑定，以及对应自建 fixtures、测试、审计说明和独立复算器。
- 仅 Python 标准库；所有时间、报告和 authority fixtures 必须完全自建。不得把真实 R 的原值、正文、header、metadata、private body 或旧 raw scanner context 复制成 fixture。

### 验收矩阵

1. 保留并重跑已接受 v7 的全部 167 methods／1210 outcomes、原 158 基线和旧 v7 ordered outcomes；不得通过改旧断言隐藏回归。
2. 合法矩阵至少覆盖：无小数、1..6 位小数、`Z`、正负 offset、跨日／月／年、闰年，以及 `+14:00/-14:00` 边界；验证 raw 不变、UTC 无损、精度与 offset 正确。
3. 非法矩阵至少覆盖：无时区、`-00:00`、offset 越界／`14:01`、非法月日／闰日、`24:00`、`:60`、0 位或 7 位以上小数、小写／空格／尾随字符、非 ASCII、类型混淆、重复／未知字段。
4. 等时异串矩阵必须证明：时刻等价可以被独立复算，但 raw hash、表示 digest、precision/offset 身份不合并；把 K 承诺值换成等时另一字符串时零 successor。
5. 分别篡改 raw、UTC、precision、offset、instant、raw hash、UTC hash、R binding、representation digest、K/M/T/adjudication pin；每项 fail closed 且零 successor。
6. 两次独立完整运行；规范化 JSON、测试结果、hash chain、ledger、terminal 与集合摘要逐字节一致，并由不导入 producer 的独立 recalculator 复算。

### 必须交付

- 完整 v8 schema、threat boundary、时间语法、转换算法、epoch／整数范围、canonical bytes 与 hash domain 定义；
- v7→v8 逐文件 provenance/diff、167 方法／1210 outcomes 映射、旧 v7 文件／证据未变证明；
- 双跑结果、独立复算、网络／DNS／第三方读取为零的证据；
- `ready_for_acceptance` 只允许 Leader 独立验收新 C，不创建或批准真实 K。

### 停止条件

- 需要读取真实 R/body/header/metadata/private 指针，或真实值被用于 fixture；
- 需要第三方库、网络、系统 locale／模糊解析、精度截断／舍入、报告改写或用新时间替代审查时间；
- 需要改变 authority DAG、逐 occurrence、预算、角色、权限、隐私、硬停止、acquisition scope 或 checkpoint；
- 无法对等时异串、篡改、非法日期／offset 或 7 位以上精度确定性 fail closed；
- 开始创建真实 K/F/M/A/T/N、获取正文、构建、模型、集成或 CP3。

命中任一项即返回 `timestamp_representation_candidate_blocked` 并回到产品决策门，不得在同一任务扩大范围。

## 授权与后续顺序

该普通、可逆、第一方、离线任务属于 Product Lead 已持续授权的范围；知识库五文档同步后，可由 Leader 单项派发，不需要重复请求用户批准。

只有新的 v8 C 经独立验收后，才重新从 `K → F → M → 新用户 A → T/N` 依序推进。v7 C 的接受记录仍有效但只读，不能被直接用于真实 K。未来建立 K 时才允许在单独任务中读取已获授权的必要真实派生字段；本决定本身不授予该读取或映射。

## 保持不变与未验证

- 两处 comment occurrence 的人工裁定范围不变；相邻字段、API、引用实现、整份源码和 WebSocket 可达性仍未清除。
- 真实 R→representation 转换、K/F/M/A/T/N、7 个剩余 seed、9 个内部边、真实闭包、P0/reachability、许可证、源码采用性、依赖、构建、制品、模型均未验证。
- 中文准确率、小米 15 性能、90 秒 20 次、飞行模式、动态音频隐私和提醒行为均未验证。
- 三步录入／找回与原始音频不落盘、不上传、不进日志不变；CP1 与 Conformer 均为 `Deferred, not removed`。
- 既有 `block`／`manual_review` 裁决不变且互不继承；`source_verdict=insufficient_evidence`，CP2 未通过，CP3 与父亲 Alpha 未批准。

允许的准确表述是：

> v7 第一方离线候选已接受，但真实审查时间无法由其整秒 UTC 字段无损表示。产品经理只批准独立 v8 离线修订时间表示；在新 C 独立验收前不得创建真实 K，其他产品与安全门槛没有变化。
