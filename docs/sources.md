# Fontes e manutenção

Data de revisão da documentação: **6 de novembro de 2026**. Estes links apoiam
conceitos da plataforma e locais de configuração. Eles não implicam endosso dos
fornecedores nem execução de todos os exemplos.

## OutSystems

- [Architecture Canvas — OutSystems 11](https://success.outsystems.com/documentation/11/app_architecture/designing_the_architecture_of_your_outsystems_applications/the_architecture_canvas/): referência para Foundation, Core e End User.
- [Documentação oficial](https://success.outsystems.com/documentation/): confirme as capacidades da plataforma e da versão aplicáveis.
- [Get started with OutSystems MCP (O11)](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/): pré-requisitos, servidor local, configuração do agente e verificação.
- [Repositório oficial OutSystems O11 MCP](https://github.com/OutSystems/outsystems11-mcp): guias de configuração por host e uma skill oficial. **Opcional**: as skills deste repositório não exigem a skill oficial; elas usam as ferramentas que o servidor MCP anuncia.
- [ODC: Use MCP servers](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/build_ai_powered_apps/agentic_apps_in_odc/tools_and_connectors/use_mcp_servers/): consumo de ferramentas MCP externas por apps agênticos do ODC; não é um guia para um agente de código editar aplicações ODC ou O11.

A referência do Architecture Canvas é do O11. Esta biblioteca não presume a
mesma organização nem os mesmos mecanismos no ODC. Cite a documentação do ODC
correspondente ao fazer recomendações específicas da plataforma.

## Agentes

- [Codex: Build skills](https://learn.chatgpt.com/docs/build-skills): estrutura, descoberta e pastas.
- [GitHub Copilot: Add agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills): pastas de skills do projeto e descoberta.
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills): pastas do projeto e invocação.
- [Claude: Custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): upload e uso na interface.
- [Gemini CLI: Agent Skills](https://geminicli.com/docs/cli/skills/): descoberta, ativação e comandos.
- [Kimi Code: Agent Skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html): locais e invocação.
- [DeepSeek: Chat Completions API](https://api-docs.deepseek.com/api/create-chat-completion/): referência de mensagens para quem usa a API, não uma especificação de instalação de skills.

## Manutenção

Confira a fonte oficial e registre a data ao mudar instruções de configuração.
Se uma interface não foi verificada, ofereça o método manual e explique o
limite. Revisar documentação não é teste de execução.

## Registro da auditoria anterior

A comparação com o MCP O11 na auditoria de 6/11/2026 usou o repositório oficial
no commit [`8f36d5a`](https://github.com/OutSystems/outsystems11-mcp/tree/8f36d5ad38bb57e34e3078f882f0909ee5650cda).
O fluxo de merge e publicação, a verificação posterior e os limites de
identificação de módulos daquela skill inspiraram as orientações daqui. Desde
24/11/2026, as skills não dependem mais da skill oficial; confira a versão
instalada das ferramentas MCP antes de executar. Veja as auditorias de
[6/11](audits/2026-11-06.md) e [24/11](audits/2026-11-24.md).
