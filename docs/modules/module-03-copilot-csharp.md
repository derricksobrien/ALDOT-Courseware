---
layout: default
title: "Module 03 — Copilot C# Development"
parent: Modules
nav_order: 3
---

# Module 03 Courseware: Copilot Assisted C# Development

## Tier
Core MVP Module

## Learning Objectives

- Use prompt patterns for targeted refactoring and test generation.
- Review AI-generated code for quality and security.
- Improve maintainability of a legacy C# component.

## Narrative

This module converts theory into productivity by using Copilot against a controlled code surface. The focus is safe acceleration, not blind generation. The lab opens with a short instructor-led demo of the GitHub Copilot upgrade agent â€” the same assess-and-plan tooling named for Module 1 in `course/design.md` â€” run live against the reference app before learners start their own manual refactor.

## Supporting Assets

- Code target: `course/repos/eShopOnWeb`
- Optional examples: `course/repos/samples`
- Copilot for Business classroom provisioning plan: `assess-labs/copilot-for-business-deployment-plan-2026-08-09_1427.md`

## Copilot Chat Surfaces in VS Code

Before starting the lab, students should understand which Copilot interface to use and when. VS Code offers two main surfaces and three chat modes â€” choosing the right one for the task makes a meaningful difference in productivity.

### Two Surfaces

| Surface | How to open | Best for |
|---|---|---|
| **Chat View** (sidebar) | Click the chat icon in the title bar, or `Ctrl+Alt+I` | Code-focused work â€” you stay in your editor, see files side-by-side, use inline diffs. **Default for this lab.** |
| **Agents Window** | Title bar â†’ "Open in Agents", or `code --agents` from terminal | High-level, multi-project orchestration â€” describe an outcome and let the agent plan and execute across the whole workspace. Sessions are shared with the Chat View, so you can switch freely. |

> **For Lab 03**, use the **Chat View** (sidebar). It keeps you close to the code during the refactor and makes reviewing diffs easier. Switch to the Agents Window later in the course when working across multiple projects.

### Three Chat Modes

Switch between modes using the dropdown at the **bottom of the Chat View**.

| Mode | What Copilot does | When to use it |
|---|---|---|
| **Ask** | Answers questions, explains code, suggests snippets â€” no file edits | Understanding legacy code before refactoring; exploring patterns |
| **Plan** | Reads the codebase and produces a detailed step-by-step implementation plan. Makes **no code changes** until you approve and hand off. | Before a large refactor â€” use Plan to get Copilot's proposed approach, review it, then click **Start Implementation** to hand off to Agent mode |
| **Agent** | Autonomously edits files, runs terminal commands, iterates on errors until done | The refactor itself â€” once you have a plan you trust, Agent mode executes it |

### Recommended Workflow for Lab 03

```
1. Ask mode   â†’ "Explain what this class does and identify code smells"
2. Plan mode  â†’ "Plan a refactor of [class] to follow single responsibility"
               Review the plan output, adjust scope if needed
3. Agent mode â†’ Click "Start Implementation" (or switch to Agent and describe the task)
               Review diffs in the Changes panel before committing
```

> **New in 2025â€“2026:** The **Plan mode** is a separate agent from Agent mode â€” it uses read-only tools only and will not touch your files until you explicitly hand off. This mirrors the real-world practice of getting a migration plan peer-reviewed before executing it â€” a direct parallel to the modernization planning work in Module 01.

### Inline Chat (Quick Edits)

For targeted, in-place edits without opening the sidebar: select a block of code and press `Ctrl+I` (`Cmd+I` on Mac). A lightweight prompt appears inline. Useful for:
- Renaming a method and updating its callers
- Adding XML doc comments to a single method
- Asking "why does this throw?" on a specific line

## Agents Window â€” Customizations Panel

When you open the Agents Window (`code --agents` or title bar â†’ "Open in Agents"), the **Customizations** panel on the left gives you control over how the agent thinks, what it knows, and what it can do. Understanding these seven items is the difference between using Copilot as a generic chat tool and using it as a configured teammate for your specific project.

### Mental Model

