# Como escrever um bom pedido

Dê ao assistente contexto suficiente para entender a tarefa, encontrar a lógica
afetada e reconhecer um bom resultado. Descreva o que observou sem presumir a
causa.

## Comece com uma frase

Na maioria dos casos, basta o módulo, a ação ou tela e o que precisa ser feito.
A skill [outsystems-developer](../skills/outsystems-developer/SKILL.md) escolhe
o fluxo sozinha, mas você pode dizer qual quer.

| Fluxo | Pedido fictício |
| --- | --- |
| Investigar | “Depois de Salvar, o registro existe, mas o spinner não para. Rastreia o fluxo e me dá um plano de correção.” |
| Refatorar | “As duas ações verificam o mesmo limite de crédito. Extrai a regra e preserva os dois contratos públicos.” |
| Implementar | “Adiciona um filtro de pedidos pendentes. Limpar o filtro deve mostrar todos os pedidos que eu posso ver.” |

## Copie e adapte

Para um pedido mais complexo, mantenha só os campos abaixo que afetam a próxima
decisão.

```text
Fluxo (opcional): [Investigar / Refatorar / Implementar]

Contexto
- Plataforma: [OutSystems 11 ou ODC]
- Tipo de aplicação: [O11: Reactive Web, Traditional Web ou Mobile; ODC: tipo real]
- Camada da arquitetura: [Foundation, Core, End User, Não sei ou Não se aplica]
- MCP do Service Studio: [configurado / verificado por leitura / indisponível / desconhecido / não se aplica]
- Módulos abertos: [nomes confirmados como abertos e acessíveis pelo MCP; Desconhecido até verificar]
- Módulo-alvo: [módulo principal a investigar ou alterar; Não se aplica se for o caso]
- Aplicação: [aplicação dona, se souber; opcional]
- Módulos relacionados: [módulos possivelmente relevantes; Desconhecido ou Nenhum identificado]
- Elementos relacionados: [nome e papel de cada elemento relevante]

Objetivo
[Descreva a falha, a estrutura a melhorar ou o comportamento a adicionar.]

Comportamento atual (para bug ou refatoração)
[Descreva o sintoma ou o comportamento que deve ser preservado.]

Critérios de aceitação
[Descreva o resultado pretendido ou a equivalência de antes e depois numa refatoração.]

Passos para reproduzir (para bug, se souber)
1. [Estado inicial]
2. [Ação do usuário]
3. [Resultado observado]

Evidências disponíveis
[Liste acesso pelo MCP, prints, fluxos de ação, logs ou contratos.]

Restrições
[Diga quais componentes, interfaces e regras devem ser preservados.]

Entrega pedida
[Peça análise, plano de correção ou alterações autorizadas.]
[Diga como quer que o resultado seja validado.]
No O11, descubra os módulos disponíveis pelo MCP e confirme o acesso ao módulo-alvo.
Use só ferramentas MCP, nunca PowerShell ou terminal. Informe falta de acesso ou de evidência.
```

Se um campo for desconhecido, diga isso em vez de chutar. No ODC, descreva a
aplicação ou library real. Para uma funcionalidade nova, explique o fluxo
existente ou diga que ainda não existe implementação.

## Identifique o escopo sem presumir acesso

Estes campos separam o escopo da tarefa do acesso pelas ferramentas. São
opcionais quando não importam; não invente valores para completar o modelo.

| Campo | Significado | Não significa |
| --- | --- | --- |
| Módulos abertos | Módulos confirmados como abertos e acessíveis por uma leitura MCP; cite o resultado | Que toda referência ou módulo da aplicação esteja aberto |
| Módulo-alvo | Módulo principal da tarefa, mesmo que ainda inacessível | Permissão ou capacidade de editá-lo |
| Aplicação | Aplicação dona ou contexto de negócio, se souber | Acesso aos seus módulos |
| Módulos relacionados | Provedores ou consumidores possivelmente relevantes | Dependências verificadas ou acesso pelas ferramentas |

Antes de uma leitura pelo MCP, escreva `Módulos abertos: Desconhecido`. Se você
sabe quais abas abriu, registre isso como **Módulos abertos segundo o
desenvolvedor** em Evidências disponíveis; o agente ainda precisa verificar o
acesso. Configuração, sozinha, não é conexão bem-sucedida.

