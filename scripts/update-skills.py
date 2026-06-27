#!/usr/bin/env python3
"""
Skill 更新脚本

从官方仓库拉取最新 SKILL.md，备份旧版本，注入中文语言规则。

用法：
    python update-skills.py --all
    python update-skills.py --skill brainstorming
    python update-skills.py --list   # 列出所有可更新的 skill
"""

import argparse
import os
import shutil
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

# ============ 路径配置 ============
SCRIPT_DIR = Path(__file__).parent.resolve()
SKILLS_DIR = Path("e:/Desktop_zm/AI_dev/skills")
BACKUP_DIR = Path("e:/Desktop_zm/AI_dev/skills_backup")
LOG_FILE = SCRIPT_DIR / "skills-update.log"

# ============ 语言规则 ============
LANGUAGE_RULES = {
    "brainstorming": """> **语言规则 (Language Rules)**
>
> 本 skill 中所有面向用户的输出（用户可见文档）必须使用**中文（简体）**：
> - 设计文档（design doc / spec）→ **中文**
> - 与用户确认的提问、选项、说明 → **中文**
> - 阶段性汇报、总结 → **中文**
>
> 仅以下场景可使用英文：
> - 内部推理、技术术语、代码示例、文件路径
> - 引用第三方文档原文
>
> **关键判断标准**：如果用户需要阅读并确认 → 中文；如果仅供 AI 自己处理 → 保留英文。

""",
    "planning-with-files": """> **语言规则 (Language Rules)**
>
> 本 skill 涉及用户可见文档时必须使用**中文（简体）**：
> - `task_plan.md` 中的目标、阶段、决策说明 → **中文**
> - `findings.md` 中的研究发现、关键结论 → **中文**
> - `progress.md` 中的进度汇报、错误日志说明 → **中文**
> - 与用户确认的阶段汇报 → **中文**
>
> 仅以下场景可使用英文：
> - 代码片段、命令、文件路径、技术术语
> - 错误信息原文（保留 stderr/stdout 原始输出）
> - git 提交信息
>
> **关键判断标准**：如果用户需要阅读并确认进度/规划 → 中文；如果仅供 AI 自己处理的临时记录 → 可保留英文。

""",
    "code-review": """> **语言规则 (Language Rules)**
>
> 本 skill 输出的代码审查报告（用户阅读的部分）必须使用**中文（简体）**：
> - 问题标题、问题描述、严重程度说明、修复建议 → **中文**
> - 审查总结、风险评估、优先级建议 → **中文**
>
> 仅以下场景可使用英文：
> - 代码片段、文件路径、行号、变量名、函数名
> - 工具命令、CI 标识符、技术术语原文（如 SQL Injection、N+1、OWASP）
>
> **关键判断标准**：报告中的描述性文字、问题说明、建议 → 中文；技术标识符和代码 → 保留原文。

""",
}

# ============ Skill 官方源 ============
SKILL_SOURCES = {
    "using-superpowers":       ("obra", "superpowers", "main", "skills/using-superpowers/SKILL.md"),
    "brainstorming":           ("obra", "superpowers", "main", "skills/brainstorming/SKILL.md"),
    "test-driven-development": ("obra", "superpowers", "main", "skills/test-driven-development/SKILL.md"),
    "mcp-builder":             ("anthropics", "skills", "main", "skills/mcp-builder/SKILL.md"),
    "code-review":             ("anthropics", "knowledge-work-plugins", "main", "engineering/skills/code-review/SKILL.md"),
    "planning-with-files":     ("OthmanAdi", "planning-with-files", "master", ".codebuddy/skills/planning-with-files/SKILL.md"),
    "context-engineering":     ("InugamiDev", "ultrathink-oss", "main", ".claude/skills/context-engineering/SKILL.md"),
    "ui-ux-pro-max":           ("nextlevelbuilder", "ui-ux-pro-max-skill", "main", ".claude/skills/ui-ux-pro-max/SKILL.md"),
}


def log(msg, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] [{level}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def backup_skill(name):
    src = SKILLS_DIR / name / "SKILL.md"
    if not src.exists():
        log(f"跳过备份：{name} 不存在", "WARN")
        return
    date = datetime.now().strftime("%Y-%m-%d")
    dst = BACKUP_DIR / date / name
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst / "SKILL.md")
    log(f"已备份：{name} → {dst}")


def inject_language_rule(name, content):
    if name not in LANGUAGE_RULES:
        return content
    rule = LANGUAGE_RULES[name]
    # 查找 frontmatter 结束位置（第二个 "---"）
    first_dash = content.find("---")
    if first_dash < 0:
        log(f"未找到 frontmatter，跳过规则注入：{name}", "WARN")
        return content
    second_dash = content.find("\n---", first_dash + 3)
    if second_dash < 0:
        log(f"未找到 frontmatter 结束，跳过规则注入：{name}", "WARN")
        return content
    insert_pos = second_dash + 4  # 跳过 "\n---"
    result = content[:insert_pos] + "\n" + rule + content[insert_pos:]
    log(f"已注入中文语言规则：{name}")
    return result


def update_skill(name):
    if name not in SKILL_SOURCES:
        log(f"未知 skill：{name}", "ERROR")
        return False
    owner, repo, branch, path = SKILL_SOURCES[name]
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    log(f"开始更新：{name}")
    log(f"  源：{url}")

    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            content = resp.read().decode("utf-8")
    except Exception as e:
        log(f"下载失败：{name} - {e}", "ERROR")
        return False

    backup_skill(name)
    content = inject_language_rule(name, content)

    target = SKILLS_DIR / name
    target.mkdir(parents=True, exist_ok=True)
    (target / "SKILL.md").write_text(content, encoding="utf-8")
    log(f"更新成功：{name} → {target / 'SKILL.md'}")
    return True


def main():
    parser = argparse.ArgumentParser(description="从官方源更新 skill")
    parser.add_argument("--all", action="store_true", help="更新所有 skill")
    parser.add_argument("--skill", type=str, help="更新指定 skill")
    parser.add_argument("--list", action="store_true", help="列出所有可更新的 skill")
    args = parser.parse_args()

    log("===== Skill 更新开始 =====")

    if args.list:
        print("\n可用 skill：")
        for n in SKILL_SOURCES:
            print(f"  - {n}")
        return

    targets = []
    if args.all:
        targets = list(SKILL_SOURCES.keys())
    elif args.skill:
        if args.skill not in SKILL_SOURCES:
            log(f"未知 skill：{args.skill}。使用 --list 查看可用列表", "ERROR")
            sys.exit(1)
        targets = [args.skill]
    else:
        parser.print_help()
        sys.exit(1)

    if args.all:
        log("批量更新所有 skill")
        success = fail = 0
        for name in targets:
            if update_skill(name):
                success += 1
            else:
                fail += 1
        log(f"批量更新完成：成功 {success}，失败 {fail}")
    else:
        for name in targets:
            update_skill(name)

    log("===== Skill 更新结束 =====")


if __name__ == "__main__":
    main()
