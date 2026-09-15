# 决策记录：CP2 v8 局部配置证据后的路线

Owner: Product Lead
Last updated: 2026-09-06
Source: ../../raw/SRC-20260906-think-cp2-local-configuration-01.md
Confidence: High（七个 occurrence 的局部语义、证据边界和未验证项经 Leader 验收）；Medium（下一候选实现文件的信息增益来自现有符号关系，尚未取得正文）
Related decisions: prd-v0.1-2026-09-04.md；cp2-narrow-runtime-boundary-design-decision-2026-09-05.md；cp2-v8-hard-stop-next-step-decision-2026-09-06.md
Next review date: 2026-09-13

Research Quality: 96 · pass
Validation Level: V2
Next evidence: 先由 Leader 只用已接受的第一方派生身份记录，为固定 tree 下单个 `online-recognizer.cc` 准备一份可复核的新正文授权请求；没有 Product Lead 新授权不得读取文件正文
Allowed next investment: 一项授权请求准备工作；不得获取 metadata/body、联网、运行、修改工具或产品源码，也不得建立 v9
Pause/Kill condition: 无法从已接受派生记录取得候选文件的精确 blob/size/mode、请求需要超过一个正文对象、需要读取新 metadata 才能完成身份绑定，或试图把请求准备解释为获取／采用批准

## RESULT

**APPROVED — 只批准 `CP2-ASR-V8-HOTWORDS-CONSUMER-AUTHORIZATION-PREPARATION-001`：为一个固定的 `online-recognizer.cc` 正文证据请求准备精确合同，并在准备完成后由 Leader 向 Product Lead 请求一次新的明确授权。当前 sherpa-onnx 获取／采用路线继续 `PAUSED`；本决定不批准新正文、依赖、metadata、网络、v9、clearance、实现、构建、模型、集成、CP2 或 CP3。**

## 已接受事实

1. 七个 occurrence 的同文件局部审查已完成并由 Leader 验收；这只扩大了产品决策证据，没有改变冻结 detector 或旧 run。
2. 行 15 的 literal include 在本次获准查看的目标 directive 及最小局部上下文中没有显示运行时操作；未查看的同文件行、`OnlineCtcFstDecoderConfig` 的实现和下游使用均未审，不能标记安全或不可达。
3. 四个 `hotwords_file` occurrence 形成了真实的局部配置表面：公开字段、const-ref 参数、成员初始化目标与来源。相邻说明还明确区分 buffered input 与 file-based loading。
4. 本次人工获准查看的 55 行目标声明、局部构造函数及相关注释中，没有看到文件打开、路径拼接、selector 调用或动态加载；未查看的同文件行与跨文件实现均不作断言。因此不能把配置表面写成“已经发生文件访问”或“业务已经暴露文件路径”。
5. 同理，“本次获准查看的构造器体为空”只能支持该局部可见范围没有显示文件读取，不能外推到未查看的同文件行、调用者、实现文件、依赖、编译产物或运行时不可达。
6. 两个 comment occurrence 在本文件局部不操作，但没有 clearance；5 个 active hard stop、comment complete-set rejection、零成功 adjudication、`fixed_point=false`、`source_verdict=insufficient_evidence` 和已消费 run 全部保持。

## 产品路线判断

个性词典／专名识别是用户已明确提出的中文语音需求，因此完全放弃与 hotword 相关的证据路线会损失真实产品价值。但产品价值是“更好识别父亲的特定词”，不是“允许业务层传文件路径”。现有 `hotwords_buf` 文档线索提供了一条可能符合窄 handle、内存输入边界的方向；是否真的能封闭 `hotwords_file` 必须由消费端实现证据回答。

三种方案比较：

| 方案 | 用户价值 | 隐私／边界 | 工作量与可验证性 | 决定 |
| --- | --- | --- | --- | --- |
| 立即永久放弃 sherpa-onnx | 丢失离线中文与个性词能力的既有投入 | 最保守 | 不再取得区分能力 | 暂不选择 |
| 直接放宽 `dynamic_paths` 或建立 v9 | 表面推进快 | 无实际 I/O／可达性证据，可能破坏窄边界 | 不可证伪且重复治理投入 | 拒绝 |
| 先准备一个单文件消费端证据请求 | 能直接判断 buffer-only 约束是否值得继续 | 不在授权前读取正文；一次一对象 | 信息增益高、成本封顶、随时停止 | 批准 |

