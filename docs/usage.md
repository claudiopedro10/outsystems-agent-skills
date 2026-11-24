# Primeiro uso

## O que é uma skill?

Um **prompt** é o pedido que você manda para um assistente de IA. Uma **skill**
é um conjunto de instruções reutilizáveis que orienta como o assistente trata
um tipo de pedido. Um **agente** é um aplicativo que, além de conversar, pode ler
arquivos ou usar ferramentas, como o MCP do Service Studio.

A skill traz o jeito de trabalhar, não o conhecimento da sua aplicação. O
assistente ainda precisa saber o módulo, a lógica envolvida, o comportamento
esperado e as evidências.

## Passo 1: instalar

Siga a seção [Como começar](../README.md#como-começar) do README: prepare o
Service Studio e cole o prompt de instalação no agente. Quando o agente
responder “Pronto, pode mandar a demanda”, está tudo configurado.

Se preferir instalar à mão, veja a [instalação por agente](agents.md). Para usar
num chat sem MCP, cole o conteúdo de
[outsystems-developer](../skills/outsystems-developer/SKILL.md) na conversa e
diga: “Use estas instruções para a tarefa que vou descrever.”

## Passo 2: mandar a demanda

Comece pelo resultado que você quer e pelo elemento afetado, se souber:

```text
Módulo: PurchaseOrders_UI
Tela e ação: OrderDetails / SubmitApproval
O que fazer: depois de aprovar, o modal não fecha e o loading continua.
```

O agente escolhe o fluxo sozinho. Uma falha vai para **Investigar**, uma melhoria
estrutural sem mudar o comportamento vai para **Refatorar**, e uma regra nova ou
alterada vai para **Implementar**. Por exemplo, “implementa a correção do
spinner” começa pelo diagnóstico.

Para tarefas maiores, o [modelo de pedido](request-template.md) tem campos
opcionais. Ajuda incluir:

- a plataforma e o tipo de aplicação, se souber;
- o módulo-alvo e os elementos afetados;
- para um bug, o resultado observado e o esperado e os passos para reproduzir;
- para uma refatoração, a duplicação a remover e o comportamento a preservar;
- para algo novo, a regra e um exemplo de sucesso ou de falha;
- restrições e evidências relevantes.

Um pedido como “arruma meu modal” não diz qual lógica nem qual a regra de
conclusão esperada. O [exemplo do modal de aprovação](../examples/loading-and-modal.md)
mostra como deixar esse pedido claro.

## Passo 3: deixar o agente ler o módulo

No O11, o agente lê o módulo aberto pelas ferramentas MCP do Service Studio. Ele
nunca deve usar PowerShell ou terminal para isso. Se o MCP falhar, ele vai pedir
para você conferir se o servidor está ligado e se o endereço está certo; veja o
[guia do MCP](service-studio-mcp.md).

Sem MCP, mande as evidências à mão. Em problemas de tela, ajudam: entradas do
Block, eventos e handlers, a ação que inicia o processamento, o caminho de
conclusão e os valores que controlam o loading e a visibilidade do modal. Em
integrações, mande o contrato sanitizado, o status da resposta, o tempo e os
logs relevantes. Em arquitetura, mande responsabilidades e direções de
dependência.

Identifique cada print ou trecho com o nome do elemento. Não envie um projeto
inteiro de cliente quando um trecho pequeno e sanitizado resolve. Esta
biblioteca não lê arquivos OML/OAP.

## Passo 4: revisar a resposta

Uma boa resposta:

- resume corretamente o comportamento esperado e o observado;
- diz quais evidências foram realmente inspecionadas;
- separa fatos VERIFICADOS, explicações INFERIDAS e informações DESCONHECIDAS,
  dizendo se a evidência veio do seu relato, de um artefato ou do MCP;
- explica a próxima verificação ou uma mudança justificada;
- descreve o efeito em componentes e contratos existentes;
- traz passos de validação.

O agente deve inspecionar o que estiver disponível antes de pedir mais coisas.
Espere uma pergunta objetiva quando uma regra de negócio ou a identidade do
alvo mudar a correção. Uma tarefa clara e autorizada não deve pedir confirmação
a cada passo.

Se a resposta inventar uma ação ou presumir a sua plataforma, peça para corrigir
a suposição antes de seguir.

## Passo 5: aplicar e validar com cuidado

Se você pediu só análise, revise a recomendação antes de pedir a implementação.
Aplique a mudança aceita em desenvolvimento e confira o comportamento esperado,
os caminhos de erro, o cancelamento e a execução repetida, quando fizer sentido.

Depois de edições pelo MCP, espere uma leitura de confirmação e a separação
entre o que ficou preparado (staged), o que entrou no módulo (merge) e o que foi
testado em execução. Veja a [avaliação](evaluation.md) para casos e limites.

Uma explicação confiante não é prova. No exemplo do modal, confirme que a
aprovação conclui, o loading para, o modal fecha e o resumo atualiza. Em caso de
falha, confirme que o modal continua aberto com um erro acionável.

## Perguntas úteis de acompanhamento

```text
Quais afirmações estão confirmadas pela evidência que eu mandei?
Qual é o menor print ou fluxo de ação adicional de que você precisa?
Explica a mudança proposta em termos do Service Studio para um iniciante.
Como verifico isso sem mudar um contrato existente?
Lista as verificações de regressão antes de eu aplicar a mudança.
```

## Dados e idioma

Remova senhas, tokens, cookies de sessão, dados pessoais e detalhes
confidenciais de clientes. Use identificadores fictícios quando fizer sentido.

O repositório está em português do Brasil. Os nomes técnicos do OutSystems
ficam em inglês. Você pode escrever em outro idioma e pedir a resposta nele.
