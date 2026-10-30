---
name: github-pages-product-ship
description: "Ships a static product site to GitHub Pages with pricing, FAQ, refund policy, SEO tags (title, meta, Open Graph), sitemap.xml and robots.txt, plus a config-driven checkout link that degrades to 'coming soon'. Use when the user wants a public demo or landing page today without a server, or says 'deploy to GitHub Pages'."
license: MIT
metadata:
  author: skillforge
  version: "1.1"
  pack: skillforge-free
---
# GitHub Pages 产品站上线

## 何时使用
需要今天就有一个公开网址展示并（稍后）收款，不想买服务器。

## 步骤
1. 静态文件放仓库根目录（或 `/docs`），加空文件 `.nojekyll`。
2. 页面必须有：一句话价值、演示/示例、定价卡、FAQ、退款说明、页脚联系方式。
3. SEO：`<title>`、`meta description`、`link rel=canonical`、Open Graph（`og:title`/`og:description`/`og:image` 1200×630）、`sitemap.xml`、`robots.txt`。
4. 收款链接放 `config.js`：`window.APP_CONFIG = { checkoutUrl: "" }`。前端判断：为空时按钮显示“即将开售”并禁用，**不能抛错**。
5. 开启 Pages：仓库 Settings → Pages → main / root；或 `gh api -X POST repos/<owner>/<repo>/pages` 传 JSON `{"source":{"branch":"main","path":"/"}}`。
6. 验证：`curl -sI https://<owner>.github.io/<repo>/` 返回 200；用无头浏览器截桌面与手机两张图。

## 输出
- 可访问 URL、两张截图、`config.js` 填写说明

## 边界情况
- 404：确认分支/路径正确，等待 1–2 分钟构建。
- 中文乱码：`<meta charset="UTF-8">`。

## 护栏
- 不提交任何密钥；结账链接只放公开 URL。
