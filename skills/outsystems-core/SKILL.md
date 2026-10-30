---
name: outsystems-core
description: "Model or review entities, invariants, and domain services in OutSystems Core; explicitly adapt O11 concepts for ODC."
---

# Core

## Scope and context

Confirm OutSystems 11 or ODC, the known version, application type, objective, and constraints. Foundation/Core/End User uses O11 as its reference. Adapt for ODC only with applicable evidence and documentation; do not transfer tool names or capabilities automatically.

Use supplied inventories, contracts, snippets, screenshots, or sanitized logs, or inspect them through authorized tools. Do not assume platform access or an OML/OAP reader. Ask only for information that changes the analysis.

## Procedure

1. Identify the domain, data owner, invariants, and consumers. Separate lasting business rules from presentation decisions.
2. Define service inputs, outputs, and preconditions/postconditions. Prefer a focused business contract over broad write access when appropriate.
3. Examine server-side authorization, transactions, concurrency, and repeated execution. Hiding a button does not enforce a business rule.
4. Assess existing data, nullability, indexes, and consumers before proposing entity changes. Explain migration and rollback where applicable.
5. Do not claim atomicity across a database and an external service without evidence. Explain how inconsistencies would be detected and reconciled.

## Deliverable

Domain model, invariants, contracts, migration risks, and positive, negative, and concurrent validation scenarios.

Link findings to inspected evidence. Separate facts, inferences, and missing information. Cite official documentation for specific capabilities when available; never invent links or line numbers. Explain unfamiliar terms when needed. Respond in the user's requested language.

Propose actions within the request's scope. This skill does not grant access or authorize unrelated edits or deployments.

## Example request

> Review ApproveOrder(OrderId): only pending orders may be approved and the actor must be recorded. Consider simultaneous approvals.
