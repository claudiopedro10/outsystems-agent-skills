# Agent setup

You can use the skills manually without installing anything. Native skill discovery depends on the application, not just the model name.

Documentation checked on **October 30, 2026**. Procedures are based on [official sources](sources.md); they have not been executed in every product.

## Choose your setup

| Application | Method described here | Check |
| --- | --- | --- |
| Codex | Skill folder in .agents/skills | Available in a new session |
| Claude Code | Skill folder in .claude/skills | /outsystems-architecture |
| Gemini CLI | Skill folder in .gemini/skills | Skill list and activation |
| Kimi Code | Skill folder in .agents/skills | /skill:outsystems-architecture |
| DeepSeek chat | Paste skill instructions | Confirm received context |
| Other chats | Paste or attach instructions | Confirm received file or text |

The Architecture skill is used below as an example. Replace its folder and name with Troubleshooting or another skill when appropriate.

## Download the library

Download the repository using GitHub's **Code > Download ZIP**, then extract it. Developers who use Git can run:

```sh
git clone https://github.com/claudiopedro10/outsystems-agent-skills.git
```

The downloaded library is the source. Your working project is where you want the agent to use a skill. Copy a complete skill folder from the source into the destination described below. Do not overwrite an existing skill without reviewing it.

## Codex

Copy `skills/outsystems-architecture/` into `.agents/skills/` in your working project:

```text
your-project/
  .agents/
    skills/
      outsystems-architecture/
        SKILL.md
```

Open a new Codex session in that project and send:

```text
Use $outsystems-architecture to review the dependencies below.
Platform: OutSystems 11.
[Add your context and evidence.]
```

The documented personal location is `~/.agents/skills/`. Here, `~` means your user home directory. In a remote environment, the folder must exist where Codex runs.

## Claude Code

Copy the skill folder into `.claude/skills/` in your working project:

```text
.claude/skills/outsystems-architecture/SKILL.md
```

Start a session in that project and send:

```text
/outsystems-architecture
Review the dependencies below. Platform: OutSystems 11.
[Add your context and evidence.]
```

Personal installations use `~/.claude/skills/`. A local Claude Code installation does not automatically make the skill available in a browser or cloud session.

### Claude in the browser

Use the manual method below. If custom skills are available for your account, follow Anthropic's official upload and packaging instructions linked in [Sources](sources.md).

## Gemini CLI

Copy the skill folder into `.gemini/skills/` in your project:

```text
.gemini/skills/outsystems-architecture/SKILL.md
```

Start a session and ask:

```text
Use the outsystems-architecture skill to review this inventory.
Platform: OutSystems 11.
[Add your context and evidence.]
```

Use `gemini skills list --all` to check discovery. Review the activation request when prompted. Gemini in the browser does not load a local folder automatically; use the manual method there.

## Kimi Code

Copy the skill folder into `.agents/skills/` in your project, one of Kimi Code's documented discovery locations:

```text
.agents/skills/outsystems-architecture/SKILL.md
```

Start a new session and send:

```text
/skill:outsystems-architecture Review the dependencies described below.
```

Add your platform, context, and evidence. Consult the official discovery documentation if your version differs. For Kimi chat, use the manual method.

## DeepSeek

This project's documented method for DeepSeek chat is **manual use**. Paste the chosen `SKILL.md` into the conversation and then send your request.

No API key is needed for this method. If you use a DeepSeek model through another client or the API, file access and skill loading depend on that client. This library does not provide a DeepSeek API integration or installer.

## Manual method: ChatGPT, Gemini web, Kimi chat, and other assistants

1. Open the chosen `SKILL.md`.
2. Copy its full text into a conversation, or attach it if supported.
3. Ask: “Use these instructions for the following task.”
4. Send a completed [request template](request-template.md).
5. Provide any additional evidence the assistant needs.

Example:

```text
Use the attached Troubleshooting skill.
I will describe a loading indicator and modal issue.
Base your analysis on the evidence I provide.
Ask for missing evidence before selecting a cause.
[Paste the completed request template.]
```

This adds instructions to the conversation. It does not establish native installation or guarantee identical results across models.

## If the assistant does not find the skill

Check that the folder contains `SKILL.md`, that it is in the correct project, and that you opened a new session. Ask which skill file was loaded. If the application cannot read local files, paste the instructions manually.

## Update or remove

Update your downloaded library, review differences, and copy only the skills you use. To remove a skill, remove its installed folder and start a new session. This does not modify your OutSystems applications.
