---
layout: default
title: "Original Labs vs. Walkthroughs and C# Migration Plan"
parent: AI in Software Testing
nav_order: 11
---

# Original Labs vs. Walkthroughs

This report compares the original labs in `sample_coursware/AI-In-Software-Testing-main/` with the verified walkthroughs in `sample_coursware/lab-walkthroughs/`. It also describes how to deliver the sequence with C#, .NET, and Visual Studio.

## Executive Summary

The walkthroughs are more reliable than the original lab documents because they record actual tool output and platform limitations. The original labs are educationally coherent, but several steps assume Linux/AWS, provisioned GitHub services, or tools that are not present on every Windows machine.

The biggest student risks are:

- mutation testing with `mutmut` does not run natively on Windows;
- the Java/Maven lab needs a precise project layout and working dependency download;
- Linux `dnf` and the SQLite CLI are not Windows prerequisites;
- GitHub Actions and Copilot Agent steps require repository permissions and browser approval;
- the original CI walkthrough contains two outcomes that do not reproduce exactly as written;
- local machine limitations can consume the lab time before the testing lesson begins.

## Machine Verification

The Windows lab machine used for this review reports:

| Tool | Status | Student impact |
|---|---|---|
| Java 21 | Installed | Lab 1.2 can run locally |
| Maven 3.9 | Installed | Lab 1.2 can run locally |
| .NET SDK | Missing | C# labs cannot run until provisioned |
| Visual Studio/MSBuild | Missing | Visual Studio workflow cannot run until provisioned |
| Docker | Missing | Container exercises cannot run |
| SQLite CLI | Missing | Use a language library or install the CLI |
| Azure CLI | Missing | Azure deployment steps cannot run |
| GitHub CLI | Missing | Use the browser or install `gh` |
| WSL | Command available; distribution not confirmed | Required for native Windows `mutmut` |

No AWS credentials were used for this review. Any credentials previously pasted into chat or lab notes should be revoked and rotated.

## Lab-by-Lab Findings

### Lab 1.1: Manual Testing Versus AI-Assisted Testing

**Original lab:** a sound experiment comparing manual tests, zero-shot AI tests, and improved-prompt AI tests.

**Walkthrough evidence:** five manual tests, eight typical zero-shot AI tests, and sixteen improved-prompt tests. The improved prompt exposes cases that a green test run alone does not prove:

- `SAVE20` must not apply to standard or guest customers;
- unknown customer types behave as guests;
- unknown coupons are ignored;
- discounts are sequential;
- rounding, zero, negative, and case-insensitive inputs matter.

**Gap that may trip students:** the original emphasizes passing tests more than test completeness. Students may report a green suite without recording what it cannot detect.

**Mitigation:** require a coverage matrix before the AI discussion and ask students to identify at least one business rule that remains untested.

### Lab 1.2: Reverse Engineering Legacy Code

**Original lab:** Java 11+, JUnit 5, Maven, and an intentionally opaque shipping calculator.

**Walkthrough evidence:** the hidden case-sensitivity defect is reproduced exactly:

- `"CA"` returns `$9.99`;
- `"ca"` returns `$16.74`;
- the same shipment is silently overcharged because Java string comparisons are case-sensitive.

**Machine gap:** this machine now has Java 21 and Maven 3.9, but students still need the exact Maven layout and internet access for JUnit dependencies. If source files are misplaced, Maven can report a misleading successful build with zero tests.

**Mitigation:** add a preflight that confirms Java, Maven, and test discovery. Require visible test counts, not only a successful Maven exit code.

### Lab 1.3: Coverage and Mutation Testing

**Original lab:** reports an example of 13 statements and 69% coverage.

**Walkthrough evidence:** the exact starter code produced:

```text
15 statements, 73% line coverage
67% branch coverage
missing lines 20, 30, 32, 35
```

The four conceptual gaps are correct: negative-price handling, `SAVE10`, premium `SAVE20`, and holiday discounting. The printed numbers are stale.

The completed local suite produced:

```text
26 passed
100% line coverage
100% branch coverage
```

