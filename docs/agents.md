# Uso por agente

Instruções verificadas na documentação em **30/10/2026**. Interfaces e caminhos podem mudar. Consulte as [fontes oficiais](sources.md). Os procedimentos foram revisados documentalmente; não foram executados em todos os produtos.

## Preparação

Clone ou baixe este repositório:

```sh
git clone https://github.com/claudiopedro10/outsystems-agent-skills.git
```

Os exemplos abaixo copiam **uma pasta de skill completa** para o projeto em que você quer trabalhar. Execute na raiz desse projeto e ajuste o caminho da cópia baixada. Não substitua uma skill existente sem revisá-la.

## Codex

Copie a pasta `outsystems-architecture` para `.agents/skills/` no projeto. Resultado:

```text
.agents/skills/outsystems-architecture/SKILL.md
```

Abra uma nova sessão no projeto e peça:

```text
Use $outsystems-architecture para revisar as dependências abaixo.
Plataforma: OutSystems 11. [adicione o contexto]
```

Para uso pessoal em vários projetos, a documentação também descreve `~/.agents/skills/`. Em ambientes remotos, a pasta precisa existir no ambiente utilizado pelo agente, não somente no seu computador.

## Claude Code

Copie a pasta para `.claude/skills/` no projeto:

```text
.claude/skills/outsystems-architecture/SKILL.md
```

Inicie uma sessão no projeto e invoque:

```text
/outsystems-architecture
Revise as dependências abaixo. Plataforma: OutSystems 11.
```

A instalação pessoal utiliza `~/.claude/skills/`. Claude Code local e Claude no navegador são superfícies distintas; a instalação local não implica disponibilidade em uma sessão na nuvem.

### Claude no navegador

Use o procedimento manual abaixo. Quando sua conta oferecer custom skills, siga o guia oficial de upload e empacotamento da Anthropic; os requisitos da conta e da interface podem variar.

## Gemini CLI

Copie a pasta para `.gemini/skills/` no projeto:

```text
.gemini/skills/outsystems-architecture/SKILL.md
```

Abra uma sessão no projeto. Peça explicitamente a skill pelo nome e confirme sua ativação quando o CLI solicitar:

```text
Use a skill outsystems-architecture para analisar este inventário.
Plataforma: OutSystems 11. [adicione o contexto]
```

O comando `gemini skills list --all` ajuda a verificar a descoberta. No Gemini web, use o procedimento manual; copiar uma pasta local não a instala no navegador.

## Kimi Code

Copie a pasta para `.agents/skills/` no projeto, um dos diretórios de descoberta documentados pelo Kimi Code:

```text
.agents/skills/outsystems-architecture/SKILL.md
```

Inicie uma nova sessão e use:

```text
/skill:outsystems-architecture Revise as dependências descritas abaixo.
```

Confira a documentação oficial de descoberta se a sua versão usar configuração diferente. No chat Kimi, o procedimento manual também pode ser usado.

## DeepSeek

**Método documentado por este projeto: uso manual.** Abra uma conversa, cole o conteúdo do `SKILL.md` escolhido e envie seu contexto na sequência.

Não é necessário criar uma chave de API para esse método. Se usar modelos DeepSeek por API ou outro cliente, o carregamento de arquivos e skills depende do cliente. A API de chat recebe mensagens; este projeto não oferece instalador ou integração própria para ela.

## ChatGPT, Gemini web, Kimi chat e outros assistentes

Método portátil:

1. Abra o `SKILL.md` escolhido e copie seu conteúdo.
2. Cole na conversa ou anexe o arquivo se a interface aceitar.
3. Solicite: “Use estas instruções para a tarefa abaixo”.
4. Acrescente o contexto mínimo e o resultado esperado.
5. Inclua referências de apoio quando existirem e forem necessárias.

Exemplo:

```text
Use o conteúdo da skill anexada para revisar meu fluxo de pedidos.
Considere apenas as evidências fornecidas.
Plataforma: OutSystems 11 / Reactive Web.
[insira contexto sanitizado]
Mostre achados, justificativas, lacunas e como validar.
```

Isso fornece instruções ao contexto da conversa; não comprova instalação nativa nem garante comportamento igual entre modelos.

## Comparação rápida

| Ambiente | Método descrito | Verificação |
| --- | --- | --- |
| Codex | Pasta em .agents/skills | Skill disponível na nova sessão |
| Claude Code | Pasta em .claude/skills | Comando /outsystems-architecture |
| Gemini CLI | Pasta em .gemini/skills | Lista de skills e ativação |
| Kimi Code | Pasta em .agents/skills | Comando /skill:outsystems-architecture |
| DeepSeek chat | Conteúdo no contexto | Confirmar instruções recebidas |
| Outros chats | Colar ou anexar | Confirmar arquivo/contexto recebido |

## Atualizar e remover

Atualize sua cópia do repositório e copie novamente somente as skills desejadas, revisando diferenças. Para remover, apague apenas a pasta instalada da skill e abra uma nova sessão. Esse procedimento não altera aplicações OutSystems.
