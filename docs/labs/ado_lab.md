---
layout: default
title: "Lab 02 — ADO Lab (Full)"
parent: Labs
nav_order: 11
---

# Lab 02: Azure DevOps Work Tracking for Application Modernization

## Module
Module 02 â€” Azure DevOps Work Tracking

## Tier
Core Lab (Optional when ADO org is not provisioned)

## Duration
45â€“60 minutes

## Goal

Set up a complete work tracking structure for your modernization project inside Azure DevOps. By the end of this lab you will have a live board with epics, features, user stories, and tasks that mirror the actual work delivered across the course.

---

## Prerequisites

| Item | Value |
|---|---|
| ADO Organization | `https://dev.azure.com/iis-labs` |
| ADO Project | `Software_Dev_Mod` |
| Your login | Provided by instructor (e.g. `sdm-2026-aug10 Student01`) |
| Reference app | eShopOnWeb (already forked to your GitHub org) |

> **Instructor note:** Ensure every student has **Contributor** access to the `Software_Dev_Mod` project before starting. The instructor account is `sdm-2026-aug10 Instructor01`.

---

## Background: The Modernization Work Hierarchy

Azure Boards uses a four-level hierarchy to organize work:

```
Epic  â”€â”€â”€ represents a major modernization theme
  â””â”€â”€ Feature  â”€â”€â”€ a deliverable outcome within that theme
        â””â”€â”€ User Story  â”€â”€â”€ a testable slice of value
              â””â”€â”€ Task  â”€â”€â”€ concrete implementation step (hours-level)
```

In this lab you model the real work you will deliver across the course. Each lab from Lab 03 onwards maps to at least one User Story.

---

## Part 1 â€” Orient Yourself in the Project

### Step 1.1 â€” Open Azure Boards