这不是恢复当前获取路线，而是为 Product Lead 的下一次知情授权准备最小证据合同。若单文件只显示委派而不能回答问题，也必须返回产品决策门，不能自动追加第二个文件。

## 政策边界

后续判断必须继续区分：

1. **上游内部可选配置**：源码可能声明文件型或 buffer 型参数；声明本身是 policy-relevant，不等于运行时已使用。
2. **构建／运行实际能力**：只有实现证据才能说明何时选择文件、是否打开路径、空值如何处理以及是否可完全不编译／不调用该支路。
3. **`think` 业务可达接口**：即使上游存在可选文件能力，仍须以后证明项目自有 adapter 只暴露固定 handle 与内存数据，并以测试／构建边界阻止文件路径进入；当前完全未证明。

以上分层不能生成 clearance 或 detector 例外。原始录音不落盘、不上传的产品红线保持；hotword 文字配置也不得借此绕过既有最小数据、文件路径和 handle 边界。

## 下一项唯一任务

任务名：`CP2-ASR-V8-HOTWORDS-CONSUMER-AUTHORIZATION-PREPARATION-001`。

Owner：Leader。Developer 与产品经理保持空闲。

### 唯一目标

只准备一份供 Product Lead 审批的新请求，目标是在未来另行授权后，对固定 upstream commit/tree 下的单个 `sherpa-onnx/csrc/online-recognizer.cc` 做一次正文获取与静态审查，用来回答：该消费端是否读取／传播 `hotwords_file`，`hotwords_buf` 与文件输入的 selector 在何处，空文件参数是否能形成可验证的 buffer-only 路径。

准备任务本身不读取或获取该正文，不执行审查。

### 候选对象与固定身份来源

- upstream commit：`917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`；tree：`fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`；
- logical path：`sherpa-onnx/csrc/online-recognizer.cc`；该路径是已批准过的原始 9 seed 之一，但旧授权与旧 run 均已结束，不可复用；
- 精确 Git blob、mode、decoded size 必须来自已接受、已提交的第一方派生身份／清单记录，并在请求中固定。不得为补齐身份读取 raw/private tree metadata、联网查询或打开正文；若派生记录没有这些字段，准备任务以 `authorization_request_preparation_blocked` 停止。

### 允许输入

- 本决定、现行 PRD、上一 v8 hard-stop 决定及本轮五份已验收派生报告；
- 已接受且已提交的第一方 policy／manifest／identity 摘要中与这一个候选路径直接对应的记录；
- 只允许复制和校验身份、预算、用途、拒绝项与停止条件，不允许运行 acquisition/scanner/controller/reviewer。

### 请求必须固定的最小范围

- 正文对象：恰好 1 个；logical path 必须是上述 `online-recognizer.cc`；
- 来源：上述固定 commit/tree 与准备阶段核实出的唯一 Git blob；
- decoded budget：请求中写入精确文件大小，且硬上限 262,144 bytes；一次 request、一次成功或失败结果；
- 用途：只定位 `hotwords_file`／`hotwords_buf` 的直接消费、selector、空值行为、文件 I/O 调用和下一层精确依赖；
- 人工可见范围：只限命中与最小 enclosing function/type；不得导出整文件正文；
- 禁止 include/symbol 跟随、第二文件、递归闭包、模型、构建、执行、网络扩展、业务实现、detector/schema/freeze 修改或旧 run 恢复；
- 任何新依赖只登记 path/symbol/evidence gap，然后停止并回产品决策门。

### 准备任务交付与验收

- 一份 pending authorization JSON＋Markdown，绑定任务合同、现行决定、候选 path、commit/tree/blob/mode/size、单次预算、用途、可见范围和全部停止条件；
- 一份独立核对记录，证明身份字段来自哪一份已接受派生记录，且没有读取新 metadata/body 或发起网络；
- 向 Product Lead 展示完整请求和以下精确授权句；在取得逐字明确批准前，不得创建 acquisition authority 或读取正文；
- 输出只允许 `authorization_request_ready_for_product_lead` 或 `authorization_request_preparation_blocked`，然后停止。

### Product Lead 新授权句

当且仅当准备任务已把 `<BLOB_SHA>`、`<MODE>` 与 `<EXACT_BYTES>` 替换为经独立核对的固定值后，Leader 才可请求以下授权；含占位符的文本无效：

