---
name: context-engineering
description: Context window optimization, token budget management, and information compression for AI-assisted workflows
---

# Context Engineering

## Purpose

Context engineering is the discipline of maximizing the signal-to-noise ratio within a finite context window. Every token spent on irrelevant information is a token unavailable for reasoning. This skill provides strategies for curating, compressing, and structuring information so that AI agents operate with maximum relevant context and minimum waste.

## Key Concepts

### Context Window Economics

Think of the context window as a budget:

| Budget Zone | Allocation | Content Type |
|-------------|------------|--------------|
| **System** (10-15%) | Fixed | System prompt, persona, rules |
| **Task** (20-30%) | Per-task | Current task instructions, requirements |
| **Reference** (30-40%) | Selective | Code, docs, examples relevant to task |
| **Working Memory** (15-25%) | Dynamic | Conversation history, intermediate results |
| **Output Reserve** (10-15%) | Reserved | Space for the model to generate response |

### The Relevance Hierarchy

Not all context is equal. Prioritize:
1. **Direct** — Code/docs the task directly modifies or depends on
2. **Adjacent** — Code/docs one degree removed (callers, callees, types)
3. **Structural** — Architecture, patterns, conventions in the codebase
4. **Historical** — Why things are the way they are (git blame, ADRs)
5. **General** — Language/framework reference (use external tools instead)

## Strategies

### Strategy 1: Layered Context Loading

Load context in layers, from most to least critical:

```
LAYER 0 — ALWAYS PRESENT:
  - Task description and acceptance criteria
  - Key constraints and requirements
  - Output format specification
LAYER 1 — LOAD FIRST:
  - Files being directly modified
  - Type definitions and interfaces used
  - Test files for the target code
LAYER 2 — LOAD IF BUDGET ALLOWS:
  - Adjacent files (importers/importees)
  - Configuration files (tsconfig, package.json)
  - Similar implementations for pattern reference
LAYER 3 — LOAD ON DEMAND:
  - Documentation and READMEs
  - Git history for changed files
  - CI/CD configuration
LAYER 4 — EXTERNAL RETRIEVAL:
  - Library documentation (use Context7)
  - Stack Overflow / community solutions (use web search)
  - Full repository structure (use repomix)
```

### Strategy 2: Progressive Summarization

Transform verbose content into increasingly dense representations:

```
LEVEL 0 — RAW (100% tokens):
  Full source file with all comments and implementations
LEVEL 1 — TRIMMED (60% tokens):
  Remove imports, empty lines, obvious implementations
  Keep signatures, complex logic, comments
LEVEL 2 — SKELETON (30% tokens):
  Type signatures, function signatures, class structure
  Remove all implementation bodies
LEVEL 3 — MANIFEST (10% tokens):
  File purpose, exported API surface, dependencies list
LEVEL 4 — TAG (2% tokens):
  "auth-service: JWT auth with role-based access control"
```

### Strategy 3: Contextual Anchoring

Place the most critical information at natural attention points:

```
STRUCTURE:
  [TASK DEFINITION — highest attention]
  [KEY CONSTRAINTS — high attention]
  [REFERENCE CODE — medium attention, scannable]
  [SUPPORTING CONTEXT — lower attention]
  [OUTPUT INSTRUCTIONS — refreshed attention at end]
```

The model attends more strongly to the beginning and end of context. Place critical constraints in both locations.

### Strategy 4: Deduplication

Aggressively remove redundant information:
- **Type + Implementation**: If you include the implementation, you don't need separate type declarations
- **Tests + Requirements**: Well-written tests ARE requirements; don't duplicate them in prose
- **Comments + Code**: If the code is self-documenting, strip the comments
- **Multiple Examples**: One good example > three mediocre ones

### Strategy 5: Reference Pointers Instead of Content

When full content is too expensive, use pointers:

```
INSTEAD OF: [500-line utility file pasted in full]
USE: "See utils/validation.ts — exports: validateEmail(), validatePhone(),
     validateAddress(). All return Result<T, ValidationError>. Uses zod schemas."
```

## Compression Techniques

### Code Compression

Before (high token cost): Full import/state/useEffect/react hook with all implementation
After (compressed): Just the function signature with a one-line purpose comment and dependency list

### Document Compression

Before: 2000-word API documentation
After: Endpoints summary table + Auth info + Rate limits + Pagination + Special rules

## Context Budget Templates

### Bug Fix (Small Context: ~4K tokens)
INCLUDE: Error/stack trace, failing function, relevant types, reproduction test
EXCLUDE: Unrelated files, full dependency source, historical context

### Feature Implementation (Medium: ~12K tokens)
INCLUDE: Requirements, files to modify, adjacent files (signatures), test files, type definitions, one similar example (compressed)
EXCLUDE: Framework docs, unrelated modules, CI/CD config

### Architecture Review (Large: ~25K tokens)
INCLUDE: Directory tree, config files, key entry points, DB schema, API routes, dependencies, ADRs
EXCLUDE: Individual implementations, test files, static assets

## Anti-Patterns

1. **Kitchen sink**: Dumping entire files "just in case"
2. **Stale context**: Carrying forward outdated information
3. **Duplicate formats**: Same info as code AND docs AND tests
4. **Ignoring output reserve**: Filling entire window leaves no room for reasoning
5. **Over-compression**: Losing critical implementation details
