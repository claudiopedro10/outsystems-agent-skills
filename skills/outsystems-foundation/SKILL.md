---
name: outsystems-foundation
description: "Projete ou revise integrações e capacidades técnicas reutilizáveis na camada Foundation do OutSystems 11; adapte a análise explicitamente para ODC."
---

# Foundation

## Escopo e contexto

Confirme OutSystems 11 ou ODC, versão conhecida, tipo de aplicação, objetivo e restrições. A organização Foundation/Core/End User tem como referência O11. Em ODC, adapte somente com evidência e documentação aplicável; não transfira automaticamente recursos e nomes de ferramentas.

Trabalhe com inventário, contratos, trechos, capturas ou logs sanitizados fornecidos ou acessíveis por ferramentas autorizadas. Não presuma acesso à plataforma nem capacidade de interpretar OML/OAP. Peça apenas as informações que mudam a análise.

## Procedimento

1. Mapeie sistema externo, operação, contrato, autenticação, limites, timeout, retentativas e responsabilidade por erros.
2. Separe adaptação técnica de decisões de negócio. Não coloque aprovações, preços ou políticas de domínio no adaptador apenas por conveniência.
3. Examine idempotência, duplicação, paginação, indisponibilidade e mudanças de contrato. Só proponha retentativa automática para falhas transitórias e operações cuja repetição seja segura.
4. Considere onde as credenciais são resolvidas e quem pode consultá-las. Não inclua segredos em URLs, respostas ou logs.
5. Defina contrato público mínimo, mapeamento de erros e impacto nos consumidores. Confirme a existência de configurações específicas na documentação da plataforma antes de citá-las.

## Entrega

Contrato proposto, responsabilidades, tabela de falhas e tratamento, impacto nos consumidores e cenários de validação.

Vincule achados às evidências consultadas; separe fatos, inferências e lacunas. Cite documentação oficial para recursos específicos quando disponível; nunca invente links ou números de linha. Responda no idioma do usuário. Proponha ações compatíveis com o pedido; esta skill não concede acesso nem autorização para editar ou publicar aplicações.

## Exemplo de pedido

> Revise uma integração de criação de pedidos com ERP. Há timeout após envio; não sabemos se o ERP criou o pedido. Proponha como evitar duplicação.
