---
name: outsystems-foundation
description: "Design or review external integrations and reusable technical capabilities in OutSystems Foundation; explicitly adapt O11 guidance for ODC."
---

# Foundation

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

1. Map the external system, operation, contract, authentication, limits, timeouts, retries, and error ownership.
2. Separate technical adaptation from business decisions. Do not move approval, pricing, or domain policy into an adapter for convenience.
3. Examine idempotency, duplicate requests, pagination, outages, and contract changes. Recommend automatic retries only for transient failures and operations safe to repeat.
4. Identify where credentials are resolved and who can access them. Keep secrets out of URLs, responses, and logs.
5. Define a minimal public contract, error mapping, and consumer impact. Verify platform-specific settings in official documentation before naming them.

## Deliverable

Proposed contract, responsibilities, failure handling, consumer impact, and validation scenarios.

Link findings to inspected evidence. Separate facts, inferences, and missing information. Cite official documentation for specific capabilities when available; never invent links or line numbers. Explain unfamiliar terms when needed. Respond in the user's requested language.

Propose actions within the request's scope. This skill does not grant access or authorize unrelated edits or deployments.

## Example request

For O11, first verify the configured Service Studio MCP connection and the open target module. Inspect available evidence with read tools; do not edit or publish for this example.

> Review an ERP order-creation integration that times out after sending. We do not know whether the ERP created the order. Investigate how to prevent duplicates.
