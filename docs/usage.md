# Como utilizar

## Skill, modelo e agente

Uma skill é um conjunto de instruções; um modelo gera respostas; um agente ou aplicativo decide como carregar instruções e usar ferramentas. Usar um modelo DeepSeek em um cliente com suporte a skills é diferente de colar texto no chat DeepSeek.

Escolha uma skill por objetivo. Combine outras apenas se ajudarem a tarefa; carregar todas aumenta o contexto e pode misturar responsabilidades.

## Contexto mínimo

Informe:

- OutSystems 11 ou ODC e versão conhecida; se não souber, declare.
- Reactive Web, Traditional Web, Mobile ou outro tipo aplicável.
- Objetivo e comportamento esperado.
- Evidências: inventário de módulos/aplicações, dependências, ações, entidades, contratos ou logs.
- Restrições: compatibilidade, prazo, volume, integrações e o que pode ser alterado.

Não envie senhas, tokens, cookies, dados pessoais, URLs internas confidenciais ou materiais de clientes sem autorização. Substitua-os por exemplos sintéticos.

## Fluxo recomendado

1. Carregue a skill conforme o [guia de agentes](agents.md).
2. Envie o contexto e defina o resultado desejado.
3. Solicite que o agente declare arquivos/evidências consultados e lacunas.
4. Revise a proposta antes de implementar.
5. Valide em desenvolvimento com cenários positivos e negativos.
6. Registre o que funcionou para melhorar a skill.

## Pedido reutilizável

```text
Use a skill outsystems-core.
Plataforma e tipo: OutSystems 11 / Reactive Web.
Objetivo: modelar aprovação de pedidos.
Regras: somente pedidos pendentes podem ser aprovados;
cada aprovação deve registrar autor e data.
Evidências: entidade Order(Id, Status, Total); ação ApproveOrder(OrderId).
Restrições: preservar o contrato atual.
Entregue proposta, lacunas, impacto e cenários de validação.
Não execute alterações ou publicações.
```

## Como avaliar

Uma boa resposta identifica a plataforma, cita evidências disponíveis, explica responsabilidades e oferece verificação prática. Se faltar informação, deve explicitar o limite em vez de inventar ações ou configurações.

Pedir uma skill pelo nome não comprova que o aplicativo a carregou. Confira o indicador de ativação do agente ou peça a identificação do arquivo e seu escopo. Um agente que não pode ler seus arquivos deve receber o conteúdo manualmente.

## Limites

As skills não substituem a documentação oficial, revisão humana ou testes. A biblioteca não inclui integração MCP, acesso à plataforma ou interpretação nativa de OML/OAP. Screenshots e trechos enviados precisam ser suficientes para a análise; ferramentas externas exigem configuração própria.
