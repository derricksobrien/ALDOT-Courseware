---
layout: default
title: "Instructor Note: Day 2 Tool Transitions"
parent: AI in Software Testing
nav_order: 12
---

# Instructor Note: Day 2 Tool Transitions

## Purpose

The Day 2 labs introduce several tools in the middle of a testing exercise. A learner who is new to software testing, Python, APIs, or GitHub may understand the testing goal but still lose time asking what the command or tool is supposed to do.

The Day 2 walkthroughs now include a short **What is it?** section before the first setup command in each lab. These sections are orientation, not a replacement for the full tool documentation.

Use them to give students a one-minute mental model before they type the command.

## Instructor Pattern

Before each new tool, ask students to answer three questions:

1. What job does this tool do?
2. What input does it receive?
3. What evidence should it produce?

Then run the smallest example before moving into the lab scenario.

For example:

```text
Uvicorn runs the FastAPI application.
It receives the app import path.
Evidence: the terminal says the server is listening on port 8000.
```

This keeps the class focused on testing rather than making students infer the purpose of unfamiliar infrastructure commands.

## Lab 2.1: Exploratory API Testing

### New tools introduced

- Flask: Python web framework that exposes a route such as `POST /register`.
- pytest: test runner that reports pass/fail results.
- Flask test client: in-memory client that sends requests without deploying a server.

### Simple example

```python
@app.get("/hello")
def hello():
    return {"message": "hello"}
```

```python
def test_hello(client):
    response = client.get("/hello")
    assert response.status_code == 200
```

### Instructor prompt

> “The test client is our controlled caller. We are not testing a browser today. We are sending an input to an endpoint and observing the response status and JSON body.”

### Student trip hazard

Students may treat a passing exploratory test as proof that the input is good. Clarify that these tests often record what the starter API actually does, including behavior that should later be classified as a defect.

## Lab 2.2: Synthetic Test Data

### New tools introduced

- SQLite: file-based database stored in `ecommerce.db`.
- SQL: language for creating tables, inserting rows, and querying data.
- FastAPI: Python framework for creating API endpoints and generated API docs.
- Uvicorn: development server that runs the FastAPI application.
- Faker: library for generating realistic-looking synthetic values.
- curl: command-line HTTP client for calling an API.

### Simple example

Create and query one SQLite row:

```sql
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
INSERT INTO products VALUES (1, 'Keyboard');
```

Run the API:

```bash
uvicorn app:app --reload
```

Call it:

```bash
curl http://localhost:8000/products
```

Explain `app:app` as “load the `app` object from `app.py`.” Explain `--reload` as a development convenience that restarts the process after a saved code change.

### Instructor prompt

> “SQLite is the storage file, FastAPI defines the web endpoint, Uvicorn runs the endpoint, and curl is one client that calls it. Faker creates test data; it does not make the data trustworthy until our validation queries pass.”

### Student trip hazards

- `sudo dnf install -y sqlite` assumes Linux/Amazon Linux and is not a Windows command.
- Windows may not have the `sqlite3` command-line tool.
- A successful `POST /orders` does not automatically prove that the customer ID exists.
- Foreign-key declarations need enforcement enabled on each SQLite connection.

Use a Python or C# database library as the fallback instead of turning the class into a SQLite installation exercise.

## Lab 2.3: CI/CD Quality Gates

### New tools introduced

- YAML: indentation-sensitive configuration format.
- GitHub Actions: hosted automation that runs jobs after pushes and pull requests.
- flake8: Python lint tool for style and simple code-quality findings.
- Coverage: measurement of executed lines or branches.
- Quality gate: a pass/fail rule that blocks the workflow when a requirement is not met.

### Simple example

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python -m pytest
```

Explain that the workflow checks out the repository onto a fresh Linux machine. Local pytest proves the current machine can run the tests; Actions proves the repository is repeatable elsewhere.

### Instructor prompt

> “A green local run is evidence about this computer. A green Actions run is evidence that the repository contains enough setup for another machine to reproduce the result.”

### Student trip hazards

- `on:` is YAML configuration, not a shell command.
- The workflow requires a GitHub repository with Actions enabled and appropriate permissions.
- The documented one-blank-line lint fix still produces `E305`; the real fix uses two blank lines.
- The branch-coverage round may remain green if the starter tests already exceed its threshold.

Have students record the actual baseline before choosing a threshold for a deliberate failure.

## Lab 2.4: TDD With a Copilot Agent

### New tools introduced

- TDD: write a failing test, implement behavior, then refactor while keeping tests green.
- Git branch: isolated line of work that protects `main`.
- Pull request: review and merge workflow for a branch.
- CI: automated build and test execution triggered by repository activity.
- Copilot coding agent: AI service that can inspect a repository, edit files, and propose commits. This is different from inline Copilot Chat suggestions.

### Simple example

```text
write a failing test -> implement the behavior -> run the test -> refactor safely
```

```bash
git switch -c feature/transfer-funds
git add bank.py test_bank.py
git commit -m "add transfer tests"
git push -u origin feature/transfer-funds
```

### Instructor prompt

> “The tests are the specification. The agent may write the implementation, but the student owns the acceptance criteria, the review, and the merge decision.”

### Student trip hazards

- An empty test file can cause pytest exit code 5 and a red setup workflow.
- A Copilot-agent commit may require manual “Approve and run” before CI executes.
- Missing `.gitignore` files can allow `__pycache__` artifacts into the pull request.
- Passing tests do not prove malformed accounts and rounding boundaries are handled.

Add `.gitignore` before the first commit and require a full diff review before merge.

## Machine Fallbacks

On the current Windows lab machine:

- Python-based Day 2 examples can run in the configured virtual environment.
- `mutmut` requires WSL/Linux and should be treated as a Lab 1.3 extension.
- Java 21 and Maven 3.9 are available for Lab 1.2.
- .NET SDK and Visual Studio are not currently installed, so a C# delivery needs a separate machine image or preflight step.
- Docker, Azure CLI, GitHub CLI, and the SQLite CLI are not installed; do not make them silent prerequisites.

Put this instruction before the first command in a live class:

> “Run the preflight check first. If a required tool is missing, use the documented fallback path. Do not spend the lab troubleshooting a platform issue that is outside today’s testing objective.”

## Reference Walkthroughs

- [Lab 2.1 walkthrough](lab2.1-walkthrough.html)
- [Lab 2.2 walkthrough](lab2.2-walkthrough.html)
- [Lab 2.3 walkthrough](lab2.3-walkthrough.html)
- [Lab 2.4 walkthrough](lab2.4-walkthrough.html)
- [Original labs vs. walkthroughs and C# migration plan](original-vs-walkthrough-csharp-migration.html)
