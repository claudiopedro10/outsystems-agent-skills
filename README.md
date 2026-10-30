# OutSystems Agent Skills

**Reusable AI skills for OutSystems architecture, development, and troubleshooting.**

A publicly available skill library maintained by the repository owner for developers, technical leads, and architects. Each skill is a Markdown file that gives an AI assistant a focused workflow and review criteria.

## New to AI? Start here

You do not need to write a complex prompt or configure an API.

1. Choose a skill from the table below.
2. Open its `SKILL.md` file and copy the contents.
3. Paste them into your AI conversation, or attach the file if your application supports it.
4. Send a request using the [guided request template](docs/request-template.md).
5. Review the proposed analysis and verify changes in a development environment.

For a complete walkthrough, read [Using skills for the first time](docs/usage.md). For installation in a coding agent, read [Agent setup](docs/agents.md).

## Why use these skills?

- **More useful context:** describe the affected module, elements, symptoms, and constraints.
- **Consistent analysis:** ask the assistant to separate evidence from assumptions.
- **Clear responsibilities:** review Foundation, Core, and End User boundaries.
- **Reviewable recommendations:** understand the proposed change, its impact, and how to validate it.
- **Reusable instructions:** use the same workflow across supported agents or manually in a chat.

Skills guide an assistant; they do not automatically connect to Service Studio, read OML/OAP files, or deploy applications. Access depends on the tools and permissions available to the assistant.

## Choose a skill

| Your task | Skill |
| --- | --- |
| Review an external integration or reusable technical capability | [Foundation](skills/outsystems-foundation/SKILL.md) |
| Model entities, business rules, and domain services | [Core](skills/outsystems-core/SKILL.md) |
| Review screens, user journeys, and interface states | [End User](skills/outsystems-enduser/SKILL.md) |
| Review responsibilities, dependencies, or cycles | [Architecture](skills/outsystems-architecture/SKILL.md) |
| Investigate an error or unexpected behavior | [Troubleshooting](skills/outsystems-troubleshooting/SKILL.md) |
| Review authentication, authorization, or sensitive data handling | [Security](skills/outsystems-security/SKILL.md) |

For a dialog that remains open after a completed operation, start with **Troubleshooting**. Use **End User** for a broader review of the user journey and interface states.

## Example request

Load the Troubleshooting skill, then describe a concrete scenario like this:

### Example: order approval dialog does not close

*Fictional scenario for OutSystems 11 / Reactive Web.*

**Context**

- **Module:** `PurchaseOrders_UI`
- **Screen:** `OrderDetails`
- **Block:** `OrderApprovalDialog`
- **Client action:** `SubmitApproval`
- **Completion event:** `ApprovalCompleted`

**Observed behavior**

The order is approved successfully, but the dialog remains open and the
loading indicator stays visible. Refreshing the screen shows the updated
order status.

**Expected behavior**

After successful approval, stop the loading indicator, close the dialog,
and refresh the order summary. If approval fails, stop the loading indicator,
keep the dialog open, and display an actionable error.

**Constraints**

Preserve existing business rules, public inputs, events, and service
contracts. Limit the correction to the affected interface flow.

**Request to the assistant**

Use `outsystems-troubleshooting` to trace the submission action, completion
event, parent handler, and interface state updates. Separate evidence from
hypotheses. Ask for the relevant action flows before selecting a cause.
Provide a focused correction plan and regression checks; do not edit or
deploy the application.

See the [complete walkthrough](examples/loading-and-modal.md) for reproduction
steps, evidence to provide, and acceptance criteria. The scenario is
fictional; it does not describe an inspected application.

## Platform scope

The Foundation/Core/End User organization uses the OutSystems 11 Architecture Canvas as a reference. ODC requires explicit adaptation to its applications, libraries, and available capabilities. O11 tools and mechanisms must not be assumed to exist unchanged in ODC.

## Documentation

- [First-time usage guide](docs/usage.md)
- [Request template and field explanations](docs/request-template.md)
- [Claude, Codex, Gemini, DeepSeek, Kimi, and other agents](docs/agents.md)
- [Order approval troubleshooting walkthrough](examples/loading-and-modal.md)
- [Architecture review example](examples/architecture-review.md)
- [Skill structure and quality criteria](docs/skill-design.md)
- [Official sources](docs/sources.md)
- [Roadmap](ROADMAP.md)
- [Repository maintenance policy](CONTRIBUTING.md)
- [Security and data handling](SECURITY.md)

## Project status

Initial edition with six starter skills. File structure and internal links are checked; execution has not been validated across every agent or OutSystems scenario. No productivity benchmark or compatibility certification is claimed.

Repository documentation and skill instructions are maintained in English. Users may write requests and ask for responses in their preferred language.

## Repository access

You may read, download, and use the skills. External contributions are not accepted: issues, pull requests, discussions, wiki editing, and repository projects are disabled. Updates to this original repository are reserved for the owner and explicitly authorized maintainers. See the [maintenance policy](CONTRIBUTING.md).

Public files and their commit history are visible to everyone. GitHub allows independent forks and downloads of public repositories; these do not grant write access to this repository.

Licensed under [MIT](LICENSE). This is an independent community project, with no affiliation with or endorsement by OutSystems or the AI vendors. Product names belong to their respective owners.
