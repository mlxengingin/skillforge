# 开卖只差你的一步（约 10 分钟）

产品、网站、技能包、封面、文案都已就绪。收款账号必须本人实名，所以只有这一步需要你：

## 推荐：爱发电（国内买家，微信/支付宝付款）
1. 打开 https://afdian.com/ → 手机号注册 → 完成实名认证
2. 「创建商品」→ 电子商品 → 上传私有仓库 https://github.com/mlxengingin/skillforge-pro 的 `dist/skillforge-pro-pack.zip`（登录 GitHub 后打开 → Download raw；或让我把文件发给你）作为自动发货文件
3. 标题、详情、价格、封面：全部照抄 `docs/listing/afdian.md` + `assets/cover-afdian.png`
4. 发布后**把商品链接发给我**（Grok Bot），我会写进网站并推送，购买按钮自动从「即将开售」变成「购买 Pro」

> 想自己改也行：编辑仓库根目录 `config.js`，把链接填进 `proPaymentUrl: ""` 的引号里，提交即可。

## 可选（以后再做）
- **Gumroad（海外买家）**：New product → Digital → 上传同一个 zip → 照抄 `docs/listing/gumroad.md` + `assets/cover-gumroad.png`。链接发我，我会填到 `proPaymentUrlEn`（英文页用 Gumroad、中文页用爱发电）。
- **Agensi（技能市场）**：注册创作者并连接 Stripe 或 USDC → 照 `docs/listing/agensi.md` 上架 3 个技能。

## 你不需要做的
写代码、做页面、做封面、写文案、部署。发布帖草稿在 `docs/launch/`，是否发布由你决定（我不会代发）。

## 售后提醒
- 退款承诺：7 天内无法加载或与描述不符可退款（写在网站与商品页）。有人申请时在平台订单页操作即可。
