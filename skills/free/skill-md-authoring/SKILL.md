---
name: skill-md-authoring
description: "Writes or repairs a SKILL.md that follows the Agent Skills spec (agentskills.io): valid name/description frontmatter, trigger-friendly description, step-by-step body, examples, edge cases, progressive disclosure via references/. Use when the user asks to create, improve, validate, or package an agent skill for Cursor, Claude Code, Codex, or OpenClaw."
license: MIT
metadata:
  author: skillforge
  version: "1.1"
  pack: skillforge-free
---
# SKILL.md 编写与校验

## 何时使用
- 用户说“做一个 skill / 写个 SKILL.md / 把这个流程变成技能”
- 已有 SKILL.md 不触发、太长、或校验失败

## 输入
- 这个技能要完成的一件事（一句话）
- 2–3 个用户真实会说的触发说法
- 有无脚本、模板、参考资料

## 步骤
1. 定 `name`：小写字母/数字/连字符，≤64 字符，不以连字符开头结尾，无 `--`，并且**与文件夹同名**。
2. 写 `description`（≤1024 字符）：第一句写“做什么”，第二句写“Use when …”，塞入用户会说的关键词（中英都放）。这是 Agent 决定是否加载技能的唯一依据。
3. 正文按顺序：何时使用 → 输入 → 步骤（编号、每步有可检查的产出）→ 输出格式 → 示例 → 边界情况 → 护栏。
4. 正文控制在 500 行内；长资料放 `references/xxx.md`，模板放 `assets/`，脚本放 `scripts/`，正文里用相对路径引用，只引用一层。
5. 可选字段：`license`、`compatibility`（仅在有环境要求时写）、`metadata`（字符串键值）。
6. 校验：运行 `python3 scripts/validate_skill.py <skill-dir>`（本技能自带），或官方 `skills-ref validate <dir>`。

## 输出格式
```markdown
---
name: <kebab-name>
description: <做什么>. Use when <触发场景与关键词>.
---
# <标题>
## 何时使用
## 步骤
## 输出
## 示例
## 边界情况
## 护栏
```

## 示例
差：`description: 帮你写文案。`
好：`description: Drafts Xianyu (闲鱼) service listings with SKUs, price tiers and delivery SOP. Use when the user wants to sell an AI/automation service on 闲鱼 or asks for 闲鱼上架文案.`

## 边界情况
- 一个技能塞了三件事 → 拆成三个技能。
- 描述里全是形容词没有关键词 → 重写为“动词 + 对象 + 场景”。
- 需要密钥 → 只写读取环境变量的方式，绝不写入真实值。

## 护栏
- 不在技能里放任何密钥、Cookie、个人信息。
- 不写未经确认的破坏性命令（rm -rf、force push）。
