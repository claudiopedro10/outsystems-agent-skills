---
name: outsystems-troubleshooting
description: "Investigue falhas em OutSystems a partir de sintomas, logs e reprodução; use quando for necessário estabelecer a causa antes de propor correções."
---

# Troubleshooting

## Escopo e contexto

Confirme OutSystems 11 ou ODC, versão conhecida, tipo de aplicação, objetivo e restrições. A organização Foundation/Core/End User tem como referência O11. Em ODC, adapte somente com evidência e documentação aplicável; não transfira automaticamente recursos e nomes de ferramentas.

Trabalhe com inventário, contratos, trechos, capturas ou logs sanitizados fornecidos ou acessíveis por ferramentas autorizadas. Não presuma acesso à plataforma nem capacidade de interpretar OML/OAP. Peça apenas as informações que mudam a análise.

## Procedimento

1. Registre esperado, observado, início da falha, frequência, alcance e mudanças recentes.
2. Correlacione evidências por horário, operação e identificadores sanitizados. Em O11, use evidências do Service Center quando fornecidas; em ODC, confirme a ferramenta de observabilidade existente.
3. Monte hipóteses priorizadas com evidência a favor, contra e o próximo teste discriminante. Não apresente correlação como causa.
4. Prefira verificações de leitura e reproduções isoladas. Não recomende repetir uma operação com efeitos financeiros ou persistência sem entender idempotência.
5. Depois de estabelecer uma causa provável, proponha correção proporcional, riscos, reversão e validação de regressão. Se faltar evidência, entregue uma coleta direcionada em vez de inventar diagnóstico.

## Entrega

Linha do tempo, evidências, hipóteses priorizadas, testes discriminantes e correção apenas quando sustentada.

Vincule achados às evidências consultadas; separe fatos, inferências e lacunas. Cite documentação oficial para recursos específicos quando disponível; nunca invente links ou números de linha. Responda no idioma do usuário. Proponha ações compatíveis com o pedido; esta skill não concede acesso nem autorização para editar ou publicar aplicações.

## Exemplo de pedido

> Uma integração passou a falhar intermitentemente após uma publicação. Tenho horários, mensagens sanitizadas e histórico de mudanças. Investigue a causa.