```
Instructions  â†’ always-on background context (passive, no switch required)
Agents        â†’ personas with instructions + scoped tool sets (switchable)
Skills        â†’ callable reusable capabilities (invoked by agents or directly)
Tools         â†’ individual capabilities the agent can use (toggleable per session)
Plugins       â†’ tools contributed by installed VS Code extensions
MCP Servers   â†’ tools that connect to external systems (GitHub, ADO, databases)
Hooks         â†’ automatic triggers on agent lifecycle events
```

---

### ðŸ  Overview

The **Overview** is a dashboard showing all your customizations in one place â€” what's active, what's installed, and quick links to create new ones. Open it first to understand what's available before starting a session.

> **Student tip:** If the agent is not behaving as expected (wrong language, wrong style, missing tools), start here to see if a conflicting instruction or agent is active.

---

### ðŸ¤– Agents

**Agents** are custom personas defined in `.agent.md` Markdown files. Each agent bundles together:
- A system prompt (role description and behavioral rules)
- A specific set of allowed tools (e.g., read-only for a planning agent)
- Optional **handoffs** to other agents at the end of a turn

**File locations:**

| Scope | Location |
|---|---|
| Workspace (shared with team) | `.github/agents/*.agent.md` |
| Personal (all workspaces) | `~/.copilot/agents/*.agent.md` |

**Example agents useful for modernization work:**

| Agent name | What it does |
|---|---|
| `planner` | Read-only tools only â€” researches the codebase and generates an implementation plan without touching files |
| `reviewer` | Reviews diffs for security issues, code smells, and missing tests |
| `migrator` | Full tools â€” executes a migration task autonomously |

To create a custom agent: **Command Palette â†’ "Chat: New Custom Agent"**, or create a `.agent.md` file manually in `.github/agents/`.

> **App modernization connection:** On a real project, you might create a `legacy-auditor` agent that has instructions to look for anti-patterns specific to your organization's legacy stack, and a `cloud-migrator` agent that knows your target Azure architecture. Each specialist agent does one job well, then hands off.

---

### ðŸ’¡ Skills

**Skills** are reusable, callable capabilities defined in `.skill.md` files â€” more targeted than a full agent persona. An agent can invoke skills as part of its tool set.

Skills are invoked either:
- **Automatically** â€” the agent picks the right skill based on the task description
- **Directly** â€” you call it in a prompt: `Use the commit skill to commit my changes`
- **By agents** â€” listed in the agent's `tools` frontmatter

**Examples of built-in skills in this session:** `commit` (stages and commits with a generated message), `sync` (pushes to GitHub).

You can write your own: create `~/.copilot/skills/my-skill.skill.md` with a description and instructions.

> **Student tip:** Skills are great for repetitive tasks you do in every project â€” "run my test suite and summarize failures," "check for hardcoded secrets," "generate a PR description from the diff."

---

### ðŸ“– Instructions

**Instructions** are always-on context files that are injected into *every* chat request automatically. Unlike agents, they don't need to be switched on â€” they are ambient project knowledge.

**Sources (in priority order):**
1. `.github/copilot-instructions.md` â€” workspace-level, shared with the team via Git
2. User-level instructions (VS Code settings â†’ `github.copilot.chat.codeGeneration.instructions`)
3. Prompt files (`.github/prompts/*.prompt.md`) â€” reusable named instructions you invoke on demand

**What to put in instructions:**
```markdown
# .github/copilot-instructions.md (example)
- This project uses .NET 8 with Clean Architecture
- Always write XML doc comments on all public methods and constructors
- Never use `var` â€” always use explicit types
- Target framework: net8.0 â€” do not use any API unavailable in .NET 8
- Test framework: xUnit with FluentAssertions
```

> **App modernization connection:** Instructions files are how you encode your team's migration standards so the agent enforces them automatically. Instead of repeating "target Azure App Service, not VMs" in every prompt, put it in the instructions file once and every session benefits.

---

### âš¡ Hooks

**Hooks** fire automatically at specific points in the agent lifecycle â€” before a commit, after a tool runs, when a session starts, when an error occurs. They inject context or enforce rules without requiring the user to ask.

**Common use cases:**
- Pre-commit hook: "Before committing, check that no hardcoded connection strings are present"
- Session-start hook: "When a session opens, read `CHANGELOG.md` and summarize recent changes for context"
- Post-edit hook: "After any file edit, verify the project still builds"

Hooks are defined in agent/skill files using a `hooks` frontmatter key. This feature is newer and still evolving â€” check the VS Code release notes for the latest supported hook types.

