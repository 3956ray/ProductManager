# Vosk Android Maven Central 元数据核定

Owner: Product Lead
Last updated: 2026-09-06
Source: `CP2-VOSK-ANDROID-MAVEN-METADATA-001`；已验收身份缺口范围决定；Q01–Q09 ledger；Apache Maven 官方说明与 Central Q08/Q09 原始 XML
Confidence: High（固定坐标与 POM 声明）；制品内容／安全仍未验证
Related decisions: `cp2-vosk-android-identity-gap-decision-2026-09-06.md`；`cp2-alternative-asr-security-intake-selection-decision-2026-09-06.md`
Next review date: 2026-09-13
Research Quality: 90/100 · pass（仅本次元数据核定，不重评历史 82／55／92 分）
Validation Level: V2（保持，未增加真实产品使用或付款证据）
Next evidence: Leader 验收后独立决定是否提出精确制品取得与审查；不得据本文件自动下载
Allowed next investment: 本任务收尾与等待验收；阶段 B/C 未获授权
Pause/Kill condition: 发现精确来源／坐标／许可关键声明冲突则回产品门；任何制品或执行需求留独立授权

## RESULT

**identity_ready_for_artifact_intake_decision**

唯一固定 Android 发行坐标为 **`com.alphacephei:vosk-android:0.3.75`，POM packaging=`aar`**。这是官方 Central 版本 metadata 和同版本 POM 的直接声明，不是由 GitHub tag `v0.3.50`、动态范围 `0.3.32+` 或包名推测。

本结果只表示后续产品授权能指认一个发行对象及其元数据来源；**不证明 AAR 实际存在、可下载、内容正确、安全、隐私合格或与源码可复现**。本任务没有对任何制品发出 GET／HEAD／Range。旧身份任务的 `identity_insufficient` 和 5/6（runtime3/3、model2/3）保留；本次是独立新批次，不覆盖旧三文档或失败记录。

POM 项目主页字段为 `http://www.alphacephei.com.com/vosk/`，与已知官网不同，标记为**异常且归属 Unknown**，未访问、未自动“纠正”。身份追溯采用已核定 Central 来源、Vosk 官方安装说明的 group/artifact 和 POM 中匹配的官方 SCM；该主页不作为信任依据。它不是已证明恶意或已证明拼写错误，后续制品审查应保留此注意项。

## 输入身份与执行范围

正式决定：`cp2-vosk-android-identity-gap-decision-2026-09-06.md`，13299 bytes，SHA-256 `e4cb90e2184db26dd5021c4acae079384f585a89f7c616f5b2e25af1a85e4dab`，与 current-task 及 Leader acceptance 匹配。Leader 仅验收研究范围，未授权制品或执行。

旧 runtime、model、readiness 的 SHA 分别为 `dbbf286e01ba240bbe242c8166f93a2c5f16e98f96f0249628d6db10a66e7576`、`14a64e8fe55844daff2394c8bef65292136262986b6e5fa1179628964d8433b1`、`8e00fa5267e9eabf10efb6b3c163360327ca303cffb6d0b8aef84d4cb61b1e51`；本次保持只读。

本批次上限：10次尝试，单响应1 MiB、累计正文5 MiB、单次30秒、一个固定版本、最多一个父POM。使用系统既有curl和Python标准库只读解析；未安装工具、未依赖Firecrawl。系统要求的网络权限逐请求批准属于运行环境审批，不是新增产品逐页审批。

## 官方来源与路径推导

