# OutSystems Agent Skills

**Reusable AI skills for OutSystems architecture, development, and troubleshooting.**

A publicly available skill library maintained by the repository owner for developers, technical leads, and architects. Each skill is a Markdown file that gives an AI assistant a focused workflow and review criteria.

## New to AI? Start here

You do not need to write a complex prompt or configure an API.

1. Choose a skill from the table below.
2. Open its `SKILL.md` file and copy the contents.
3. Paste them into your AI conversation, or attach the file if your application supports it.
4. Send a request using the [guided request template](docs/request-template.md).
5. Review the proposed analysis and verify changes in a development environment.

For a complete walkthrough, read [Using skills for the first time](docs/usage.md). For installation in a coding agent, read [Agent setup](docs/agents.md).

## Why use these skills?

- **More useful context:** describe the affected module, elements, symptoms, and constraints.
- **Consistent analysis:** ask the assistant to separate evidence from assumptions.
- **Clear responsibilities:** review Foundation, Core, and End User boundaries.
- **Reviewable recommendations:** understand the proposed change, its impact, and how to validate it.
- **Reusable instructions:** use the same workflow across supported agents or manually in a chat.

Skills guide an assistant; they do not automatically connect to Service Studio, read OML/OAP files, or deploy applications. Access depends on the tools and permissions available to the assistant.

## Choose a skill

| Your task | Skill |
| --- | --- |
| Review an external integration or reusable technical capability | [Foundation](skills/outsystems-foundation/SKILL.md) |
| Model entities, business rules, and domain services | [Core](skills/outsystems-core/SKILL.md) |
| Review screens, user journeys, and interface states | [End User](skills/outsystems-enduser/SKILL.md) |
| Review responsibilities, dependencies, or cycles | [Architecture](skills/outsystems-architecture/SKILL.md) |
| Investigate an error or unexpected behavior | [Troubleshooting](skills/outsystems-troubleshooting/SKILL.md) |
| Review authentication, authorization, or sensitive data handling | [Security](skills/outsystems-security/SKILL.md) |

If a loading indicator remains active and a modal does not close, start with **Troubleshooting**. Use **End User** if the investigation needs a broader review of interface states.

## Example request

After loading the Troubleshooting skill, send:

```text
Use outsystems-troubleshooting.

Platform and application type: Not yet confirmed.
Module: 123456_WB_ACESSWEB
Related elements: WB_CheckProcess and BlockTESTDETAILS
Identified issue: The loading indicator remains active and the modal does not close.
Current behavior: Changing the block parameters does not trigger the expected completion behavior.
Expected behavior: When processing completes, the loading indicator should stop and the modal should close according to the functional rule.
Constraints: Preserve existing components, contracts, and business rules.

First identify the missing evidence needed to trace the completion flow.
Separate confirmed facts from hypotheses. Propose the smallest justified
change and explain how to validate it. Do not edit or publish anything yet.
```

These names are illustrative identifiers, not files inspected by this project. See the [complete walkthrough](examples/loading-and-modal.md) for what to provide next and what a useful response should contain.

## Platform scope

The Foundation/Core/End User organization uses the OutSystems 11 Architecture Canvas as a reference. ODC requires explicit adaptation to its applications, libraries, and available capabilities. O11 tools and mechanisms must not be assumed to exist unchanged in ODC.

## Documentation

- [First-time usage guide](docs/usage.md)
- [Request template and field explanations](docs/request-template.md)
- [Claude, Codex, Gemini, DeepSeek, Kimi, and other agents](docs/agents.md)
- [Loading indicator and modal walkthrough](examples/loading-and-modal.md)
- [Architecture review example](examples/architecture-review.md)
- [Skill structure and quality criteria](docs/skill-design.md)
- [Official sources](docs/sources.md)
- [Roadmap](ROADMAP.md)
- [Repository maintenance policy](CONTRIBUTING.md)
- [Security and data handling](SECURITY.md)

## Project status

Initial edition with six starter skills. File structure and internal links are checked; execution has not been validated across every agent or OutSystems scenario. No productivity benchmark or compatibility certification is claimed.

Repository documentation and skill instructions are maintained in English. Users may write requests and ask for responses in their preferred language.

## Repository access

You may read, download, and use the skills. External contributions are not accepted: issues, pull requests, discussions, wiki editing, and repository projects are disabled. Updates to this original repository are reserved for the owner and explicitly authorized maintainers. See the [maintenance policy](CONTRIBUTING.md).

Public files and their commit history are visible to everyone. GitHub allows independent forks and downloads of public repositories; these do not grant write access to this repository.

Licensed under [MIT](LICENSE). This is an independent community project, with no affiliation with or endorsement by OutSystems or the AI vendors. Product names belong to their respective owners.