**Machine gap:** `mutmut run` refuses to run on native Windows and requires WSL/Linux.

**Mitigation:** make coverage the required Windows path and mutation testing a WSL/Linux extension. Add a boundary test for `price == 0` and explicitly explain that coverage does not measure assertion strength.

### Lab 2.1: Exploratory and Edge-Case Testing

**Original lab:** Flask registration endpoint tested with AI-generated boundaries, invalid inputs, long strings, and security-shaped payloads.

**Walkthrough evidence:** the documented weaknesses reproduce:

- whitespace-only names return `201`;
- ages `999` and `9999` return `201`;
- `age=true` returns `400` for the wrong reason because `bool` is an `int` subclass in Python;
- `alice@` is accepted;
- a 10,000-character name is accepted.

An additional gap was found: `name` accepts an integer and a JSON array because the starter code does not validate its type.

**Mitigation:** add explicit type checks, whitespace rejection, length limits, email validation, and tests for the intended `400` behavior.

### Lab 2.2: AI-Generated Test Data

**Original lab:** FastAPI, SQLite, Faker, AI-generated seed data, quality queries, and a 1,000/50/10,000 record scale-up.

**Walkthrough evidence:** the local path generated 1,000 customers, 50 products, and 10,000 orders. Duplicate, null, orphan, product-listing, missing-customer, and valid-order checks passed.

**Machine gaps:** `sudo dnf` is Linux/Amazon-Linux-specific, and Windows does not include the SQLite CLI by default. The endpoint also needs stronger customer existence validation and SQLite foreign-key enforcement on every connection.

**Mitigation:** use Python or .NET database libraries, pin compatible FastAPI/Starlette/httpx versions, enable foreign keys on every connection, and validate both customer and product IDs before inserting orders.

### Lab 2.3: CI/CD With GitHub Actions

**Original lab:** lint, test, coverage, and four deliberate break/fix rounds.

**Walkthrough evidence:**

- the first documented lint fix still fails because `E305` requires two blank lines;
- the actual two-blank-line fix passes;
- the branch-coverage round may stay green because the starter tests already exceed the threshold;
- the Round 3 wording refers to a guest test that is not clearly present in the five-test starter file.

**Machine/service gap:** local pytest success does not validate GitHub Actions. A GitHub repository, Actions permissions, network access, and a usable branch are required.

**Mitigation:** run lint locally before pushing, record the actual baseline before choosing a threshold, use a fork or disposable repository, and separate required CI checks from optional deployment steps.

### Lab 2.4: TDD With a Copilot Agent

**Original lab:** students write failing tests, push them as a specification, ask the Copilot Agent to implement the function, and review the pull request.

**Walkthrough evidence:** the seven acceptance tests fail against the stub, the agent implementation passes them, and human review catches operational details.

**Gaps that may trip students:**

- the empty-test setup check produces CI exit code 5, which looks like a broken workflow;
- agent-triggered workflow runs may require manual “Approve and run” interaction;
- agent commits can include `__pycache__` files when no `.gitignore` exists;
- the initial tests do not cover malformed accounts, missing keys, or all numeric edge cases.

**Mitigation:** add `.gitignore` before the first commit, explain the expected empty-test red state, protect the test file from agent edits, review the entire diff, and add malformed-input and rounding tests.

## C#/.NET and Visual Studio Re-run

The testing lessons transfer cleanly to C#, but the current machine needs the following before a C# delivery:

- .NET 8 or later SDK;
- Visual Studio 2022 with .NET desktop and ASP.NET workloads, or VS Code with the C# Dev Kit;
- Git and GitHub Copilot;
- Docker only for container extensions;
- Azure CLI only for Azure extensions;
- WSL 2 or Linux only if a selected mutation tool requires it.

Use a shared solution:

```text
AiTestingWithDotNet.sln
src/
  DiscountLab/
  ShippingLab/
  RegistrationApi/
  EcommerceApi/
  BankTransfer/
tests/
  DiscountLab.Tests/
  ShippingLab.Tests/
  RegistrationApi.Tests/
  EcommerceApi.Tests/
  BankTransfer.Tests/
```

