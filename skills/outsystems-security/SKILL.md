---
name: outsystems-security
description: "Review authentication, authorization, and data handling in an OutSystems flow using evidence; this is not a complete audit or certification."
---

# Security

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

1. Identify actors, data, trust boundaries, and privileged operations.
2. Trace login, session handling, and protected requests using the actual mechanisms. Check server-side authorization for each operation and resource.
3. Map credential and token origin, storage, access, transport, expiry, renewal, revocation, and logout. Record unseen aspects as missing information.
4. Check exposure through logs, URLs, client state, and responses. Assess parameterized queries and input validation using the available artifacts.
5. For integrations, assess least privilege, rotation, and authentication failures. Do not assume O11 and ODC share identity mechanisms or settings.
6. Prioritize findings by impact and exploitability without declaring a vulnerability unsupported by evidence. Suggest authorized validation; do not initiate invasive testing.

## Deliverable

Trust flow, credential/token map, supported findings, missing information, and positive and negative authorization checks.

Link findings to inspected evidence. Separate facts, inferences, and missing information. Cite official documentation for specific capabilities when available; never invent links or line numbers. Explain unfamiliar terms when needed. Respond in the user's requested language.

Propose actions within the request's scope. This skill does not grant access or authorize unrelated edits or deployments.

## Example request

For O11, first verify the configured Service Studio MCP connection and the open target module. Inspect available evidence with read tools; do not edit or publish for this example.

> Review order access when a user can change OrderId in a request. Evaluate the supplied server-side checks.