Use `Desconhecido` para o que não foi estabelecido, `Nenhum identificado` quando
uma investigação não achou módulos relevantes e `Não se aplica` quando o campo
não faz sentido. No ODC, Módulo-alvo e Módulos abertos do Service Studio podem
não se aplicar; identifique a aplicação ou library real em Aplicação e
Elementos relacionados.

Pedidos antigos continuam funcionando: `Open module` ou `Módulo aberto` vale
como candidato informado, e `Module or application` é interpretado pelo
contexto. O agente só pergunta se a ambiguidade afetar a próxima operação. Não
é preciso reescrever o pedido nem preencher todos os campos numa tarefa simples.

## Trabalhando com o MCP do Service Studio

No OutSystems 11, diga se o agente está conectado ao MCP local do Service Studio
e qual é o módulo-alvo. Liste só módulos abertos verificados; deixe as abas que
você abriu em Evidências disponíveis. O endereço vem da janela do seu Service
Studio; este modelo não fixa porta. Veja a [configuração e o teste de conexão](service-studio-mcp.md).
No ODC, identifique à parte as ferramentas realmente suportadas.

## Escolha a camada da arquitetura

Use **Camada da arquitetura** para indicar a responsabilidade do módulo afetado
no OutSystems 11:

| Opção | Responsabilidade típica |
| --- | --- |
| Foundation | Integrações, adaptadores e capacidades técnicas reutilizáveis |
| Core | Entidades, regras de negócio e serviços de domínio |
| End User | Screens, Blocks e orquestração da jornada do usuário |
| Não sei | Peça ao assistente para avaliar as responsabilidades informadas |

Numa tarefa com vários módulos, indique a camada de cada um. Não deduza a camada
só pelo nome ou sufixo. O assistente deve conferir a camada informada com as
responsabilidades e explicar qualquer divergência.

No ODC, use **Não se aplica** quando essa classificação do O11 não servir e
descreva as responsabilidades reais da aplicação ou library.

## O que cada seção traz

| Seção | O que incluir | Para quê |
| --- | --- | --- |
| Contexto | Plataforma, tipo de aplicação, camada e papel dos elementos | Define o escopo técnico |
| Objetivo | Sintoma ou meta, em poucas palavras | Diz qual é a tarefa |
| Comportamento atual | Sintoma ou base atual | Fundamenta o diagnóstico ou a refatoração |
| Critérios de aceitação | Exemplos de sucesso, falha ou equivalência | Define o que é correto |
| Passos para reproduzir | Condições iniciais e ações | Torna o problema repetível |
| Evidências disponíveis | Trechos ou prints identificados | Permite uma análise rastreável |
| Restrições | Contratos, componentes e regras a preservar | Limita o escopo da mudança |
| Entrega pedida | Análise, plano ou implementação autorizada | Define o que o assistente deve fazer |

Um identificador sozinho não descreve a implementação. Diga se o elemento é uma
Screen, um Block, uma ação ou um evento, quando souber.

## Exemplo completo

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

No O11, confirme a conexão MCP com o Service Studio e o módulo aberto; use as
ferramentas de leitura disponíveis. Se não houver acesso, peça evidências
sanitizadas e diga que nenhum módulo foi inspecionado.

Investigue a ação de envio, o evento de conclusão, o handler na Screen pai e as
atualizações de estado da interface. Separe evidências de hipóteses. Inspecione
primeiro os fluxos disponíveis; peça só a evidência que ainda faltar antes de
escolher uma causa. Entregue um plano de correção focado e verificações de
regressão; não edite nem publique a aplicação.

### Passos para reproduzir

1. Abra um pedido pendente na Screen `OrderDetails`.
2. Abra o `OrderApprovalDialog`.
3. Clique em **Approve** e espere a aprovação retornar.
4. Observe que o indicador de carregamento e o modal continuam visíveis.
5. Atualize a tela e confirme que o status do pedido é **Approved**.

### Evidências a fornecer

Comece pelo fluxo da ação `SubmitApproval`, pela definição do evento
`ApprovalCompleted`, pelo handler na Screen pai e pelas expressões que controlam
o carregamento e a visibilidade do modal. Acrescente o tratamento de erro e logs
sanitizados relevantes.

O cenário é fictício. O comportamento relatado não estabelece a causa. Veja o
[passo a passo completo](../examples/loading-and-modal.md) para avaliar a
resposta e validar a correção proposta.
