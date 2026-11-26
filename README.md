# OutSystems Agent Skills

**Investigue bugs, refatore e implemente mudanças em OutSystems com um agente de IA.**

Você instala as skills uma vez, junto com a skill oficial da OutSystems, e
depois só manda as demandas. O agente escolhe
sozinho a skill certa, lê o módulo aberto no Service Studio pelo MCP, começa o
trabalho e pergunta quando faltar informação.

## Como começar

**Antes de colar o prompt**, deixe o Service Studio pronto:

1. Abra o módulo no Service Studio (versão 11.55.91 ou mais recente; recomendada
   11.55.99 ou mais recente, que tem o contrato MCP 2).
2. Ligue o servidor em **Edit > MCP Server** e confira o endereço exibido.
   Normalmente é `http://127.0.0.1:41820/mcp`. Se a porta for outra, troque o
   endereço na primeira linha do prompt.

Você não precisa registrar o MCP à mão: o próprio agente cria o arquivo de
configuração com o JSON certo.

**Para começar a usar estas skills, cole o prompt abaixo no seu agente.**

```text
Endereço do MCP Server (Service Studio > Edit > MCP Server):
http://127.0.0.1:41820/mcp

Instale e configure as skills OutSystems do repositório
https://github.com/claudiopedro10/outsystems-agent-skills
e a skill oficial da OutSystems do repositório
https://github.com/OutSystems/outsystems11-mcp

1. Baixe os dois repositórios. Copie todas as pastas de skills/ do primeiro e a
   pasta servicestudio-mcp-oml do segundo para a pasta de skills que você usa
   neste projeto (por exemplo .claude/skills, .agents/skills, .github/skills ou
   .gemini/skills). Se já existir uma skill com o mesmo nome, me pergunte antes
   de sobrescrever. Se você não consegue instalar skills, leia
   skills/outsystems-developer/SKILL.md e siga essas instruções nesta conversa.

2. No arquivo de instruções do projeto (AGENTS.md, CLAUDE.md ou o equivalente
   que você usa), adicione estas regras:
   "Para qualquer tarefa OutSystems, use a skill outsystems-developer como
   ponto de entrada. A skill oficial servicestudio-mcp-oml serve só como
   referência de como usar as ferramentas MCP e a Model API; não a use para
   escolher o fluxo da tarefa. Acesse o Service Studio somente pelas
   ferramentas MCP; nunca use PowerShell nem terminal para testar ou se
   conectar ao MCP. Se a skill oficial e as skills outsystems-* entrarem em
   conflito, vale a regra de não usar terminal e o fluxo da
   outsystems-developer."

3. Registre o MCP do Service Studio neste projeto com o endereço da primeira
   linha. Crie ou atualize o arquivo de configuração MCP do projeto com a sua
   ferramenta de edição de arquivos, sem testar a conexão. O formato depende
   de qual agente VOCÊ é, não do editor em que está rodando:
   - Se você é o Claude Code (inclusive a extensão dentro do VS Code): copie o
     arquivo .mcp.json da raiz do repositório outsystems-agent-skills baixado
     no passo 1 para a RAIZ do projeto, sem redigitar o JSON. Ele é cópia do
     .mcp.json do repositório oficial da OutSystems. Se o endereço da primeira
     linha for diferente de http://127.0.0.1:41820/mcp, troque só o "url".
     Não use .vscode/mcp.json: o Claude Code não lê esse arquivo.
   - Se você é o GitHub Copilot no VS Code: copie
     .vscode/mcp.json do mesmo repositório para .vscode/mcp.json do projeto.
   - Outro agente: o arquivo de configuração MCP que a documentação dele indica,
     com o servidor "servicestudio".
   Se o arquivo já existir, acrescente só o servidor "servicestudio" sem apagar
   os outros. Se já houver outro servidor apontando para o mesmo endereço (por
   exemplo "outsystems", de uma instalação anterior), me pergunte antes de
   trocar: dois servidores para o mesmo Service Studio confundem o agente. Salve o arquivo no disco (não deixe só aberto no editor), leia de
   novo e confira se é um JSON válido e completo. Diga em uma linha qual agente
   você é e qual arquivo criou. Se você já tinha ferramentas MCP do Service Studio antes deste
   passo, pule direto para o passo 4. Se não tinha, pare aqui e me peça para
   reiniciar a sessão (ou recarregar o VS Code), aprovar o servidor
   "servicestudio" quando aparecer e depois responder "continue".

4. Confirme o acesso ao Service Studio usando somente as ferramentas MCP.
   Liste os módulos abertos e me diga qual módulo você conseguiu ler. Nunca use
   PowerShell, terminal, curl, scripts nem varredura de portas para testar ou
   se conectar ao MCP. O terminal só pode ser usado no passo 1, para baixar e
   copiar as skills.

5. Se as ferramentas MCP não aparecerem ou a leitura falhar, pare e me peça
   para conferir se o MCP Server está ligado (Running) no Service Studio, se o
   endereço mostrado lá é o mesmo da primeira linha deste prompt, se aprovei o
   servidor "servicestudio" no agente e a conexão no Service Studio e se o módulo
   certo está aberto.

6. Quando tudo estiver pronto, responda: "Pronto, pode mandar a demanda:
   módulo, ação ou tela e o que precisa ser feito."

A partir daí, para cada demanda, use a skill outsystems-developer: diga em uma
linha qual fluxo escolheu (Investigar, Refatorar ou Implementar) e se vai
consultar algum especialista, comece o trabalho e me pergunte só o que faltar.
Em edições pelo MCP, siga a skill oficial para preparar, fazer o merge e
validar, e só publique quando eu pedir explicitamente.
```

