---
layout: default
title: "Lab 10 Capstone Competition Kit"
parent: Resources
nav_order: 7
---

# Lab 10 Capstone Competition Kit

Use this kit to run Lab 10 as a transparent Red Team vs Blue Team modernization challenge.

---

## Launch the scoreboard

Open the front end here:

- [lab-10-capstone-scoreboard.html](lab-10-capstone-scoreboard.html)

This is the live GitHub Pages scoring UI instructors can use during the showdown.

---

## What this kit does

It gives you:

- one shared legacy starter app baseline
- one simple sample data file for both teams
- one published scoring rubric
- one scorecard manifest format each team must include in its repo
- one graphical scoreboard that reads public GitHub repos and calculates points

This keeps the competition fair because both teams start from the same place and the scoring rules are visible before the challenge begins.

---

## Shared starter for both teams

Use the same starter repository for both teams:

- Course baseline: `course/repos/eShopOnWeb`
- Public reference baseline: `https://github.com/dotnet-architecture/eShopOnWeb`

Recommended instructor setup:

1. Create one starter repo in your GitHub org from the same baseline.
2. Give Team Red and Team Blue their own fork or copy from that same starter.
3. Tell both teams they must keep all capstone artifacts under a predictable `capstone/` folder so the scorer can find them.

---

## Shared sample data

Use the same sample data file for both teams:

- [lab-10-capstone-sample-data.json](lab-10-capstone-sample-data.json)

Recommended usage:

- import it as seed data
- expose it through one new or modernized endpoint
- use it to drive dashboard, reporting, or AI chat features

The sample data is intentionally small so teams spend their time on modernization work, not data cleanup.

---

## Submission contract

Each team must add this file to its repo:

```text
capstone/scorecard.json
```

Start from:

- [lab-10-capstone-scorecard-template.json](lab-10-capstone-scorecard-template.json)

The scoreboard reads that manifest and validates the files the team claims as evidence.

---

## Expected repo structure

Teams do not need to match this exactly, but using this structure makes scoring easier and more consistent:

```text
capstone/
  scorecard.json
  mission.md
  architecture.md
  runbook.md
  retrospective.md
  ai-notes.md
data/
  lab10-sample-data.json
ops/
  observability.md
  alerts.md
infra/
  main.bicep
.github/
  workflows/
    capstone.yml
```

---

## Published scoring rubric

### Base score: 100 points

| Area | Points | Learning objective | What the scorer looks for |
|---|---:|---|---|
| Mission and architecture | 10 | Modules 01 and 10 | `capstone/mission.md`, `capstone/architecture.md` |
| Feature implementation and sample data | 15 | Modules 03 and 04 | feature files listed in scorecard + sample data file |
| Quality gates | 15 | Modules 05 and 08 | tests + GitHub Actions build/test workflow |
| Containerization | 15 | Module 06 | Dockerfile + compose/container runtime artifacts |
| Deployment automation and IaC | 15 | Modules 07, 08, and 09 | Bicep/Terraform/Kubernetes/App Service deployment assets |
| Observability and reliability | 15 | Module 09 | health, monitor, alerts, telemetry, plus live verification |
| Security modernization | 10 | Module 09 | secret-store, identity, env-var, or Key Vault patterns |
| Runbook and retrospective | 5 | Module 10 | `capstone/runbook.md`, `capstone/retrospective.md` |

### AI bonus: 15 points

| Bonus area | Points | What earns it |
|---|---:|---|
| AI capability added to the app | 5 | Repo includes AI feature files |
| AI feature is grounded on data | 5 | AI files or notes show prompts, grounding, or data usage |
| Live AI demo verified | 5 | Instructor confirms the AI feature actually works |

### Total possible score

```text
115 points = 100 base + 15 AI bonus
```

---

## Manual verification points

Most of the score is repo-based. Three checks are instructor-verified in the scoreboard UI:

- deployment URL works
- health endpoint works
- AI demo works

These are shown on screen so students can see exactly where manual verification changed the score.

---

## Tie-breakers

If the total score is tied:

1. higher base score wins
2. if still tied, higher observability and reliability score wins
3. if still tied, higher AI bonus wins
4. if still tied, instructor chooses the clearer demo story

---

## Fairness rules to publish before the challenge

Use these rules exactly as written:

1. Both teams get the same starter repo.
2. Both teams get the same sample data.
3. Both teams must publish `capstone/scorecard.json`.
4. Only evidence in the GitHub repo and the visible live checks can be scored.
5. Hidden work or verbal claims do not count unless they are linked in the repo.
6. AI bonus points require a working feature, not just a placeholder button.

---

## How to run the scoreboard

1. Publish both team repos to GitHub.
2. Make sure `capstone/scorecard.json` exists in each repo.
3. Open [lab-10-capstone-scoreboard.html](lab-10-capstone-scoreboard.html).
4. Enter the starter repo URL, Team Red repo URL, and Team Blue repo URL.
5. Check the live verification boxes after testing the running apps.
6. Click **Score teams**.

The scoreboard will:

- read each repo
- fetch `capstone/scorecard.json`
- validate listed evidence files
- calculate base points and AI bonus
- show category breakdowns
- show the winner graphically

---

## Files in this kit

- [Interactive scoreboard](lab-10-capstone-scoreboard.html)
- [Scorecard template](lab-10-capstone-scorecard-template.json)
- [Sample data](lab-10-capstone-sample-data.json)

---

## Recommended instructor script

Use this short script when introducing the capstone:

> "Red Team and Blue Team are starting from the same legacy app, the same sample data, and the same scoring rules. The public scoreboard will pull your GitHub repos and score your modernization evidence against the course learning objectives. If it is not in the repo or visibly running, it does not count."

---

## Suggested modernization ideas students can pursue

- add one new API endpoint backed by the sample data
- add unit or functional tests around the new slice
- add a GitHub Actions workflow with build and test gates
- containerize the app and run it locally or on the Ubuntu VM
- add IaC or deployment automation
- add health checks and monitoring notes
- remove secrets from config and move to environment-based configuration
- add an AI chat panel that answers questions about the sample data

---

## AI bonus ideas that fit the course

- "Ask the catalog" chat experience
- "Summarize open support tickets" assistant
- "What products are low stock?" question box
- "Which customer has the most open orders?" assistant view

To earn full AI bonus points, teams should also explain:

- what model or service they used
- what data the AI feature can access
- what safety limits or disclaimers they added
