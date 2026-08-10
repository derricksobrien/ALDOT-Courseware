# Lab 03: GitHub Copilot Refactor and Unit Tests

## Module Alignment
Module 3: GitHub Copilot AI-Assisted C# Development

## Timebox
75 minutes

## Objectives
- Use Copilot to refactor a legacy C# component.
- Generate unit tests with meaningful edge cases.
- Apply governance and secure coding review.

## Prerequisites
- GitHub Copilot enabled in VS Code or Visual Studio.
- Access to `course/repos/eShopOnWeb` or another local C#/.NET codebase with legacy-style classes.

## Instructor Demo: GitHub Copilot Upgrade Agent (5–10 min intro)
Before students start their own refactor, the instructor runs a short live demo of the GitHub Copilot upgrade agent against `eShopOnWeb` — this is the "GitHub Copilot Upgrade Agent / Extension" named in `course/design.md` for Module 1, shown here as the bridge into hands-on Copilot work.

- Install if needed: VS Code Extensions view → search **"GitHub Copilot upgrade"** → Install.
- In Copilot Chat: `@upgrade Upgrade my solution to .NET 9`, choose **Guided** mode.
- Walk through the generated `.github/upgrades/{scenarioId}/assessment.md` and `plan.md` live — a real, automated version of the candidate-finding work from Lab 01.
- Stop after the Planning stage; don't run Execution during the demo.

**Optional for students:** only if a GitHub Copilot for Business seat is confirmed active for them (see the Day-1 checklist in `assess-labs/copilot-for-business-deployment-plan-2026-08-09_1427.md`). Students with an active seat may repeat the same steps themselves, then compare the agent's assessment against their own read of the code before moving into the manual refactor below.

## Step-by-Step
1. Select a legacy class in the reference app with code smells.
2. Prompt Copilot to propose a refactor plan before code changes.
3. Refactor for readability, separation of concerns, and null safety.
4. Prompt Copilot to generate xUnit tests covering happy and unhappy paths.
5. Add XML documentation for public methods.
6. Run `dotnet test --collect:"XPlat Code Coverage" --results-directory ./TestResults` from the solution root and save the generated coverage report.
7. Run static analysis and manually review generated code for security issues.
8. Record prompt patterns that were effective and ineffective.

## Validation Checks
- Refactored class compiles and behavior is preserved.
- Test project passes and a coverage report is generated for the changed code.
- Security review checklist is completed.

## Deliverables
- Refactored code commit.
- Test report and coverage snapshot.
- Prompt engineering notes.

## Stretch Goals
- Add mutation testing for one critical class.
