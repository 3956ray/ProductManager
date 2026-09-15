# 决策记录：CP2 人工审查原 token 证据补录

Owner: Product Lead
Last updated: 2026-09-06
Source: ../../raw/SRC-20260906-think-cp2-token-provenance-01.md
Confidence: High（v8 验收、字段缺口、脚本非单射行为、原授权对象与范围均由固定第一方记录交叉确认）；Medium（原 9 bytes 尚未由新任务补录和独立验收）
Related decisions: prd-v0.1-2026-09-04.md；cp2-review-timestamp-representation-decision-2026-09-06.md；cp2-manual-capability-evidence-decision-2026-09-06.md
Next review date: 2026-09-13

Research Quality: 95 · pass
Validation Level: V2
Next evidence: Leader 在原用户授权的同一 retained object 上完成两处固定区间的最小原 token provenance 补录，并由另一验收步骤独立复核权限、字节、哈希、完整 tuple、append-only 和零扩权
Allowed next investment: 一个由 Leader 执行的单独、只读、离线证据补录任务；只访问已授权同一 envelope/header 的两个 9-byte 区间，不修改产品仓库、v8、原 R、原时间或 decision，不创建 K
Pause/Kill condition: retained object 身份／权限漂移、需要读取两个区间以外的新上下文、需要重新获取或联网、无法证明 exact bytes，或必须修改 v8/schema/R/decision/authority 才能继续

## RESULT

**APPROVED — 只批准对原用户已授权的同一 retained header、同两处 occurrence 做一次独立、最小、append-only 的原 token 字节来源补录。该补录不重新人工裁定，不修改原 R、原审查时间、decision 或已接受 v8，不创建 K，也不增加任何 clearance、获取或运行权限。**

## 已确认事实

1. v8 候选 `C=1fe85740a185a63ca4f35df2abd22ae410f82fbb`、tree `68924b2a71443664b5d1203a1456066c49d7335d`、bundle `9bd39cec857137703c205b92b755eca200c58a2345d197a1ce853825cd1fe1bf` 已被 Leader 接受；两轮各 174 tests／1338 outcomes／0 skip，原 167 methods／1210 outcomes 与最初 158 基线均保留。
2. v8 要求 `raw_token` 进入完整 occurrence identity 和 `occurrence_id`，并在新运行时从当前已验证 body 的精确区间重建。不能改成规则名、统一小写或省略。
3. 原 R `0d8b34...` 与 verification `ca492d...` 固定了两处 9-byte 绝对区间及双行 hash，却没有保存原 token bytes。历史脚本 `923d06...` 使用 `segment.lower().index/count`，只能证明大小写不敏感命中，不能反推原始大小写。
4. K 前置任务因此正确停止；`K/F/M/A/T/N` 均未创建，pending 未清除，v8 未改变。

## 授权判断

本次补录在原用户批准的持续范围内，不需要再次请求 Product Lead 授权，依据如下：

- request `c66a9f...` 与 approval `df26a4...` 精确绑定同一 upstream commit/tree/path、body SHA/bytes、Git blob、8579-byte private envelope、0600 文件／0700 私有父目录、7939-byte header、规则和行 57／60；
- 允许范围明确包含：在 no-follow／hash／size／type／mode 检查后读取该 retained object、检查同一两处命中，并记录原始 byte ranges；批准文本没有一次性读取、读取后失效或截止时间；
- 新任务比原人工 review 更窄：不再阅读同文件上下文，只提取既已固定的 `[1893,1902)` 与 `[1972,1981)` 两个 9-byte 区间，为同一裁定补齐来源；不产生新的语义决定；
- “不得复用旧 acquisition authority”禁止恢复旧 run、联网或获取新正文。本任务只读已经由独立人工 review 授权的 retained object，不是 acquisition，也不把本产品决定冒充用户授权。

若任一固定身份／权限不匹配、retained object 不再可用、需要其他文件／区间／上下文或需要重新获取，则现有授权不覆盖；任务必须停止，由 Leader 提交新的具体授权请求后才能询问用户。

## 唯一允许的 provenance 语义

补录记录命名为 `P`，domain 固定为 `think-manual-token-provenance-v1`，是原历史人工审查的独立追加证据，不是原 R 的修订版，也不是 K 或新 review。

`P` 必须绑定：

- 原 review request、用户 approval、原 R、原 verification report/script 的精确 SHA-256；
- 历史 review-context freeze `H=d78577b8bac1108791e0c4ba3c7a0cd672958c94` 及原 formal decision identity；
- upstream commit/tree、source path、body SHA/bytes、Git blob；
- envelope SHA/bytes、regular-single-link、0600 与私有父目录 0700/no-follow 检查；
- 每个 occurrence 的 line、两种 line-hash domain/hash、line start/end、token start/end、rule、原 decision；
- 各区间的 `token_bytes=9`、严格 ASCII 解码值、canonical base64、lowercase hex，以及 domain=`sha256-original-token-bytes-at-absolute-interval-v1` 的 token SHA-256；三种编码必须解码为同一 9 bytes；
- 补录脚本精确 bytes/hash、补录记录创建时间和本决定／原用户授权依据。补录创建时间必须使用独立字段，禁止冒充或替换原 `reviewed_at`。

