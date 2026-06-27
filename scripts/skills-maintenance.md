# Skills 维护

## 1. 获取 Skills

直接访问本项目仓库，AI 会自动根据 README 找到需要的 skill：

**https://github.com/Tobeicer/AI_dev**

## 2. 更新脚本

`scripts/update-skills.py` 用于从官方源拉取最新 SKILL.md 并覆盖本地版本。

**使用方法：**

```bash
# 更新所有 skill
python scripts/update-skills.py --all

# 更新指定 skill
python scripts/update-skills.py --skill brainstorming

# 列出所有可更新的 skill
python scripts/update-skills.py --list
```

**脚本执行流程：**

1. 从 `SKILL_SOURCES` 配置的官方源拉取最新 SKILL.md
2. 备份当前版本到 `e:\Desktop_zm\AI_dev\skills_backup\YYYY-MM-DD\`
3. 对以下 skill 自动注入中文语言规则（在 frontmatter 之后）：
   - **brainstorming** → 用户可见的设计文档、确认提问、阶段汇报使用中文
   - **planning-with-files** → task_plan/findings/progress 三个文件使用中文
   - **code-review** → 审查报告的问题描述、修复建议使用中文
4. 写入 `e:\Desktop_zm\AI_dev\skills\<skill-name>\SKILL.md`
5. 记录日志到 `e:\Desktop_zm\AI_dev\scripts\skills-update.log`

**中文规则修改位置：** 脚本中的 `LANGUAGE_RULES` 字典。

## 3. Skill 来源

| Skill | 评分 | 官方来源 |
|-------|------|----------|
| using-superpowers | 10 | [obra/superpowers](https://github.com/obra/superpowers) |
| brainstorming | 10 | [obra/superpowers](https://github.com/obra/superpowers) |
| planning-with-files | 10 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) |
| code-review | 9 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| markitdown ⚠️ | 9 | 非官方，基于 [microsoft/markitdown](https://github.com/microsoft/markitdown) 封装 |
| ui-ux-pro-max | 8.5 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| test-driven-development | 8.5 | [obra/superpowers](https://github.com/obra/superpowers) |
| mcp-builder | 8.5 | [anthropics/skills](https://github.com/anthropics/skills) |
| context-engineering | 8 | [InugamiDev/ultrathink-oss](https://github.com/InugamiDev/ultrathink-oss) |

> ⚠️ **markitdown** 是本仓库维护者基于微软开源项目编写的 skill，microsoft/markitdown 不提供官方 SKILL.md。
