# OutSystems Agent Skills

**Troubleshoot, refactor, and implement changes in OutSystems.**

Start with [OutSystems Developer](skills/outsystems-developer/SKILL.md) and
describe the outcome in your own words. The skill selects a workflow from the
request. Invoke it without a task to see the three options.

| Workflow | Example developer request | What you get |
| --- | --- | --- |
| [Troubleshoot](skills/outsystems-developer/SKILL.md#troubleshoot) | “Approval succeeds, but the dialog stays open.” | A supported cause or a check that distinguishes the remaining hypotheses, plus a regression case. |
| [Refactor](skills/outsystems-developer/SKILL.md#refactor) | “Extract the duplicated approval check and keep the public action signature.” | A focused structural change or plan, plus before/after checks for existing consumers. |
| [Implement](skills/outsystems-developer/SKILL.md#implement) | “Allow the author to cancel a draft order.” | A design or implementation against observable acceptance criteria, including a denied or boundary case. |

Ask for a review, a plan, or edits as appropriate. You can start without
knowing which layer owns the problem.

> [!IMPORTANT]
> **Before using these skills with an OutSystems 11 module**
>
> Follow the official OutSystems MCP recommendations first:
>
> 1. Install the [official OutSystems O11 MCP skill](https://github.com/OutSystems/outsystems11-mcp) for your agent.
> 2. Open your module and start the MCP Server in Service Studio.
> 3. Register the address shown in Service Studio in your agent.
> 4. Confirm that the agent can read the open module.
> 5. Choose a complementary skill from this repository.
>
> [Official OutSystems setup](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/)
> · [Step-by-step MCP guide](docs/service-studio-mcp.md)
>
> These prerequisites apply to O11 module access through Service Studio MCP.
> You can also use the skills manually with supplied evidence. For ODC, use
> the applicable ODC documentation and tools.

## New to AI? Start here

You do not need to write a complex prompt or configure an API.

1. Open [OutSystems Developer](skills/outsystems-developer/SKILL.md).
2. Copy its instructions.
3. Paste them into your AI conversation, or attach the file if your application supports it.
   To inspect an open OutSystems 11 module, also configure the [Service Studio MCP connection](docs/service-studio-mcp.md).
4. Describe the task in one sentence. Use the [guided request template](docs/request-template.md) when you need to share more context.
5. Review the proposed analysis and verify changes in a development environment.

For a complete walkthrough, read [Using skills for the first time](docs/usage.md). For installation in a coding agent, read [Agent setup](docs/agents.md).

## Why use these skills?

- **More useful context:** describe the affected module, elements, symptoms, and constraints.
- **Consistent analysis:** ask the assistant to separate evidence from assumptions.
- **Clear responsibilities:** review Foundation, Core, and End User boundaries.
- **Reviewable recommendations:** understand the proposed change, its impact, and how to validate it.
- **Reusable instructions:** use the same workflow across supported agents or manually in a chat.

For OutSystems 11, a supported agent can inspect the open module using the separately configured Service Studio MCP server and official OutSystems O11 MCP skill. This repository's skills guide the task; they do not install or connect those components. The endpoint and port are taken from each developer's Service Studio settings.

## Optional specialist skills

The developer workflow covers common checks directly. Use a specialist independently when a particular question calls for a deeper review.

| For a deeper review of | Specialist |
| --- | --- |
| Review an external integration or reusable technical capability | [Foundation](skills/outsystems-foundation/SKILL.md) |
| Model entities, business rules, and domain services | [Core](skills/outsystems-core/SKILL.md) |
| Review screens, user journeys, and interface states | [End User](skills/outsystems-enduser/SKILL.md) |
| Review responsibilities, dependencies, or cycles | [Architecture](skills/outsystems-architecture/SKILL.md) |
| Investigate an error or unexpected behavior | [Troubleshooting](skills/outsystems-troubleshooting/SKILL.md) |
| Review authentication, authorization, or sensitive data handling | [Security](skills/outsystems-security/SKILL.md) |

For a dialog that stays open, start in **Troubleshoot**. Bring in **End User** if the evidence points to state shared by a block and its parent.

## Example request

Load OutSystems Developer and describe the symptom. This longer example shows what to share when those details are available.

### Example: order approval dialog does not close

*Fictional scenario for OutSystems 11 / Reactive Web.*

**Context**

- **Architecture layer:** End User
- **Target module:** `PurchaseOrders_UI`
- **Application:** `Procurement` (fictional)
- **Open modules:** Unknown; verify through MCP if available.
- **Related modules:** Unknown; establish relevant providers and consumers.
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

First verify the configured Service Studio MCP connection and the open target
module. Use available read tools with the official O11 MCP skill. If not
connected, request sanitized action flows; do not claim inspection succeeded.

Use Troubleshoot to trace the submission action, completion
event, parent handler, and interface state updates. Separate evidence from
hypotheses. Inspect available action flows first; ask only for evidence that
remains missing before selecting a cause.
Provide a focused correction plan and regression checks; do not edit or
deploy the application.

See the [complete walkthrough](examples/loading-and-modal.md) for reproduction
steps, evidence to provide, and acceptance criteria. The scenario is
fictional; it does not describe an inspected application.

## Platform scope

The Foundation/Core/End User organization uses the OutSystems 11 Architecture Canvas as a reference. ODC requires explicit adaptation to its applications, libraries, and available capabilities. O11 tools and mechanisms must not be assumed to exist unchanged in ODC.

## Documentation

- [First-time usage guide](docs/usage.md)
- [Service Studio MCP setup and connection test](docs/service-studio-mcp.md)
- [Request template and field explanations](docs/request-template.md)
- [Claude, Codex, Gemini, DeepSeek, Kimi, and other agents](docs/agents.md)
- [Order approval troubleshooting walkthrough](examples/loading-and-modal.md)
- [Architecture review example](examples/architecture-review.md)
- [Skill structure and quality criteria](docs/skill-design.md)
- [Structural checks and behavioral evaluation cases](docs/evaluation.md)
- [Repository audit and decisions](docs/audits/2026-11-06.md)
- [Official sources](docs/sources.md)
- [Roadmap](ROADMAP.md)
- [Repository maintenance policy](CONTRIBUTING.md)
- [Security and data handling](SECURITY.md)

## Project status

One developer entry point and six independently installable specialties, with automated structural checks and
[documented behavioral evaluation cases](docs/evaluation.md). Structural checks
cover metadata, local links, and packaging; they do not validate model decisions
or OutSystems runtime behavior. See the evaluation guide for the scope of offline
cases. Live O11/ODC tests are pending. No productivity benchmark or
compatibility certification is claimed.

Repository documentation and skill instructions are maintained in English. Users may write requests and ask for responses in their preferred language.

## Repository access

You may read, download, and use the skills. External contributions are not accepted: issues, pull requests, discussions, wiki editing, and repository projects are disabled. Updates to this original repository are reserved for the owner and explicitly authorized maintainers. See the [maintenance policy](CONTRIBUTING.md).

Public files and their commit history are visible to everyone. GitHub allows independent forks and downloads of public repositories; these do not grant write access to this repository.

Licensed under [MIT](LICENSE). This is an independent community project, with no affiliation with or endorsement by OutSystems or the AI vendors. Product names belong to their respective owners.
