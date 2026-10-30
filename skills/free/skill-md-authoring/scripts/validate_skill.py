#!/usr/bin/env python3
"""Validate Agent Skills (agentskills.io spec) SKILL.md files. Usage: validate_skill.py <skill-dir-or-root> ..."""
import os, re, sys

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

def parse_frontmatter(text):
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with '---' YAML frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("frontmatter not closed with '---'")
    fm, body = text[4:end], text[end + 4:]
    data, cur = {}, None
    for line in fm.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) and cur:
            data.setdefault(cur + ".", []).append(line.strip()); continue
        if ":" not in line:
            raise ValueError(f"bad frontmatter line: {line!r}")
        k, v = line.split(":", 1)
        cur = k.strip(); data[cur] = v.strip().strip('"').strip("'")
    return data, body

def validate(d):
    errs = []
    p = os.path.join(d, "SKILL.md")
    if not os.path.isfile(p):
        return [f"{d}: missing SKILL.md"]
    text = open(p, encoding="utf-8").read()
    try:
        fm, body = parse_frontmatter(text)
    except ValueError as e:
        return [f"{p}: {e}"]
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name: errs.append("name missing")
    elif len(name) > 64 or not NAME_RE.match(name): errs.append(f"invalid name {name!r}")
    elif name != os.path.basename(os.path.abspath(d)): errs.append(f"name {name!r} != folder {os.path.basename(d)!r}")
    if not desc: errs.append("description missing")
    elif len(desc) > 1024: errs.append(f"description too long ({len(desc)})")
    elif "use when" not in desc.lower(): errs.append("description should say 'Use when ...'")
    if "compatibility" in fm and not (1 <= len(fm["compatibility"]) <= 500): errs.append("compatibility length")
    if body.count("\n") > 500: errs.append("body > 500 lines; move details to references/")
    if re.search(r"(ghp_|github_pat_|sk-[A-Za-z0-9]{20}|AKIA[0-9A-Z]{16})", text): errs.append("possible secret in SKILL.md")
    return [f"{p}: {e}" for e in errs]

def find(root):
    if os.path.isfile(os.path.join(root, "SKILL.md")):
        yield root; return
    for dp, dn, fn in os.walk(root):
        if "SKILL.md" in fn: yield dp

if __name__ == "__main__":
    roots = sys.argv[1:] or ["."]
    n, errs = 0, []
    for r in roots:
        for d in sorted(find(r)):
            n += 1; errs += validate(d)
    for e in errs: print("FAIL", e)
    print(f"checked {n} skill(s), {len(errs)} problem(s)")
    sys.exit(1 if errs or n == 0 else 0)
