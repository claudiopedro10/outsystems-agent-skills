# Write a clear request

Give the assistant enough context to understand the task, locate the affected
logic, and recognize a successful outcome. Describe observations without
assuming a root cause.

## Copy and adapt

Load the selected skill, then copy the template below and replace the
bracketed text. Keep only fields relevant to your task.

```text
Skill: [selected skill]

Context
- Platform: [OutSystems 11 or ODC]
- Application type: [Reactive Web, Traditional Web, or Mobile]
- Module or application: [name]
- Related elements: [name and role of each relevant element]

Issue or objective
[Summarize the problem or intended improvement.]

Observed behavior
[Describe what happens, when it happens, and its impact.]

Expected behavior
[Describe the outcome for success and relevant failure conditions.]

Reproduction steps
1. [Starting state]
2. [User action]
3. [Observed result]

Available evidence
[List labeled screenshots, action flows, logs, or contracts.]

Constraints
[State which components, interfaces, and rules must be preserved.]

Requested deliverable
[Ask for analysis, a correction plan, or explicitly authorized edits.]
[Include how you want the result to be validated.]
```

If a field is unknown, state that rather than guessing. In ODC, describe the
actual application or library. For a new feature, explain the existing flow
or state that no implementation exists yet.

## What each section contributes

| Section | What to include | Purpose |
| --- | --- | --- |
| Context | Platform, application type, names, and element roles | Identifies the technical scope |
| Issue or objective | A concise symptom or goal | States the task |
| Observed behavior | Reproducible facts and user impact | Keeps diagnosis grounded |
| Expected behavior | Success and failure outcomes | Defines correctness |
| Reproduction steps | Starting conditions and actions | Makes the problem repeatable |
| Available evidence | Labeled excerpts or screenshots | Supports a traceable analysis |
| Constraints | Contracts, components, and rules to preserve | Controls the scope of change |
| Requested deliverable | Analysis, plan, or authorized implementation | Defines what the assistant should do |

An identifier alone does not describe implementation. Specify whether an
element is a screen, block, action, or event when known.

## Worked example

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

### Reproduction steps

1. Open a pending order on the `OrderDetails` screen.
2. Open `OrderApprovalDialog`.
3. Select **Approve** and wait for the approval request to return.
4. Observe that the loading indicator and dialog remain visible.
5. Refresh the screen and confirm that the order status is **Approved**.

### Evidence to provide

Start with the `SubmitApproval` action flow, the `ApprovalCompleted` event
definition, its parent handler, and the expressions controlling loading and
dialog visibility. Add relevant error handling and sanitized logs.

The scenario is fictional. The reported behavior does not establish a root
cause. See the [full walkthrough](../examples/loading-and-modal.md) for how to
evaluate the response and validate a proposed correction.
