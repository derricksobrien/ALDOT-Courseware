# AI Coding Agent Sharing Plan

- Timestamp: 2026-08-09T04:48:22.7974789-06:00
- Scope: Recommended approaches for giving students access to GitHub Copilot or similar AI coding agents in the MVP course environment.

## Summary

The best approach depends on the product and the classroom model:

- For GitHub Copilot, use per-student seats provisioned through a GitHub organization or enterprise account.
- For API-based models such as Azure OpenAI or OpenAI, a single central subscription can be used behind a classroom proxy or gateway.
- For low-cost or offline scenarios, local models such as Ollama can be installed on lab machines.

## Recommended Options

### Option 1: GitHub Copilot for Business / Enterprise (recommended for real developer workflows)

**Best for:** students who need the native Copilot experience inside VS Code or Visual Studio.

Benefits:
- closest match to real-world coding workflows
- per-user identity and policy control
- easier support for classroom administration

Implementation approach:
- provision Copilot seats for each student through the organization
- assign students to the course org or enterprise account
- enable policies for acceptable use, data handling, and billing oversight

**Important:** do not attempt to route all student usage through a single shared Copilot account. Use seat-based provisioning instead.

### Option 2: Azure OpenAI or OpenAI API behind a classroom gateway (recommended for centralized access)

**Best for:** courses that want one central model deployment and a managed per-student experience.

Benefits:
- one central provider subscription can be used
- usage can be tracked and capped per student or per class
- easier to enforce cost controls and logging

Implementation approach:
- students authenticate to a course portal or lab environment
- a gateway or proxy routes requests to the shared AI deployment
- the gateway applies quotas, logging, rate limits, and content filtering
- prompts are scoped to course-specific tasks and do not expose sensitive data

**Caution:** do not hand students a shared API key directly and let them use it arbitrarily. Use a managed gateway instead.

### Option 3: Local models on lab machines (recommended for privacy and low cost)

**Best for:** offline labs, constrained budgets, or privacy-sensitive environments.

Benefits:
- no per-token cloud cost
- no reliance on internet connectivity
- good for basic coding assistance and prompt-driven exercises

Implementation approach:
- install Ollama or a similar local runtime on each lab VM or shared image
- configure VS Code or another client to use the local model endpoint
- keep the model size appropriate for the classroom hardware

## Can one shared API be used for all students?

Yes, but only if it is managed carefully.

The recommended pattern is:

1. Students authenticate with a class identity or course portal.
2. Your middleware or gateway maps that identity to a student-specific quota.
3. Requests are forwarded to a central AI deployment using one provider subscription.
4. Usage, errors, and prompts are logged for governance and cost control.

What not to do:
- do not share a direct API key with all students without restriction
- do not rely on a single consumer account for all usage
- do not send secrets or private data to the model without review

## Suggested rollout plan

### Phase 1: simple and low risk
- use GitHub Copilot seats for students who need native IDE integration
- keep the rest of the course on standard development tools and lab instructions

### Phase 2: centralized AI access
- add a classroom gateway that routes AI requests for coding help and assessment support
- enforce per-student quotas and preserve audit logs

### Phase 3: advanced governance
- add student-level usage reporting, prompt review, and content-security guardrails
- optionally integrate with an LMS or lab management portal

## Recommended choice for this course

For the MVP modernization course, the best practical path is:

- **Primary path:** GitHub Copilot seats for students who need the full IDE experience.
- **Secondary path:** Azure OpenAI or an equivalent API gateway for centralized, instructor-managed AI support.
- **Fallback path:** local models for budget-sensitive or offline environments.

## Final recommendation

Use a managed identity-based model where possible. For GitHub Copilot, use per-user seats. For API-based models, use a shared deployment behind a classroom gateway with quotas and logging rather than a single shared account.
