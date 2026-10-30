# 你只需要做的一次性动作（之后可以完全不管）

产品与仓库已由 AI 建好。要开始收款，只需完成下面 **1 件事**（任选一种收款方式）：

## 选项 A（国内最快）：爱发电
1. 打开 https://afdian.com/ 用手机号注册创作者
2. 新建商品「SkillForge Pro Pack」，定价 **19 元或 $19 等值**
3. 商品说明可直接复制 `docs/AGENSI_LISTING.md` 中文版段落
4. 复制商品链接，发给我或自己改仓库文件：
   - 编辑 `web/config.js`
   - 把 `proPaymentUrl` 改成你的商品链接
5. 推送到 `main` 后，GitHub Pages 上的 **Buy** 按钮会自动生效

## 选项 B（出海）：Gumroad / Creem
1. 注册 Gumroad 或 Creem，创建 $19 一次性商品
2. 上传 `dist/skillforge-pro-pack.zip` 作为自动发货文件
3. 把结账链接写入 `web/config.js` 的 `proPaymentUrl`

## 选项 C（Agent 市场）：Agensi
1. 注册 https://www.agensi.io/ 创作者并连接 Stripe/USDC
2. 按 `docs/AGENSI_LISTING.md` 上架 Pro skills（可拆开卖或打包 $19–$49）
3. 平台抽成约 30%，创作者约 70%

## 不需要你做的
- 写代码、改文案、做页面、开 GitHub 仓库、部署演示站
- 拍短视频、每天运营账号、做客服话术（仓库里已有交付模板）

完成选项 A/B/C 任一之后，把支付链接贴回对话即可，我会替你写进 `config.js` 并推送。
