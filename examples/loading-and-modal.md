# Troubleshooting walkthrough: order approval dialog

This fictional OutSystems 11 / Reactive Web example shows how to prepare a
useful request, supply evidence, and assess a recommendation. It is not a
diagnosis of an inspected application.

## 1. Load the skill

Use [outsystems-troubleshooting](../skills/outsystems-troubleshooting/SKILL.md)
through your agent's supported setup, or paste the skill instructions into
your conversation. Then send the scenario below.

Before using the example against a real module, configure the
[Service Studio MCP server](../docs/service-studio-mcp.md), install the
official OutSystems O11 MCP skill, and verify the open module. This example
is fictional and is not a claim that a module was inspected.

## 2. Describe the problem

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

Verify the configured Service Studio MCP and that the intended module is
open. Use available read tools with the official O11 MCP skill. If the
connection is unavailable, ask for sanitized action flows and explain the
inspection limit.

Use `outsystems-troubleshooting` to trace the submission action, completion
event, parent handler, and interface state updates. Separate evidence from
hypotheses. Inspect available action flows first; ask only for evidence that
remains missing before selecting a cause.
Provide a focused correction plan and regression checks; do not edit or
deploy the application.

## 3. Make the issue reproducible

1. Open an order with status **Pending approval** on `OrderDetails`.
2. Open `OrderApprovalDialog`.
3. Select **Approve** and wait for the approval request to return.
4. Observe that the loading indicator and dialog remain visible.
5. Refresh the screen and confirm that the order status is **Approved**.

In a real request, record whether this happens on every attempt, when it
started, and whether failure or cancellation behaves differently.

## 4. Supply focused evidence

Use available MCP read tools to inspect the open module when connected. Otherwise provide labeled screenshots or logic excerpts for:

- `SubmitApproval`, including success and exception paths.
- Where `ApprovalCompleted` is raised and its existing event contract.
- The parent handler assigned to `ApprovalCompleted`.
- The state or expressions controlling loading and dialog visibility.
- The action that refreshes the order summary.
- Relevant logs and reproduction observations, with sensitive data removed.

Start with the submission flow and parent handler. Provide additional
artifacts when the assistant explains which uncertainty they will resolve.
A fictional name in this guide is not a requirement to add or rename an
element in your application.

## 5. Evaluate the analysis

A useful response should acknowledge that approval appears to persist while
interface completion remains unresolved. It should identify the evidence
needed to establish whether the success path, event, parent handler, and
state assignments execute as expected.

| Investigation question | Evidence to inspect |
| --- | --- |
| Does execution reach the success path? | Action flow and observed response |
| Is the completion event raised and handled? | Event wiring and parent handler |
| Which element owns each interface state? | State declarations and assignments |
| Do error paths clear the loading state? | Exception handling |
| Does a second approval attempt behave correctly? | Repeated-use reproduction |

These are investigation questions, not established causes. Successful data
persistence alone does not prove that a particular interface handler ran.

Ask for clarification if the assistant assumes a missing event, invents
existing actions, or proposes changing a public contract without evidence.

## 6. Review the correction plan

Before implementation, expect:

- The specific existing element and path to change.
- Evidence supporting the proposed correction.
- How the plan preserves the stated contracts and business rules.
- Any remaining uncertainty or conflict with a constraint.
- Validation steps and a practical rollback approach.

Keep the change scoped to the demonstrated issue. A broader redesign needs
a separate justification.

## 7. Validate the outcome in development

| Scenario | Acceptance criteria |
| --- | --- |
| Successful approval | Loading stops, dialog closes, and summary shows Approved |
| Approval rejected by a business rule | Loading stops, dialog stays open, and an actionable message appears |
| Request failure | Loading stops; no false success or unintended closure |
| Repeated use | Opening and submitting another pending order uses fresh state |
| Existing consumers | Public inputs, events, and service contracts remain compatible |

Check cancellation and duplicate submission according to existing functional
rules. Do not infer that closing a dialog cancels an in-flight request.

Record observed results before declaring the issue resolved. This guide
provides a request and validation structure; it does not claim a verified fix.