> **Student tip:** Hooks are powerful for enforcing team standards automatically. A `pre-commit` hook that checks for TODO comments or missing tests catches issues before they reach code review.

---

### ðŸ–¥ï¸ MCP Servers

**MCP (Model Context Protocol) Servers** extend the agent with connections to external systems. They turn the agent from a local code editor assistant into something that can read and write data across your entire toolchain.

**Configuration:** `.vscode/mcp.json` in your workspace or VS Code user settings.

**Examples relevant to this course:**

| MCP Server | What it enables |
|---|---|
| `github` | Read PRs, issues, repos; create branches; comment on PRs |
| `azure-devops` | Read/write work items, sprints, queries in ADO |
| `fetch` | Retrieve any web URL as context (docs, APIs, tickets) |
| `filesystem` | Expanded file operations beyond the workspace |
| `database` | Query a SQL Server or PostgreSQL schema for context |

**How to add an MCP server:**
1. Open Agents Window â†’ Customizations â†’ **MCP Servers**
2. Click **Add MCP Server**
3. Provide the server URL or install from the marketplace
4. The server's tools appear in the **Tools** panel automatically

> **App modernization connection:** With an ADO MCP server, the agent can read your sprint backlog, mark tasks done as it completes them, and create new tasks when it discovers scope. With a GitHub MCP server, it can open PRs, respond to review comments, and update issue status â€” all without leaving VS Code.

---

### ðŸ”Œ Plugins

**Plugins** are tools and capabilities contributed by installed VS Code extensions. When an extension registers agent tools, they appear here and can be enabled/disabled per session.

**Examples:**
- Docker extension â†’ `build image`, `run container`, `check container logs` tools
- Azure extension â†’ `list resources`, `deploy to App Service` tools
- Test runner extensions â†’ `run failing tests`, `generate test report` tools

Check this panel if you expect a tool to be available (e.g., "run my tests") but it's not appearing in the agent's tool list â€” the plugin may be disabled.

---

### ðŸ”§ Tools

**Tools** are the individual capabilities the agent can use in the current session. This is the most granular control level â€” you can enable or disable specific operations.

**Built-in tool categories:**

| Category | Tools included |
|---|---|
| **File operations** | Read file, write file, create file, delete file, list directory |
| **Terminal** | Run shell command, read terminal output |
| **Search** | Grep codebase, find files by pattern, semantic search |
| **Browser** | Open URL, read page, take screenshot, click elements |
| **Web** | Fetch URL content |
| **Agent** | Run subagent, invoke skill |

**When to restrict tools:**
- **Read-only review session:** disable write and terminal tools â€” the agent can analyze but not change anything
- **Planning session:** disable all write tools â€” use with Plan mode for zero-risk exploration
- **Locked-down environment:** disable browser/web tools to keep the agent working only on local code

> **Student tip:** If you're nervous about an autonomous agent making unwanted changes, disable the file-write and terminal tools before running it. You can then review what it *would* have done by looking at the plan output, then re-enable tools and run again with confidence.

## Lab Alignment

- Matching lab: `mvp-delivery/labs/lab-03-copilot-refactor-and-tests.md`
- Lab opens with an instructor demo of the GitHub Copilot upgrade agent (`@upgrade` in Copilot Chat); hands-on for students is optional and gated on an active Copilot for Business seat
- Required output: refactor commit, tests, prompt and review notes

## Success Criteria

- Refactored code compiles, tests pass, and learner can explain the decisions made.

## Further Reading

- [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/get-started/best-practices)
- [GitHub Copilot upgrade overview â€” Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-upgrade/overview)
- [Install GitHub Copilot upgrade â€” Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-upgrade/install)
- [Use chat in VS Code â€” Chat surfaces, modes, and context (VS Code docs)](https://code.visualstudio.com/docs/chat/chat-overview)
- [Agents window â€” Multi-project orchestration (VS Code docs)](https://code.visualstudio.com/docs/agents/run/agents-window)
- [Agent mode, Plan mode, Ask mode â€” GitHub Docs](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide)
- [Custom agents in VS Code (.agent.md files)](https://code.visualstudio.com/docs/agent-customization/custom-agents)
- [Agent skills in VS Code (.skill.md files)](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Custom instructions for Copilot (copilot-instructions.md)](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- [MCP Servers in VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

