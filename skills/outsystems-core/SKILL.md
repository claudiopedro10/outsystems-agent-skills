---
name: outsystems-core
description: "Modele ou revise entidades, invariantes e serviços de negócio na camada Core do OutSystems 11; adapte os conceitos para ODC."
---

# Core

## Escopo e contexto

Confirme OutSystems 11 ou ODC, versão conhecida, tipo de aplicação, objetivo e restrições. A organização Foundation/Core/End User tem como referência O11. Em ODC, adapte somente com evidência e documentação aplicável; não transfira automaticamente recursos e nomes de ferramentas.

Trabalhe com inventário, contratos, trechos, capturas ou logs sanitizados fornecidos ou acessíveis por ferramentas autorizadas. Não presuma acesso à plataforma nem capacidade de interpretar OML/OAP. Peça apenas as informações que mudam a análise.

## Procedimento

1. Identifique o domínio, o dono dos dados, as invariantes e os consumidores. Separe regras persistentes de decisões de apresentação.
2. Defina entradas, saídas e pré/pós-condições dos serviços. Evite expor entidades e operações de escrita amplas quando o contrato de negócio puder ser mais restrito.
3. Examine autorização no servidor, transações, concorrência e execução repetida. Não trate esconder um botão como validação de negócio.
4. Analise impacto em dados existentes, nulabilidade, índices e consumidores antes de propor mudança de entidade. Explicite estratégia de migração e reversão quando aplicável.
5. Não afirme atomicidade entre banco e sistema externo sem evidência do mecanismo. Defina como inconsistências serão identificadas e reconciliadas.

## Entrega

Modelo de domínio, invariantes, contratos, riscos de migração e cenários de teste positivos, negativos e concorrentes.

Vincule achados às evidências consultadas; separe fatos, inferências e lacunas. Cite documentação oficial para recursos específicos quando disponível; nunca invente links ou números de linha. Responda no idioma do usuário. Proponha ações compatíveis com o pedido; esta skill não concede acesso nem autorização para editar ou publicar aplicações.

## Exemplo de pedido

> Revise ApproveOrder(OrderId): apenas pedidos pendentes podem ser aprovados e o autor deve ser registrado. Considere duas aprovações simultâneas.
