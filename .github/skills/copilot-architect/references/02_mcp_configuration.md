# Módulo 02: Especificación de Configuración MCP Dual y Sandboxing

## 1. La Arquitectura Dual MCP

Para garantizar portabilidad entre el editor VS Code, el Agent Host, el CLI y agentes portables, se deben mantener dos archivos en paralelo:

```
Raíz del Proyecto
├── .mcp.json             <-- Leído por el Agent Host de Copilot, Copilot CLI y agentes portables
└── .vscode/
    └── mcp.json          <-- Leído por el editor VS Code (con sandboxing y variables interactivas)
```

---

## 2. Formato Portable: `.mcp.json` (Raíz)

```json
{
  "mcpServers": {
    "projectTools": {
      "type": "stdio",
      "command": "python",
      "args": ["scripts/tool_server.py"],
      "env": {
        "ENV_MODE": "production"
      }
    }
  }
}
```

---

## 3. Formato Editor con Sandboxing: `.vscode/mcp.json`

```json
{
  "inputs": [
    {
      "id": "vault_api_key",
      "type": "promptString",
      "description": "API Key para servicio externo (almacenada cifrada por el editor)",
      "password": true
    }
  ],
  "servers": {
    "projectTools": {
      "type": "stdio",
      "command": "python",
      "args": ["scripts/tool_server.py"],
      "env": {
        "API_KEY": "${input:vault_api_key}"
      },
      "dev": {
        "watch": "scripts/**/*.py",
        "debug": false
      },
      "sandboxEnabled": true,
      "sandbox": {
        "filesystem": {
          "allowWrite": ["${workspaceFolder}/output", "${workspaceFolder}/tmp"],
          "denyRead": ["~/.ssh", "~/.aws", "${workspaceFolder}/.env"]
        },
        "network": {
          "allowedDomains": [
            "api.github.com",
            "models.inference.ai.azure.com"
          ]
        }
      }
    }
  }
}
```

### Reglas Críticas de Sandboxing
1. **`sandboxEnabled: true`**: Obligatorio en entornos empresariales para restringir la capacidad de escritura de herramientas de terceros.
2. **`allowWrite`**: Debe apuntar exclusivamente a rutas relativas dentro del workspace o carpetas de salida específicas.
3. **`denyRead`**: Protege credenciales de usuario y claves criptográficas (`.ssh`, `.aws`, `.env`).
4. **`allowedDomains`**: Lista blanca para peticiones HTTP salientes generadas por servidores MCP.
