# Using skills for the first time

## What is a skill?

A **prompt** is the request you send to an AI assistant. A **skill** is a reusable set of instructions that guides how the assistant handles a category of requests. An **agent** is an application that may also read files or use tools.

A skill supplies a workflow, not knowledge of your application. The assistant still needs your module names, relevant logic, expected behavior, and evidence.

## Step 1: Choose one skill

Use Troubleshooting for a bug, Architecture for dependencies, Core for business rules, Foundation for integrations, End User for screens, or Security for access and data handling.

Start with one skill. Add another only when its scope helps the task.

## Step 2: Load the instructions

The simplest method works in a chat:

1. Open the selected `SKILL.md` from the repository.
2. Copy its full text into a new conversation, or attach the file if supported.
3. Say: “Use these instructions for the task I will describe next.”

If you use a coding agent, follow [Agent setup](agents.md) instead. A GitHub link alone may not be readable by your assistant. If it cannot open the file, provide the contents directly.

## Connect to Service Studio (OutSystems 11)

To analyze the actual open module, follow the
[Service Studio MCP setup guide](service-studio-mcp.md). It covers the
official OutSystems O11 MCP skill, starting the local server, registering
the URL displayed by your Service Studio, session approval, and a read-only
connection test. Each developer's port can differ.

A copied instruction file does not establish an MCP connection. If the
agent cannot access the configured tools, supply sanitized screenshots or
excerpts and treat the result as an analysis of those materials only.

## Step 3: Describe your task

Copy the [request template](request-template.md), replace its example values, and remove fields that do not apply. Write “Unknown” when information is unavailable.

Include:

- The platform and application type, if known.
- The architecture layer: Foundation, Core, End User, or Not sure.
- The affected module and elements.
- What happens now and what should happen instead.
- The steps that reproduce the issue.
- Constraints and relevant evidence.

A request such as “Fix my modal” does not identify the logic or expected completion rule. The [order approval walkthrough](../examples/loading-and-modal.md) shows how to make that request actionable.

Use the layer descriptions in the [request template](request-template.md).
For several modules, identify each module's layer. Ask the assistant to
check responsibilities rather than assuming that the declared layer is
correct. In ODC, use Not applicable when the O11 classification does not fit.

## Step 4: Inspect the module or supply evidence

For O11, ask the connected agent to verify the open target module and use the available Service Studio MCP read tools. If those tools are unavailable, provide relevant evidence manually.

For a screen issue, useful evidence may include block inputs, events and handlers, the action that starts processing, the completion path, and the values controlling loading and modal visibility.

For an integration issue, provide a sanitized contract, response status, timing, and relevant logs. For architecture, provide responsibilities and dependency directions.

Label each screenshot or snippet with its element name. Do not upload an entire client project when a small sanitized excerpt is enough. This library does not provide an OML/OAP reader; confirm the assistant's capabilities before attaching exports.

## Step 5: Review the response

A useful answer should:

- Summarize the expected and observed behavior accurately.
- Identify which evidence was actually inspected.
- Separate confirmed facts, hypotheses, and missing information.
- Explain a targeted next check or a justified change.
- Describe effects on existing components and contracts.
- Provide validation steps.

If the answer invents an action or assumes your platform, ask it to correct the assumption before proceeding.

## Step 6: Apply and validate deliberately

If you requested analysis only, review the recommendation before asking for implementation. Apply an accepted change in development and check the expected behavior, error paths, cancellation, and repeated execution as relevant.

Do not treat a confident explanation as proof. For the order approval example, verify that approval completes, loading stops, the dialog closes, and the summary refreshes. On failure, confirm that the dialog remains open with an actionable error.

## Useful follow-up requests

```text
Which statements are confirmed by the evidence I provided?
What is the smallest additional screenshot or action flow you need?
Explain the proposed change in Service Studio terms for a beginner.
How can I verify this without changing an existing contract?
List the regression checks before I apply the change.
```

## Data and language

Remove passwords, tokens, session cookies, personal data, and confidential client details. Use synthetic identifiers where appropriate.

The repository is written in English. You may describe your task in another language and ask the assistant to respond in that language.
