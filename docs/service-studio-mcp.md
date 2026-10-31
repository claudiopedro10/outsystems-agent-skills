# Connect the Service Studio MCP server (OutSystems 11)

This guide describes the **local OutSystems 11 Service Studio MCP server**.
It connects a supported AI agent to the module open in Service Studio. The
skills in this repository add task-specific guidance; they do not install
the server, register a connection, or replace OutSystems' official O11 MCP
skill. ODC uses different capabilities; consult its own documentation.

## Before you start

- Service Studio 11.55.91 or later, running with the target module open.
- An AI agent or host that supports MCP, with any required account access.
- The [official OutSystems O11 MCP skill](https://github.com/OutSystems/outsystems11-mcp),
  installed for your agent using the official setup instructions.
- The relevant skill from this repository installed or loaded in your agent.

The version requirement and setup are documented in
[Get started with OutSystems MCP](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/).
The official skill supplies the Model API contract and tool instructions.

### Recommended order

1. Follow the [official OutSystems O11 MCP setup](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/) and install its official skill for your agent.
2. Start the Service Studio MCP Server and open the target module.
3. Register the address shown in Service Studio in your agent.
4. Approve the connection when prompted and verify a read of the open module.
5. Load one of this repository's complementary skills for your task.

These repository skills do not replace the official skill or configure the
connection. Manual analysis with supplied evidence remains available without
MCP. For ODC, follow the applicable ODC documentation and tools.

## 1. Start the server

1. Open the target module in Service Studio.
2. Choose **Edit > MCP Server**. Menu wording may vary by version.
3. Start the server and confirm the status is **Running**.
4. Copy the URL shown in that window. It has the form:

```text
http://127.0.0.1:<PORT>/mcp
```

Replace `<PORT>` with the port shown in your own Service Studio window.
For example, `41820` may be shown, but it is not a required fixed port.
If you change the port, update the agent's configuration to match.

## 2. Register the endpoint in your agent

An MCP host is the application that runs the agent and connects it to tools.
Register the URL copied from Service Studio in the MCP settings of that
host. Follow the current [official O11 setup instructions](https://github.com/OutSystems/outsystems11-mcp)
for your particular host; each host uses its own configuration.

- **Codex:** follow the [official Codex setup](https://github.com/OutSystems/outsystems11-mcp/blob/main/setup-docs/codex.md).
- **Claude Code and other supported hosts:** use the host-specific directions
  linked from the official repository.
- **DeepSeek, Gemini, Kimi, ChatGPT, or another interface:** support depends on
  the actual client, version, and account, not merely the model name. Check
  that the client can connect to an MCP server and follow its setup.
- **Chat without MCP:** paste the repository skill instructions and supply
  sanitized evidence. The chat cannot inspect the open module through MCP
  unless its client is separately configured with access to it.

`127.0.0.1` refers to the machine where the MCP client runs. A cloud or
remote agent cannot assume that address reaches Service Studio on the
developer's computer. Use a supported connection arrangement appropriate to
the host; this guide does not prescribe exposing the local server.

## 3. Approve and verify

1. Start or restart the agent session as required by your host.
2. If Service Studio asks whether to allow the agent to connect, approve the
   session if you intend to use it.
3. Ask the agent:

```text
Use the configured Service Studio MCP tools to summarize the module
currently open. Report the module name and the evidence you inspected.
Do not change, merge, or publish anything.
```

4. Confirm the reported module name and content against Service Studio. A
   generic response or a claim that tools exist is not proof of a successful
   module read.
5. Load the appropriate Foundation, Core, End User, Architecture,
   Troubleshooting, or Security skill and submit a task using the
   [request template](request-template.md).

## Permissions and troubleshooting

For analysis, ask the agent to use read operations only. For intended edits,
review Service Studio's **Write permissions** and the proposed changes;
manual Compare and Merge lets the developer review changes. Publishing is
a separate action and must follow the developer's instructions.

If the connection fails, check that the server is running, the registered
URL matches the displayed port, the agent has MCP support, and any session
approval has been granted. If the agent cannot find a module, open the
correct module and retry. If unavailable, ask for a manual analysis based on
sanitized screenshots or excerpts; do not represent it as an MCP inspection.

Official documentation: [Get started with OutSystems MCP](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/)
and [OutSystems O11 MCP skill and host setup](https://github.com/OutSystems/outsystems11-mcp).