Use xUnit or MSTest, `Microsoft.NET.Test.Sdk`, `coverlet.collector`, nullable reference types, and a root `.gitignore`:

```text
bin/
obj/
.vs/
TestResults/
coverage/
*.db
```

### C# Lab 1.1

Create a `DiscountCalculator` class library and compare:

- human-written xUnit or MSTest tests;
- zero-shot Copilot tests;
- improved-prompt Copilot tests.

Use `decimal` rather than `double` for prices. Keep the same discount rules and require a coverage matrix so the lesson remains about test design, not syntax.

### C# Lab 1.2

Create a legacy `ShippingCalculator` class with abbreviated variables and hard-coded zones. Students should:

1. read it without AI;
2. ask Copilot to explain it;
3. ask Copilot to find defects;
4. write tests;
5. reproduce the lowercase destination overcharge;
6. fix it with `Trim().ToUpperInvariant()`.

Visual Studio adds useful evidence through Test Explorer, breakpoints, Locals, Call Stack, CodeLens, and Git diff review.

### C# Lab 1.3

Use built-in .NET coverage:

```powershell
dotnet test --collect:"XPlat Code Coverage"
```

Generate an HTML report with ReportGenerator:

```powershell
dotnet tool install -g dotnet-reportgenerator-globaltool
reportgenerator -reports:**/coverage.cobertura.xml -targetdir:coverage-report -reporttypes:Html
```

Use Stryker.NET, pinned and tested before class, for mutation testing:

```powershell
dotnet tool install -g dotnet-stryker
dotnet stryker
```

If Stryker.NET cannot be provisioned, use a controlled manual mutation exercise as the fallback rather than pretending coverage is mutation testing.

### C# Lab 2.1

Replace Flask with an ASP.NET Core Minimal API and test it with `WebApplicationFactory<TEntryPoint>`, `HttpClient`, xUnit theories, and `System.Net.Http.Json`. Preserve the same exploratory payloads, including whitespace, boolean age, long strings, arrays, Unicode, SQL-shaped text, and XSS-shaped text.

Visual Studio `.http` files provide a beginner-friendly way to send the same requests manually.

### C# Lab 2.2

Replace Faker with Bogus and use `Microsoft.Data.Sqlite`, EF Core, or Dapper. Generate the same customer/product/order volumes and validate:

- unique emails;
- null required fields;
- valid foreign keys;
- record counts;
- country and category distributions;
- realistic price ranges;
- server-computed order totals.

Do not require the SQLite CLI; run setup and validation from C# tests or a seed console project.

### C# Lab 2.3

Use GitHub Actions with `actions/setup-dotnet`, `dotnet restore`, `dotnet build`, `dotnet test`, `dotnet format --verify-no-changes`, and coverage collection. Recreate the four break/fix rounds with formatting, failing assertions, coverage drop, and branch coverage.

### C# Lab 2.4

Use `Account`, `TransferService`, and `TransferResult` classes. Keep the same acceptance criteria and red-green-refactor sequence. Require tests for:

- non-positive amounts;
- boolean-like or invalid numeric input where applicable;
- insufficient funds;
- same account;
- balance mutation;
- transaction details;
- rounding boundaries;
- malformed account objects.

Have Copilot modify only the implementation project. Review the pull request and run Test Explorer locally before merging.

## Recommended Preflight

Before class, run a machine check and stop at the first hard blocker:

```powershell
dotnet --info
java -version
mvn -version
git --version
docker run hello-world
az account show
gh auth status
wsl -l -v
```

Classify each lab dependency as:

- **Required:** missing means use the documented fallback;
- **Optional:** useful extension, not part of the core lesson;
- **External:** GitHub, Azure, ADO, Docker, or Copilot service access.

The safest classroom core is:

```text
Visual Studio + .NET + xUnit/MSTest + ASP.NET Core TestServer
SQLite through a language library
GitHub Actions
Stryker.NET or a manual mutation exercise
```

Make Docker, Azure, OpenShift, Tosca, and live deployment separate extensions until a real student machine passes the corresponding preflight checks.
