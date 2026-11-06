# Sources and maintenance

Documentation review date: **November 6, 2026**. These links support platform concepts and setup locations. They do not imply vendor endorsement or execution of every example.

## OutSystems

- [Architecture Canvas — OutSystems 11](https://success.outsystems.com/documentation/11/app_architecture/designing_the_architecture_of_your_outsystems_applications/the_architecture_canvas/): reference for Foundation, Core, and End User.
- [Official documentation](https://success.outsystems.com/documentation/): confirm capabilities for the applicable platform and version.

- [Get started with OutSystems MCP (O11)](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/): prerequisites, local server, agent setup, and verification.
- [Official OutSystems O11 MCP skill and host setup](https://github.com/OutSystems/outsystems11-mcp): agent instructions and host-specific setup.
- [ODC: Use MCP servers](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/build_ai_powered_apps/agentic_apps_in_odc/tools_and_connectors/use_mcp_servers/): consuming external MCP tools in ODC agentic apps; not a setup guide for an external coding agent to edit ODC or O11 applications.

The Architecture Canvas reference is for O11. This library does not assume the same organization or mechanisms in ODC. Cite the corresponding ODC documentation when making platform-specific recommendations.

## Agents

- [Codex: Build skills](https://learn.chatgpt.com/docs/build-skills): structure, discovery, and directories.
- [GitHub Copilot: Add agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills): project skill directories and discovery.
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills): project folders and invocation.
- [Claude: Custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): upload and interface usage.
- [Gemini CLI: Agent Skills](https://geminicli.com/docs/cli/skills/): discovery, activation, and commands.
- [Kimi Code: Agent Skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html): locations and invocation.
- [DeepSeek: Chat Completions API](https://api-docs.deepseek.com/api/create-chat-completion/): message reference for API users, not a skill installation specification.

## Maintenance

Check the official source and record the date when changing setup instructions. If an interface has not been verified, offer the manual method and explain the limit. A documentation review is not an execution test.

## Audit snapshot

The O11 MCP comparison used the official repository at commit
[`8f36d5a`](https://github.com/OutSystems/outsystems11-mcp/tree/8f36d5ad38bb57e34e3078f882f0909ee5650cda).
The skill's merge/publication workflow, follow-up verification, and known
module-identity limits informed the complementary guidance. Tool schemas and
Model API contracts remain owned by that official project; recheck the
installed version before execution. See the [audit record](audits/2026-11-06.md)
for scope and limitations.
