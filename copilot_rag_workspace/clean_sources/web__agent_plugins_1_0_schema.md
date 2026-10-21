# Official JSON Schema: agent_plugins_1_0_schema

```json
{
  "$id": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "description": "Machine-readable schema for plugin.json in Agent Plugins 1.0.0. The Agent Plugins specification defines additional semantic and operational requirements.",
  "properties": {
    "$schema": {
      "const": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
      "description": "Canonical identifier of the plugin manifest schema for the Agent Plugins version targeted by this document."
    },
    "author": {
      "additionalProperties": false,
      "properties": {
        "email": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "description": {
      "type": "string"
    },
    "extensions": {
      "additionalProperties": {
        "type": "object"
      },
      "description": "Client-specific manifest data keyed by reverse-domain extension namespace. Agent Plugins assigns no semantics to namespace object contents.",
      "type": "object"
    },
    "homepage": {
      "type": "string"
    },
    "keywords": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "license": {
      "type": "string"
    },
    "name": {
      "description": "Human-readable plugin name.",
      "maxLength": 64,
      "minLength": 1,
      "pattern": "^(?!.*(?:--|\\.\\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$",
      "type": "string"
    },
    "repository": {
      "type": "string"
    },
    "version": {
      "type": "string"
    }
  },
  "required": [
    "$schema",
    "name"
  ],
  "title": "Agent Plugins Manifest",
  "type": "object"
}
```
