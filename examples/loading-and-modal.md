# Passo a passo de investigação: modal de aprovação de pedido

Este exemplo fictício em OutSystems 11 / Reactive Web mostra como preparar um
bom pedido, fornecer evidências e avaliar uma recomendação. Não é o diagnóstico
de uma aplicação inspecionada.

## 1. Carregue a skill

Com as skills instaladas (veja [Como começar](../README.md#como-começar)), basta
mandar a demanda: a [outsystems-developer](../skills/outsystems-developer/SKILL.md)
escolhe o fluxo Investigar. Para uma investigação aprofundada com logs, você
pode pedir diretamente a
[outsystems-troubleshooting](../skills/outsystems-troubleshooting/SKILL.md).

Antes de usar o exemplo num módulo real, ligue o
[MCP do Service Studio](../docs/service-studio-mcp.md) e confirme o módulo
aberto. Este exemplo é fictício e não afirma que algum módulo foi inspecionado.

## 2. Descreva o problema

### Exemplo: o modal de aprovação de pedido não fecha

*Cenário fictício em OutSystems 11 / Reactive Web.*

**Contexto**

- **Camada da arquitetura:** End User
- **Módulo-alvo:** `PurchaseOrders_UI`
- **Aplicação:** `Procurement` (fictícia)
- **Módulos abertos:** Desconhecido; verificar pelo MCP.
- **Módulos relacionados:** Desconhecido; estabelecer provedores e consumidores relevantes.
- **Screen:** `OrderDetails`
- **Block:** `OrderApprovalDialog`
- **Client Action:** `SubmitApproval`
- **Evento de conclusão:** `ApprovalCompleted`

**Comportamento observado**

O pedido é aprovado, mas o modal continua aberto e o indicador de carregamento
continua visível. Ao atualizar a tela, o status novo do pedido aparece.

**Comportamento esperado**

Depois de uma aprovação bem-sucedida, parar o carregamento, fechar o modal e
atualizar o resumo do pedido. Se a aprovação falhar, parar o carregamento,
manter o modal aberto e mostrar um erro acionável.

**Restrições**

Preservar regras de negócio, entradas públicas, eventos e contratos de serviço
existentes. Limitar a correção ao fluxo de interface afetado.

**Pedido ao assistente**

Confirme a conexão MCP com o Service Studio e que o módulo pretendido está
aberto. Use só as ferramentas de leitura do MCP, nunca PowerShell ou terminal.
Se a conexão não estiver disponível, peça fluxos de ação sanitizados e explique
o limite da inspeção.

Rastreie a ação de envio, o evento de conclusão, o handler na Screen pai e as
atualizações de estado da interface. Separe evidências de hipóteses. Inspecione
primeiro os fluxos disponíveis; peça só a evidência que ainda faltar antes de
escolher uma causa. Entregue um plano de correção focado e verificações de
regressão; não edite nem publique a aplicação.

## 3. Torne o problema reproduzível

1. Abra um pedido com status **Pending approval** em `OrderDetails`.
2. Abra o `OrderApprovalDialog`.
3. Clique em **Approve** e espere a aprovação retornar.
4. Observe que o indicador de carregamento e o modal continuam visíveis.
5. Atualize a tela e confirme que o status do pedido é **Approved**.

Num pedido real, registre se isso acontece toda vez, quando começou e se a
falha ou o cancelamento se comportam de forma diferente.

## 4. Forneça evidências focadas

Com o MCP conectado, o agente lê o módulo aberto. Sem MCP, mande prints ou
trechos de lógica identificados de:

- `SubmitApproval`, incluindo os caminhos de sucesso e de exceção;
- onde `ApprovalCompleted` é disparado e o contrato do evento;
- o handler na Screen pai associado a `ApprovalCompleted`;
- o estado ou as expressões que controlam o carregamento e a visibilidade do modal;
- a ação que atualiza o resumo do pedido;
- logs e observações de reprodução relevantes, sem dados sensíveis.

Comece pelo fluxo de envio e pelo handler na Screen pai. Mande mais artefatos
quando o assistente explicar qual dúvida eles resolvem. Um nome fictício deste
guia não é um pedido para criar ou renomear elementos na sua aplicação.

## 5. Avalie a análise

Uma boa resposta reconhece que a aprovação parece ser gravada, mas a conclusão
da interface continua em aberto. Ela identifica a evidência necessária para
saber se o caminho de sucesso, o evento, o handler na Screen pai e as
atribuições de estado executam como esperado.

| Pergunta da investigação | Evidência a inspecionar |
| --- | --- |
| A execução chega ao caminho de sucesso? | Fluxo da ação e resposta observada |
| O evento de conclusão é disparado e tratado? | Ligação do evento e handler na Screen pai |
| Qual elemento é dono de cada estado da interface? | Declarações e atribuições de estado |
| Os caminhos de erro limpam o carregamento? | Tratamento de exceção |
| Uma segunda aprovação se comporta corretamente? | Reprodução com uso repetido |

São perguntas de investigação, não causas estabelecidas. O dado ser gravado não
prova que um handler específico da interface executou.

Peça esclarecimento se o assistente presumir um evento faltando, inventar ações
existentes ou propor mudar um contrato público sem evidência.

## 6. Revise o plano de correção

Antes de implementar, espere:

- o elemento existente e o caminho específico a mudar;
- a evidência que apoia a correção proposta;
- como o plano preserva os contratos e as regras de negócio informados;
- qualquer incerteza restante ou conflito com uma restrição;
- passos de validação e um jeito prático de desfazer.

Mantenha a mudança limitada ao problema demonstrado. Um redesenho maior precisa
de justificativa própria.

## 7. Valide o resultado em desenvolvimento

| Cenário | Critério de aceitação |
| --- | --- |
| Aprovação bem-sucedida | O carregamento para, o modal fecha e o resumo mostra Approved |
| Aprovação negada por regra de negócio | O carregamento para, o modal continua aberto e aparece uma mensagem acionável |
| Falha na requisição | O carregamento para; sem falso sucesso nem fechamento indevido |
| Uso repetido | Abrir e enviar outro pedido pendente usa estado novo |
| Consumidores existentes | Entradas públicas, eventos e contratos de serviço continuam compatíveis |

Confira cancelamento e envio duplicado conforme as regras funcionais existentes.
Não deduza que fechar o modal cancela uma requisição em andamento.

Registre os resultados observados antes de dar o problema como resolvido. Este
guia traz uma estrutura de pedido e de validação; não afirma uma correção
verificada.
