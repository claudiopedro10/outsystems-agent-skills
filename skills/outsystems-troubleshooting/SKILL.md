---
name: outsystems-troubleshooting
description: "Investigate OutSystems errors and unexpected behavior using symptoms, logs, and reproduction evidence before selecting a cause or correction."
---

# Troubleshooting

## Scope and context

Confirm OutSystems 11 or ODC, the known version, application type, objective, and constraints. Foundation/Core/End User uses O11 as its reference. Adapt for ODC only with applicable evidence and documentation; do not transfer tool names or capabilities automatically.

Use supplied inventories, contracts, snippets, screenshots, or sanitized logs, or inspect them through authorized tools. Do not assume platform access or an OML/OAP reader. Ask only for information that changes the analysis.

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

> Module: 123456_WB_ACESSWEB. Related elements: WB_CheckProcess and BlockTESTDETAILS. Loading remains active and the modal does not close after block parameters change. Preserve components, contracts, and rules. Ask for the missing completion-flow evidence before selecting a cause.