1. Navigate to [https://dev.azure.com/iis-labs/Software_Dev_Mod](https://dev.azure.com/iis-labs/Software_Dev_Mod).
2. In the left sidebar click **Boards â†’ Boards**.
3. Confirm you see the **Software_Dev_Mod Team** board.
4. Click **Backlogs** in the left sidebar and verify the backlog is empty (you will populate it next).

---

## Part 2 â€” Create the Modernization Epic and Feature Structure

You will create **two epics** that map to the two days of the course.

### Step 2.1 â€” Create Epic: Day 1 â€” Foundations

1. In the left sidebar click **Boards â†’ Backlogs**.
2. At the top of the backlog view, open the **hierarchy selector** (the dropdown next to "Stories") and switch to **Epics**.
3. Click **+ New Work Item** at the top of the list.
4. Type the title:
   ```
   Day 1 â€” Modern Development Foundations and AI-Assisted Coding
   ```
5. Press **Enter** to save.
6. Click the Epic to open it and fill in:
   - **Description:** Covers modernization strategy, ADO work tracking, GitHub Copilot, and modern .NET API development.
   - **Area:** Software_Dev_Mod
   - **Iteration:** Leave blank for now (you will assign to a sprint in Part 3).
7. Click **Save & Close**.

### Step 2.2 â€” Create Epic: Day 2 â€” Automation and Cloud Delivery

1. Repeat Step 2.1 with the title:
   ```
   Day 2 â€” Containerization, CI/CD, and Azure Deployment
   ```
2. Fill in:
   - **Description:** Covers Docker, Kubernetes/OpenShift, GitHub Actions pipelines, Azure deployment, and the capstone.
3. Click **Save & Close**.

### Step 2.3 â€” Add Features Under Day 1

Switch the backlog level to **Features**. Under the **Day 1** Epic add these four features (one at a time using **+ Add Feature**):

| # | Feature Title |
|---|---|
| F1 | Work Item Tracking and Sprint Planning |
| F2 | AI-Assisted C# Refactoring with GitHub Copilot |
| F3 | Modern .NET API and SQL Server Data Access |
| F4 | Test Automation Foundation |

### Step 2.4 â€” Add Features Under Day 2

Under the **Day 2** Epic add these four features:

| # | Feature Title |
|---|---|
| F5 | Application Containerization with Docker |
| F6 | Kubernetes and OpenShift Deployment |
| F7 | CI/CD Pipeline with GitHub Actions |
| F8 | Azure Cloud Deployment and Observability |

---

## Part 3 â€” Create the Sprint

### Step 3.1 â€” Define Sprint 1

1. In the left sidebar click **Project settings â†’ Boards â†’ Team configuration**.
2. Under **Iterations**, click **+ New child** (under the root path).
3. Name it:
   ```
   Sprint 1 â€” Course Delivery
   ```
4. Set dates to match the course dates (e.g. Day 1 start through Day 2 end).
5. Click **Save**.

### Step 3.2 â€” Assign the Sprint to your Team

1. Still in Team configuration, click the **Iterations** tab.
2. Click **Select iterations** and check **Sprint 1 â€” Course Delivery**.
3. Click **Save**.

---

## Part 4 â€” Add User Stories and Tasks

You will now create one User Story per lab and add tasks under each. Start with Feature F1 (Work Item Tracking).

### Step 4.1 â€” Add User Story for Lab 02 (this lab)

1. Go to **Boards â†’ Backlogs** and switch level to **Stories**.
2. Expand **Feature F1 â€” Work Item Tracking and Sprint Planning**.
3. Click **+ Add User Story** and type:
   ```
   As a modernization team member, I can track all sprint work in ADO so that
   progress is visible to stakeholders.
   ```
4. Open the story and fill in:
   - **Acceptance Criteria:**
     ```
     - Work item hierarchy (Epic â†’ Feature â†’ Story â†’ Task) is in place
     - Sprint is defined with start and end dates
     - At least one query returns work items filtered by sprint
     - Dashboard shows sprint burndown and work item counts
     ```
   - **Story Points:** 2
   - **Iteration:** Sprint 1 â€” Course Delivery
5. Save the story.

### Step 4.2 â€” Add Tasks to the Lab 02 Story

Inside the User Story, click **+ Add Task** and create the following tasks (assign each to yourself):

| Task Title | Remaining Work (hours) |
|---|---|
| Create Epic and Feature hierarchy in ADO | 0.5 |
| Define Sprint 1 with dates and assign to team | 0.25 |
| Create User Story and link to Feature | 0.25 |
| Create a sprint query and save it | 0.25 |
| Add sprint burndown widget to dashboard | 0.25 |

### Step 4.3 â€” Seed Stories for Remaining Labs

Add one User Story for each remaining lab. Link each story to the correct Feature. Use the table below:

| Lab | Feature | Story Title | Points |
|---|---|---|---|
| Lab 03 | F2 â€” AI-Assisted C# Refactoring | As a developer, I can use GitHub Copilot to refactor legacy C# and generate unit tests. | 3 |
| Lab 04 | F3 â€” Modern .NET API | As a developer, I can add a SQL Server-backed REST endpoint to eShopOnWeb using minimal APIs. | 3 |
| Lab 05 | F4 â€” Test Automation | As a QA engineer, I can design and execute a Tosca test suite against the reference app. | 3 |
| Lab 06 | F5 â€” Containerization | As a developer, I can containerize the eShopOnWeb app and push the image to Azure Container Registry. | 3 |
| Lab 07 | F6 â€” Kubernetes/OpenShift | As a DevOps engineer, I can deploy the container to OpenShift and expose it via a route. | 3 |
| Lab 08 | F7 â€” CI/CD Pipeline | As a DevOps engineer, I can create a GitHub Actions workflow that builds, tests, and deploys on every push. | 3 |
| Lab 09 | F8 â€” Azure Operations | As an operator, I can deploy the app to Azure with Application Insights monitoring enabled. | 3 |

Set all stories to **Sprint 1 â€” Course Delivery** and **State: New**.

---

## Part 5 â€” Create Queries and a Dashboard

### Step 5.1 â€” Create a Sprint Query

1. In the left sidebar click **Boards â†’ Queries**.
2. Click **New query**.
3. Configure the query:

   | Field | Operator | Value |
   |---|---|---|
   | Work Item Type | = | User Story |
   | Iteration Path | Under | Software_Dev_Mod\Sprint 1 â€” Course Delivery |
   | State | <> | Removed |

4. Click **Run query** and verify you see all 8 User Stories.
5. Click **Save query** and name it:
   ```
   Sprint 1 â€” All User Stories
   ```
6. Save it under **My Queries** (or **Shared Queries** if the instructor grants access).

### Step 5.2 â€” Add Widgets to the Dashboard

1. Go to **Overview â†’ Dashboards â†’ Software_Dev_Mod Team - Overview**.
2. Click **Edit dashboard**.
3. Add the following widgets (click **+ Add widget** for each):

   | Widget | Configuration |
   |---|---|
   | **Sprint Burndown** | Team: Software_Dev_Mod, Iteration: Sprint 1 |
   | **Work Item Count** | Query: Sprint 1 â€” All User Stories |
   | **Velocity** | Team: Software_Dev_Mod |

4. Click **Done editing** to save the dashboard.

---

## Part 6 â€” Link Work Items to Source Control

### Step 6.1 â€” Connect Your GitHub Repo

> Skip this step if the instructor has not yet connected GitHub to the ADO project.

1. Go to **Project Settings â†’ GitHub connections**.
2. Click **Connect your GitHub account**.
3. Follow the OAuth flow and authorize the `iis-labs` ADO organization.
4. Select your fork of **eShopOnWeb** and click **Save**.

### Step 6.2 â€” Link a Commit to a Work Item

When you make any commit in a later lab, include the ADO work item ID in the commit message:

```bash
git commit -m "refactor: extract OrderService to separate class AB#<work-item-id>"
```

The `AB#` prefix automatically creates a link between the commit and the ADO work item. After pushing, open the work item in ADO and verify the **Development** section shows the commit.

---

## Validation Checklist

Complete each item and screenshot or export as evidence.

| # | Check | Done |
|---|---|---|
| 1 | Two Epics exist with correct titles | â˜ |
| 2 | Eight Features are created under the correct Epics | â˜ |
| 3 | Eight User Stories exist with Acceptance Criteria, Story Points, and Sprint assigned | â˜ |
| 4 | Lab 02 story has 5 tasks with hours estimates | â˜ |
| 5 | Sprint 1 is defined with start and end dates | â˜ |
| 6 | Query "Sprint 1 â€” All User Stories" returns all 8 stories | â˜ |
| 7 | Dashboard shows Sprint Burndown, Work Item Count, and Velocity widgets | â˜ |
| 8 | At least one commit is linked to a work item (or GitHub connection confirmed) | â˜ |

---

## Evidence to Submit

1. **Screenshot:** ADO backlog showing Epic â†’ Feature â†’ Story hierarchy
2. **Screenshot:** Sprint board with stories in the New column
3. **Screenshot:** Query results showing all 8 User Stories
4. **Screenshot:** Dashboard with all three widgets populated
5. **Screenshot (optional):** Work item Development section showing a linked commit

---

## Instructor Notes

- The ADO project URL is: `https://dev.azure.com/iis-labs/Software_Dev_Mod`
- Student accounts are provisioned as `sdm-2026-aug10 StudentNN` where NN is the student number.
- If sprint dates need to be adjusted, do so in **Project Settings â†’ Boards â†’ Team configuration â†’ Iterations** before the class starts.
- The GitHub connection in Step 6.1 requires the instructor to have GitHub org admin rights. Pre-configure this if possible.
- The Tosca User Story (Lab 05) may be removed from the sprint if Tosca licenses are not available â€” replace with a placeholder Bug titled "Tosca environment not provisioned."

---

## Further Reading

- [Azure Boards documentation](https://learn.microsoft.com/en-us/azure/devops/boards/)
- [Work item types and hierarchy](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items)
- [Connect Azure DevOps to GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github)
- [Dashboard widgets catalog](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/widget-catalog)

