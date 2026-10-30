# Walkthrough: loading indicator stays active and modal does not close

This teaching example uses the identifiers supplied for the request format. No application source, action flow, or runtime evidence has been inspected. It demonstrates how to ask for help, not a verified diagnosis.

## 1. Load the Troubleshooting skill

Copy [outsystems-troubleshooting/SKILL.md](../skills/outsystems-troubleshooting/SKILL.md) into your conversation, attach it, or use your agent's installed invocation.

## 2. Send the request

```text
Use outsystems-troubleshooting.

Platform: Unknown.
Application type: Unknown.
Module: 123456_WB_ACESSWEB
Related elements: WB_CheckProcess and BlockTESTDETAILS
Identified issue: The loading indicator remains active and the modal does not close.
Current behavior: Changing the block parameters does not trigger the expected completion behavior.
Expected behavior: When processing completes, the loading indicator should stop and the modal should close according to the functional rule.
Constraints: Preserve existing components, contracts, and business rules.
Evidence available: Behavior description only.
Requested help: Investigate the completion flow and propose the smallest
justified correction. Explain the reasoning and validation steps.
Do not edit or publish anything yet.
```

Replace unknown fields when you know them. Do not infer an element's type or behavior from its name.

## 3. Provide the evidence needed next

A useful assistant should first request the smallest set of evidence that can distinguish possible causes:

- The actual platform and application type.
- The role of each named element and its parent/consumer relationship.
- The action that starts processing and sets the loading state.
- The condition that means processing is complete.
- The logic that clears loading and controls modal visibility.
- Relevant block inputs, events, and parent handlers.
- Reproduction steps and whether the issue affects success, errors, or both.

Send labeled screenshots or logic excerpts for these paths. If an item is unavailable, say so. Do not include live credentials or customer data.

## 4. Expect a grounded analysis

A useful initial response might say:

> The reported symptom is that the completion behavior does not occur after block parameters change. The evidence does not yet establish whether processing completed, whether a completion event was raised and handled, or whether loading and modal visibility have different owners. Please provide the processing completion path and the related state/event handling before choosing a fix.

Possible investigation questions include:

| Question | Evidence to inspect | Why it matters |
| --- | --- | --- |
| Does processing actually reach completion? | Completion condition and observed result | The interface may still be waiting for work |
| Does execution reach the completion handler? | Event wiring and parent action flow | A missing or unhandled signal could interrupt the path |
| Where are loading and modal visibility controlled? | State assignments and owning elements | Two states may be updated by different logic |
| What happens on failure or cancellation? | Error and cancellation paths | A path may leave loading active |
| What happens on a second execution? | Reproduction with repeated use | Stale state may affect later attempts |

These are questions, not confirmed causes. A parameter change alone does not prove that the correct completion path ran. Do not add lifecycle hooks or alter contracts without verifying the platform and implementation.

## 5. Review the proposed correction

Ask the assistant to identify:

- The specific element and path to change.
- The evidence supporting that change.
- How existing components, contracts, and rules remain preserved.
- Any remaining uncertainty.
- How to validate the change and revert it if necessary.

If the evidence shows that a required correction conflicts with your constraints, the assistant should explain the conflict before proceeding.

## 6. Validate in development

Check the actual functional rule:

1. Start processing and confirm the loading state.
2. Complete processing successfully and verify that loading stops.
3. Verify that the modal closes only under the intended completion condition.
4. Exercise failure and cancellation paths according to their existing rules.
5. Repeat the flow and check that state resets correctly.
6. Confirm that unrelated consumers and existing contracts still work.

No fix is claimed by this example. A correction requires the missing implementation evidence and successful validation.