| 步骤 | 观察／引用位置 | 来源确认与限制 |
| --- | --- | --- |
| 已有官方起点 | Vosk安装说明R02的 `mavenCentral()`、`com.alphacephei:vosk-android` | 只用已取得内容，不重新请求；不从动态范围选择固定版本 |
| Q04 搜索发现 | RSS item标题“Welcome to Apache Maven”，链接 `https://maven.apache.org/` | 仅用于导航，不将摘要当作包存在性证据；第三方镜像和聚合站结果未访问 |
| Q05 Apache 官方主体 | 页面“Apache Software Foundation”段及 `www.apache.org` 官方链接，正文写 Maven 属于 Apache Software Foundation | 确认Apache官方文档入口；不是仅凭HTTPS或名称相似 |
| Q06 官方 Central 交叉链接 | “Maven Central Repository”正文，图谱中 `alt="repo"` 明确链接 `https://repo.maven.apache.org/maven2/` | 在Q08前确认该Central端点；采用可信官方交叉链接路线，不依赖搜索摘要中的repo地址 |
| Q06 运营相关链接 | Central公告／OSSRH／Producers 指向 `central.sonatype.org` | 仅记录官方文档中的指向；未访问这些页，未独立核定Central完整运营法律主体，不把Sonatype链接当包发布者证明 |
| Q07 布局规范 | “Maven Repository Layout”树及groupId说明 | 原文规定groupId中的点替换为斜杠，artifact层放 `maven-metadata.xml`，version层放 `${artifactId}-${version}.pom` |
| Q08 URL Derived | 已确认root + `com/alphacephei/vosk-android/maven-metadata.xml` | 官方布局＋既有group/artifact的确定性推导，不是路径存在性猜测 |
| Q09 URL Derived | Q08明确release=0.3.75，再按Q07加入版本目录和POM文件名 | 在观察version后才生成并请求；不猜具体版本、不轮询第二版本 |

关键官方原文片段（Q05–Q07）：

```text
Maven is a part of the Apache Software Foundation.
<area shape="rect" coords="65,348,205,383" alt="repo" href="https://repo.maven.apache.org/maven2/" />
${groupId as directory} is the groupId with . replaced by /
artifactId directory: maven-metadata.xml
version directory: ${artifactId}-${version}.pom
```

前两行分别为Q05文字与Q06原HTML；后三行是Q07规则的最小结构摘记，不冒充整段逐字引文。完整临时响应文件及摘要列于下表；Q08/Q09原XML另完整嵌入本文，不依赖临时目录才能复核关键字段。

## 完整请求 Ledger

日期均为2026-09-06。时间取响应头Date（UTC），不是客户端开始时间；耗时取curl time_total。没有自动重定向、自动重试、浏览器子资源、脚本执行或隐式依赖获取；HTTP 302也计入尝试。请求均GET且只针对搜索／说明／元数据。

| ID | 尝试 URL（本次实际final相同，无自动跟随） | 来源／用途 | UTC响应时间 | HTTP／类型 | bytes | 累计bytes | 秒 |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| Q01 | https://www.google.com/search?q=Maven+Central+official+Sonatype+repository+layout | 公开入口搜索 | 14:10:12 | 302 text/html | 444 | 444 | 0.585283 |
| Q02 | https://www.google.com.hk/search?q=Maven+Central+official+Sonatype+repository+layout | Q01地区跳转中的目标查询 | 14:10:41 | 200 text/html；无可直接使用结果 | 91997 | 92441 | 0.343362 |
| Q03 | https://www.bing.com/search?q=Maven+Central+official+Sonatype+repository+layout&format=rss | 搜索渠道恢复 | 14:11:11 | 302 text/html | 210 | 92651 | 0.445785 |
| Q04 | https://cn.bing.com/search?q=Maven+Central+official+Sonatype+repository+layout&format=rss | Q03 Location目标 | 14:11:33 | 200 text/xml | 5682 | 98333 | 0.308830 |
| Q05 | https://maven.apache.org/ | Q04明确链接，确认官方主体 | 14:12:08 | 200 text/html | 12930 | 111263 | 0.457739 |
| Q06 | https://maven.apache.org/repository/index.html | Q05明确链接，确认Central端点 | 14:12:38 | 200 text/html | 11529 | 122792 | 0.648866 |
| Q07 | https://maven.apache.org/repository/layout.html | Q06导航链接，核定布局 | 14:13:18 | 200 text/html | 15499 | 138291 | 0.626480 |
| Q08 | https://repo.maven.apache.org/maven2/com/alphacephei/vosk-android/maven-metadata.xml | 已核定布局推导，版本列表 | 14:14:05 | 200 text/xml | 625 | 138916 | 0.583203 |
| Q09 | https://repo.maven.apache.org/maven2/com/alphacephei/vosk-android/0.3.75/vosk-android-0.3.75.pom | Q08release＋Q07布局，唯一POM | 14:14:37 | 200 text/xml | 1811 | 140727 | 0.316487 |

