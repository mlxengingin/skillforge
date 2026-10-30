#!/usr/bin/env python3
"""Generate og.png, favicon and store covers with Pillow. Run: python3 tools/make_covers.py"""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
R = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SC = 2  # Simplified Chinese face index in the .ttc
def f(path, size): return ImageFont.truetype(path, size, index=SC)
BG, CARD, LINE, FG, MUT, ACC, ACC2 = (11,13,18), (20,24,36), (35,42,59), (232,236,244), (154,165,189), (124,92,255), (34,211,238)

def bg(w, h):
    im = Image.new("RGB", (w, h), BG); d = ImageDraw.Draw(im)
    for i in range(0, w, 40): d.line([(i, 0), (i, h)], fill=(16,19,27))
    for j in range(0, h, 40): d.line([(0, j), (w, j)], fill=(16,19,27))
    # gradient bar
    for x in range(w):
        t = x / w; c = tuple(int(ACC[k]*(1-t) + ACC2[k]*t) for k in range(3))
        d.line([(x, 0), (x, 10)], fill=c)
    return im, d

def chips(d, x, y, items, size):
    ft = f(R, size)
    for it in items:
        tw = d.textlength(it, font=ft); pad = size*0.7
        d.rounded_rectangle([x, y, x+tw+2*pad, y+size*2], radius=size, outline=LINE, fill=CARD, width=2)
        d.text((x+pad, y+size*0.35), it, font=ft, fill=MUT); x += tw + 2*pad + size*0.6
    return x

def make(name, w, h, title, sub, chips_items, price=None, logo_size=None):
    im, d = bg(w, h); s = w/1200
    ls = int((logo_size or 44)*s)
    d.text((int(70*s), int(60*s)), "Skill", font=f(B, ls), fill=FG)
    d.text((int(70*s)+d.textlength("Skill", font=f(B, ls)), int(60*s)), "Forge", font=f(B, ls), fill=ACC)
    y = int(150*s)
    for line in title:
        d.text((int(70*s), y), line, font=f(B, int(68*s)), fill=FG); y += int(88*s)
    y += int(10*s)
    for line in sub:
        d.text((int(70*s), y), line, font=f(R, int(30*s)), fill=MUT); y += int(44*s)
    chips(d, int(70*s), h - int(110*s), chips_items, int(22*s))
    if price:
        pf = f(B, int(46*s)); tw = d.textlength(price, font=pf)
        x1 = w - int(70*s); x0 = x1 - tw - int(60*s); y0 = int(56*s)
        d.rounded_rectangle([x0, y0, x1, y0+int(80*s)], radius=int(18*s), fill=ACC)
        d.text((x0+int(30*s), y0+int(6*s)), price, font=pf, fill=(255,255,255))
    out = os.path.join(ROOT, "assets", name); im.save(out, optimize=True); print(out, im.size)

make("og.png", 1200, 630, ["Agent Skills that ship", "products & get you paid"],
     ["Free SKILL.md generator + 13 spec-compliant Pro skills", "for Cursor · Claude Code · Codex"],
     ["SKILL.md", "agentskills.io spec", "13 Pro skills", "zh / en"])
make("cover-afdian.png", 1200, 800, ["AI 编程助手技能包", "13 个 Pro Agent Skills"],
     ["出海工具站 · 程序化SEO · 闲鱼服务上架 · 小程序虚拟支付", "AI内容标识合规 · 收款路径 · 定价实验 · 发布帖套件", "放进 Cursor / Claude Code / Codex 直接用"],
     ["SKILL.md 规范", "中文说明", "免费更新", "7 天退款"], price="¥79")
make("cover-gumroad.png", 1280, 720, ["SkillForge Pro", "13 Agent Skills to ship & sell"],
     ["Micro-SaaS SEO · Programmatic SEO · Chrome extension MVP", "Marketplace listing · Payment rails · Pricing tests", "Works in Cursor, Claude Code, Codex"],
     ["SKILL.md", "Lifetime updates", "7-day refund"], price="$15")
make("cover-agensi.png", 1200, 630, ["SkillForge Pro Pack", "Build → List → Get paid"],
     ["13 SKILL.md workflows for indie builders", "spec-valid · guardrails · references included"],
     ["Cursor", "Claude Code", "Codex", "OpenClaw"], price="$15")
# square thumbnail (Gumroad thumbnail 600x600) + favicon
im, d = bg(600, 600)
d.text((60, 190), "Skill", font=f(B, 120), fill=FG); d.text((60, 320), "Forge", font=f(B, 120), fill=ACC)
d.text((64, 480), "13 Pro Agent Skills", font=f(R, 34), fill=MUT)
im.save(os.path.join(ROOT, "assets", "thumb-600.png"), optimize=True)
fv = Image.new("RGB", (64, 64), ACC); fd = ImageDraw.Draw(fv); fd.text((14, 2), "S", font=f(B, 48), fill=(255,255,255))
fv.save(os.path.join(ROOT, "assets", "favicon.png"))
print("thumb+favicon ok")
