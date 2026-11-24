# Ler uma Server Action pelo MCP do Service Studio

Com o módulo aberto no Service Studio e o MCP Server ligado, inicie uma
conversa e cole o prompt abaixo. Os nomes `BibliotecaDemo_CS` e
`ConsultarDisponibilidadeLivro` são fictícios. Troque-os pelos nomes do seu
ambiente ao fazer o teste.

```text
Leia somente a Server Action ConsultarDisponibilidadeLivro do módulo BibliotecaDemo_CS.
Use apenas as ferramentas de leitura anunciadas pelo MCP do Service Studio, com os parâmetros declarados por elas. Se precisar da key do módulo, consulte-a primeiro pelo MCP. Não use PowerShell nem qualquer comando de terminal para testar ou se conectar ao MCP.

Se faltar uma ferramenta necessária, pare e informe qual operação ficou bloqueada. Se uma chamada falhar, pare na primeira falha e informe a ferramenta, os argumentos e o erro retornado, ocultando credenciais e dados sensíveis. Depois me peça para conferir se o MCP Server está ligado no Service Studio e se o endereço registrado está certo.

Ao concluir a leitura, mostre o nome da ação e um detalhe do fluxo presente no retorno. Se o retorno não contiver o fluxo, informe essa limitação sem inferir o comportamento pelo nome da ação.
```

Se o agente responder com o nome da ação e um detalhe real do fluxo, a conexão
está funcionando. Se ele tentar abrir um terminal ou rodar PowerShell, pare a
execução: as skills proíbem isso, e é sinal de que a skill não foi carregada.
