# Example: a dependency cycle between integration and interface

Synthetic scenario; illustrative analysis, not an execution test against a real application.

## Input

OutSystems 11 / Reactive Web.

- Target module: Orders_UI (starting point for the cross-module review).
- Application: Unknown.
- Open modules: Unknown; no MCP read has been performed.
- Related modules: Orders_CS, ERP_IS, Shared_UI (reported inventory).

- Orders_UI: screens. Architecture layer: End User.
- Orders_CS: order rules and entities. Architecture layer: Core.
- ERP_IS: REST integration with an ERP. Architecture layer: Foundation.
- Shared_UI: visual components. Architecture layer: Not sure; assess responsibilities.
- Reported dependencies: Orders_UI -> Orders_CS -> ERP_IS -> Orders_UI.

Skill: `outsystems-architecture`.

For a real O11 review, verify the [Service Studio MCP setup](../docs/service-studio-mcp.md) and inspect the available open module using read tools. Confirm other modules separately when available; do not infer their contents from one open module. This example supplies a synthetic inventory and is not an MCP result.

## Expected analysis

**Evidence:** the supplied dependency directions form a cycle. ERP_IS depends on an interface consumer.

**Interpretation:** Orders_UI belongs to End User; Orders_CS represents Core; ERP_IS represents Foundation. Shared_UI requires inspection to establish whether its components are technical or contain business behavior. Suffixes do not prove responsibility.

**Proposal:** identify the element ERP_IS consumes from Orders_UI. For a data contract, evaluate moving it to its appropriate owner and updating consumers. For a visual notification, return a technical result and let the interface decide presentation. Inspect semantics before moving a whole flow.

**Sequence:** inventory the shared element; define a compatible contract; update ERP_IS and its consumers; remove the reverse dependency; validate the user flow and regressions.

**Validation:** the updated graph no longer contains the cycle; valid orders and ERP failures remain handled; screens do not receive ERP implementation details.

**Missing information:** no actual actions, contracts, references, or metrics were supplied. Classification is preliminary. Performance impact and final compatibility cannot be established.
