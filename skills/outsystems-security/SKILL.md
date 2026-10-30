---
name: outsystems-security
description: "Revise autenticação, autorização e proteção de dados em um fluxo OutSystems com evidências; não equivale a auditoria completa nem certificação."
---

# Segurança

## Escopo e contexto

Confirme OutSystems 11 ou ODC, versão conhecida, tipo de aplicação, objetivo e restrições. A organização Foundation/Core/End User tem como referência O11. Em ODC, adapte somente com evidência e documentação aplicável; não transfira automaticamente recursos e nomes de ferramentas.

Trabalhe com inventário, contratos, trechos, capturas ou logs sanitizados fornecidos ou acessíveis por ferramentas autorizadas. Não presuma acesso à plataforma nem capacidade de interpretar OML/OAP. Peça apenas as informações que mudam a análise.

## Procedimento

1. Delimite atores, dados, fronteiras de confiança e operações privilegiadas.
2. Trace login, sessão e chamadas protegidas a partir dos mecanismos realmente usados. Confirme validação no servidor e autorização por operação e por recurso.
3. Mapeie credenciais e tokens: origem, armazenamento, acesso, transporte, validade, renovação, revogação e logout. Se um aspecto não estiver visível, registre como lacuna.
4. Verifique exposição em logs, URLs, estado do cliente e respostas. Analise consultas parametrizadas e validação de entrada conforme os artefatos disponíveis.
5. Para integrações, examine permissões mínimas, rotação e falhas de autenticação. Não presuma que O11 e ODC compartilham mecanismos de identidade ou configuração.
6. Priorize achados por impacto e possibilidade de exploração, sem atribuir vulnerabilidade sem evidência. Proponha validações em ambiente autorizado; não execute testes invasivos por iniciativa própria.

## Entrega

Fluxo de confiança, mapa de credenciais/tokens, achados sustentados, lacunas e testes de autorização positivos e negativos.

Vincule achados às evidências consultadas; separe fatos, inferências e lacunas. Cite documentação oficial para recursos específicos quando disponível; nunca invente links ou números de linha. Responda no idioma do usuário. Proponha ações compatíveis com o pedido; esta skill não concede acesso nem autorização para editar ou publicar aplicações.

## Exemplo de pedido

> Revise a autorização de consulta de pedidos: o usuário pode alterar o OrderId na requisição. Avalie as verificações de servidor fornecidas.
