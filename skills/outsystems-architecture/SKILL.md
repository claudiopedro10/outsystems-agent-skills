---
name: outsystems-architecture
description: "Review OutSystems responsibilities, dependencies, and cycles using the O11 Architecture Canvas; avoid automatic equivalence with ODC."
---

# Architecture

## Scope and context

Confirm OutSystems 11 or ODC, the known version, application type, objective, and constraints. Foundation/Core/End User uses O11 as its reference. Adapt for ODC only with applicable evidence and documentation; do not transfer tool names or capabilities automatically.

Use supplied inventories, contracts, snippets, screenshots, or sanitized logs, or inspect them through authorized tools. Do not assume platform access or an OML/OAP reader. Ask only for information that changes the analysis.

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

> Analyze Orders_UI -> Orders_CS -> ERP_IS -> Orders_UI in O11. Explain how to investigate and remove the cycle.