Na primeira vez, o agente para no passo 3 e pede para você reiniciar a sessão
e aprovar o servidor `servicestudio`. É normal: as ferramentas MCP só aparecem
depois disso. Responda "continue" e ele termina a instalação.

Confira o arquivo que ele criou: no **Claude Code** é `.mcp.json` na raiz do
projeto (com `mcpServers`); no **Copilot** é `.vscode/mcp.json` (com `servers`).
Se o Claude Code criou `.vscode/mcp.json`, copie o [`.mcp.json`](.mcp.json) da
raiz deste repositório para a raiz do projeto.

O `.mcp.json` da raiz é cópia do arquivo do
[repositório oficial](https://github.com/OutSystems/outsystems11-mcp) e usa o
mesmo nome de servidor, `servicestudio`. Se você já registrou o servidor oficial
com `claude mcp add servicestudio`, não registre outro com nome diferente.

Depois disso, o desenvolvedor só precisa mandar as demandas, com o módulo, a
ação ou tela e o que precisa ser feito. Por exemplo:

```text
Módulo: PurchaseOrders_UI
Tela e ação: OrderDetails / SubmitApproval
O que fazer: depois de aprovar, o modal não fecha e o loading continua.
```

## O que o agente faz com cada demanda

A skill [outsystems-developer](skills/outsystems-developer/SKILL.md) é a porta
de entrada. Ela escolhe o fluxo pelo que você escreveu:

| Você escreve algo como... | Fluxo | O que você recebe |
| --- | --- | --- |
| “O pedido aprova, mas o modal não fecha.” | [Investigar](skills/outsystems-developer/SKILL.md#investigar) | A causa com evidência, ou a verificação que separa as hipóteses, mais um caso de regressão. |
| “Extrai a validação duplicada sem mudar a assinatura da ação.” | [Refatorar](skills/outsystems-developer/SKILL.md#refatorar) | A mudança estrutural ou o plano, com verificações de antes e depois para quem usa a ação. |
| “Cria uma ação para o autor cancelar um pedido em rascunho.” | [Implementar](skills/outsystems-developer/SKILL.md#implementar) | O desenho ou a implementação, com critérios de aceitação e um caso negado ou de limite. |

Peça uma análise, um plano ou a alteração direta, como preferir. Você não
precisa saber em qual camada está o problema.

## Especialistas

Quando precisa de uma revisão mais profunda, a `outsystems-developer` consulta
um especialista. Você também pode pedir um diretamente.

| Assunto | Skill |
| --- | --- |
| Integrações externas, contratos, timeouts e retries | [Foundation](skills/outsystems-foundation/SKILL.md) |
| Entidades, regras de negócio e serviços de domínio | [Core](skills/outsystems-core/SKILL.md) |
| Screens, Blocks, jornadas e estados de tela | [End User](skills/outsystems-enduser/SKILL.md) |
| Dependências e ciclos entre módulos | [Arquitetura](skills/outsystems-architecture/SKILL.md) |
| Investigação aprofundada com logs e várias hipóteses | [Investigação aprofundada](skills/outsystems-troubleshooting/SKILL.md) |
| Autenticação, autorização e dados sensíveis | [Segurança](skills/outsystems-security/SKILL.md) |

A skill oficial da OutSystems, `servicestudio-mcp-oml`, é instalada junto pelo
prompt. Ela não escolhe o fluxo: serve de referência para o agente usar as
ferramentas MCP e a Model API, principalmente ao escrever no modelo.

## Regras que o agente segue

- Acessa o módulo **somente pelo MCP do Service Studio**. Nunca usa PowerShell
  nem terminal para testar ou se conectar ao MCP.
- Se o MCP falhar, para e pede para você conferir o Service Studio, em vez de
  tentar outro caminho.
- Separa o que verificou do que está supondo (VERIFICADO, INFERIDO,
  DESCONHECIDO).
- Em edições, segue a skill oficial para preparar, fazer o merge e validar.
  Confira as mudanças no Compare and Merge do Service Studio antes de aceitar:
  a escrita pelo MCP ainda é Beta.
- Pergunta só o que muda o resultado.
- Não publica sem você pedir.

## Sem MCP

As skills também funcionam num chat comum. Cole o conteúdo de
[outsystems-developer](skills/outsystems-developer/SKILL.md), descreva a tarefa e
envie prints ou trechos sanitizados. Nesse caso, o agente analisa só o que você
mandou. Para ODC, use a documentação e as ferramentas do ODC.

## Já usa este repositório? Atualize assim

1. Atualize o Service Studio para a **11.55.99 ou mais recente** (Help > About
   mostra a versão).
2. Baixe de novo os dois repositórios (`git pull` em cada clone, ou baixe o ZIP
   de novo).
3. Copie de novo as pastas `skills/outsystems-*` para a pasta de skills do seu
   agente (no Claude Code: `.claude/skills/`), substituindo as antigas.
4. Atualize a skill oficial: no clone do `outsystems11-mcp`, rode
   `powershell -ExecutionPolicy Bypass -File scripts\install.ps1 -Source .`
5. **O servidor MCP agora se chama `servicestudio`.** No `.mcp.json` do seu
   projeto, troque `"outsystems"` por `"servicestudio"` (ou copie o
   [`.mcp.json`](.mcp.json) deste repositório). Não deixe os dois nomes: o
   agente veria ferramentas duplicadas.
6. Abra uma sessão nova do agente, aprove o servidor `servicestudio` e aprove o
   pedido na janela do Service Studio.

## Documentação

Para usar:

- [Primeiro uso](docs/usage.md)
- [Conectar o MCP do Service Studio](docs/service-studio-mcp.md)
- [Instalação por agente: Claude, Codex, Copilot, Gemini, Kimi e outros](docs/agents.md)
- [Modelo de pedido](docs/request-template.md)
- [Exemplo: modal de aprovação que não fecha](examples/loading-and-modal.md)
- [Exemplo: ler uma Server Action pelo MCP](examples/mcp-read-server-action.md)
- [Exemplo: revisão de arquitetura](examples/architecture-review.md)

Para manter o repositório:

- [Estrutura e qualidade das skills](docs/manutencao/skill-design.md)
- [Avaliação e casos de teste](docs/manutencao/evaluation.md)
- [Auditorias](docs/manutencao/audits/2026-11-24.md)
- [Fontes oficiais](docs/manutencao/sources.md)
- [Roadmap](ROADMAP.md) · [Manutenção](CONTRIBUTING.md) · [Segurança](SECURITY.md)

## Status do projeto

Uma skill de entrada e seis especialistas que podem ser instalados
separadamente, usados junto com a skill oficial da OutSystems, com testes
automáticos de estrutura. Os testes cobrem metadados,
links e empacotamento; eles não provam as decisões do modelo nem o
comportamento no OutSystems. Testes ao vivo em O11 e ODC ainda estão pendentes.

A documentação e as skills são mantidas em português do Brasil. Os nomes
técnicos do OutSystems (Server Action, Service Studio, Screen etc.) ficam em
inglês, como aparecem na plataforma.

## Acesso ao repositório

Você pode ler, baixar e usar as skills. Contribuições externas não são aceitas:
issues, pull requests, discussões, wiki e projetos estão desativados. Só o dono
e mantenedores autorizados atualizam este repositório. Veja a
[política de manutenção](CONTRIBUTING.md).

Licença [MIT](LICENSE). Projeto independente da comunidade, sem afiliação ou
endosso da OutSystems ou dos fornecedores de IA. Os nomes de produtos pertencem
aos seus donos.
