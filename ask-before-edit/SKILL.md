---
name: "ask-before-edit"
description: "Before modifying any code or files, explains the planned changes and asks for user confirmation. Invoke automatically before making edits, creating files, or refactoring code."
---

# Ask Before Edit

This skill ensures users have full control over code modifications by requiring confirmation before any changes are made.

## When to Use This Skill

**CRITICAL: This skill must be invoked BEFORE making ANY of the following:**
- Editing existing files
- Creating new files
- Deleting files
- Refactoring code
- Modifying configurations
- Running commands that modify the codebase

## Core Principle

**"Think First, Then Ask"** - Always explain before you act.

## Required Steps

### 1. Analyze the Request
Understand what the user wants to accomplish:
- Read the relevant files
- Understand the current code structure
- Identify what changes are needed

### 2. Formulate a Plan
Before making any changes, clearly state:
- **What will be changed**: Which files, functions, or components
- **How it will be changed**: The specific modification approach
- **Why this change is needed**: Brief rationale based on user request

### 3. Ask for Confirmation
Present the plan and ask explicitly:
```
I plan to make the following changes:
1. Edit [filename] - [specific change]
2. Edit [filename] - [specific change]

Do you confirm these changes?
```

### 4. Wait for Response
Do NOT proceed until user explicitly confirms.

### 5. Execute Only After Confirmation
After user confirms:
- Make the changes as described
- Report what was done
- If unexpected issues arise, stop and inform the user

## Example Scenarios

### Scenario 1: User asks to fix a bug

**Wrong approach (without this skill):**
```javascript
// Immediately starts editing without asking
function calculateTotal(items) {
  let total = 0;
  for (let i = 0; i < items.length; i++) {
    total += items[i].price;
  }
  return total;
}
```

**Correct approach (with this skill):**
```
I plan to make the following changes:

1. Modify `calculateTotal` function (file.js:1-7)
   - Current issue: Does not handle null/undefined items in array
   - Fix: Add null check

2. Add parameter validation (file.js:1-3)
   - Add if (!items) return 0; defensive check

Do you confirm these changes?
```

### Scenario 2: User asks to add a feature

**Correct approach:**
```
I plan to make the following changes:

1. Create new file `utils/helpers.js`
   - Purpose: Store utility functions

2. Modify `app.js`
   - Add import statement at top
   - Call new function at appropriate location

3. Modify `package.json`
   - Add new dependencies if needed

Do you confirm?
```

## Output Format for Plan

When presenting a plan, use this structure:

```
## 📋 Modification Plan

### Goal
[Brief description of what the user wants to achieve]

### Files to be modified
| File | Action | Description |
|------|--------|-------------|
| path/to/file | Edit/Create/Delete | Reason |

### Specific Changes
1. [file:line] - [description]
2. [file:line] - [description]

### Risk Notes (if any)
⚠️ [Any potential risks to be aware of]

---
Please confirm whether to proceed with these changes?
```

## Important Reminders

- **NEVER skip the confirmation step**
- **Be specific** about line numbers and what will change
- **Keep plans concise** but complete
- **If user provides feedback**, adjust the plan accordingly and re-ask
- **After confirmation**, execute exactly as described
