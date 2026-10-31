---
name: outsystems-enduser
description: "Review OutSystems screens, user journeys, and interface states in the End User layer; account for application type and adapt explicitly for ODC."
---

# End User

## Scope and context

Confirm OutSystems 11 or ODC, the known version, application type, objective, and constraints. Foundation/Core/End User uses O11 as its reference. Adapt for ODC only with applicable evidence and documentation; do not transfer tool names or capabilities automatically.

Use supplied inventories, contracts, snippets, screenshots, or sanitized logs, or inspect them through authorized tools. Do not assume platform access or an OML/OAP reader. Ask only for information that changes the analysis.

For O11 module access through Service Studio MCP, follow the
[official OutSystems setup](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/)
and use the [official O11 MCP skill](https://github.com/OutSystems/outsystems11-mcp)
for the agent's tool and Model API instructions. This skill complements
that setup; it does not install or configure it. Manual analysis using
supplied evidence remains possible without MCP.

## Service Studio MCP workflow (OutSystems 11)

For a task involving an O11 module, discover the configured Service Studio
MCP tools and use their available read capabilities to inspect the target
module when connected and authorized. Confirm the open module matches the
request; check the actual available tools and avoid inventing tool names,
properties, or results. The [official OutSystems O11 MCP skill](https://github.com/OutSystems/outsystems11-mcp)
supplies the tool and Model API instructions and is used alongside this skill.

The MCP endpoint is configured in the agent host using the URL shown in
Service Studio; ports vary. Never assume a fixed address or scan local ports.
Do not claim a connection or inspection succeeded without tool evidence.
If tools or the target module are unavailable, explain the gap, provide
setup guidance, and request the relevant sanitized evidence. An analysis-only
request must not invoke write, merge, or publish operations. For authorized
edits, respect the user's scope and Service Studio's write-review settings.

This local Service Studio MCP workflow is specific to O11. For ODC, establish
the applicable tools and documentation separately; do not assume equivalence.

## Procedure

1. Map the journey, user roles, and loading, empty, success, error, and unavailable states.
2. Keep presentation and journey orchestration in the interface. Identify rules that must be enforced on the server and domain contracts the interface should consume.
3. For block or modal issues, identify input parameters, events, parent handlers, state ownership, and the completion condition. Do not assume changing a parameter automatically closes a modal or finishes processing.
4. Examine input validation, actionable messages, keyboard navigation, labels, and focus. Do not claim accessibility compliance without evaluation.
5. Review data fetching, pagination, redundant requests, and repeated submissions. Do not treat Reactive, Traditional, and Mobile mechanisms as interchangeable.
6. Review client-side data and state exposure; authorization must be checked on the server. For offline Mobile, confirm synchronization and conflict handling before recommending a solution.

## Deliverable

Reviewed journey, state transitions and ownership, client/server boundary, required contracts, and acceptance criteria.

Link findings to inspected evidence. Separate facts, inferences, and missing information. Cite official documentation for specific capabilities when available; never invent links or line numbers. Explain unfamiliar terms when needed. Respond in the user's requested language.

Propose actions within the request's scope. This skill does not grant access or authorize unrelated edits or deployments.

## Example request

For O11, first verify the configured Service Studio MCP connection and the open target module. Inspect available evidence with read tools; do not edit or publish for this example.

Review a fictional OutSystems 11 / Reactive Web order approval journey.

After successful approval, `OrderApprovalDialog` should stop loading, close,
and refresh the order summary. On failure, it should stop loading, stay
open, and display an actionable error. Review state ownership, the
`ApprovalCompleted` event, and its parent handler using the supplied flows.
Preserve public contracts and business rules; define acceptance criteria
before recommending changes.