`P` 和补录验收记录都不得包含完整 header、完整行、相邻字段或其他 source bytes。若任一 9-byte slice 不是 strict printable ASCII、长度不是 9、`lower()` 后不精确等于固定 rule `websocket`，或任何 tuple 不匹配，必须停止，不得猜测或修复。

## 下一项唯一任务

任务名：`CP2-ASR-REVIEW-TOKEN-PROVENANCE-COMPLETION-001`。

Owner：Leader。产品经理和开发者不得执行该补录。

### 唯一目标

从已授权、已固定的同一 retained object 中，只提取两个既定绝对区间的原 9 bytes，生成一个不可变 `P` 记录及独立验证材料。输出只能是 `token_provenance_complete_for_acceptance` 或 `token_provenance_blocked`。

### 允许步骤

1. 以 descriptor-relative、逐层 no-follow 方式重新验证路径；固定私有父目录 0700、文件 regular-single-link 0600、8579 bytes 与 envelope SHA。
2. 仅在内存解析 envelope；验证 path/role、body 7939 bytes、UTF-8/NUL、body SHA 与 Git blob，不导出 body 或 source tree。
3. 复算两行的 historical／physical hash 与 line/token 绝对区间，只读取 body `[1893,1902)`、`[1972,1981)`；两个区间之外不进入语义检查。
4. 生成 canonical `P`、最小验证报告和静态第一方验证脚本；只保存两个 9-byte token 的 ASCII/base64/hex/hash 和完整身份 tuple。
5. 由独立验收步骤重新检查文件身份、权限、两个 slice、编码互证、P hash、原记录未变、零网络和零额外读取；补录与验收不得合并为 K。

### 明确不做

- 不修改或重签 7051-byte 原 R、原 verification、原 review time／decision、v8 C/schema/tests/evidence、旧 freeze/run 或产品代码；不建立 v9。
- 不读取完整行／相邻上下文用于新判断，不重新裁定 comment、字段、API、实现或可达性。
- 不执行旧 verification script，不运行 v8 candidate/controller/scanner，不联网、不重新获取、不读取其他 private/corpus/metadata/LICENSE/API。
- 不创建 representation、K/F/M/A/T/N，不解除 pending，不授予源码、构建、模型、CP2/CP3 权限。

### 验收与停止条件

通过必须同时证明：原 request/approval/R/verification/v8 hashes 未变；只读一个固定 envelope；两个且仅两个 9-byte slice；P 的每个 tuple 和编码/hash 可独立复算；输出不包含其他正文；网络与获取为零。

任一身份、权限、大小、hash、line/interval、ASCII/长度/lowercase-rule、编码互证或输出最小化失败即 `token_provenance_blocked`。若需要其他材料、修改 schema/R/v8、重新获取或扩大语义，立即回产品决策门；不得在同一任务修补或启动 K。

## 后续顺序

严格顺序为：

1. 单独完成 `P`；
2. 单独由 Leader 验收 `P`；
3. 另开 K 任务，以原 R digest 和已接受 P digest 构造 v8 representation，并在 K 验收记录中显式绑定 P；v8 canonical K schema 不增加字段，K 的 representation digest 间接绑定 exact raw token，独立验收负责证明 R＋P→representation 的来源；
4. K 独立接受后才建立 F；随后单独建立 M；
5. 只有 F/M 完成后，才向 Product Lead 请求**全新的 acquisition A**；再建立 T/N。

P 不产生 clearance 或 operational authority。P、K、F、M、新 A、T/N 不得合并。旧 acquisition 授权仍不可复用。

## 保持不变与未验证

- 原 review 决定仍只适用于同 body、同两 occurrence 的 comment bytes；相邻字段、API、实现、整份源码和 WebSocket 可达性未清除。
- 真实 P 尚未生成，R＋P→representation、K/F/M/A/T/N、源码闭包、P0/reachability、许可证、源码采用性、构建、制品、模型均未验证。
- 中文准确率、小米 15 性能、90 秒 20 次、飞行模式和动态音频隐私未验证。
- 三步录入／找回、原始音频不落盘／不上传／不进日志、CP1 与 Conformer `Deferred, not removed` 不变。
- 既有 `block`／`manual_review` 裁决互不继承；`source_verdict=insufficient_evidence`，CP2 未通过，CP3 与父亲 Alpha 未批准。

允许的准确表述是：

> v8 已通过第一方离线验收，但原人工报告缺少两个 occurrence 的原 token bytes。产品经理确认原用户对同一 retained object 的离线 review 授权覆盖更小的 exact-slice provenance 补录；只有 P 单独完成并验收后，才可另行恢复 K。
