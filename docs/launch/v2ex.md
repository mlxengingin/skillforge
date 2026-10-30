# V2EX 草稿（节点：分享创造 /go/create）

**标题**：做了个 Agent Skills 技能包 + 免费 SKILL.md 生成器，帮 AI 编程助手把“做产品到收款”的流程跑通

**正文**
大家好，最近 Cursor / Claude Code / Codex 都支持 Agent Skills（SKILL.md），我做了两个东西：

1. **免费的 SKILL.md 在线生成器**：填表实时生成符合 agentskills.io 规范的 SKILL.md（name 校验、description 带 "Use when"），纯前端，数据不出浏览器。另外开源了 3 个技能和一个校验脚本（MIT）。
2. **Pro 技能包（13 个）**：出海工具站选词与落地页、程序化 SEO（带防薄内容闸门）、MV3 插件 MVP、闲鱼 AI 服务产品化、个人主体小程序虚拟支付接入（签名/发货推送幂等/查单兜底）、AI 内容标识合规、收款路径选择、定价实验、发布帖等。

技术上就是一个 GitHub Pages 静态站，技能用一个 Python 源文件生成并统一校验。

- 网站：https://mlxengingin.github.io/skillforge/
- 仓库：https://github.com/mlxengingin/skillforge

Pro 定价 ¥79 一次买断。想听听大家意见：哪些技能值得做成免费的，哪些流程你最希望交给 Agent？