Q01完整Location为 `https://www.google.com.hk/url?sa=p&hl=zh-CN&pref=hkredirect&pval=yes&q=https://www.google.com.hk/search%3Fq%3DMaven%2BCentral%2Bofficial%2BSonatype%2Brepository%2Blayout&ust=1788703842745187&usg=AOvVaw1gyuBUw0QUjmSe8JHDBstv`；Q02直接读取其中q参数明确编码的地区搜索目标，没有请求该url包装页。Q03 Location就是Q04 URL。其余成功响应无重定向。代理CONNECT的200不作为目标响应200。

合计 **9/10次，正文140727 bytes（小于5 MiB）**；最大单次91997 bytes（小于1 MiB），最大耗时0.648866秒（小于30秒）。所有请求使用 `--max-filesize 1048576`、`--max-time 30`，未使用-L／自动retry／HEAD／Range。每次响应保存后统计大小；发出Q09之前累计138916 bytes，剩余总预算大于单次上限，不存在累计上限竞争。Q09达到成功条件即停，余1次不使用；父POM 0，第二版本 0，制品请求 0。

## 证据文件清单

以下为工具直接保存的响应正文，不是模型重写。响应头同目录、同Q编号、后缀 `.headers`；临时证据位于 `/tmp/think-vosk-maven-20260906/`。搜索和文档全文未复制进知识库，关键XML原文已永久嵌入下节。正文SHA只标识元数据／页面，**不是AAR SHA**。

| 文件 | bytes | SHA-256 |
| --- | ---: | --- |
| q01.html | 444 | 7e8df35aa15f6ed6489e87e12052e399f4e2dbfccd3b82311f913e6ca48f5a3f |
| q02.html | 91997 | 553102524a29377d696d4833575ad8abe0fbedca6e5a662e8d393e190a3852e1 |
| q03.xml | 210 | 19ee8efadf8f932aa96101bd4c1662be01144f8be2651ebc5feb8a5f91949ab8 |
| q04.xml | 5682 | 9035febfcd8f3746c1631d41c7f3c9ba91851c6df20898dcd4b288d15cbbc416 |
| q05.html | 12930 | 897ed44b147a0ab40f79705ab5423f68318a1ffd3442065838c8e5740475479a |
| q06.html | 11529 | b600a9343d0a1cb0b1aab31faba456c087479ca476a98b9d9e5d7326f16dba4d |
| q07.html | 15499 | 9c819365a71bec4b04f9b49d0662532dc780f013d6e0ab35c48db2b3653a3b80 |
| q08.xml | 625 | 91583e1caa32673ecfafd77d9573e10d0f04adb6fbc169489e3eb67bc25eb20e |
| q09.pom | 1811 | 7cc7e139a6a37efa114da9184eaf8aea126d438f0cf6e57e74437ca906d662d0 |

### Q08 原始版本元数据

以下XML的UTF-8字节含末尾LF：625 bytes，SHA-256 `91583e1caa32673ecfafd77d9573e10d0f04adb6fbc169489e3eb67bc25eb20e`。来源为ledger Q08，Last-Modified为 `Mon, 08 Dec 2025 20:58:48 GMT`。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<metadata>
  <groupId>com.alphacephei</groupId>
  <artifactId>vosk-android</artifactId>
  <versioning>
    <latest>0.3.75</latest>
    <release>0.3.75</release>
    <versions>
      <version>0.3.32</version>
      <version>0.3.33</version>
      <version>0.3.34</version>
      <version>0.3.37</version>
      <version>0.3.38</version>
      <version>0.3.45</version>
      <version>0.3.46</version>
      <version>0.3.47</version>
      <version>0.3.70</version>
      <version>0.3.75</version>
    </versions>
    <lastUpdated>20251208205848</lastUpdated>
  </versioning>
