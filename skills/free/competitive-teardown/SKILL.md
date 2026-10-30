---
name: competitive-teardown
description: "Builds a dated competitor matrix (features, pricing tiers, acquisition channel, weaknesses) and turns it into a one-week shippable wedge and a first paid SKU. Use when the user asks for 竞品分析, competitor research, market comparison, or 'who else does this and how do they make money' before building a product."
license: MIT
metadata:
  author: skillforge
  version: "1.1"
  pack: skillforge-free
---
# 竞品拆解 → 一周可交付的切入点

## 何时使用
动手做产品前，或者用户问“有没有人做过 / 竞品怎么收费 / 我们怎么差异化”。

## 输入
- 产品一句话设想
- 目标市场（国内 / 出海）

## 步骤
1. **找 5–8 个竞品**：搜索“<品类> alternative”“<品类> pricing”、Product Hunt、GitHub、小红书/即刻同类帖。每个记下 URL 和查阅日期。
2. **每个竞品填一行**：一句话定位｜核心功能（≤5 条）｜定价档位（原文照抄，标注日期）｜获客渠道（SEO / 社媒 / 市场 / 广告 / 开源 star）｜差评或缺口（来自评论、issue、Reddit）。
3. **归类**：直接竞品（同人群同任务）/ 替代方案（Excel、人工、免费开源）/ 渠道方（市场平台，可能是合作者而非对手）。
4. **找切入点**：从“缺口”列挑一个满足三条的：一周内能做出；能用一句话说清；目标用户会为它付钱（已有人在为类似东西付钱）。
5. **定第一个付费 SKU**：价格参照竞品最低付费档或更低的一次性买断；写出 7 天成功指标（如访问 → 下载 → 付费各多少）。

## 输出
1. 竞品表（Markdown 表格，含来源列）
2. 一段差异化声明：「给 <人群> 做 <任务>，不同于 <竞品> 的是 <切入点>」
3. 第一个 SKU：名称、价格、交付物、7 天指标

## 边界情况
- 查不到收入数据 → 写“未公开”，不要估算后当事实写。
- 竞品是开源免费 → 看能否卖“省时间的打包/托管/中文本地化”，而不是同功能。

## 护栏
- 每个数字都要有来源和日期。
- 不抄竞品文案和素材。
