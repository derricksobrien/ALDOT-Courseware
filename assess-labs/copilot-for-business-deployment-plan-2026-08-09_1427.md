# GitHub Copilot for Business — Classroom Deployment Plan

- Timestamp: 2026-08-09T14:27:00-06:00
- Scope: Concrete steps to provision and manage GitHub Copilot for Business seats for students in the MVP modernization course.

---

## Overview

GitHub Copilot for Business (CfB) gives each student their own licensed Copilot seat under a centrally managed GitHub organization. The instructor or organization admin controls who has access, what policies are enforced, and what data handling rules apply. Students use Copilot inside VS Code or Visual Studio using their own GitHub identity.

---

## Prerequisites

Before Day 1:

- A GitHub organization already exists or will be created for the course
- The organization owner or billing admin has a payment method configured
- Each student has a personal GitHub account (free accounts are fine)
- Students have VS Code or Visual Studio installed on their lab machine
- Internet access is available from lab machines to github.com

---

## Step 1: Set up the GitHub organization

1. Go to [github.com/organizations/new](https://github.com/organizations/new).
2. Choose a name such as `iis-labs-modernization-course`.
3. Select the **GitHub Copilot Business** plan during organization setup, or upgrade an existing org:
   - Organization → Settings → Billing and plans → GitHub Copilot → Enable for organization
4. Confirm billing. Copilot for Business is billed per seat per month. Unused seats can be removed at the end of the course.

---

## Step 2: Invite students as organization members

1. Go to **Organization → People → Invite member**.
2. Enter each student's GitHub username or email address.
3. Assign the **Member** role (not Owner).
4. Students accept the invitation from their GitHub email.

**Bulk invite option:**
- Use the GitHub CLI to script bulk invitations:

```powershell
# Install GitHub CLI if not present
winget install GitHub.cli

# Authenticate
gh auth login

# Invite a student
gh api orgs/iis-labs-modernization-course/invitations \
  -f invitee_login="studentusername" \
  -f role="direct_member"
```

---

## Step 3: Assign Copilot seats

1. Go to **Organization → Settings → GitHub Copilot → Access**.
2. Select **All members of the organization** to grant access automatically on join, or choose **Selected members** for manual seat assignment.
3. For a classroom, **All members** is the simpler option.
4. Confirm the seat count matches the number of enrolled students.

**Check active seats:**

```powershell
gh api orgs/iis-labs-modernization-course/copilot/billing/seats --jq '.seats[] | .assignee.login'
```

---

## Step 4: Configure organization policies

Go to **Organization → Settings → GitHub Copilot → Policies** and apply these recommended classroom settings:

| Policy | Recommended setting | Reason |
|---|---|---|
| Suggestions matching public code | Block | Prevents accidental reproduction of copyrighted code |
| Allow Copilot to use my code snippets | Disabled | Keeps student work private |
| Allow GitHub to use my feedback | Optional, inform students | Transparency |
| Copilot Chat in IDE | Enabled | Required for lab exercises |
| Copilot in GitHub.com | Enabled | Useful for PR review and documentation tasks |

---

## Step 5: Student setup on lab machines

Each student does the following on their lab machine:

1. Open VS Code.
2. Install the **GitHub Copilot** extension from the VS Code marketplace:
   - Extension ID: `GitHub.copilot`
3. Install the **GitHub Copilot Chat** extension:
   - Extension ID: `GitHub.copilot-chat`
4. Sign in with their GitHub account when prompted.
5. Verify Copilot is active:
   - Look for the Copilot icon in the VS Code status bar (bottom right).
   - Open a `.cs` file and start typing — completions should appear within seconds.

**Quick verification command:**

```powershell
# Confirm extensions are installed
code --list-extensions | Select-String "GitHub.copilot"
```

---

## Step 6: Instructor validation before class

Run this checklist the day before or morning of each class session:

- [ ] All students have accepted their organization invitation
- [ ] All Copilot seats show as active under Organization → Copilot → Seats
- [ ] At least one test machine shows Copilot completions in VS Code
- [ ] Policies are applied and confirmed in the organization settings
- [ ] A recovery path exists for students who cannot sign in (see below)

---

## Recovery paths

### Student cannot accept the invitation
- Re-send the invitation from Organization → People.
- Check the student's spam folder.
- Confirm the email address matches their GitHub account.

### Student cannot sign in to Copilot in VS Code
- Ask the student to run: `Ctrl+Shift+P` → `GitHub Copilot: Sign In`
- Check that the VS Code extension version is current.
- Confirm the student's GitHub account is a member of the org with an active seat.

### Copilot is installed but not suggesting
- Open a `.cs` file and wait 10 seconds.
- Check VS Code Output panel → GitHub Copilot for errors.
- Try toggling Copilot off and on via the status bar icon.

---

## Cost and seat management

| Item | Detail |
|---|---|
| Price | ~$19 USD per seat per month (verify current pricing at github.com/features/copilot) |
| Billing | Monthly, prorated for partial months |
| Removing a seat | Organization → Copilot → Seats → Remove user |
| Course end cleanup | Remove all student members from the org, or cancel the Copilot plan |

**Recommended:** remove seats at the end of the course to avoid continued billing. Students who need continued access can purchase their own individual Copilot subscription.

---

## Lab-specific notes for the MVP course

| Lab | Copilot use |
|---|---|
| Lab 03 - Copilot Refactor | Primary — students use Copilot completions and chat directly |
| Lab 04 - Modern .NET API | Supporting — students can use Copilot to scaffold endpoint code |
| Lab 06 - Containerization | Supporting — students can prompt Copilot for Dockerfile patterns |
| Lab 08 - GitHub Actions | Supporting — students can use Copilot to generate workflow YAML |
| Lab 10 - Capstone | Optional — students may use Copilot to document their work |

---

## Timeline

| When | Action |
|---|---|
| 2 weeks before class | Create org, enable Copilot for Business, send invitations |
| 1 week before class | Confirm all students have accepted, validate one test machine |
| Day before class | Run the instructor validation checklist |
| Day 1 morning | Spot-check 2–3 student machines before starting Lab 03 |
| End of course | Remove seats, archive student workspaces, close the org or downgrade plan |

---

## Notes on compliance and acceptable use

- Inform students that Copilot suggestions may draw on public code and they should review all generated code before submitting.
- Students should not paste secrets, credentials, or sensitive data into Copilot chat prompts.
- The instructor should review the organization's data residency and privacy policies with the IT or security team before the course begins.
