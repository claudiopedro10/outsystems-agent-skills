# Conectar o MCP do Service Studio (OutSystems 11)

Este guia descreve o **servidor MCP local do Service Studio (OutSystems 11)**.
Ele conecta um agente de IA compatível ao módulo aberto no Service Studio. As
skills deste repositório orientam a tarefa; elas não ligam o servidor nem
registram a conexão. O ODC usa outros recursos; consulte a documentação dele.

## Antes de começar

- Service Studio 11.55.91 ou mais recente, aberto com o módulo-alvo.
- Um agente ou host com suporte a MCP, com o acesso de conta necessário.
- As skills deste repositório e a skill oficial `servicestudio-mcp-oml`
  instaladas no agente. O jeito mais simples é colar o prompt da seção
  [Como começar](../README.md#como-começar) do README, que instala as duas.

Os requisitos de versão e a configuração estão em
[Get started with OutSystems MCP](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/).

## Regra principal: só MCP, nunca terminal

O agente acessa o Service Studio **somente** pelas ferramentas MCP registradas
nele. Ele nunca deve usar PowerShell, cmd, bash, curl, `Invoke-WebRequest`,
`netstat`, scripts ou varredura de portas para testar, descobrir ou se conectar
ao MCP. Se as ferramentas MCP não funcionarem, ele para e pede para você
conferir o Service Studio. Essa regra já está em todas as skills.

A skill oficial da OutSystems é a referência das ferramentas e da Model API,
mas parte do material dela mostra como chamar o servidor por shell e `curl`
(transporte HTTP), e os guias de setup sugerem `netstat` para achar a porta.
As skills deste repositório e a regra do AGENTS.md mandam o agente **não**
seguir essas partes: em conflito, vale a regra de não usar terminal.

## 1. Ligar o servidor

1. Abra o módulo-alvo no Service Studio.
2. Escolha **Edit > MCP Server**. O nome do menu pode variar conforme a versão.
3. Inicie o servidor e confirme que o status está **Running**.
4. Copie o endereço exibido nessa janela. Ele tem este formato:

```text
http://127.0.0.1:<PORTA>/mcp
```

Troque `<PORTA>` pela porta que aparece no seu Service Studio. Por exemplo,
pode aparecer `41820`, mas a porta não é fixa. Se você mudar a porta, atualize
também a configuração do agente.

## 2. Registrar o endereço no agente

O jeito mais simples é deixar o agente fazer isso: o prompt da seção
[Como começar](../README.md#como-começar) traz o endereço na primeira linha e
manda o agente criar o arquivo de configuração com o JSON certo. Na primeira
vez, ele para e pede para você reiniciar a sessão e aprovar o servidor; depois
responda "continue".

Se preferir registrar à mão, **copie o arquivo pronto** em vez de digitar ou
colar o JSON. Colar trechos do chat é a causa mais comum de arquivo quebrado
(falta o começo `{"mcpServers": {...` e o agente não encontra o servidor).

| Agente | Arquivo pronto neste repositório | Onde colocar no projeto |
| --- | --- | --- |
| Claude Code | [`.mcp.json`](../.mcp.json) (cópia do arquivo oficial da OutSystems) | `.mcp.json` na raiz |
| GitHub Copilot no VS Code | [`config/vscode-copilot.mcp.json`](../config/vscode-copilot.mcp.json) | `.vscode/mcp.json` |

O Claude Code dentro do VS Code continua sendo Claude Code: ele usa `.mcp.json`
na raiz, não `.vscode/mcp.json`. Salve o arquivo antes de recarregar.

Se a porta no Service Studio não for `41820`, troque só o número no `url`.
Depois recarregue o agente (no VS Code: **Developer: Reload Window**) e aprove o
servidor `servicestudio`. No Claude Code, `/mcp` deve mostrar `servicestudio`
como **Connected**.

O nome `servicestudio` é o mesmo do repositório oficial e das mensagens de erro
da skill oficial. Não registre um segundo servidor com outro nome (por exemplo
`outsystems`) para o mesmo endereço: o agente passa a ver ferramentas
duplicadas.

- **Outros hosts com MCP (Codex, Gemini CLI, Kimi etc.):** use a configuração de
  servidores MCP do host. O [repositório oficial da OutSystems](https://github.com/OutSystems/outsystems11-mcp)
  tem guias de configuração por host. Esses guias são para você, não para o
  agente.
- **DeepSeek, ChatGPT ou outra interface:** o suporte depende do cliente, da
  versão e da conta, não só do nome do modelo. Confira se o cliente consegue se
  conectar a um servidor MCP.
- **Chat sem MCP:** cole as instruções da skill e envie evidências sanitizadas.
  O chat não consegue inspecionar o módulo aberto.

`127.0.0.1` é a máquina onde o cliente MCP roda. Um agente na nuvem ou remoto
não alcança o Service Studio do seu computador por esse endereço. Este guia não
recomenda expor o servidor local.

## 3. Aprovar e verificar

1. Inicie ou reinicie a sessão do agente, se o host pedir.
2. Se o Service Studio perguntar se o agente pode se conectar, aprove.
3. Peça ao agente:

```text
Use somente as ferramentas MCP do Service Studio que estão configuradas para
você. Não use PowerShell nem terminal. Liste os módulos abertos e acessíveis.
Módulo-alvo: [nome]. Leia esse módulo e resuma o que encontrou. Informe o nome
do módulo, a evidência inspecionada e qualquer falha de acesso ou de
identificação. Não altere, não faça merge e não publique nada.
```

4. Confira o nome e o conteúdo informados com o que aparece no Service Studio.
   Uma resposta genérica ou a simples afirmação de que as ferramentas existem
   não prova que o módulo foi lido.
5. Mande a sua demanda. A skill [outsystems-developer](../skills/outsystems-developer/SKILL.md)
   escolhe o fluxo. Use o [modelo de pedido](request-template.md) se quiser dar
   mais contexto.

Para testar a leitura de uma Server Action específica, use o
[exemplo de leitura pelo MCP](../examples/mcp-read-server-action.md).

## Identidade do módulo e acesso

No [modelo de pedido](request-template.md), separe o módulo-alvo dos módulos
abertos verificados, da aplicação e dos módulos relacionados. Um inventário
pode incluir referências carregadas; isso não prova que cada provedor esteja
aberto ou legível. Confirme cada módulo necessário para a tarefa.

Quando as ferramentas identificam módulos só pelo nome, pode não ser possível
distinguir ambientes. Se a identidade estiver ambígua, o agente deve confirmar
o alvo com você antes de uma operação dependente. Não deduza o ambiente por um
nome ou sufixo.

## Permissões e problemas

Para análise, peça ao agente que use só operações de leitura. Para edições,
revise as **Write permissions** do Service Studio e as mudanças propostas; o
Compare and Merge manual deixa você revisar as mudanças. Não mude essas
configurações para pular a revisão. Na documentação oficial, a leitura é GA e a
escrita no modelo é Beta. Confira as capacidades da versão instalada.

Uma edição pode existir primeiro só num modelo preparado (staged). Em edições
autorizadas, o agente deve conferir o resultado do merge, ler de novo os
elementos afetados e as mensagens de validação e informar separadamente o que
ficou preparado, o que entrou no módulo, o que foi publicado e o que foi testado
em execução. Merge não publica, e validação do modelo não prova comportamento
em execução. Publique só com autorização explícita.

Se a conexão falhar, confira:

1. se o servidor está **Running** no Service Studio;
2. se o arquivo de configuração MCP é um JSON completo (compare com os
   [arquivos prontos](#2-registrar-o-endereço-no-agente)) e usa a mesma porta exibida;
3. se o agente tem suporte a MCP;
4. se a conexão foi aprovada no Service Studio;
5. se o módulo certo está aberto.

Se a listagem de módulos funciona e só uma leitura demora até estourar o tempo
(`did not respond within 120s`), o problema não é a conexão. Confira se o
Service Studio está ocupado (diálogo aberto, publicação ou compilação em
andamento, módulo sem salvar) e peça para o agente repetir uma vez. Se
continuar, mande o trecho (SQL, fluxo ou print) para ele analisar sem essa
leitura.

O agente não deve tentar diagnosticar a conexão pelo terminal. Se o MCP
continuar indisponível, peça uma análise manual com prints ou trechos
sanitizados; ela não deve ser apresentada como inspeção pelo MCP.

Documentação oficial: [Get started with OutSystems MCP](https://success.outsystems.com/documentation/11/outsystems_mcp/get_started_with_outsystems_mcp/).
