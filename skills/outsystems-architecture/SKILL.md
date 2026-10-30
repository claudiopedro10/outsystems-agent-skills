---
name: outsystems-architecture
description: "Revise responsabilidades e dependências de aplicações OutSystems, usando o Architecture Canvas em O11 e evitando equivalências automáticas com ODC."
---

# Arquitetura

## Escopo e contexto

Confirme OutSystems 11 ou ODC, versão conhecida, tipo de aplicação, objetivo e restrições. A organização Foundation/Core/End User tem como referência O11. Em ODC, adapte somente com evidência e documentação aplicável; não transfira automaticamente recursos e nomes de ferramentas.

Trabalhe com inventário, contratos, trechos, capturas ou logs sanitizados fornecidos ou acessíveis por ferramentas autorizadas. Não presuma acesso à plataforma nem capacidade de interpretar OML/OAP. Peça apenas as informações que mudam a análise.

## Procedimento

1. Inventarie módulos/aplicações, responsabilidades, elementos públicos e dependências realmente observadas.
2. Em O11, use Foundation para capacidades técnicas, Core para conceitos e serviços de negócio e End User para jornadas e interface. Classifique pelo conteúdo, não apenas pelo nome ou sufixo.
3. Trace consumidores e provedores. Procure ciclos e dependências de camadas inferiores para End User. Examine dependências entre pares e justifique decisões por responsabilidade e acoplamento.
4. Não imponha uma cadeia única para todo consumo: avalie o contrato e o contexto antes de determinar se um acesso é inadequado.
5. Proponha a menor mudança coerente; avalie consumidores, contratos e dados. Prefira migração incremental quando preservar compatibilidade for necessário.
6. Para ODC, descreva a organização real em aplicações/bibliotecas e confirme limites e mecanismos na documentação correspondente.

## Entrega

Inventário classificado, grafo textual de dependências, achados com evidências, proposta incremental e verificação de compatibilidade.

Vincule achados às evidências consultadas; separe fatos, inferências e lacunas. Cite documentação oficial para recursos específicos quando disponível; nunca invente links ou números de linha. Responda no idioma do usuário. Proponha ações compatíveis com o pedido; esta skill não concede acesso nem autorização para editar ou publicar aplicações.

## Exemplo de pedido

> Analise Orders_UI -> Orders_CS -> ERP_IS -> Orders_UI em O11 e proponha como investigar e remover o ciclo.
