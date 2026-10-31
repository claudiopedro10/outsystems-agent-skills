---
name: outsystems-troubleshooting
description: "Investigate OutSystems errors and unexpected behavior using symptoms, logs, and reproduction evidence before selecting a cause or correction."
---

# Troubleshooting

## Scope and context

Confirm OutSystems 11 or ODC, the known version, application type, objective, and constraints. Foundation/Core/End User uses O11 as its reference. Adapt for ODC only with applicable evidence and documentation; do not transfer tool names or capabilities automatically.

Use supplied inventories, contracts, snippets, screenshots, or sanitized logs, or inspect them through authorized tools. Do not assume platform access or an OML/OAP reader. Ask only for information that changes the analysis.

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

1. Capture the module/application, related elements, observed behavior, expected behavior, reproduction steps, onset, frequency, and recent changes. Accept unknown fields; ask only for missing details that affect diagnosis.
2. For loading and modal issues, trace processing start, the completion condition, block inputs, emitted events, parent handlers, and assignments controlling loading and visibility. Establish element types and state ownership from evidence rather than identifiers.
3. Correlate evidence by time, operation, and sanitized identifiers. Use supplied Service Center evidence for O11; confirm the available observability tools for ODC.
4. Prioritize hypotheses with supporting evidence, contradictory evidence, and the next check that would distinguish them. A parameter change or timing correlation alone does not establish a cause.
5. Prefer read-only inspection and isolated reproduction. Do not repeat operations with financial or persistent effects without understanding idempotency.
6. Once evidence supports a likely cause, propose a focused correction, impact, rollback, and regression checks. Preserve stated components, contracts, and business rules. If a necessary change conflicts with a constraint, explain that conflict before proceeding.
7. When evidence is insufficient, request targeted action flows, event wiring, or state observations instead of inventing a fix. Explain the next check in terms a developer new to AI can follow.

## Deliverable

Expected/observed summary, inspected evidence, prioritized hypotheses, targeted next checks, and a correction only when justified. Include validation of success, error, cancellation, and repeated execution when relevant.

Link findings to inspected evidence. Separate facts, inferences, and missing information. Cite official documentation for specific capabilities when available; never invent links or line numbers. Explain unfamiliar terms when needed. Respond in the user's requested language.

Propose actions within the request's scope. This skill does not grant access or authorize unrelated edits or deployments.

## Example request

For O11, first verify the configured Service Studio MCP connection and the open target module. Inspect available evidence with read tools; do not edit or publish for this example.

Fictional scenario: OutSystems 11 / Reactive Web.

- Module: `PurchaseOrders_UI`
- Block: `OrderApprovalDialog`
- Action: `SubmitApproval`
- Completion event: `ApprovalCompleted`

The order is approved, but loading stays active and the dialog remains open.
Trace the success path, event handling, and state ownership using the
provided evidence. Preserve existing business rules and public contracts.
Propose a focused correction plan and checks for success, failure, and
repeated use. Request missing action flows before selecting a cause.
