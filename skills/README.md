# Skills 索引

| Skill | 评分 | 使用场景 | 核心功能 | 来源 |
|-------|------|---------|---------|------|
| [using-superpowers](./using-superpowers/) | 10 | Skill 自动发现与调度 | 对话开始时检查可用 Skills，确保相关 Skills 被触发调用 | [obra/superpowers](https://github.com/obra/superpowers) |
| [brainstorming](./brainstorming/) | 10 | 设计/创意阶段需求梳理 | 引导式头脑风暴，一问一步，将模糊想法转化为设计文档和规格说明 | [obra/superpowers](https://github.com/obra/superpowers) |
| [planning-with-files](./planning-with-files/) | 10 | 复杂任务状态保持 | 把规划写进文件（task_plan/findings/progress），上下文压缩也不丢状态 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) |
| [code-review](./code-review/) | 9 | 代码审查 | 多维度审查（安全/性能/正确性/可维护性），结构化输出问题分级 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| [markitdown](./markitdown/) ⚠️ | 9 | 文档格式转换 | 调用微软 markitdown CLI 将 PDF/Office/图片/音频/网页转 Markdown | **非官方** — 见下方说明 |
| [ui-ux-pro-max](./ui-ux-pro-max/) | 8.5 | UI/UX 设计 | 67 种风格 + 161 套配色 + 57 字体配对，覆盖 17 个技术栈 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| [test-driven-development](./test-driven-development/) | 8.5 | 测试驱动开发 | 红-绿-重构循环，先写测试再写代码 | [obra/superpowers](https://github.com/obra/superpowers) |
| [mcp-builder](./mcp-builder/) | 8.5 | MCP 服务器开发 | 快速构建 MCP 服务器，低代码定义工具接口（TypeScript/Python） | [anthropics/skills](https://github.com/anthropics/skills) |
| [context-engineering](./context-engineering/) | 8 | 上下文窗口优化 | 上下文工程学，结构化压缩以最大化模型理解力 | [InugamiDev/ultrathink-oss](https://github.com/InugamiDev/ultrathink-oss) |

## ⚠️ 关于 markitdown（唯一非官方 skill）

**markitdown 不是 Claude Code Skill 格式**——`microsoft/markitdown` 是微软开源的 Python 工具库（CLI + Python API），不提供官方 SKILL.md。

**当前 SKILL.md 由本仓库维护者编写**，基于微软 markitdown 官方文档（PyPI + GitHub README），主要作用是：
- 让 AI 在触发条件命中时自动调用 `markitdown` CLI
- 包含安装检查、CLI/Python 用法、批量转换等可执行步骤
- 文档来源客观准确（基于官方 README），但 skill 封装本身非官方

**跟进方式**：当 markitdown 新版本发布时（PyPI/GitHub Releases），本 skill 需要同步更新触发条件和 API 用法。

## 更新机制

所有 ⚠️ 标记外的 skill 都通过 [`scripts/update-skills.ps1`](../scripts/update-skills.ps1) 自动从官方仓库拉取最新 SKILL.md，并保留用户在 [brainstorming](./brainstorming/)、[planning-with-files](./planning-with-files/)、[code-review](./code-review/) 三个 skill 顶部添加的中文语言规则。

