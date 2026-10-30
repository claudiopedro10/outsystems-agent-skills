---
name: outsystems-enduser
description: "Review OutSystems screens, user journeys, and interface states in the End User layer; account for application type and adapt explicitly for ODC."
---

# End User

## Scope and context

Confirm OutSystems 11 or ODC, the known version, application type, objective, and constraints. Foundation/Core/End User uses O11 as its reference. Adapt for ODC only with applicable evidence and documentation; do not transfer tool names or capabilities automatically.

Use supplied inventories, contracts, snippets, screenshots, or sanitized logs, or inspect them through authorized tools. Do not assume platform access or an OML/OAP reader. Ask only for information that changes the analysis.

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

> Review a processing modal where changing block parameters does not stop loading or close the modal. Confirm the platform and trace completion and parent handlers before proposing changes.
