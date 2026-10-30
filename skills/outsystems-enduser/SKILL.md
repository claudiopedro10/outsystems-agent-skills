---
name: outsystems-enduser
description: "Revise telas, jornadas e consumo de serviços na camada End User do OutSystems 11, considerando o tipo de aplicação; adapte explicitamente para ODC."
---

# End User

## Escopo e contexto

Confirme OutSystems 11 ou ODC, versão conhecida, tipo de aplicação, objetivo e restrições. A organização Foundation/Core/End User tem como referência O11. Em ODC, adapte somente com evidência e documentação aplicável; não transfira automaticamente recursos e nomes de ferramentas.

Trabalhe com inventário, contratos, trechos, capturas ou logs sanitizados fornecidos ou acessíveis por ferramentas autorizadas. Não presuma acesso à plataforma nem capacidade de interpretar OML/OAP. Peça apenas as informações que mudam a análise.

## Procedimento

1. Mapeie jornada, perfis e estados: carregando, vazio, sucesso, erro e indisponibilidade.
2. Mantenha apresentação e orquestração da jornada na interface. Identifique regras que precisam ser garantidas no servidor e contratos de negócio que devem ser consumidos.
3. Examine validação de entrada, mensagens acionáveis, navegação por teclado, rótulos e foco. Evite afirmar conformidade de acessibilidade sem avaliação.
4. Analise quando dados são buscados, paginação, solicitações redundantes e submissões repetidas. Não recomende recursos de Reactive, Traditional ou Mobile como se fossem intercambiáveis.
5. Revise exposição de dados, identificadores e estado local; autorização precisa ser verificada no servidor. Para Mobile/offline, confirme sincronização e conflitos antes de sugerir solução.

## Entrega

Jornada revisada, estados da tela, fronteira entre cliente e servidor, contratos necessários e critérios de aceitação.

Vincule achados às evidências consultadas; separe fatos, inferências e lacunas. Cite documentação oficial para recursos específicos quando disponível; nunca invente links ou números de linha. Responda no idioma do usuário. Proponha ações compatíveis com o pedido; esta skill não concede acesso nem autorização para editar ou publicar aplicações.

## Exemplo de pedido

> Revise uma tela de aprovação de pedidos em Reactive Web: carregamento, lista vazia, falha do servidor e clique duplo no botão Aprovar.
