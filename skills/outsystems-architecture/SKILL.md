---
name: outsystems-architecture
description: "Review OutSystems responsibilities, dependencies, and cycles using the O11 Architecture Canvas; avoid automatic equivalence with ODC."
---

# Architecture

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

1. Inventory actual modules/applications, responsibilities, public elements, and observed dependencies.
2. In O11, use Foundation for technical capabilities, Core for business concepts/services, and End User for journeys and interfaces. Classify by content, not names or suffixes.
3. Trace consumers and providers. Look for cycles and dependencies from lower layers to End User. Assess peer dependencies by responsibility and coupling.
4. Do not impose one consumption chain for every scenario. Evaluate the contract and context before labeling a dependency inappropriate.
5. Propose the smallest coherent change and assess consumers, contracts, and data. Use incremental migration when compatibility needs to be preserved.
6. For ODC, describe the actual application/library organization and verify boundaries and mechanisms in the corresponding documentation.

## Deliverable

Classified inventory, textual dependency graph, evidence-backed findings, incremental proposal, and compatibility checks.

Link findings to inspected evidence. Separate facts, inferences, and missing information. Cite official documentation for specific capabilities when available; never invent links or line numbers. Explain unfamiliar terms when needed. Respond in the user's requested language.

Propose actions within the request's scope. This skill does not grant access or authorize unrelated edits or deployments.

## Example request

For O11, first verify the configured Service Studio MCP connection and the open target module. Inspect available evidence with read tools; do not edit or publish for this example.

> Analyze Orders_UI -> Orders_CS -> ERP_IS -> Orders_UI in O11. Explain how to investigate and remove the cycle.
