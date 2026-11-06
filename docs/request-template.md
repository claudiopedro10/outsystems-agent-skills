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
- Application type: [O11: Reactive Web, Traditional Web, or Mobile; ODC: actual type]
- Architecture layer: [Foundation, Core, End User, Not sure, or Not applicable]
- Service Studio MCP: [reported configured / verified by a tool read / unavailable / unknown / not applicable]
- Open modules: [names verified open and accessible by MCP; Unknown until checked]
- Target module: [main module to investigate or change; Not applicable if needed]
- Application: [owning application, if known; optional]
- Related modules: [potentially relevant modules; Unknown or None identified]
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
[List available MCP access, screenshots, action flows, logs, or contracts.]

Constraints
[State which components, interfaces, and rules must be preserved.]

Requested deliverable
[Ask for analysis, a correction plan, or explicitly authorized edits.]
[Include how you want the result to be validated.]
For O11, discover available modules and verify access to the target module.
Use read tools for analysis; report missing access or evidence.
```

If a field is unknown, state that rather than guessing. In ODC, describe the
actual application or library. For a new feature, explain the existing flow
or state that no implementation exists yet.

## Identify the scope without assuming access

These fields separate task scope from tool access. They are optional when
irrelevant; do not invent values to complete the template.

| Field | Meaning | Does not imply |
| --- | --- | --- |
| Open modules | Modules confirmed open and accessible by an MCP read; cite the result | That every reference or application module is open |
| Target module | Main module the task concerns, even if currently inaccessible | Permission or ability to edit it |
| Application | Owning application or business context, if known | Access to its modules |
| Related modules | Potentially relevant providers/consumers | Verified dependencies or tool access |

Before a tool read, write `Open modules: Unknown`. If you know which tabs you
opened, record that as **Developer-reported open modules** under Available
evidence; the agent must still verify access. Configuration alone is not a
successful connection. Preserve the distinction in the response.

Use `Unknown` for information not established, `None identified` for an
investigation that found no relevant modules, and `Not applicable` when a
field does not fit. For ODC, Target module and Service Studio Open modules
may be inapplicable; identify the actual application/library under Application
and Related elements.

Older requests still work: treat `Open module` as a reported candidate and
interpret `Module or application` from context. Ask which it is only if an
unresolved ambiguity affects the next operation. Do not require a rewritten
request or all four fields for a simple task.

## Working with Service Studio MCP

For OutSystems 11, specify whether your agent is connected to the local
Service Studio MCP server and which module is the target. List only verified
open modules; keep developer-reported tabs in Available evidence. The configured endpoint
comes from your Service Studio window; no port is fixed by this template.
See [setup and connection test](service-studio-mcp.md). For ODC, identify the
actual supported tools separately.

## Select the architecture layer

Use **Architecture layer** to identify the responsibility of the affected
module in OutSystems 11:

| Option | Typical responsibility |
| --- | --- |
| Foundation | Integrations, adapters, and reusable technical capabilities |
| Core | Business entities, rules, and domain services |
| End User | Screens, blocks, and user journey orchestration |
| Not sure | Ask the assistant to assess the supplied responsibilities |

For a task involving several modules, state the layer for each module.
Do not infer the layer from a name or suffix alone. The assistant should
check the declared layer against the supplied responsibilities and explain
any mismatch.

For ODC, use **Not applicable** when this O11 classification does not fit.
Describe the actual application/library responsibilities instead.

## What each section contributes

| Section | What to include | Purpose |
| --- | --- | --- |
| Context | Platform, application type, architecture layer, and element roles | Identifies the technical scope |
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

For O11, verify the configured Service Studio MCP and open module; use
available read tools. If access is unavailable, request sanitized evidence
and state that no module was inspected.

Use `outsystems-troubleshooting` to trace the submission action, completion
event, parent handler, and interface state updates. Separate evidence from
hypotheses. Inspect available action flows first; ask only for evidence that
remains missing before selecting a cause.
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
