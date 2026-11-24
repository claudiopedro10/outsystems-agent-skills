# Exemplo: ciclo de dependência entre integração e interface

Cenário sintético; análise ilustrativa, não um teste numa aplicação real.

## Entrada

OutSystems 11 / Reactive Web.

- Módulo-alvo: Orders_UI (ponto de partida da revisão entre módulos).
- Aplicação: Desconhecida.
- Módulos abertos: Desconhecido; nenhuma leitura MCP foi feita.
- Módulos relacionados: Orders_CS, ERP_IS, Shared_UI (inventário informado).

- Orders_UI: telas. Camada: End User.
- Orders_CS: regras e entidades de pedido. Camada: Core.
- ERP_IS: integração REST com um ERP. Camada: Foundation.
- Shared_UI: componentes visuais. Camada: Não sei; avaliar as responsabilidades.
- Dependências informadas: Orders_UI -> Orders_CS -> ERP_IS -> Orders_UI.

Skill: `outsystems-architecture`.

Numa revisão real em O11, confira a [configuração do MCP do Service Studio](../docs/service-studio-mcp.md)
e inspecione o módulo aberto com as ferramentas de leitura. Confirme os outros
módulos separadamente; não deduza o conteúdo deles a partir de um módulo aberto.
Este exemplo traz um inventário sintético e não é resultado do MCP.

## Análise esperada

**Evidência:** as direções de dependência informadas formam um ciclo. ERP_IS
depende de um consumidor de interface.

**Interpretação:** Orders_UI pertence a End User; Orders_CS representa Core;
ERP_IS representa Foundation. Shared_UI precisa ser inspecionado para saber se
os componentes são técnicos ou contêm comportamento de negócio. Sufixos não
provam responsabilidade.

**Proposta:** identifique o elemento que ERP_IS consome de Orders_UI. Se for um
contrato de dados, avalie movê-lo para o dono adequado e atualizar os
consumidores. Se for uma notificação visual, devolva um resultado técnico e
deixe a interface decidir a apresentação. Entenda a semântica antes de mover um
fluxo inteiro.

**Sequência:** levantar o elemento compartilhado; definir um contrato
compatível; atualizar ERP_IS e os consumidores; remover a dependência reversa;
validar o fluxo do usuário e as regressões.

**Validação:** o grafo atualizado não tem mais o ciclo; pedidos válidos e falhas
do ERP continuam tratados; as telas não recebem detalhes de implementação do ERP.

**Informação faltante:** nenhuma ação, contrato, referência ou métrica real foi
fornecida. A classificação é preliminar. O impacto em desempenho e a
compatibilidade final não podem ser estabelecidos.
