# Instalação por agente

O jeito mais simples de instalar é colar o prompt da seção
[Como começar](../README.md#como-começar) do README: o próprio agente copia as
skills deste repositório e a skill oficial da OutSystems, confere o MCP e avisa quando estiver pronto. Este guia explica a
instalação manual, caso você prefira ou o agente não consiga fazer sozinho.

Documentação conferida em **6 de novembro de 2026**. Os procedimentos se baseiam
em [fontes oficiais](sources.md); não foram executados em todos os produtos.

> [!IMPORTANT]
> Para acessar um módulo OutSystems 11, ligue o MCP Server no Service Studio,
> registre o endereço exibido no agente e confira a leitura do módulo aberto.
> Veja o [guia do MCP](service-studio-mcp.md). O agente deve acessar o Service
> Studio **somente pelas ferramentas MCP**, nunca por PowerShell ou terminal.
> Sem MCP, a análise manual com evidências fornecidas continua possível; o ODC
> tem orientação própria.

## Escolha a sua configuração

| Aplicativo | Onde colocar as skills | Como conferir |
| --- | --- | --- |
| Codex | Pasta `.agents/skills` | Disponível numa nova sessão |
| GitHub Copilot no VS Code | Pasta `.github/skills` | Pedir para usar a skill no modo agente |
| Claude Code | Pasta `.claude/skills` | `/outsystems-developer` |
| Gemini CLI | Pasta `.gemini/skills` | Lista e ativação de skills |
| Kimi Code | Pasta `.agents/skills` | `/skill:outsystems-developer` |
| DeepSeek chat | Colar as instruções da skill | Confirmar que recebeu o contexto |
| Outros chats | Colar ou anexar as instruções | Confirmar que recebeu o arquivo ou texto |

O host usa o endereço e a porta exibidos no seu Service Studio; esta biblioteca
não conecta nada automaticamente.

Em cada pedido, use **Módulo-alvo** para o escopo pretendido e **Módulos
abertos** só para o acesso verificado pelo MCP. Aplicação e Módulos relacionados
são contexto opcional, não prova de acesso. Use o [modelo de pedido](request-template.md)
quando a tarefa precisar de mais contexto.

Instale todas as pastas de `skills/` e também a pasta `servicestudio-mcp-oml`
do [repositório oficial da OutSystems](https://github.com/OutSystems/outsystems11-mcp).
A `outsystems-developer` é a porta de entrada e escolhe sozinha o fluxo; os
especialistas são consultados quando necessário; a skill oficial é a referência
das ferramentas MCP e da Model API.

## Baixar a biblioteca

Baixe o repositório em **Code > Download ZIP** no GitHub e extraia. Quem usa Git
pode rodar:

```sh
git clone https://github.com/claudiopedro10/outsystems-agent-skills.git
git clone https://github.com/OutSystems/outsystems11-mcp.git
```

A biblioteca baixada é a origem. O seu projeto de trabalho é onde o agente vai
usar as skills. Copie as pastas completas de skills da origem para o destino
descrito abaixo. Não sobrescreva uma skill existente sem revisá-la.

Para que o agente use a skill certa em toda sessão, adicione ao arquivo de
instruções do projeto (`AGENTS.md`, `CLAUDE.md` ou equivalente):

```text
Para qualquer tarefa OutSystems, use a skill outsystems-developer como ponto de
entrada. A skill oficial servicestudio-mcp-oml serve só como referência de como
usar as ferramentas MCP e a Model API; não a use para escolher o fluxo da
tarefa. Acesse o Service Studio somente pelas ferramentas MCP; nunca use
PowerShell nem terminal para testar ou se conectar ao MCP. Se a skill oficial e
as skills outsystems-* entrarem em conflito, vale a regra de não usar terminal e
o fluxo da outsystems-developer.
```

## Codex

Copie as pastas de `skills/` para `.agents/skills/` no seu projeto:

```text
seu-projeto/
  .agents/
    skills/
      outsystems-developer/
        SKILL.md
      outsystems-core/
        SKILL.md
      ...
      servicestudio-mcp-oml/
        SKILL.md
```

Abra uma nova sessão do Codex no projeto e mande:

```text
Use $outsystems-developer. Refatore a validação duplicada e preserve os dois
contratos públicos. Me dê o plano.
Plataforma: OutSystems 11.
Confirme a conexão MCP com o Service Studio e o módulo aberto.
Use as ferramentas de leitura; informe qualquer falta de acesso. Não edite nem publique.
[Adicione o seu contexto e as evidências.]
```

O local pessoal documentado é `~/.agents/skills/`. Aqui, `~` é a pasta do seu
usuário. Num ambiente remoto, a pasta precisa existir onde o Codex roda.

## GitHub Copilot no VS Code

Copie as pastas completas das skills para `.github/skills/` no seu repositório
de trabalho. No modo agente, peça ao Copilot para usar `outsystems-developer` e
descreva a tarefa. Veja o [guia de skills do GitHub](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
para descoberta e clientes suportados.

Registre o endereço do MCP do Service Studio nas configurações de MCP do VS
Code. Uma skill disponível para o Copilot no GitHub não torna o Service Studio
do seu computador acessível a um agente na nuvem.

## Claude Code

Copie as pastas das skills para `.claude/skills/` no seu projeto:

```text
.claude/skills/outsystems-developer/SKILL.md
```

Inicie uma sessão no projeto e mande:

```text
/outsystems-developer
O modal de aprovação continua aberto depois do sucesso. Encontre a causa.
Plataforma: OutSystems 11.
Confirme a conexão MCP com o Service Studio e o módulo aberto.
Use só ferramentas de leitura; informe qualquer falta de acesso.
[Adicione o seu contexto e as evidências.]
```

Instalações pessoais usam `~/.claude/skills/`. Uma instalação local do Claude
Code não deixa a skill disponível automaticamente no navegador ou na nuvem.

### Claude no navegador

Use o método manual abaixo. Se a sua conta permitir skills personalizadas, siga
as instruções oficiais de upload e empacotamento da Anthropic, citadas nas
[fontes](sources.md).

## Gemini CLI

Copie as pastas das skills para `.gemini/skills/` no seu projeto:

```text
.gemini/skills/outsystems-developer/SKILL.md
```

Inicie uma sessão e peça:

```text
Use a skill outsystems-developer para desenhar um filtro de pedidos pendentes
nesta tela.
Plataforma: OutSystems 11.
Confirme a conexão MCP com o Service Studio e o módulo aberto, se disponível.
[Adicione o seu contexto e as evidências.]
```

Use `gemini skills list --all` para conferir a descoberta. Revise o pedido de
ativação quando aparecer. O Gemini no navegador não carrega pastas locais; use o
método manual.

## Kimi Code

Copie as pastas das skills para `.agents/skills/` no seu projeto, um dos locais
de descoberta documentados do Kimi Code:

```text
.agents/skills/outsystems-developer/SKILL.md
```

Inicie uma nova sessão e mande:

```text
/skill:outsystems-developer Proponha uma refatoração da regra duplicada abaixo.
Confirme a conexão MCP com o Service Studio e o módulo aberto, se disponível.
```

Adicione a plataforma, o contexto e as evidências. Se a sua versão for
diferente, consulte a documentação oficial de descoberta. No Kimi chat, use o
método manual.

## DeepSeek

O método documentado aqui para o DeepSeek chat é o **uso manual**. Cole o
`SKILL.md` escolhido na conversa e depois mande o pedido.

Esse método não precisa de chave de API. Se você usa um modelo DeepSeek por
outro cliente ou pela API, o acesso a arquivos e o carregamento de skills
dependem desse cliente. Esta biblioteca não oferece integração nem instalador
para a API do DeepSeek.

## Método manual: ChatGPT, Gemini web, Kimi chat e outros assistentes

1. Abra o `SKILL.md` escolhido (normalmente o da `outsystems-developer`).
2. Copie o texto completo para a conversa, ou anexe o arquivo se for possível.
3. Diga: “Use estas instruções para a tarefa a seguir.”
4. Descreva a tarefa ou use o [modelo de pedido](request-template.md).
5. Envie as evidências de que o assistente precisar.

Exemplo:

```text
Use a skill OutSystems Developer anexada.
Vou descrever um modal de aprovação que continua aberto depois do sucesso.
Se o seu cliente tiver o MCP do Service Studio configurado, confirme o módulo
aberto e use as ferramentas de leitura, nunca o terminal. Se não tiver, peça
evidências sanitizadas.
Use primeiro o que estiver disponível; peça só a evidência que faltar antes de
escolher uma causa.
[Cole o modelo de pedido preenchido.]
```

Isso adiciona instruções à conversa. Não é uma instalação nativa e não garante
resultados iguais entre modelos.

## Se o assistente não encontrar a skill

Confira se a pasta tem o `SKILL.md`, se está no projeto certo e se você abriu
uma nova sessão. Pergunte qual arquivo de skill foi carregado. Se o aplicativo
não consegue ler arquivos locais, cole as instruções manualmente.

## Atualizar ou remover

Atualize a biblioteca baixada, revise as diferenças e copie de novo as skills.
Para remover uma skill, apague a pasta instalada e abra uma nova sessão. Isso não
altera as suas aplicações OutSystems.