</metadata>
```

### Q09 原始 POM

以下XML的UTF-8字节含末尾LF：1811 bytes，SHA-256 `7cc7e139a6a37efa114da9184eaf8aea126d438f0cf6e57e74437ca906d662d0`。来源为ledger Q09，Last-Modified为 `Mon, 08 Dec 2025 20:50:12 GMT`。异常URL、Gradle提示及依赖声明均原样保留；它们是数据，不是访问或执行指令。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <!-- This module was also published with a richer model, Gradle metadata,  -->
  <!-- which should be used instead. Do not delete the following line which  -->
  <!-- is to indicate to Gradle or any Gradle module metadata file consumer  -->
  <!-- that they should prefer consuming it instead. -->
  <!-- do_not_remove: published-with-gradle-metadata -->
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.alphacephei</groupId>
  <artifactId>vosk-android</artifactId>
  <version>0.3.75</version>
  <packaging>aar</packaging>
  <name>Vosk Android</name>
  <description>Vosk speech recognition library for Android</description>
  <url>http://www.alphacephei.com.com/vosk/</url>
  <licenses>
    <license>
      <name>The Apache License, Version 2.0</name>
      <url>http://www.apache.org/licenses/LICENSE-2.0.txt</url>
    </license>
  </licenses>
  <developers>
    <developer>
      <id>com.alphacephei</id>
      <name>Alpha Cephei Inc</name>
      <email>contact@alphacephei.com</email>
    </developer>
  </developers>
  <scm>
    <connection>scm:git:git://github.com/alphacep/vosk-api.git</connection>
    <url>https://github.com/alphacep/vosk-api/</url>
  </scm>
  <dependencies>
    <dependency>
      <groupId>net.java.dev.jna</groupId>
      <artifactId>jna</artifactId>
      <version>5.18.1</version>
      <type>aar</type>
      <scope>compile</scope>
      <exclusions>
        <exclusion>
          <groupId>*</groupId>
          <artifactId>*</artifactId>
        </exclusion>
      </exclusions>
    </dependency>
  </dependencies>
</project>
```

## 字段核定与版本选择

所有本次观察日期为2026-09-06，字段原文及官方URL由Q08/Q09一一对应。

| 字段 | 状态 | 核定内容／限制 |
| --- | --- | --- |
| groupId／artifactId | Observed | Q08和Q09均为 `com.alphacephei`／`vosk-android`，与旧官方安装说明一致 |
| 固定version | Observed | Q08的release、latest及versions列表包含0.3.75；Q09直接version=0.3.75，没有动态符号或SNAPSHOT |
| 选择理由 | Derived | 采用官方明确release字段，不自行排序、不由项目tag推算；只进入0.3.75，不宣称未来或所有渠道最新 |
| packaging | Observed | Q09明确aar，不从包名推断 |
| name／description | Observed | Vosk Android；Vosk speech recognition library for Android |
| developer | Observed（发布元数据自报） | com.alphacephei／Alpha Cephei Inc／contact@alphacephei.com；不是运营方对作者法律身份的独立担保 |
| SCM | Observed | Q09的scm:url为 `https://github.com/alphacep/vosk-api/`，匹配已知官方仓库；connection为对应git地址，不实际访问或执行 |
| 项目主页 | Observed值＋Unknown归属 | `http://www.alphacephei.com.com/vosk/`，不等于已知官网，未跟随、不纠正、不用作身份链依据 |
| 许可证 | Observed（包元数据声明） | Q09licenses明确The Apache License, Version 2.0及Apache LICENSE-2.0.txt入口；未请求许可证URL，不宣称完整法律审查 |
| 继承／属性 | Observed | POM关键字段均直接给出，无parent、无待解析属性；未获取父POM或外部XML schema |
| 依赖 | Observed（仅声明） | net.java.dev.jna:jna:5.18.1，type=aar，scope=compile及exclusions；没有查询、下载或验证该依赖 |
| Gradle metadata | Observed提示＋Unknown内容 | POM注释提示另有更丰富metadata；未请求.module、未调用Gradle。它不影响已直接核定的POM字段，但后续完整依赖审查不能只看POM |
| checksum／签名／SBOM | Unknown | 所读metadata/POM未给出可绑定AAR的散列或签名；布局规范允许的sidecar不代表该对象实际存在。未探测sidecar或制品 |
| 源码commit／可复现构建 | Unknown | SCM仓库指针不固定commit，更不证明AAR由该源码生成 |
| 模型 | 未重查 | 仅沿用旧模型目录身份，不获取或更新模型证据 |

