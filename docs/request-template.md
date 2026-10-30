# Write a clear request

Use this template after loading a skill. You do not need to know the root cause. Describe what you can observe and mark unknown information explicitly.

## Copy and adapt

```text
Skill: [selected skill name]
Platform: [OutSystems 11, ODC, or Unknown]
Application type: [Reactive Web, Traditional Web, Mobile, or Unknown]
Module or application: [affected name]
Related elements: [screens, blocks, actions, events, or entities]
Identified issue or objective: [one-sentence summary]
Current behavior: [what happens now]
Expected behavior: [what should happen and under which condition]
Steps to reproduce: [short sequence]
Evidence available: [sanitized screenshots, logic, logs, or contracts]
Constraints: [what must be preserved]
Requested help: [analysis, explanation, implementation plan, or authorized edits]

Identify missing evidence before selecting a cause.
Separate facts from hypotheses, explain the proposed change,
and provide validation steps. Preserve the stated constraints.
```

In ODC, describe the relevant application or library rather than inventing an O11 module structure. For a new feature, replace “Current behavior” with the existing flow or state that no implementation exists yet.

## What each field means

| Field | What to provide | Why it helps |
| --- | --- | --- |
| Skill | The workflow you selected | Sets the scope of the analysis |
| Platform | O11, ODC, or Unknown | Avoids incompatible platform advice |
| Application type | The type you actually use | Avoids mixing lifecycle and UI mechanisms |
| Module or application | Exact affected identifier | Locates the scope without guessing |
| Related elements | Names and roles, when known | Connects the request to specific logic |
| Issue or objective | A concise symptom or goal | States the task clearly |
| Current behavior | Observed results, not a presumed cause | Keeps diagnosis grounded |
| Expected behavior | Outcome and functional condition | Defines success |
| Steps to reproduce | Starting state, actions, and result | Makes the behavior repeatable |
| Evidence | Labeled excerpts or screenshots | Enables a traceable explanation |
| Constraints | Contracts, components, or rules to preserve | Prevents an unnecessarily broad change |
| Requested help | What the assistant should deliver or do | Distinguishes explanation from implementation |

Names alone do not reveal an element's implementation or type. If you do not know whether an element is a block, action, or event handler, say so and provide a screenshot.

## Example: loading indicator and modal

```text
Skill: outsystems-troubleshooting
Platform: Unknown; confirm before giving platform-specific steps.
Application type: Unknown.
Module: 123456_WB_ACESSWEB
Related elements: WB_CheckProcess and BlockTESTDETAILS
Identified issue: The loading indicator remains active and the modal does not close.
Current behavior: Changing the block parameters does not trigger the expected completion behavior.
Expected behavior: When processing completes, the loading indicator should stop and the modal should close according to the functional rule.
Constraints: Preserve existing components, contracts, and business rules.
Evidence available: Behavior description only; no action flow or screenshots supplied yet.
Requested help: Identify the evidence needed, investigate the completion flow,
and propose the smallest justified correction with validation steps.
Do not edit or publish anything yet.
```

The platform, element roles, and implementation are intentionally not invented. Add them when known. Follow the [walkthrough](../examples/loading-and-modal.md) to continue the investigation.
