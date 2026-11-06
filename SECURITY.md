# Security and data handling

The skills are text instructions. Maintainer-only Python tests validate local
repository files and disposable fixtures; they make no network or MCP calls.
There is no MCP implementation, telemetry, or conversation storage in this
library. External AI hosts and MCP tools have their own permissions and data
policies.

Review skill content and your AI provider's data policies before use. Share only sanitized evidence. Do not publish passwords, tokens, session cookies, personal data, or confidential information in issues or examples.

If an instruction could lead to data exposure or an unintended change, do not post sensitive details in a public issue. Use GitHub private vulnerability reporting only if it is enabled. Public issues and pull requests are disabled; do not publish sensitive details through commit comments or other public channels. If no private reporting channel is available, do not disclose the sensitive content publicly.

If a secret has been exposed, revoke it in the originating service. Removing text from Git does not invalidate a credential.
