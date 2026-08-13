---
layout: default
title: "GitHub and GitHub Actions Primer"
parent: AI in Software Testing
nav_order: 9
---

# GitHub and GitHub Actions Primer

This primer covers only the GitHub concepts needed for Lab 2.3. You do not need to become a Git expert before starting. The goal is to understand where your files live, how changes move to GitHub, and how GitHub runs the workflow you create.

## The Big Picture

```text
your computer -> commit -> push -> GitHub repository -> Actions workflow -> test result
```

You write and test files on your computer. Git records a named snapshot of those files. When you push the snapshot, GitHub receives it. GitHub Actions then reads the workflow file in the repository and runs the commands on a separate hosted machine.

## What Is GitHub?

**GitHub** is a website that stores Git repositories and adds collaboration features around them. A repository is a project folder with:

- the source code and tests;
- the history of changes;
- branches for separate lines of work;
- pull requests for review;
- Actions workflows for automation.

A repository is not the same thing as your local folder. Your local folder is your copy. GitHub holds the shared remote copy.

## What Is Git?

**Git** is the version-control tool that records changes to files. The most useful beginner commands are:

```bash
git status
git add .
git commit -m "describe the change"
git push
```

Read them as:

1. `git status` — show what changed.
2. `git add .` — prepare the changed files for the next snapshot.
3. `git commit` — create a named snapshot on your computer.
4. `git push` — send your local commits to GitHub.

A commit is not yet on GitHub. The push is what sends it to the remote repository.

## Repository, Remote, and Clone

A **remote** is a saved name for another copy of the repository, usually GitHub. The standard remote name is `origin`.

```bash
git remote -v
```

A **clone** creates a local copy of a GitHub repository:

```bash
git clone https://github.com/your-name/discount-ci-lab.git
cd discount-ci-lab
```

In Lab 2.3, students should work in their own fork or disposable repository. Do not push classroom exercises to the read-only courseware repository.

## What Is a Branch?

A **branch** is a separate line of project history. `main` is normally the stable branch. A branch lets you try a change without changing `main` immediately.

```bash
git switch -c experiment/ci-workflow
git branch --show-current
```

The second command should print `experiment/ci-workflow`.

Lab 2.3 can be completed directly on `main` in a disposable student repository, but branches are safer when you are practicing pull requests.

## What Is a Pull Request?

A **pull request**, often called a PR, asks GitHub to merge changes from one branch into another. A PR provides:

- a review conversation;
- a view of the file differences;
- status checks from GitHub Actions;
- a place to decide whether the change is ready to merge.

A green check means the configured checks passed. It does not mean a human reviewed the design or that the tests are complete.

## What Is GitHub Actions?

**GitHub Actions** is GitHub's automation service. A workflow is a YAML file stored at:

```text
.github/workflows/ci.yml
```

A minimal workflow looks like this:

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

The parts mean:

- `name` — the label shown in the Actions tab;
- `on` — the events that start the workflow;
- `jobs` — the groups of work to run;
- `runs-on` — the type of hosted machine;
- `steps` — the individual commands or reusable actions;
- `actions/checkout` — a reusable step that downloads your repository onto the hosted machine;
- `run` — a shell command executed on that machine.

## Workflow, Run, Job, and Step

These words describe different levels:

```text
workflow
  -> run
       -> job
            -> step
```

- A **workflow** is the YAML recipe.
- A **run** is one execution of that recipe, created by a push, pull request, or manual trigger.
- A **job** is a group of steps on one runner machine.
- A **step** is one action or shell command inside the job.

When a check fails, open the run, open the failed job, and expand the failed step. Read the first error before changing files.

## What Happens After a Push?

When you run:

```bash
git add .
git commit -m "add CI workflow"
git push origin main
```

GitHub receives the commit and looks for workflow files under `.github/workflows/`. If the workflow trigger includes `push`, GitHub creates a run. The run checks out the commit and executes the steps in order.

The local computer and the Actions runner are separate machines. A package installed locally is not automatically installed on the runner. That is why the workflow must install its own dependencies.

## Common Status Messages

### Queued

GitHub has accepted the run, but a runner is not available yet. Wait or open the run details.

### In progress

The workflow is currently executing. Expand the job to watch the steps.

### Success

All required steps completed with exit code 0.

### Failure

At least one step returned a non-zero exit code. Open that step's log and read the exact command and error.

### Action required

GitHub is waiting for a person to approve a workflow run. This can happen with workflows associated with pull requests or commits created by an automated agent. Look for **Approve and run workflow** in the Actions interface.

### No workflow run appears

Check these in order:

1. Did `git push` finish successfully?
2. Did you push to the branch named in the workflow trigger?
3. Is the file exactly `.github/workflows/ci.yml`?
4. Is GitHub Actions enabled for the repository?
5. Does the workflow YAML parse correctly?
6. Are you looking at the correct repository and branch?

## What Students Should Verify

Before calling the pipeline green, students should be able to show:

- the repository URL;
- the commit that contains the workflow;
- the workflow name in the Actions tab;
- the run status;
- each job and step result;
- the exact test and coverage output;
- the pull request checks, if using a branch workflow.

A green badge without readable evidence is not enough for this lab.

## Machine and Permission Limits

GitHub Actions requires internet access and a GitHub repository with Actions enabled. Students may also need permission to push, create branches, open pull requests, or approve workflow runs.

The local Windows lab machine can run the Python tests, but local success does not prove that GitHub Actions is configured. Use a disposable repository or a personal fork, and never put passwords, access keys, or other secrets in source files or workflow YAML.

## Before Lab 2.3

Run:

```bash
git --version
python --version
git remote -v
```

Then confirm that you can open your own GitHub repository in a browser. If `git` or Python is missing, stop at the preflight and use the instructor's fallback path instead of troubleshooting during the CI exercise.
