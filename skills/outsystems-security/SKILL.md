---
name: outsystems-security
description: "Review authentication, authorization, and data handling in an OutSystems flow using evidence; this is not a complete audit or certification."
---

# Security

## Scope and context

Confirm OutSystems 11 or ODC, the known version, application type, objective, and constraints. Foundation/Core/End User uses O11 as its reference. Adapt for ODC only with applicable evidence and documentation; do not transfer tool names or capabilities automatically.

Use supplied inventories, contracts, snippets, screenshots, or sanitized logs, or inspect them through authorized tools. Do not assume platform access or an OML/OAP reader. Ask only for information that changes the analysis.

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

> Review order access when a user can change OrderId in a request. Evaluate the supplied server-side checks.
