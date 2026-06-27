---
name: code-review
description: Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.
argument-hint: "<PR URL, diff, or file path>"
---
# /code-review

> **语言规则 (Language Rules)**
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

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).
Review code changes with a structured lens on security, performance, correctness, and maintainability.
## Usage
```
/code-review <PR URL or file path>
```
Review the provided code changes: @$1
If no specific file or URL is provided, ask what to review.
## How It Works
```
┌─────────────────────────────────────────────────────────────────┐
│                      CODE REVIEW                                   │
├─────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                       │
│  ✓ Paste a diff, PR URL, or point to files                      │
│  ✓ Security audit (OWASP top 10, injection, auth)               │
│  ✓ Performance review (N+1, memory leaks, complexity)           │
│  ✓ Correctness (edge cases, error handling, race conditions)    │
│  ✓ Style (naming, structure, readability)                        │
│  ✓ Actionable suggestions with code examples                    │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Source control: Pull PR diff automatically                    │
│  + Project tracker: Link findings to tickets                     │
│  + Knowledge base: Check against team coding standards           │
└─────────────────────────────────────────────────────────────────┘
```
## Review Dimensions
### Security
- SQL injection, XSS, CSRF
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure deserialization
- Path traversal
- SSRF
### Performance
- N+1 queries
- Unnecessary memory allocations
- Algorithmic complexity (O(n²) in hot paths)
- Missing database indexes
- Unbounded queries or loops
- Resource leaks
### Correctness
- Edge cases (empty input, null, overflow)
- Race conditions and concurrency issues
- Error handling and propagation
- Off-by-one errors
- Type safety
### Maintainability
- Naming clarity
- Single responsibility
- Duplication
- Test coverage
- Documentation for non-obvious logic
## Output
```markdown
## Code Review: [PR title or file]
### Summary
[1-2 sentence overview of the changes and overall quality]
### Critical Issues
| # | File | Line | Issue | Severity |
|---|------|------|-------|----------|
| 1 | [file] | [line] | [description] | 🔴 Critical |
### Suggestions
| # | File | Line | Suggestion | Category |
|---|------|------|------------|----------|
| 1 | [file] | [line] | [description] | Performance |
### What Looks Good
- [Positive observations]
### Verdict
[Approve / Request Changes / Needs Discussion]
```
## If Connectors Available
If **~~source control** is connected:
- Pull the PR diff automatically from the URL
- Check CI status and test results
If **~~project tracker** is connected:
- Link findings to related tickets
- Verify the PR addresses the stated requirements
If **~~knowledge base** is connected:
- Check changes against team coding standards and style guides
## Tips
1. **Provide context** — "This is a hot path" or "This handles PII" helps me focus.
2. **Specify concerns** — "Focus on security" narrows the review.
3. **Include tests** — I'll check test coverage and quality too.
