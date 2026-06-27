---
name: "playwright"
description: "Complete browser automation with Playwright. Auto-detects dev servers, writes test scripts, takes screenshots, validates UX. Invoke when user wants to test websites, automate browser interactions, or validate web functionality."
---

# Playwright Browser Automation

General-purpose browser automation skill. Writes custom Playwright code for any automation task and executes it via the universal executor.

**CRITICAL WORKFLOW - Follow these steps in order:**

1. **Auto-detect dev servers** - For localhost testing, ALWAYS run server detection FIRST:

```bash
cd $SKILL_DIR && node -e "require('./lib/helpers').detectDevServers().then(servers => console.log(JSON.stringify(servers)))"
```

- If **1 server found**: Use it automatically, inform user
- If **multiple servers found**: Ask user which one to test
- If **no servers found**: Ask for URL or offer to help start dev server

2. **Write scripts to /tmp** - NEVER write test files to skill directory; always use `/tmp/playwright-test-*.js`

3. **Use visible browser by default** - Always use `headless: false` unless user specifically requests headless mode

4. **Parameterize URLs** - Always make URLs configurable via environment variable or constant at top of script

## How It Works

1. Describe what you want to test/automate
2. Auto-detect running dev servers (or ask for URL if testing external site)
3. Write custom Playwright code in `/tmp/playwright-test-*.js` (won't clutter your project)
4. Execute via: `cd $SKILL_DIR && node run.js /tmp/playwright-test-*.js`
5. Results displayed in real-time, browser window visible for debugging
6. Test files auto-cleaned from /tmp by your OS

## Setup (First Time)

```bash
cd $SKILL_DIR
npm run setup
```

This installs Playwright and Chromium browser. Only needed once.

## Execution Pattern

**Step 1: Detect dev servers (for localhost testing)**

```bash
cd $SKILL_DIR && node -e "require('./lib/helpers').detectDevServers().then(s => console.log(JSON.stringify(s)))"
```

**Step 2: Write test script to /tmp with URL parameter**

```javascript
// /tmp/playwright-test-page.js
const { chromium } = require('playwright');

// Parameterized URL (detected or user-provided)
const TARGET_URL = 'http://localhost:3001'; // <-- Auto-detected or from user

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto(TARGET_URL);
  console.log('Page loaded:', await page.title());

  await page.screenshot({ path: '/tmp/screenshot.png', fullPage: true });

  await browser.close();
})();
```

**Step 3: Execute**

```bash
cd $SKILL_DIR && node run.js /tmp/playwright-test-page.js
```

## Common Patterns

### Test a Page (Basic Health Check)

```javascript
const { chromium } = require('playwright');
const TARGET_URL = 'http://localhost:3000';

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto(TARGET_URL);
  console.log('Title:', await page.title());
  console.log('URL:', page.url());

  await page.screenshot({ path: '/tmp/page.png', fullPage: true });
  await browser.close();
})();
```

### Test Responsive Design

```javascript
const { chromium } = require('playwright');
const TARGET_URL = 'http://localhost:3000';

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  const viewports = [
    { name: 'Desktop', width: 1920, height: 1080 },
    { name: 'Tablet', width: 768, height: 1024 },
    { name: 'Mobile', width: 375, height: 667 }
  ];

  for (const viewport of viewports) {
    await page.setViewportSize({ width: viewport.width, height: viewport.height });
    await page.goto(TARGET_URL);
    await page.screenshot({ path: `/tmp/${viewport.name.toLowerCase()}.png`, fullPage: true });
    console.log(`${viewport.name} screenshot saved`);
  }

  await browser.close();
})();
```

### Test Login Flow

```javascript
const { chromium } = require('playwright');
const TARGET_URL = 'http://localhost:3000';

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto(`${TARGET_URL}/login`);
  await page.fill('input[name="email"]', 'user@example.com');
  await page.fill('input[name="password"]', 'password123');
  await page.click('button[type="submit"]');

  await page.waitForURL('**/dashboard');
  console.log('Login successful, redirected to dashboard');

  await browser.close();
})();
```

### Check for Broken Links

```javascript
const { chromium } = require('playwright');
const TARGET_URL = 'http://localhost:3000';

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto(TARGET_URL);

  const links = await page.$$eval('a[href]', as => as.map(a => a.href));
  console.log(`Found ${links.length} links`);

  const results = await Promise.all(links.map(async (link) => {
    try {
      const response = await page.request.get(link);
      return { url: link, status: response.status() };
    } catch (e) {
      return { url: link, status: 'error' };
    }
  }));

  const broken = results.filter(r => r.status >= 400 || r.status === 'error');
  console.log(`Broken links: ${broken.length}`);
  broken.forEach(b => console.log(`  ${b.status}: ${b.url}`));

  await browser.close();
})();
```

## Common Use Cases

- **Automated Functional Testing**: Login flows, multi-step forms, critical user paths
- **Responsive Design & UI Validation**: Screenshots across viewports (Mobile, Tablet, Desktop)
- **Site Health & Link Auditing**: Scan for broken links, verify HTTP status codes
- **Local Development Integration**: Test localhost apps by auto-detecting running dev servers
- **Form Validation**: Fill out and submit forms, check error states
- **Visual Regression**: Capture screenshots before/after changes
- **Data Scraping**: Extract content from web pages

## Path Resolution

This skill can be installed in different locations. Before executing any commands, determine the skill directory based on where you loaded this SKILL.md file, and use that path in all commands. Replace `$SKILL_DIR` with the actual discovered path.

Common installation paths:

- Plugin system: `~/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill`
- Manual global: `~/.claude/skills/playwright-skill`
- Project-specific: `<project>/.claude/skills/playwright-skill`

## Safety Notes

- NEVER write test files to skill directory; always use `/tmp/playwright-test-*.js`
- ALWAYS use `headless: false` (visible browser) by default
- Always clean up browser instances with `await browser.close()`
- Use `try/catch/finally` patterns to ensure screenshots are taken on errors
