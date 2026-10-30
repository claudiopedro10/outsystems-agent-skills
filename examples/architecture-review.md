# Exemplo: ciclo entre integração e interface

**Cenário sintético; análise ilustrativa, não resultado de teste em uma aplicação real.**

## Entrada

OutSystems 11 / Reactive Web.

- Orders_UI: telas.
- Orders_CS: regras e entidades de pedidos.
- ERP_IS: integração REST com ERP.
- Shared_UI: componentes visuais.
- Dependências informadas: Orders_UI -> Orders_CS -> ERP_IS -> Orders_UI.

Skill: `outsystems-architecture`.

## Resultado esperado

**Evidência:** as dependências fornecidas formam um ciclo. ERP_IS depende de um consumidor de interface.

**Interpretação:** Orders_UI pertence a End User; Orders_CS representa Core; ERP_IS representa Foundation. Shared_UI exige examinar se os componentes são técnicos ou contêm comportamento de negócio. Os sufixos não provam a responsabilidade.

**Proposta:** descobrir qual elemento de Orders_UI é usado por ERP_IS. Se for um contrato de dados, avaliar movê-lo para o responsável apropriado e atualizar consumidores. Se for uma notificação visual, devolver um resultado técnico e deixar a interface decidir sua apresentação. Não mover todo o fluxo sem examinar a semântica.

**Sequência:** inventariar o elemento compartilhado; definir contrato compatível; atualizar ERP_IS e consumidores; remover a dependência inversa; validar fluxo e regressões.

**Validação:** o grafo atualizado não contém o ciclo; pedidos válidos e falhas do ERP continuam tratados; as telas não recebem detalhes internos do ERP.

**Lacunas:** não há ações, contratos, referências reais ou métricas. A classificação é preliminar. Não há base para afirmar impacto de performance ou compatibilidade final.
