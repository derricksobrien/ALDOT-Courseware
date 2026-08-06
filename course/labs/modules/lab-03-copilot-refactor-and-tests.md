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

## Step-by-Step
1. Select a legacy class in the reference app with code smells.
2. Prompt Copilot to propose a refactor plan before code changes.
3. Refactor for readability, separation of concerns, and null safety.
4. Prompt Copilot to generate xUnit tests covering happy and unhappy paths.
5. Add XML documentation for public methods.
6. Run static analysis and manually review generated code for security issues.
7. Record prompt patterns that were effective and ineffective.

## Validation Checks
- Refactored class compiles and behavior is preserved.
- Test project passes with at least 80 percent line coverage for changed code.
- Security review checklist is completed.

## Deliverables
- Refactored code commit.
- Test report and coverage snapshot.
- Prompt engineering notes.

## Stretch Goals
- Add mutation testing for one critical class.