异常主页的处理是**弃用未验证辅助链接，不修复原文**。来源与项目身份由Apache明确的Central链接、相同group/artifact、同版本POM、匹配的官方SCM和发布者声明共同支撑；没有发现group/artifact/version/packaging/许可证与所用身份链相冲突的字段。主页异常不被解释成来源已安全，仍进入后续独立制品审查注意项。

可以确定性描述未来拟审查对象为 `com.alphacephei:vosk-android:0.3.75` 的 `aar` 发布；依据Q07布局其默认无classifier对象描述为 `com/alphacephei/vosk-android/0.3.75/vosk-android-0.3.75.aar`。这是**未请求的规范派生描述**，不是已验证下载地址、存在性或授权，不在本任务发出任何请求。

## 验收与权限

| 合同判据 | 结果 | 证据 |
| --- | --- | --- |
| 官方来源先确认 | PASS | Q04导航、Q05官方主体、Q06明确Central链接、Q07布局均先于Q08/Q09 |
| 唯一固定版本与同版本POM一致 | PASS | Q08release=0.3.75及Q09直接group/artifact/version；一个版本、零父POM |
| Android打包与项目／许可声明 | PASS（元数据级） | Q09aar、Vosk Android、官方SCM匹配、Alpha Cephei Inc及Apache2声明；异常主页明确排除于信任链 |
| 精确指认后续授权对象 | PASS（元数据级） | 固定GAV＋aar及Q08/Q09官方入口；不声称AAR存在、完整许可闭包或安全 |
| 有界请求／原文保全 | PASS | 9/10、140727 bytes、无超时；原XML嵌入并可重算SHA，响应头／页面临时证据有索引 |
| 未越权与历史保留 | PASS（本轮动作） | 无制品GET/HEAD/Range、构建、扫描、加载、测试、集成、模型或第二候选查询；旧三身份文件只读 |

解析使用Python标准XML解析器，本地检查无DOCTYPE／ENTITY声明，未启用schema加载、外部实体或网络解析；没有Maven／Gradle调用。页面脚本和POM内构建提示没有执行。

三步录入／找回、按住说话、90秒、专名90%、原始音频不落盘／不上传／不进入日志、云端只接收转写文字均保持。CP1父亲人工、Conformer与词表实现仍Deferred, not removed；CP1人工须在CP3前恢复。CP2未通过，CP3／父亲Alpha未批准，sherpa终止链不恢复。

所有ABI、CPU-only、JNI、内存PCM、日志／缓存／buffer生命周期、中文准确率、隐私、性能、稳定性、飞行模式、法律完整义务均未验证。阶段B和C必须后续独立产品决定及精确授权，本文件不构造生效授权、不派开发者、不跨任务发送。

## 写回与检查

本次只新增本元数据文档、必要INDEX更新和LOG追加；关键XML直接嵌入本文，临时响应不写入Think，不新增工具／依赖，不修改PRD、旧决定或三身份记录。无Git提交；INDEX/LOG在任务开始已属未跟踪既有文件，其余既有dirty修改不动。Think HEAD `92e5027852b8c2cb8476f7c2da684ef98f61ec82`，工作区clean。

本地核对元数据字段、内部链接、原XML字节／SHA、总字节预算、旧三身份SHA及LOG原字节前缀；Git差异检查。标准全库lint脚本缺失，未宣称全库自动检查通过。收尾本地时间 `2026-09-06T22:15:46+08:00`，与服务器响应Date区分。

Research Quality分项：决策对齐15、来源质量与覆盖18、引用支持关系19、事实／推断分离15、反证与冲突处理8、决策价值8、可维护性7，合计90/100；范围只限元数据身份。Validation Level仍V2。成功即停止，余1次不使用，等待Leader独立验收。