> 我批准 `CP2-ASR-V8-HOTWORDS-CONSUMER-SINGLE-BODY-REVIEW-001`：只针对 upstream commit `917bed95c8e5c7c18aa4d69fea42e9ef8ef0a60e`、tree `fd2c4e97c9f7499b6ed91c7c2854b4211f61bdc0`、path `sherpa-onnx/csrc/online-recognizer.cc`、Git blob `<BLOB_SHA>`、mode `<MODE>`、decoded size `<EXACT_BYTES>`，允许一次正文获取和一次离线静态审查；只判断 `hotwords_file`／`hotwords_buf` 的直接消费、selector、空值行为与文件 I/O 线索。不得获取或跟随任何第二文件、include、symbol、依赖或 metadata，不得运行第三方内容、构建、加载、测试、集成、联网扩展、修改 detector/schema/freeze/旧 run 或形成 clearance；任一身份不匹配、超过 262,144 bytes、需要下一文件或出现其他禁止能力时立即停止并回产品决策门。本授权不批准 v9、源码采用、CP2、CP3 或父亲 Alpha。

该句现在只是待完成身份字段的请求模板，不是 Product Lead 授权，也不授权 Leader 自行补取身份。

## 恢复、失败与回退

- 若准备阶段找不到精确身份：保持 `PAUSED`，由产品经理决定是否值得为“单个 tree metadata identity”再请求一次更小授权；不得把路径＋tree 推断成 blob。
- 若 Product Lead 不授权：保持 `PAUSED`，不影响可逆 UI／本地数据骨架，但不能声称 CP2 有进展。
- 若未来单文件证据显示直接文件 I/O 或无法以空值／buffer-only 封闭：保持 hard stop，暂停 sherpa-onnx，另做替代离线中文 ASR 候选的产品决策。
- 若单文件只委派给实现类：登记唯一下一依赖并停止；不得自动获取 `online-recognizer-impl.*`。
- 若单文件支持 buffer-only：仍只形成下一轮窄边界证据，不是安全或采用结论；后续依赖、构建与真机门禁全部照常。

## 未验证与保持不变

- 本次仅人工查看 55 行局部上下文；没有证明或排除未查看的同文件行与跨文件实现中的实际文件访问、selector 执行、默认值、动态加载、调用图、编译可达性或 `think` 业务 API 暴露／封闭。
- `online-ctc-fst-decoder-config.h` 及 line 15 include 的跨文件语义仍未验证，本次因产品信息价值较低而不列入唯一下一对象。
- 剩余 seed/internal/external edges、完整闭包、P0/reachability、许可证、源码可采用性、构建、制品、模型都未验证。
- 旧 run 永久结束；原 denylist、complete-set rejection、pending、零 adjudication、`fixed_point=false` 与 `source_verdict=insufficient_evidence` 不变。
- 三步录入／找回、原始录音不落盘／不上传／不进日志、CP1 与 Conformer `Deferred, not removed` 不变。
- 中文准确率、小米 15 性能、90 秒 20 次稳定性、飞行模式与音频隐私仍需真实 CP2 证据。
- CP2 未通过；CP3、父亲 Alpha、账号、同步、支付、Flutter、KMP、公开发布与云端语音识别均未批准。

允许的准确表述是：

> v8 局部审查确认 `hotwords_file` 是 policy-relevant 配置表面，但没有证明实际文件 I/O 或业务可达性。当前路线继续暂停；只批准 Leader 准备一个单文件、需 Product Lead 新授权的消费端证据请求。

禁止的表述包括“已证明 sherpa-onnx 会读文件”“已证明文件能力不可达”“hotwords 已安全”“dynamic_paths 已清除”“可以建立 v9／集成／进入 CP2 或 CP3”。

## 开发仓库后续同步清单

Leader 后续只需在 `/Users/orderly_ray/Projects/think` 的治理入口同步以下状态，不得在本任务中修改：

1. CP2 当前仍 `PAUSED / not passed`，不得将本决定计为 App 开发进度；
2. 七 occurrence 局部审查已完成，但零 clearance，旧 hard stop/pending/run 不变；
3. 唯一下一动作是授权请求准备，尚无新正文获取权；
4. 若请求准备成功，必须先取得 Product Lead 新明确授权，再另开单文件任务；
5. 三步路径、原始录音不落盘／不上传及所有真机、性能、稳定性与飞行模式门槛保持。
