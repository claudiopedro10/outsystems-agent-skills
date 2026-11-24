# Segurança e tratamento de dados

As skills são instruções em texto. Os testes em Python, só para mantenedores,
validam arquivos locais do repositório e fixtures descartáveis; eles não fazem
chamadas de rede nem ao MCP. Esta biblioteca não tem implementação de MCP,
telemetria nem armazenamento de conversas. Os hosts de IA e as ferramentas MCP
externas têm as suas próprias permissões e políticas de dados.

As skills mandam o agente acessar o Service Studio só pelas ferramentas MCP
registradas, sem PowerShell, terminal ou varredura de portas, e não publicar sem
autorização explícita.

Revise o conteúdo das skills e as políticas de dados do seu fornecedor de IA
antes de usar. Compartilhe só evidências sanitizadas. Não publique senhas,
tokens, cookies de sessão, dados pessoais nem informações confidenciais em
issues ou exemplos.

Se uma instrução puder causar exposição de dados ou uma mudança não pretendida,
não poste detalhes sensíveis publicamente. Use o relato privado de
vulnerabilidades do GitHub só se estiver ativado. Issues e pull requests
públicos estão desativados; não publique detalhes sensíveis em comentários de
commit nem em outros canais públicos. Se não houver canal privado, não divulgue
o conteúdo sensível publicamente.

Se um segredo foi exposto, revogue-o no serviço de origem. Remover o texto do Git
não invalida uma credencial.
