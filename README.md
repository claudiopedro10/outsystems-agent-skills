# OutSystems Agent Skills

**Skills de IA para transformar contexto técnico em decisões de arquitetura, implementação e diagnóstico no OutSystems.**

Biblioteca aberta da comunidade para desenvolvedores, tech leads e arquitetos. Instruções reutilizáveis em Markdown, organizadas por responsabilidade e utilizáveis em diferentes assistentes.

> Projeto independente, sem afiliação ou endosso da OutSystems ou dos fornecedores de IA. Primeira versão: skills iniciais para revisão e evolução pela comunidade. Não há benchmark de produtividade ou certificação de compatibilidade.

## Por que usar?

- **Consistência:** explicita o contexto e os critérios que a IA deve considerar.
- **Menos respostas genéricas:** pede evidências, identifica lacunas e diferencia fatos de hipóteses.
- **Responsabilidades claras:** ajuda a discutir Foundation, Core e End User.
- **Resultados revisáveis:** recomendações incluem justificativa, impacto e como verificar.
- **Portabilidade:** cada pasta reúne as instruções necessárias; o conteúdo também pode ser usado manualmente em chats.

As skills orientam o agente. Não conectam automaticamente ao Service Studio, não leem arquivos OML por conta própria e não publicam aplicações. O acesso depende das ferramentas e permissões disponíveis.

## Comece em 5 minutos

1. Escolha uma skill no catálogo abaixo.
2. Leia o arquivo `SKILL.md` antes de utilizá-lo.
3. Siga o [guia do seu agente](docs/agents.md) ou copie o conteúdo da skill para uma conversa.
4. Informe plataforma, tipo de aplicação, objetivo e evidências sanitizadas.
5. Revise o resultado e valide as alterações em desenvolvimento.

**Exemplo de pedido após carregar a skill:**

```text
Use outsystems-architecture.
Plataforma: OutSystems 11, Reactive Web.
Objetivo: revisar as dependências de um fluxo de pedidos.
Módulos: Orders_UI (telas), Orders_CS (regras e entidades),
ERP_IS (REST), Shared_UI (componentes visuais).
Dependências: Orders_UI -> Orders_CS -> ERP_IS;
ERP_IS -> Orders_UI.
Analise o ciclo, proponha responsabilidades e uma migração incremental.
Não altere nem publique nada. Diferencie evidências e hipóteses.
```

Veja a [análise ilustrativa desse exemplo](examples/architecture-review.md).

## Catálogo inicial

| Skill | Quando usar |
| --- | --- |
| [Foundation](skills/outsystems-foundation/SKILL.md) | Integrações, adaptadores e capacidades técnicas reutilizáveis |
| [Core](skills/outsystems-core/SKILL.md) | Entidades, regras de negócio e serviços de domínio |
| [End User](skills/outsystems-enduser/SKILL.md) | Telas, jornadas, estados de interface e consumo de serviços |
| [Arquitetura](skills/outsystems-architecture/SKILL.md) | Responsabilidades, dependências, ciclos e evolução modular |
| [Troubleshooting](skills/outsystems-troubleshooting/SKILL.md) | Diagnóstico com sintomas, logs e reprodução |
| [Segurança](skills/outsystems-security/SKILL.md) | Revisão de autenticação, autorização e proteção de dados |

**Escopo:** a organização em três camadas é uma referência de OutSystems 11. Em ODC, as skills exigem adaptação explícita às aplicações, bibliotecas e recursos existentes; não tratam módulos, ferramentas ou mecanismos de O11 como equivalentes automáticos.

## Documentação

- [Como utilizar e avaliar os resultados](docs/usage.md)
- [Claude, Codex, Gemini, DeepSeek, Kimi e outros agentes](docs/agents.md)
- [Estrutura e critérios de qualidade de uma skill](docs/skill-design.md)
- [Fontes e verificação da documentação](docs/sources.md)
- [Próximas etapas](ROADMAP.md)
- [Como contribuir](CONTRIBUTING.md)
- [Tratamento de informações sensíveis](SECURITY.md)

## Estrutura

```text
skills/
  outsystems-foundation/SKILL.md
  outsystems-core/SKILL.md
  outsystems-enduser/SKILL.md
  outsystems-architecture/SKILL.md
  outsystems-troubleshooting/SKILL.md
  outsystems-security/SKILL.md
docs/
  agents.md
  usage.md
  skill-design.md
  sources.md
examples/
  architecture-review.md
```

## Idioma e licença

Conteúdo inicial em português brasileiro. As skills devem responder no idioma solicitado pelo usuário. Contribuições e traduções são bem-vindas.

Licença [MIT](LICENSE). OutSystems e nomes de produtos pertencem aos respectivos titulares.
