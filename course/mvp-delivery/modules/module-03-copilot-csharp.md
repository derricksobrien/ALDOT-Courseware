# Module 03 Courseware: Copilot Assisted C# Development

## Tier
Core MVP Module

## Learning Objectives

- Use prompt patterns for targeted refactoring and test generation.
- Review AI-generated code for quality and security.
- Improve maintainability of a legacy C# component.

## Narrative

This module converts theory into productivity by using Copilot against a controlled code surface. The focus is safe acceleration, not blind generation. The lab opens with a short instructor-led demo of the GitHub Copilot upgrade agent — the same assess-and-plan tooling named for Module 1 in `course/design.md` — run live against the reference app before learners start their own manual refactor.

## Supporting Assets

- Code target: `course/repos/eShopOnWeb`
- Optional examples: `course/repos/samples`
- Copilot for Business classroom provisioning plan: `assess-labs/copilot-for-business-deployment-plan-2026-08-09_1427.md`

## Copilot Chat Surfaces in VS Code

Before starting the lab, students should understand which Copilot interface to use and when. VS Code offers two main surfaces and three chat modes — choosing the right one for the task makes a meaningful difference in productivity.

### Two Surfaces

| Surface | How to open | Best for |
|---|---|---|
| **Chat View** (sidebar) | Click the chat icon in the title bar, or `Ctrl+Alt+I` | Code-focused work — you stay in your editor, see files side-by-side, use inline diffs. **Default for this lab.** |
| **Agents Window** | Title bar → "Open in Agents", or `code --agents` from terminal | High-level, multi-project orchestration — describe an outcome and let the agent plan and execute across the whole workspace. Sessions are shared with the Chat View, so you can switch freely. |

> **For Lab 03**, use the **Chat View** (sidebar). It keeps you close to the code during the refactor and makes reviewing diffs easier. Switch to the Agents Window later in the course when working across multiple projects.

### Three Chat Modes

Switch between modes using the dropdown at the **bottom of the Chat View**.

| Mode | What Copilot does | When to use it |
|---|---|---|
| **Ask** | Answers questions, explains code, suggests snippets — no file edits | Understanding legacy code before refactoring; exploring patterns |
| **Plan** | Reads the codebase and produces a detailed step-by-step implementation plan. Makes **no code changes** until you approve and hand off. | Before a large refactor — use Plan to get Copilot's proposed approach, review it, then click **Start Implementation** to hand off to Agent mode |
| **Agent** | Autonomously edits files, runs terminal commands, iterates on errors until done | The refactor itself — once you have a plan you trust, Agent mode executes it |

### Recommended Workflow for Lab 03

```
1. Ask mode   → "Explain what this class does and identify code smells"
2. Plan mode  → "Plan a refactor of [class] to follow single responsibility"
               Review the plan output, adjust scope if needed
3. Agent mode → Click "Start Implementation" (or switch to Agent and describe the task)
               Review diffs in the Changes panel before committing
```

> **New in 2025–2026:** The **Plan mode** is a separate agent from Agent mode — it uses read-only tools only and will not touch your files until you explicitly hand off. This mirrors the real-world practice of getting a migration plan peer-reviewed before executing it — a direct parallel to the modernization planning work in Module 01.

### Inline Chat (Quick Edits)

For targeted, in-place edits without opening the sidebar: select a block of code and press `Ctrl+I` (`Cmd+I` on Mac). A lightweight prompt appears inline. Useful for:
- Renaming a method and updating its callers
- Adding XML doc comments to a single method
- Asking "why does this throw?" on a specific line

## Lab Alignment

- Matching lab: `mvp-delivery/labs/lab-03-copilot-refactor-and-tests.md`
- Lab opens with an instructor demo of the GitHub Copilot upgrade agent (`@upgrade` in Copilot Chat); hands-on for students is optional and gated on an active Copilot for Business seat
- Required output: refactor commit, tests, prompt and review notes

## Success Criteria

- Refactored code compiles, tests pass, and learner can explain the decisions made.

## Further Reading

- [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/get-started/best-practices)
- [GitHub Copilot upgrade overview — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-upgrade/overview)
- [Install GitHub Copilot upgrade — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-upgrade/install)
- [Use chat in VS Code — Chat surfaces, modes, and context (VS Code docs)](https://code.visualstudio.com/docs/chat/chat-overview)
- [Agents window — Multi-project orchestration (VS Code docs)](https://code.visualstudio.com/docs/agents/run/agents-window)
- [Agent mode, Plan mode, Ask mode — GitHub Docs](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide)
