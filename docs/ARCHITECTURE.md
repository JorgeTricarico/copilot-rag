

# Arquitectura de Monitoreo Determinista e Ingeniería de Contexto RAG para el Ecosistema de Agentes de Visual Studio Code Copilot


## Evolución Estructural del Ecosistema Documental y del Agent Harness en VS Code


El ecosistema de inteligencia artificial integrada en Visual Studio Code ha experimentado una transformación arquitectónica profunda, evolucionando desde un asistente de autocompletado en línea hacia una plataforma distribuida de orquestación de agentes autónomos. Esta transición técnica se manifiesta directamente en la obsolescencia de la extensión histórica GitHub.copilot —actualmente deprecada y relegada a un paquete de extensión secundario— en favor de GitHub.copilot-chat como motor primario de interacción, planificación y ejecución de herramientas. Paralelamente, la estructura documental oficial dentro del repositorio microsoft/vscode-docs y del portal code.visualstudio.com ha migrado desde la jerarquía monolítica tradicional (docs/copilot/*) hacia una taxonomía modular dividida en tres dominios especializados: la arquitectura y ejecución operativa de agentes (docs/agents/*), la personalización declarativa del entorno (docs/agent-customization/*) y las interfaces programáticas de extensibilidad (api/extension-guides/ai/*).


Un hallazgo fundamental dentro de la infraestructura del repositorio microsoft/vscode-docs es la existencia de una habilidad interna de auditoría denominada docs-product-alignment, alojada en la ruta .github/skills/docs-product-alignment/SKILL.md. Este artefacto define las directrices mediante las cuales el equipo de ingeniería de Microsoft audita y alinea la documentación frente a los lanzamientos de producto, estableciendo que el contenido técnico sirve simultáneamente a dos audiencias: desarrolladores humanos que leen la prosa explicativa y agentes de inteligencia artificial o indexadores de búsqueda que procesan los campos Keywords, MetaDescriptions y los párrafos de apertura. La especificación de dicha habilidad estructura la evolución continua de la plataforma en cinco áreas de capacidad crítica que determinan las prioridades de monitoreo documental.


| Área de Capacidad Auditada | Alcance Técnico y Mecanismos Documentados | Rutas de Alto Tráfico Prioritarias (microsoft/vscode-docs) |
| --- | --- | --- |
| Agentes | Planificación, implementación, verificación, sesiones paralelas, ejecución local, en segundo plano o en la nube, y soporte para arneses de terceros. | docs/agents/overview.md, docs/copilot/overview.md. |
| Contexto | Búsqueda semántica, inteligencia de lenguaje vía Language Server Protocol (LSP), búsqueda de código en GitHub y conciencia transversal entre repositorios. | docs/agents/reference/workspace-context.md, docs/copilot/concepts/overview.md. |
| Flujo de Trabajo SDLC | Agente de planificación (Plan), agente de implementación (Agent), revisión de código asistida y transferencia de sesiones (handoff) entre entornos. | docs/agents/reference/ai-features-cheat-sheet.md, docs/copilot/getting-started.md. |
| Escala | Manejo de bases de código masivas, monorepositorios, espacios de trabajo multi-raíz (multi-root workspaces) e indexación remota. | docs/agents/best-practices.md, docs/agents/reference/workspace-context.md. |
| Gobernanza Empresarial | Políticas organizacionales, controles de acceso a modelos, exclusiones de contenido y límites de confianza (trust boundaries). | docs/agents/agent-troubleshooting/faq.md, docs/setup/copilot.md. |



Para que un equipo de ingeniería mantenga sus arquitecturas de agentes permanentemente actualizadas y alimente un sistema de Generación Aumentada por Recuperación (RAG) en Google NotebookLM sin sufrir degradación por documentación obsoleta, resulta indispensable comprender primero la anatomía técnica actual del Agent Harness, mapear exhaustivamente las fuentes de verdad tanto en VS Code (microsoft/vscode-docs) como en el ecosistema transversal de GitHub (github/docs), e implementar un sistema determinista de extracción, normalización y verificación criptográfica de cambios.


## Anatomía Técnica del Agent Harness, Gestión de Contexto y Primitivas de Extensibilidad


### Desacoplamiento entre Modelo, Rol, Harness y Entorno de Ejecución


En la arquitectura vigente de Visual Studio Code, el término Agent Harness (arnés del agente) define la capa de software o runtime encargada de ejecutar una sesión de agente. Su función consiste en transformar un modelo de lenguaje (LLM) en un agente operativo conectándolo con el contexto del proyecto y las definiciones de herramientas disponibles, coordinando el bucle iterativo del agente (agent loop: razonamiento, invocación de herramienta, evaluación de permisos, ejecución en el entorno de destino y validación de resultados) y manteniendo el estado de la sesión a lo largo del tiempo.


La ingeniería de sistemas de agentes en VS Code exige distinguir con precisión cuatro componentes ortogonales que frecuentemente se confunden en implementaciones preliminares: el modelo de lenguaje, el rol del agente, el arnés del agente y el entorno de ejecución. El Modelo de Lenguaje (Language Model) actúa exclusivamente como el motor de inferencia y razonamiento; un mismo arnés puede ofrecer múltiples modelos y un mismo modelo puede estar disponible a través de distintos arneses, operando en una ubicación física o nube independiente de donde se ejecutan las herramientas locales. En flujos de trabajo estructurados, el sistema permite incluso asignar modelos diferenciados según la etapa mediante configuraciones específicas, utilizando chat.planAgent.defaultModel para la fase de diseño arquitectónico y la configuración experimental github.copilot.chat.implementAgent.model para la ejecución de los cambios en la misma conversación.


Por su parte, el Rol del Agente (Agent Role) determina qué instrucciones del sistema, herramientas y restricciones de comportamiento se aplican a una tarea específica dentro de la sesión. Entre los roles integrados destacan Ask (restringido estrictamente a herramientas de solo lectura para investigación de código sin capacidad de editar archivos ni ejecutar comandos que alteren el estado), Plan (enfocado en investigación arquitectónica, clarificación de requisitos e identificación de riesgos antes de modificar el código) y Agent (habilitado para mutación de archivos y validación mediante pruebas), a los cuales se suman los agentes personalizados definidos por el usuario en archivos *.agent.md. Cambiar el rol modifica el comportamiento de la tarea dentro del arnés activo, pero en ningún caso reemplaza el arnés subyacente; asimismo, dentro del arnés de Copilot, opciones como Plan y Autopilot operan como modos con flujos de trabajo propios en lugar de roles integrados adicionales.


En un nivel estructural más profundo, el Arnés del Agente (Agent Harness) define el motor de coordinación subyacente (Local, Copilot, Claude, Codex o el arnés del proveedor en la nube), gobernando las capacidades del SDK, las opciones de modelos, los formatos de configuración soportados y el ciclo de vida del proceso. Finalmente, el Entorno de Ejecución (Execution Environment) constituye la infraestructura física o virtual donde se ejecutan las herramientas del espacio de trabajo y se aplican las modificaciones al código, pudiendo ser la máquina local del desarrollador, un contenedor de desarrollo (Dev Container), un host remoto conectado por SSH o túnel de desarrollo mediante el Agent Host Protocol (AHP), o la infraestructura efímera en la nube basada en GitHub Actions.


La selección del arnés altera radicalmente el comportamiento del proceso subyacente y las garantías de continuidad de las sesiones de ingeniería. El análisis detallado de las especificaciones técnicas permite contrastar las cuatro modalidades operativas disponibles en el editor y en la ventana dedicada de Agentes (Agents window, accesible mediante el comando code --agents).


| Dimensión Arquitectónica | Arnés Local | Arnés Copilot | Arneses Claude / Codex | Destino Cloud (Cloud Agents) |
| --- | --- | --- | --- | --- |
| Proceso de Ejecución (Runtime) | Extension Host integrado en VS Code. | Agent Host independiente basado en el Copilot SDK. | Agent Host / Integración nativa con SDK del proveedor. | Infraestructura remota efímera impulsada por GitHub Actions. |
| Persistencia de la Sesión | Vinculada a la ventana del editor; cerrar la ventana detiene el trabajo inmediatamente. | Independiente de la ventana del editor; continúa en segundo plano mientras la aplicación VS Code siga activa. | Ejecución local de herramientas bajo la experiencia de sesión unificada de VS Code. | Ejecución totalmente asíncrona en la nube; límite estricto no extensible de 59 minutos por sesión. |
| Continuidad Multi-Interfaz | Limitada a la sesión local o transferencia (handoff) manual hacia otro destino. | Reanudación nativa entre VS Code, GitHub Copilot CLI (Resume in Terminal) y GitHub Copilot App. | Soporta transferencia de historial desde sesiones locales y ejecución paralela. | Opera sobre una rama de un único repositorio de GitHub y entrega resultados vía Pull Request. |
| Lectura de Configuración MCP | Lee directamente .vscode/mcp.json (soporta ${input:...} e IntelliSense). | Lee el formato portable .mcp.json o ~/.copilot/mcp-config.json; VS Code reenvía servidores desde .vscode/mcp.json salvo los que requieren input interactivo. | Gestionado según las capacidades de herramientas del proveedor en el entorno seleccionado. | Configurado a nivel de repositorio; incluye por defecto el servidor MCP de GitHub acotado al repositorio activo. |
| Autenticación y Facturación | Suscripción de GitHub Copilot o credenciales propias (Bring Your Own Key - BYOK). | Suscripción de GitHub Copilot (ciertas integraciones de Agent Host requieren Copilot Pro+ o cuenta ChatGPT). | Suscripción del proveedor, configuración BYOK de Claude o créditos del plan Copilot según el modo. | Créditos del plan Copilot y minutos de cómputo de GitHub Actions con políticas habilitadas para agentes de terceros. |



Una implicación de segundo orden crítica para la arquitectura de agentes radica en la autonomía del proceso Agent Host frente al editor. Por ejemplo, al configurar el ajuste chat.mcp.autostart en el valor never, únicamente se desactiva el pase de inicio automático del editor, pero esto no impide que una sesión del arnés Copilot inicie sus servidores MCP configurados, dado que el Agent Host administra el ciclo de vida de sus servidores de manera independiente. Asimismo, para sesiones delegadas hacia máquinas remotas, la ventana de Agentes utiliza el Agent Host Protocol (AHP) sobre SSH o túneles de desarrollo (code tunnel o code-insiders tunnel), exponiendo cuatro herramientas internas de orquestación distribuida: list_agent_hosts (para descubrir hosts conectados, modelos disponibles, memoria, CPUs lógicas y carga de sesiones), create_remote_session (que adjudica automáticamente la sesión al host que cumpla los requisitos de sistema operativo y hardware con el menor número de sesiones activas o pendientes), get_remote_session (para inspeccionar el estado y última respuesta) y send_remote_message (para enviar seguimiento o reportar resultados al chat de origen).


### Ingeniería de Contexto, Subagentes, Compactación y Memoria de Tres Niveles


El rendimiento y la precisión determinista de un agente dependen de cómo el arnés ensambla, aísla y depura la ventana de contexto a lo largo de turnos sucesivos. En cada turno, la ventana de contexto aloja cuatro bloques de datos fundamentales: las instrucciones del sistema junto con los esquemas JSON de todas las herramientas habilitadas (que ocupan una fracción fija y permanente de la ventana), los mensajes enviados por el usuario, las respuestas generadas por el modelo y el registro completo de llamadas a herramientas con sus respectivas salidas. Cuando una herramienta lee un archivo extenso o ejecuta un comando de terminal con salida voluminosa, el consumo de tokens se acelera drásticamente. Para evitar la degradación por contaminación de contexto (context pollution) y el agotamiento de la ventana, el ecosistema implementa cuatro mecanismos complementarios de ingeniería de contexto.


El primer mecanismo es el aislamiento de contexto mediante subagentes (Subagents), a través del cual un agente principal delega subtareas acotadas a subagentes que operan en su propia ventana de contexto aislada y devuelven únicamente el resultado sintetizado al hilo principal. En el arnés Local, los subagentes reciben exclusivamente la tarea delegada y las instrucciones aplicables, omitiendo el historial de la conversación principal, y pueden ejecutarse de forma paralela cuando el arnés soporta concurrencia para verificaciones independientes, tales como revisiones simultáneas de rendimiento y corrección lógica. Es fundamental distinguir arquitectónicamente que el aislamiento de contexto no equivale a aislamiento de código: un subagente no crea por sí mismo un árbol de trabajo de Git (Git worktree) ni un sandbox de sistema de archivos a menos que el entorno de ejecución y los controles de permisos así lo definan.


El segundo mecanismo corresponde a la compactación automática y manual (/compact). En sesiones prolongadas del motor de Copilot, cuando la conversación alcanza aproximadamente el 80% de la capacidad de la ventana de contexto, el sistema inicia automáticamente un proceso de compactación en segundo plano, reservando un margen del 20% para que las llamadas a herramientas en curso puedan continuar ejecutándose sin interrupción. Si el consumo de contexto escala hasta el 95% antes de que finalice dicho proceso asíncrono, el motor pausa brevemente la ejecución hasta completar la síntesis estructurada del historial y generar un punto de control (checkpoint). El ingeniero también puede invocar /compact manualmente en cualquier momento añadiendo instrucciones específicas sobre qué información preservar antes de iniciar una nueva fase de implementación. Mientras que los checkpoints del espacio de trabajo permiten revertir ediciones de archivos y turnos de chat (sin deshacer comandos de terminal ya ejecutados ni mutaciones en servicios externos), una compactación completada no es reversible.


El tercer mecanismo se centra en la optimización del caché de prompts mediante el Cache Explorer. Mantener estables los segmentos iniciales del prompt y las instrucciones del sistema entre turnos sucesivos permite reutilizar el caché de prompts del proveedor de IA, reduciendo tanto la latencia como el consumo de créditos del plan. Para auditar este comportamiento, VS Code incorpora la herramienta diagnóstica Cache Explorer, que permite inspeccionar la tasa de aciertos (cache hit rate) y localizar el punto exacto donde se invalida el caché.


Finalmente, el cuarto mecanismo introduce una arquitectura de memoria persistente (/memories/) separada del contexto conversacional efímero. Cuando la herramienta de memoria está habilitada, el agente almacena notas estructuradas localmente en la máquina del desarrollador divididas en tres ámbitos jerárquicos: la Memoria de Usuario (/memories/), que persiste transversalmente en todos los espacios de trabajo y conversaciones, y cuyas primeras 200 líneas se cargan automáticamente al inicio de cada sesión; la Memoria de Repositorio (/memories/repo/), acotada al espacio de trabajo actual y persistente entre distintas conversaciones sobre ese proyecto; y la Memoria de Sesión (/memories/session/), acotada exclusivamente a la conversación activa y purgada de forma automática cuando esta concluye.


### Primitivas de Personalización y Extensibilidad: MCP, Skills, Hooks y Plugins


La configuración avanzada de un arnés de agentes en proyectos profesionales se articula mediante primitivas declarativas basadas en archivos dentro del repositorio o perfil de usuario, complementadas por puntos de contribución programáticos en la API de extensiones de VS Code.


| Primitiva / Componente | Ubicación de Archivos y Esquemas | Alcance y Comportamiento Arquitectónico |
| --- | --- | --- |
| Servidores MCP (Formato VS Code) | .vscode/mcp.json (workspace) o configuración de perfil de usuario. Objeto raíz: "servers": { ... }. | Soporta capacidades específicas del editor: variables de entrada interactivas encriptadas (${input:...}), modo de desarrollo ("dev": { "watch": ..., "debug": ... }) y sandboxing por servidor ("sandboxEnabled": true, con reglas filesystem.allowWrite, filesystem.denyRead y network.allowedDomains). |
| Servidores MCP (Formato Portable Copilot) | .mcp.json (raíz del workspace) o $COPILOT_HOME/mcp-config.json (fallback: ~/.copilot/mcp-config.json). Objeto raíz: "mcpServers": { ... }. | Leído directamente por las sesiones del arnés Copilot (Agent Host), el CLI y agentes portables. Soporta transporte stdio y http (Streamable HTTP / SSE) con flujos OAuth y descubrimiento dinámico de herramientas. |
| MCP Apps (UI Interactiva) | Paquete @modelcontextprotocol/ext-apps (clase App, método connect()). | Renderiza componentes interactivos (formularios, visualizaciones, listas drag-and-drop) directamente en la vista de chat dentro de iframes aislados bajo políticas estrictas de Content Security Policy (CSP). |
| Agent Skills (Estándar Abierto) | Proyecto: .github/skills/, .claude/skills/, .agents/skills/. Usuario: ~/.copilot/skills/, ~/.agents/skills/. | Carpetas autocontenidas con un archivo obligatorio SKILL.md, scripts y recursos adicionales que el agente carga bajo demanda cuando son relevantes para tareas especializadas. Compatible con VS Code, Copilot CLI, Cloud Agent y Code Review. |
| Custom Agents | Directorio agents/*.agent.md. | Define asistentes especializados con instrucciones propias, subconjunto permitido de herramientas, modelo de lenguaje preseleccionado y reglas de transferencia (handoffs). |
| Lifecycle Hooks | hooks.json en la raíz del plugin o en hooks/. | Interceptores de eventos que ejecutan comandos deterministas en puntos críticos del ciclo de vida: preToolUse, postToolUse, subagentStart, subagentStop, inicio/fin de sesión y envío o transformación del prompt del usuario. |
| Plugins (Agent Plugins 1.0 y Legacy) | Manifiesto plugin.json con $schema apuntando a https://agent-plugins.org/schemas/1.0.0/plugin.schema.json. | Empaqueta y distribuye skills/ y mcp.json de forma portable entre clientes compatibles, o combina agentes, hooks y configuraciones LSP (lsp.json). Se instala declarativamente vía enabledPlugins y extraKnownMarketplaces en .github/copilot/settings.json o ~/.copilot/settings.json. |
| Extension AI APIs (VS Code SDK) | package.json (contributes.languageModelTools, mcpServerDefinitionProviders, chatParticipants, languageModelChatProviders). | Registro programático mediante vscode.lm.registerTool (implementando prepareInvocation e invoke), vscode.lm.registerMcpServerDefinitionProvider, vscode.chat.createChatParticipant y vscode.lm.registerLanguageModelChatProvider. |



## Cartografía Exhaustiva de Recursos, Enlaces y Fuentes de Verdad


Para construir un corpus RAG en NotebookLM que abarque la totalidad del conocimiento arquitectónico sobre el arnés, las herramientas y las capacidades de VS Code Copilot, el sistema de extracción debe indexar cuatro clústeres documentales primarios. A diferencia de los enlaces dispersos o heredados de versiones anteriores —donde múltiples rutas históricas bajo /docs/copilot/ redirigen hoy hacia /docs/agents/ o /docs/agent-customization/—, las tablas siguientes consolidan las rutas canónicas activas tanto en su versión web renderizada como en su archivo fuente Markdown dentro de los repositorios oficiales microsoft/vscode-docs y github/docs.


### Clúster 1: Arquitectura de Agentes, Harnesses y Ejecución en VS Code (microsoft/vscode-docs)


| Dominio Funcional | URL Web Canónica (code.visualstudio.com) | Ruta Raw en microsoft/vscode-docs (Rama main) | Valor Arquitectónico para el Corpus RAG |
| --- | --- | --- | --- |
| Visión General de Agentes | https://code.visualstudio.com/docs/agents/overview | docs/agents/overview.md | Marco general de flujos de trabajo, aislamiento en Git worktrees y selección de autonomía. |
| Inicio Rápido de Agentes | https://code.visualstudio.com/docs/agents/quickstart | docs/agents/quickstart.md | Configuración inicial del flujo de trabajo asistido por agentes. |
| Tutorial de Ventana de Agentes | https://code.visualstudio.com/docs/agents/agents-tutorial | docs/agents/agents-tutorial.md | Uso del navegador integrado, selección de elementos DOM como contexto y revisión de diffs. |
| Mejores Prácticas de Agentes | https://code.visualstudio.com/docs/agents/best-practices | docs/agents/best-practices.md | Criterios de elección de arnés, compactación (/compact), Cache Explorer, checkpoints y escala. |
| Conceptos de Agentes y Loop | https://code.visualstudio.com/docs/agents/concepts/agents | docs/agents/concepts/agents.md | Funcionamiento del agent loop, subagentes aislados y los 3 niveles de memoria (/memories/). |
| Conceptos de Agent Harnesses | https://code.visualstudio.com/docs/agents/concepts/agent-harnesses | docs/agents/concepts/agent-harnesses.md | Desacoplamiento entre modelo, rol, arnés y entorno de ejecución; anatomía de un turno. |
| Conceptos de Contexto | https://code.visualstudio.com/docs/agents/concepts/context | docs/agents/concepts/context.md | Ensamblaje de contexto del sistema, descubrimiento dinámico y aislamiento en subagentes. |
| Selección y Operación de Harnesses | https://code.visualstudio.com/docs/agents/run/agent-harnesses | docs/agents/run/agent-harnesses.md | Comparativa operativa entre Local (Extension Host), Copilot (Agent Host), Claude, Codex y Cloud; creación de extensiones Canvas (/create-canvas). |
| Ventana Dedicada de Agentes | https://code.visualstudio.com/docs/agents/run/agents-window | docs/agents/run/agents-window.md | Operación multi-espacio de trabajo con code --agents, quick chats, Dev Containers y creación de PRs. |
| Gestión de Herramientas (Tools) | https://code.visualstudio.com/docs/agents/run/tools | docs/agents/run/tools.md | Invocación con #, edición de parámetros en confirmaciones, ejecución en terminal y tools.terminal.enforceTimeoutFromModel. |
| Flujo de Planificación (Plan Mode) | https://code.visualstudio.com/docs/agents/run/planning | docs/agents/run/planning.md | Uso de /plan, agente de investigación (research agent), Start with Autopilot y ajustes chat.planAgent.defaultModel / additionalTools. |
| Sesiones Remotas y Protocolo AHP | https://code.visualstudio.com/docs/agents/run/remote-agent-sessions | docs/agents/run/remote-agent-sessions.md | Conexión vía Agent Host Protocol (AHP), túneles (code tunnel), cliente web (insiders.vscode.dev/agents) y herramientas de delegación remota. |
| Guías de Ingeniería y TDD | https://code.visualstudio.com/docs/agents/guides/overview | docs/agents/guides/overview.md | Flujos de ingeniería de contexto, desarrollo guiado por pruebas (TDD) y ejecución paralela en worktrees. |



### Clúster 2: Configuración de Contexto, MCP, Personalización y Referencia Técnica (microsoft/vscode-docs)


| Dominio Funcional | URL Web Canónica (code.visualstudio.com) | Ruta Raw en microsoft/vscode-docs (Rama main) | Valor Arquitectónico para el Corpus RAG |
| --- | --- | --- | --- |
| Configuración Inicial y Cuentas | https://code.visualstudio.com/docs/setup/copilot | docs/setup/copilot.md | Autenticación, planes, BYOK, telemetría, GitHub Enterprise (GHE) y preferencias de cuenta por workspace. |
| Contexto en Chat (# y @) | https://code.visualstudio.com/docs/chat/copilot-chat-context | docs/chat/copilot-chat-context.md | Menciones #, adjuntos de Issues/PRs, #fetch, visión multimodal y captura de consola/screenshots del navegador. |
| Servidores MCP (Guía de Gestión) | https://code.visualstudio.com/docs/agent-customization/mcp-servers | docs/agent-customization/mcp-servers.md | Galería @mcp, editor de personalizaciones, MCP Apps y comportamiento de chat.mcp.autostart frente al Agent Host. |
| Referencia de Esquema MCP | https://code.visualstudio.com/docs/agents/reference/mcp-configuration | docs/agents/reference/mcp-configuration.md | Especificación de .vscode/mcp.json vs .mcp.json, reglas de sandbox (allowWrite, allowedDomains), OAuth y modo dev. |
| Instrucciones Personalizadas | https://code.visualstudio.com/docs/agent-customization/custom-instructions | docs/agent-customization/custom-instructions.md | Definición de reglas persistentes de estilo y arquitectura por repositorio o usuario. |
| Referencia de Contexto de Workspace | https://code.visualstudio.com/docs/agents/reference/workspace-context | docs/agents/reference/workspace-context.md | Página de alto tráfico auditada para búsqueda semántica, LSP e indexación remota. |
| Hoja de Referencia de Funciones IA | https://code.visualstudio.com/docs/agents/reference/ai-features-cheat-sheet | docs/agents/reference/ai-features-cheat-sheet.md | Matriz de decisión para elegir la opción menos autónoma que resuelva cada tipo de tarea. |
| Diagnóstico y FAQ de Agentes | https://code.visualstudio.com/docs/agents/agent-troubleshooting/faq | docs/agents/agent-troubleshooting/faq.md | Resolución de problemas de disponibilidad de arneses, políticas corporativas y extensiones. |
| Skill de Auditoría Documental | (Archivo interno de repositorio) | .github/skills/docs-product-alignment/SKILL.md | Fuente meta-arquitectónica que lista las páginas críticas y áreas de capacidad que Microsoft audita en cada lanzamiento. |



### Clúster 3: Especificaciones Transversales de Copilot SDK, CLI, Plugins, Skills y Cloud Agent (github/docs)


Dado que el arnés Copilot en VS Code se ejecuta sobre el Copilot SDK y comparte el motor de sesiones, plugins, skills y hooks con el GitHub Copilot CLI, la GitHub Copilot App y el Copilot Cloud Agent, el cuaderno de NotebookLM requiere incorporar la documentación técnica del repositorio github/docs para cubrir la totalidad del ecosistema.


| Dominio Funcional | URL Web Canónica (docs.github.com) | Ruta Raw en github/docs (Rama main) | Valor Arquitectónico para el Corpus RAG |
| --- | --- | --- | --- |
| Estándar Agent Skills (SKILL.md) | https://docs.github.com/en/copilot/concepts/agents/about-agent-skills | content/copilot/concepts/agents/about-agent-skills.md | Especificación del estándar abierto de carpetas de habilidades (.github/skills, .claude/skills, .agents/skills). |
| Arquitectura de Plugins (Agent Plugins 1.0) | https://docs.github.com/en/copilot/concepts/agents/about-plugins | content/copilot/concepts/agents/about-plugins.md | Esquema plugin.json, integración de agents/, skills/, hooks.json, mcp.json, lsp.json y mercados (enabledPlugins). |
| Gestión de Contexto y Compactación | https://docs.github.com/en/copilot/concepts/agents/copilot-cli/context-management | content/copilot/concepts/agents/copilot-cli/context-management.md | Mecánica exacta de la ventana de contexto, umbrales del 80% y 95% de compactación y checkpoints. |
| Referencia de Lifecycle Hooks | https://docs.github.com/en/copilot/reference/hooks-reference | content/copilot/reference/hooks-reference.md | Especificación de eventos (preToolUse, postToolUse, subagentStart, subagentStop, ciclo de vida de sesión). |
| Copilot SDK y Fleet Mode | https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode | (Árbol content/copilot/how-tos/copilot-sdk/) | Ejecución multi-agente (Fleet Mode), bucle del agente en el SDK, persistencia de sesión, steering y colas. |
| Arquitectura de Cloud Agent | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent | content/copilot/concepts/agents/cloud-agent/about-cloud-agent.md | Entorno efímero en GitHub Actions, límite duro de 59 minutos, copilot-setup-steps.yml y alcance MCP. |
| Automatizaciones en la Nube | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations | content/copilot/concepts/agents/cloud-agent/about-automations.md | Programación recurrente de agentes para mantenimiento, pruebas y notas de lanzamiento. |
| Indexación Semántica de Repositorios | https://docs.github.com/en/copilot/concepts/context/repository-indexing | content/copilot/concepts/context/repository-indexing.md | Funcionamiento del índice semántico de código en GitHub, VS Code y repositorios externos a GitHub. |
| Exclusión de Contenido y Gobernanza | https://docs.github.com/en/copilot/concepts/context/content-exclusion | content/copilot/concepts/context/content-exclusion.md | Filtrado de datos confidenciales en el índice semántico y políticas empresariales. |
| Índice Maestro de Copilot CLI y ACP | https://docs.github.com/en/copilot/how-tos/copilot-cli | content/copilot/how-tos/copilot-cli/index.md | Mapa de rutas hacia Autopilot, Rubber Duck, Research, servidores LSP, servidor ACP y conexión con VS Code. |



### Clúster 4: APIs de Extensibilidad IA y Canales de Detección Temprana (Release Notes y Changelogs)


| Dominio Funcional | URL Web Canónica | Ruta Raw en Repositorio / Feed | Valor Arquitectónico para el Corpus RAG |
| --- | --- | --- | --- |
| API de Chat Participants | https://code.visualstudio.com/api/extension-guides/ai/chat | api/extension-guides/ai/chat.md | Creación de participantes @ con vscode.chat.createChatParticipant y ChatRequestHandler. |
| API de Language Model Tools | https://code.visualstudio.com/api/extension-guides/ai/tools | api/extension-guides/ai/tools.md | Registro de herramientas mediante vscode.lm.registerTool y clase LanguageModelTool. |
| API de Proveedores MCP | https://code.visualstudio.com/api/extension-guides/ai/mcp | api/extension-guides/ai/mcp.md | Registro programático con vscode.lm.registerMcpServerDefinitionProvider y SDK de MCP Apps. |
| API de Modelos de Lenguaje | https://code.visualstudio.com/api/extension-guides/ai/language-model | api/extension-guides/ai/language-model.md | Consumo directo de LLMs desde extensiones de VS Code. |
| Puntos de Contribución (package.json) | https://code.visualstudio.com/api/references/contribution-points | api/references/contribution-points.md | Declaración de promptFiles, languageModelTools, mcpServerDefinitionProviders y proveedores de chat. |
| Notas de Lanzamiento de VS Code | https://code.visualstudio.com/updates | Directorio release-notes/v1_*.md en microsoft/vscode-docs | Detalla cada nuevo ajuste experimental (ej. chat.tools.terminal.enableAutoApprove, chat.planAgent.defaultModel) antes de que llegue a la documentación general. |
| GitHub Changelog (Filtro Copilot) | https://github.blog/changelog/label/copilot/ | Feed RSS: https://github.blog/changelog/label/copilot/feed/ | Fuente oficial de anuncios en tiempo real sobre disponibilidad general (GA) de herramientas (ej. Browser Tools) y retiro de modelos. |



## Diseño del Sistema Determinista de Scraping, Normalización y Hashing Diferencial


### El Problema de la No-Determinicidad en el Scraping Web Tradicional


Cuando un sistema de monitoreo consulta directamente una página web renderizada en https://code.visualstudio.com/docs/... o https://docs.github.com/en/copilot/... y calcula el hash criptográfico sobre el documento HTML crudo, el resultado sufre de falsos positivos constantes. Los portales de documentación modernos inyectan identificadores de sesión, nonces de seguridad (CSP), banners promocionales dinámicos (como anuncios de eventos o botones de descarga de versiones Insiders), menús de navegación laterales que cambian cuando se agrega una página no relacionada en otra sección del sitio, y enlaces interactivos del tipo Open in VS Code o Ask in VS Code Insiders.


Por otro lado, extraer exclusivamente los archivos Markdown crudos desde los repositorios microsoft/vscode-docs y github/docs evita el ruido del DOM HTML, pero introduce un desafío sintáctico propio: los archivos fuente utilizan plantillas Liquid y macros propietarios como {% data variables.product.prodname_vscode_shortname %}, {% data variables.copilot.chat_view %}, {% data reusables.gated-features.copilot-cli %}, kb(workbench.action.chat.open) o setting(chat.planAgent.defaultModel). Si estos marcadores se envían sin procesar a NotebookLM, se degrada la legibilidad semántica del corpus RAG; y si se procesan sin una regla estricta de normalización, cualquier cambio menor de espaciado o salto de línea alteraría el hash.


### Arquitectura de Doble Vía: Canonicalización AST/Texto y Hashing SHA-256


Para lograr un sistema estrictamente determinista, donde el hash cambie única y exclusivamente cuando el contenido semántico o técnico de la documentación se haya modificado, la arquitectura propuesta implementa un motor híbrido estructurado en tres etapas secuenciales. En la primera etapa, correspondiente al descubrimiento dinámico mediante GitHub Git Trees API y RSS, el sistema reemplaza las listas estáticas de URLs —propensas a quedar desactualizadas cuando Microsoft incorpora archivos nuevos bajo docs/agents/ o release-notes/— por consultas directas al endpoint de árboles Git (GET /repos/{owner}/{repo}/git/trees/main?recursive=1) tanto para microsoft/vscode-docs como para github/docs. Esta operación devuelve en una sola respuesta JSON la totalidad de las rutas activas que coinciden con los prefijos de interés (docs/agents/, docs/agent-customization/, docs/copilot/, docs/chat/, api/extension-guides/ai/, release-notes/ y content/copilot/) junto con el hash blob SHA-1 nativo de Git. Si el blob SHA de un archivo en GitHub no ha variado respecto a la ejecución previa registrada en el manifiesto local, el motor omite incluso la descarga del archivo, logrando una verificación de estado en tiempo constante O(1)O(1)O(1).


En la segunda etapa, denominada pipeline de normalización canónica (Liquid Resolver y DOM Scrubber), el sistema procesa el contenido según su formato de origen para extirpar cualquier elemento volátil o cosmético. Para las fuentes Markdown provenientes de los repositorios de GitHub, el texto descargado atraviesa un motor de resolución determinista que traduce las variables Liquid conocidas a sus nombres canónicos (Visual Studio Code, GitHub Copilot, Chat view, Agents window, GitHub Copilot CLI, Copilot cloud agent), transforma las macros de configuración y atajos (setting(x) y kb(y)) en bloques de código en línea legibles, suprime comentarios HTML ocultos, estandariza los saltos de línea al formato LF (\n), aplica normalización Unicode NFKC y colapsa múltiples líneas en blanco consecutivas. Paralelamente, para las fuentes web HTML o feeds RSS consultados en code.visualstudio.com y github.blog/changelog, el analizador sintáctico emplea BeautifulSoup para aislar exclusivamente el nodo contenedor del artículo principal (<main>, <article> o div[role="main"]), destruye mediante decompose() todos los nodos no semánticos (<script>, <style>, <nav>, <header>, <footer>, <aside>, <svg>, <button>, formularios y widgets interactivos de Copy as Markdown u Open in VS Code), convierte el árbol DOM resultante a Markdown estructurado y aplica la misma normalización léxica NFKC.


En la tercera etapa, centrada en la verificación criptográfica SHA-256 y empaquetado diferencial, el sistema calcula el resumen criptográfico sobre el texto limpio y normalizado (TcleanT_{\text{clean}}Tclean​) aplicando la función:
Hdoc=SHA-256(NFKC(Normalize(Tclean)))H_{\text{doc}} = \text{SHA-256}\left(\text{NFKC}\left(\text{Normalize}(T_{\text{clean}})\right)\right)Hdoc​=SHA-256(NFKC(Normalize(Tclean​)))

El valor resultante HdocH_{\text{doc}}Hdoc​ se contrasta contra el registro persistido en state_manifest.json. Si el hash coincide exactamente, el recurso se marca como inalterado (UNCHANGED) y se descarta cualquier iteración posterior sobre ese documento. Si el hash difiere o corresponde a un documento recién descubierto, el sistema reemplaza la copia local limpia, genera un reporte de diferencias línea por línea (unified_diff) para documentar qué parámetros o capacidades cambiaron en la especificación oficial, y marca como pendiente de recompilación (dirty_bundle) únicamente el compendio maestro de NotebookLM afectado por dicha modificación.


### Implementación del Motor en Python (copilot_docs_sync.py)


El siguiente sistema en Python implementa de forma completa el motor determinista de monitoreo, limpieza canónica, verificación de hashes SHA-256, generación de reportes de cambios (changelog_diffs/) y empaquetado automático en compendios listos para Google NotebookLM. El script utiliza tanto la API de árboles Git de GitHub —para descubrir dinámicamente cualquier nuevo documento en microsoft/vscode-docs y github/docs— como el scraping sanitizado para páginas web y el feed oficial del Changelog de Copilot.
Python

```code-container
#!/usr/bin/env python3
"""
Sistema Determinista de Monitoreo Documental y Empaquetado RAG para VS Code Copilot.
Extrae, normaliza, calcula hashes SHA-256 sobre contenido semántico limpio, detecta
modificaciones reales sin falsos positivos y construye compendios para Google NotebookLM.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import logging
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Comment

# Configuración de logging estructurado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("CopilotDocsSync")


# =====================================================================
# 1. DICCIONARIO DE RESOLUCIÓN CANÓNICA PARA MACROS LIQUID Y VSCODE
# =====================================================================
LIQUID_VARIABLES_MAP: Dict[str, str] = {
    "product.prodname_vscode_shortname": "VS Code",
    "product.prodname_vscode": "Visual Studio Code",
    "product.prodname_copilot": "GitHub Copilot",
    "product.prodname_copilot_short": "Copilot",
    "product.prodname_github_codespaces": "GitHub Codespaces",
    "product.prodname_actions": "GitHub Actions",
    "product.prodname_dotcom_the_website": "GitHub.com",
    "product.prodname_ghe_server": "GitHub Enterprise Server",
    "product.prodname_cli": "GitHub CLI",
    "product.github": "GitHub",
    "product.company_short": "GitHub",
    "copilot.chat_view": "Chat view",
    "copilot.agents_window": "Agents window",
    "copilot.copilot_cli": "GitHub Copilot CLI",
    "copilot.copilot_cli_short": "Copilot CLI",
    "copilot.copilot_cloud_agent": "Copilot cloud agent",
    "copilot.copilot_chat": "GitHub Copilot Chat",
    "copilot.copilot_chat_short": "Copilot Chat",
    "copilot.copilot_free_short": "Copilot Free",
    "copilot.copilot_business_short": "Copilot Business",
    "copilot.copilot_enterprise_short": "Copilot Enterprise",
    "copilot.github_copilot_app": "GitHub Copilot app",
    "copilot.copilot_custom_agent_short": "custom agent",
    "copilot.copilot_code-review_short": "Copilot code review",
}


# =====================================================================
# 2. DEFINICIÓN DE FUENTES Y REGLAS DE AGRUPACIÓN PARA NOTEBOOKLM
# =====================================================================
@dataclass
class RepoTreeRule:
    owner: str
    repo: str
    branch: str
    path_prefixes: List[str]
    web_base_url: str
    bundle_router: Dict[str, str]


REPO_RULES: List[RepoTreeRule] = [
    RepoTreeRule(
        owner="microsoft",
        repo="vscode-docs",
        branch="main",
        path_prefixes=[
            "docs/agents/",
            "docs/agent-customization/",
            "docs/copilot/",
            "docs/chat/",
            "docs/setup/copilot.md",
            "api/extension-guides/ai/",
            ".github/skills/docs-product-alignment/SKILL.md",
        ],
        web_base_url="https://code.visualstudio.com/",
        bundle_router={
            "docs/agents/concepts/": "01_Architecture_And_Agent_Harnesses",
            "docs/agents/run/agent-harnesses": "01_Architecture_And_Agent_Harnesses",
            "docs/agents/overview": "01_Architecture_And_Agent_Harnesses",
            "docs/agents/best-practices": "01_Architecture_And_Agent_Harnesses",
            "docs/setup/copilot": "01_Architecture_And_Agent_Harnesses",
            ".github/skills/": "01_Architecture_And_Agent_Harnesses",
            "docs/chat/": "02_Context_Memory_And_Compaction",
            "docs/agents/reference/workspace-context": "02_Context_Memory_And_Compaction",
            "docs/agent-customization/mcp-servers": "03_MCP_Servers_And_Tools_Execution",
            "docs/agents/reference/mcp-configuration": "03_MCP_Servers_And_Tools_Execution",
            "docs/agents/run/tools": "03_MCP_Servers_And_Tools_Execution",
            "docs/agent-customization/": "04_Customization_Skills_Hooks_And_Plugins",
            "docs/agents/run/": "05_Workflows_Planning_And_Remote_AHP",
            "docs/agents/guides/": "05_Workflows_Planning_And_Remote_AHP",
            "docs/agents/": "05_Workflows_Planning_And_Remote_AHP",
            "api/extension-guides/ai/": "06_Extension_AI_APIs_And_Copilot_SDK",
        },
    ),
    RepoTreeRule(
        owner="github",
        repo="docs",
        branch="main",
        path_prefixes=[
            "content/copilot/concepts/agents/",
            "content/copilot/concepts/context/",
            "content/copilot/reference/hooks-reference.md",
            "content/copilot/reference/copilot-cli-reference/",
            "content/copilot/how-tos/copilot-sdk/",
            "content/copilot/how-tos/copilot-cli/index.md",
        ],
        web_base_url="https://docs.github.com/en/",
        bundle_router={
            "content/copilot/concepts/agents/copilot-cli/context-management": "02_Context_Memory_And_Compaction",
            "content/copilot/concepts/context/": "02_Context_Memory_And_Compaction",
            "content/copilot/concepts/agents/about-agent-skills": "04_Customization_Skills_Hooks_And_Plugins",
            "content/copilot/concepts/agents/about-plugins": "04_Customization_Skills_Hooks_And_Plugins",
            "content/copilot/reference/hooks-reference": "04_Customization_Skills_Hooks_And_Plugins",
            "content/copilot/how-tos/copilot-sdk/": "06_Extension_AI_APIs_And_Copilot_SDK",
            "content/copilot/": "05_Workflows_Planning_And_Remote_AHP",
        },
    ),
]

# URLs web directas y feeds de anuncios para detección temprana de cambios
DIRECT_WEB_SOURCES: List[Dict[str, str]] = [
    {
        "id": "vscode_api_contribution_points",
        "url": "https://code.visualstudio.com/api/references/contribution-points",
        "bundle": "06_Extension_AI_APIs_And_Copilot_SDK",
        "type": "html",
    },
    {
        "id": "github_changelog_copilot_rss",
        "url": "https://github.blog/changelog/label/copilot/feed/",
        "bundle": "07_Release_Notes_And_Changelog_Radar",
        "type": "rss",
    },
]


# =====================================================================
# 3. MOTOR DE NORMALIZACIÓN DETERMINISTA Y HASHING SHA-256
# =====================================================================
class ContentCanonicalizer:
    """
    Transforma Markdown con sintaxis Liquid o HTML web dinámico en una
    representación textual estrictamente canónica e invariante a estilos.
    """

    # Expresiones regulares precompiladas para máxima velocidad y determinismo
    RE_LIQUID_DATA = re.compile(
        r"\{%\s*data\s+variables\.([a-zA-Z0-9_.-]+)\s*%\}"
    )
    RE_LIQUID_GENERIC = re.compile(r"\{%.*?%\}")
    RE_VSCODE_KB = re.compile(r"kb\(([a-zA-Z0-9_.-]+)\)")
    RE_VSCODE_KBSTYLE = re.compile(r"kbstyle\(([^)]+)\)")
    RE_VSCODE_SETTING = re.compile(r"setting\(([a-zA-Z0-9_.-]+)\)")
    RE_HTML_COMMENTS = re.compile(r"<!--[\s\S]*?-->")
    RE_FRONTMATTER = re.compile(r"\A---\s*\n([\s\S]*?)\n---\s*\n")
    RE_TRAILING_SPACES = re.compile(r"[ \t]+$", re.MULTILINE)
    RE_MULTI_BLANK_LINES = re.compile(r"\n{3,}")

    @classmethod
    def normalize_markdown(cls, raw_md: str) -> str:
        """Limpia un archivo Markdown crudo de GitHub resolviendo variables y macros."""
        text = raw_md.replace("\r\n", "\n").replace("\r", "\n")

        # 1. Extraer metadatos relevantes del frontmatter YAML (title, description)
        # ignorando campos volátiles de auditoría interna.
        frontmatter_summary = []
        fm_match = cls.RE_FRONTMATTER.search(text)
        if fm_match:
            fm_content = fm_match.group(1)
            for key in ("title", "shortTitle", "intro", "MetaDescription"):
                m = re.search(rf"^{key}:\s*(.+)$", fm_content, re.MULTILINE)
                if m:
                    val = m.group(1).strip().strip("'\"")
                    frontmatter_summary.append(f"**{key}**: {val}")
            text = text[fm_match.end():]

        if frontmatter_summary:
            text = "\n".join(frontmatter_summary) + "\n\n" + text

        # 2. Eliminar comentarios HTML
        text = cls.RE_HTML_COMMENTS.sub("", text)

        # 3. Resolver variables Liquid conocidas de manera determinista
        def _replace_liquid_var(match: re.Match) -> str:
            var_key = match.group(1).strip()
            return LIQUID_VARIABLES_MAP.get(var_key, f"[{var_key}]")

        text = cls.RE_LIQUID_DATA.sub(_replace_liquid_var, text)
        text = cls.RE_LIQUID_GENERIC.sub("", text)

        # 4. Normalizar macros propios de microsoft/vscode-docs
        text = cls.RE_VSCODE_KB.sub(r"`Shortcut: \1`", text)
        text = cls.RE_VSCODE_KBSTYLE.sub(r"`\1`", text)
        text = cls.RE_VSCODE_SETTING.sub(r"`\1`", text)

        # 5. Normalización Unicode NFKC y limpieza de espacios en blanco
        text = unicodedata.normalize("NFKC", text)
        text = cls.RE_TRAILING_SPACES.sub("", text)
        text = cls.RE_MULTI_BLANK_LINES.sub("\n\n", text)
        return text.strip() + "\n"

    @classmethod
    def normalize_html_to_text(cls, raw_html: str) -> str:
        """
        Extrae únicamente el contenido semántico principal de una página HTML,
        eliminando hojas de estilo, scripts, menús y widgets interactivos.
        """
        soup = BeautifulSoup(raw_html, "html.parser")

        # Aislar contenedor principal del artículo
        main_node = (
            soup.find("main")
            or soup.find("article")
            or soup.find("div", attrs={"role": "main"})
            or soup.body
            or soup
        )

        # Eliminar etiquetas ruidosas o dinámicas
        for tag in main_node.find_all(
            [
                "script",
                "style",
                "nav",
                "header",
                "footer",
                "aside",
                "noscript",
                "svg",
                "iframe",
                "button",
                "form",
            ]
        ):
            tag.decompose()

        # Eliminar comentarios del DOM
        for comment in main_node.find_all(
            string=lambda t: isinstance(t, Comment)
        ):
            comment.extract()

        # Eliminar widgets de interfaz de VS Code ("Open in VS Code", "Copy as Markdown")
        UI_NOISE_PATTERNS = {
            "Copy as Markdown",
            "Ask in VS Code",
            "Ask in VS Code Insiders",
            "Open in VS Code",
            "Open in VS Code Insiders",
            "Edit this document",
        }

        lines: List[str] = []
        for element in main_node.find_all(
            ["h1", "h2", "h3", "h4", "p", "li", "pre", "code", "table"]
        ):
            # Evitar duplicar nodos hijos ya procesados dentro de <pre> o <table>
            if element.name == "code" and element.parent.name == "pre":
                continue
            if element.find_parent("table") and element.name != "table":
                continue

            raw_txt = element.get_text(" ", strip=True)
            if not raw_txt or raw_txt in UI_NOISE_PATTERNS:
                continue

            if element.name in ("h1", "h2", "h3", "h4"):
                level = int(element.name[1])
                lines.append(f"\n{'#' * level} {raw_txt}\n")
            elif element.name == "pre":
                code_txt = element.get_text("\n", strip=True)
                lines.append(f"\n```\n{code_txt}\n```\n")
            elif element.name == "li":
                lines.append(f"- {raw_txt}")
            elif element.name == "table":
                for row in element.find_all("tr"):
                    cells = [
                        c.get_text(" ", strip=True).replace("|", "\\|")
                        for c in row.find_all(["th", "td"])
                    ]
                    if cells:
                        lines.append("| " + " | ".join(cells) + " |")
                lines.append("")
            else:
                lines.append(raw_txt)

        joined = "\n".join(lines)
        joined = unicodedata.normalize("NFKC", joined)
        joined = cls.RE_TRAILING_SPACES.sub("", joined)
        joined = cls.RE_MULTI_BLANK_LINES.sub("\n\n", joined)
        return joined.strip() + "\n"

    @classmethod
    def normalize_rss_feed(cls, raw_xml: str, max_items: int = 25) -> str:
        """Convierte el feed RSS del Changelog de GitHub Copilot en Markdown determinista."""
        root = ET.fromstring(raw_xml)
        channel = root.find("channel")
        if channel is None:
            return ""

        items_md: List[str] = ["# GitHub Copilot Official Changelog Feed\n"]
        for item in channel.findall("item")[:max_items]:
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            pub_date = (item.findtext("pubDate") or "").strip()
            desc_html = item.findtext("description") or ""
            clean_desc = cls.normalize_html_to_text(desc_html)
            items_md.append(
                f"## {title}\n- **Date**: {pub_date}\n- **URL**: {link}\n\n{clean_desc}\n"
            )

        joined = "\n".join(items_md)
        joined = unicodedata.normalize("NFKC", joined)
        return cls.RE_MULTI_BLANK_LINES.sub("\n\n", joined).strip() + "\n"

    @staticmethod
    def compute_sha256(clean_text: str) -> str:
        """Calcula el hash criptográfico SHA-256 sobre el texto canónico en UTF-8."""
        return hashlib.sha256(clean_text.encode("utf-8")).hexdigest()


# =====================================================================
# 4. GESTOR DE ESTADO, SINCRONIZACIÓN DIFERENCIAL Y EMPAQUETADO RAG
# =====================================================================
@dataclass
class DocumentRecord:
    doc_id: str
    source_url: str
    Canonical_web_url: str
    bundle_name: str
    git_blob_sha: Optional[str]
    content_sha256: str
    word_count: int
    last_updated_utc: str
    local_clean_path: str


class CopilotDocumentationSynchronizer:
    def __init__(self, base_dir: Path, github_token: Optional[str] = None):
        self.base_dir = base_dir
        self.clean_cache_dir = base_dir / "clean_sources"
        self.bundles_dir = base_dir / "notebooklm_bundles"
        self.diffs_dir = base_dir / "changelog_diffs"
        self.manifest_path = base_dir / "state_manifest.json"

        for d in (self.clean_cache_dir, self.bundles_dir, self.diffs_dir):
            d.mkdir(parents=True, exist_ok=True)

        self.session = requests.Session()
        headers = {
            "User-Agent": "VSCode-Copilot-Deterministic-RAG-Sync/2.0",
            "Accept": "application/vnd.github+json",
        }
        if github_token:
            headers["Authorization"] = f"Bearer {github_token}"
        self.session.headers.update(headers)

        self.manifest: Dict[str, DocumentRecord] = self._load_manifest()
        self.dirty_bundles: set[str] = set()
        self.change_reports: List[str] = []

    def _load_manifest(self) -> Dict[str, DocumentRecord]:
        if not self.manifest_path.exists():
            return {}
        try:
            raw = json.loads(self.manifest_path.read_text(encoding="utf-8"))
            return {
                k: DocumentRecord(**v) for k, v in raw.get("documents", {}).items()
            }
        except Exception as exc:
            logger.warning("Manifiesto previo inválido, iniciando limpio: %s", exc)
            return {}

    def _save_manifest(self) -> None:
        payload = {
            "schema_version": "2.0",
            "last_sync_utc": datetime.now(timezone.utc).isoformat(),
            "total_documents": len(self.manifest),
            "documents": {k: asdict(v) for k, v in sorted(self.manifest.items())},
        }
        self.manifest_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    def _resolve_bundle(self, path: str, router: Dict[str, str]) -> str:
        # Ordenar prefijos de mayor a menor especificidad
        for prefix in sorted(router.keys(), key=len, reverse=True):
            if path.startswith(prefix):
                return router[prefix]
        return "05_Workflows_Planning_And_Remote_AHP"

    def _build_canonical_web_url(self, rule: RepoTreeRule, file_path: str) -> str:
        if file_path.startswith(".github/"):
            return f"https://github.com/{rule.owner}/{rule.repo}/blob/{rule.branch}/{file_path}"
        clean_path = re.sub(r"\.md$", "", file_path)
        if rule.owner == "github" and clean_path.startswith("content/"):
            clean_path = clean_path[len("content/"):]
        if clean_path.endswith("/index"):
            clean_path = clean_path[: -len("/index")]
        return urljoin(rule.web_base_url, clean_path)

    def sync_github_repositories(self, force_recheck: bool = False) -> Tuple[int, int, int]:
        """
        Consulta los árboles Git de microsoft/vscode-docs y github/docs,
        incluyendo las últimas notas de lanzamiento (release-notes/v1_*.md).
        """
        added, updated, skipped = 0, 0, 0

        for rule in REPO_RULES:
            tree_url = f"https://api.github.com/repos/{rule.owner}/{rule.repo}/git/trees/{rule.branch}?recursive=1"
            logger.info("Consultando árbol Git de %s/%s...", rule.owner, rule.repo)
            resp = self.session.get(tree_url, timeout=30)
            resp.raise_for_status()
            tree_data = resp.json().get("tree", [])

            # Seleccionar archivos relevantes según prefijos
            matched_nodes = []
            release_note_nodes = []

            for node in tree_data:
                if node.get("type") != "blob":
                    continue
                path: str = node.get("path", "")
                if not path.endswith(".md"):
                    continue

                if any(path.startswith(p) for p in rule.path_prefixes):
                    matched_nodes.append(node)
                elif rule.repo == "vscode-docs" and re.match(r"^release-notes/v1_\d+\.md$", path):
                    release_note_nodes.append(node)

            # Tomar las 3 versiones más recientes de release-notes de VS Code
            if release_note_nodes:
                release_note_nodes.sort(
                    key=lambda n: int(re.search(r"v1_(\d+)", n["path"]).group(1)),
                    reverse=True,
                )
                matched_nodes.extend(release_note_nodes[:3])

            for node in matched_nodes:
                path = node["path"]
                git_sha = node["sha"]
                doc_id = f"{rule.owner}_{rule.repo}::{path}"
                bundle = (
                    "07_Release_Notes_And_Changelog_Radar"
                    if path.startswith("release-notes/")
                    else self._resolve_bundle(path, rule.bundle_router)
                )

                existing = self.manifest.get(doc_id)

                # Optimización O(1): Si el Git Blob SHA es idéntico, el archivo en
                # el repositorio no ha sufrido ni un solo byte de cambio.
                if (
                    existing
                    and not force_recheck
                    and existing.git_blob_sha == git_sha
                    and (self.base_dir / existing.local_clean_path).exists()
                ):
                    skipped += 1
                    continue

                raw_url = f"https://raw.githubusercontent.com/{rule.owner}/{rule.repo}/{rule.branch}/{path}"
                raw_resp = self.session.get(raw_url, timeout=30)
                raw_resp.raise_for_status()

                clean_text = ContentCanonicalizer.normalize_markdown(raw_resp.text)
                new_sha256 = ContentCanonicalizer.compute_sha256(clean_text)

                if (
                    existing
                    and not force_recheck
                    and existing.content_sha256 == new_sha256
                    and (self.base_dir / existing.local_clean_path).exists()
                ):
                    # El blob de Git cambió por un cambio cosmético/espaciado ignorado,
                    # pero el contenido canónico limpio tiene exactamente el mismo SHA-256.
                    existing.git_blob_sha = git_sha
                    skipped += 1
                    continue

                web_url = self._build_canonical_web_url(rule, path)
                was_added = existing is None
                self._persist_document_change(
                    doc_id=doc_id,
                    source_url=raw_url,
                    web_url=web_url,
                    bundle_name=bundle,
                    git_blob_sha=git_sha,
                    new_sha256=new_sha256,
                    clean_text=clean_text,
                    existing=existing,
                )
                if was_added:
                    added += 1
                else:
                    updated += 1

        return added, updated, skipped

    def sync_direct_web_sources(self, force_recheck: bool = False) -> Tuple[int, int, int]:
        """Sincroniza páginas HTML directas y feeds RSS aplicando limpieza DOM/XML."""
        added, updated, skipped = 0, 0, 0

        for src in DIRECT_WEB_SOURCES:
            doc_id = f"web::{src['id']}"
            url = src["url"]
            bundle = src["bundle"]
            src_type = src["type"]

            logger.info("Verificando fuente web directa: %s", url)
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()

            if src_type == "rss":
                clean_text = ContentCanonicalizer.normalize_rss_feed(resp.text)
            else:
                clean_text = ContentCanonicalizer.normalize_html_to_text(resp.text)

            new_sha256 = ContentCanonicalizer.compute_sha256(clean_text)
            existing = self.manifest.get(doc_id)

            if (
                existing
                and not force_recheck
                and existing.content_sha256 == new_sha256
                and (self.base_dir / existing.local_clean_path).exists()
            ):
                skipped += 1
                continue

            was_added = existing is None
            self._persist_document_change(
                doc_id=doc_id,
                source_url=url,
                web_url=url,
                bundle_name=bundle,
                git_blob_sha=None,
                new_sha256=new_sha256,
                clean_text=clean_text,
                existing=existing,
            )
            if was_added:
                added += 1
            else:
                updated += 1

        return added, updated, skipped

    def _persist_document_change(
        self,
        doc_id: str,
        source_url: str,
        web_url: str,
        bundle_name: str,
        git_blob_sha: Optional[str],
        new_sha256: str,
        clean_text: str,
        existing: Optional[DocumentRecord],
    ) -> None:
        safe_filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", doc_id) + ".md"
        rel_clean_path = Path("clean_sources") / safe_filename
        abs_clean_path = self.base_dir / rel_clean_path

        # Si el archivo ya existía, generar diff semántico exacto
        if existing and abs_clean_path.exists():
            old_text = abs_clean_path.read_text(encoding="utf-8")
            diff_lines = list(
                difflib.unified_diff(
                    old_text.splitlines(),
                    clean_text.splitlines(),
                    fromfile=f"{doc_id} (prev: {existing.content_sha256[:8]})",
                    tofile=f"{doc_id} (new: {new_sha256[:8]})",
                    lineterm="",
                )
            )
            if diff_lines:
                diff_snippet = "\n".join(diff_lines[:120])
                self.change_reports.append(
                    f"### [MODIFICADO] `{doc_id}`\n"
                    f"- **URL Canónica**: {web_url}\n"
                    f"- **Hash Anterior**: `{existing.content_sha256}`\n"
                    f"- **Hash Nuevo**: `{new_sha256}`\n\n"
                    f"```diff\n{diff_snippet}\n```\n"
                )
            logger.info("ACTUALIZADO: %s (Hash: %s)", doc_id, new_sha256[:10])
        else:
            self.change_reports.append(
                f"### [NUEVO RECURSO] `{doc_id}`\n"
                f"- **URL Canónica**: {web_url}\n"
                f"- **Hash Inicial**: `{new_sha256}`\n"
            )
            logger.info("NUEVO: %s (Hash: %s)", doc_id, new_sha256[:10])

        abs_clean_path.write_text(clean_text, encoding="utf-8")
        word_count = len(clean_text.split())

        self.manifest[doc_id] = DocumentRecord(
            doc_id=doc_id,
            source_url=source_url,
            Canonical_web_url=web_url,
            bundle_name=bundle_name,
            git_blob_sha=git_blob_sha,
            content_sha256=new_sha256,
            word_count=word_count,
            last_updated_utc=datetime.now(timezone.utc).isoformat(),
            local_clean_path=str(rel_clean_path),
        )
        self.dirty_bundles.add(bundle_name)

    def build_notebooklm_bundles(self, rebuild_all: bool = False) -> List[Path]:
        """
        Empaqueta los documentos limpios en Compendios Maestros (.md) optimizados
        para Google NotebookLM, verificando el límite de 500,000 palabras por archivo.
        """
        MAX_WORDS_PER_BUNDLE = 450_000  # Margen seguro bajo el tope de 500,000 de NotebookLM
        bundles_map: Dict[str, List[DocumentRecord]] = {}

        for record in self.manifest.values():
            bundles_map.setdefault(record.bundle_name, []).append(record)

        generated_files: List[Path] = []
        target_bundles = (
            set(bundles_map.keys()) if rebuild_all else self.dirty_bundles
        )

        for bundle_name in sorted(target_bundles):
            records = sorted(
                bundles_map.get(bundle_name, []), key=lambda r: r.doc_id
            )
            if not records:
                continue

            part_idx = 1
            current_words = 0
            current_chunks: List[str] = []

            for rec in records:
                abs_path = self.base_dir / rec.local_clean_path
                if not abs_path.exists():
                    continue
                body = abs_path.read_text(encoding="utf-8")

                doc_header = (
                    f"\n\n---\n"
                    f"# DOCUMENT_SOURCE: {rec.doc_id}\n"
                    f"- **CANONICAL_URL**: {rec.Canonical_web_url}\n"
                    f"- **RAW_SOURCE_URL**: {rec.source_url}\n"
                    f"- **SHA256_FINGERPRINT**: `{rec.content_sha256}`\n"
                    f"- **LAST_VERIFIED_UTC**: {rec.last_updated_utc}\n"
                    f"---\n\n"
                )
                full_entry = doc_header + body
                entry_words = rec.word_count + 35

                if current_words + entry_words > MAX_WORDS_PER_BUNDLE and current_chunks:
                    out_path = self._write_bundle_file(
                        bundle_name, part_idx, current_chunks, current_words
                    )
                    generated_files.append(out_path)
                    part_idx += 1
                    current_chunks = []
                    current_words = 0

                current_chunks.append(full_entry)
                current_words += entry_words

            if current_chunks:
                out_path = self._write_bundle_file(
                    bundle_name, part_idx, current_chunks, current_words
                )
                generated_files.append(out_path)

        return generated_files

    def _write_bundle_file(
        self, bundle_name: str, part_idx: int, chunks: List[str], total_words: int
    ) -> Path:
        suffix = f"_part{part_idx}" if part_idx > 1 else ""
        out_path = self.bundles_dir / f"{bundle_name}{suffix}.md"
        master_header = (
            f"# COMPENDIO RAG NOTEBOOKLM: {bundle_name}{suffix}\n"
            f"- **Generado (UTC)**: {datetime.now(timezone.utc).isoformat()}\n"
            f"- **Total Palabras**: {total_words:,} / 500,000 máx.\n"
            f"- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, "
            f"citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` "
            f"declarados en el encabezado de cada sección.\n"
        )
        out_path.write_text(master_header + "".join(chunks), encoding="utf-8")
        logger.info(
            "Compendio generado: %s (%d palabras)", out_path.name, total_words
        )
        return out_path

    def write_audit_report(self, added: int, updated: int, skipped: int) -> Optional[Path]:
        if not self.change_reports:
            logger.info("Sin cambios semánticos detectados. Todos los hashes coinciden.")
            return None

        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        report_path = self.diffs_dir / f"diff_report_{ts}.md"
        header = (
            f"# Reporte de Novedades Documentales VS Code Copilot ({ts} UTC)\n\n"
            f"- **Nuevos Documentos**: {added}\n"
            f"- **Documentos Actualizados**: {updated}\n"
            f"- **Documentos Sin Cambios (Omitidos por Hash)**: {skipped}\n"
            f"- **Compendios de NotebookLM Recompilados**: {', '.join(sorted(self.dirty_bundles))}\n\n"
        )
        report_path.write_text(
            header + "\n".join(self.change_reports), encoding="utf-8"
        )
        logger.info("Reporte de diferencias guardado en: %s", report_path)
        return report_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sincronizador Determinista de Documentación de VS Code Copilot para NotebookLM"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./copilot_rag_workspace"),
        help="Directorio raíz para manifiesto, caché limpio y compendios.",
    )
    parser.add_argument(
        "--force-recheck",
        action="store_true",
        help="Ignorar caché de hashes y recalcular todas las fuentes.",
    )
    parser.add_argument(
        "--rebuild-all-bundles",
        action="store_true",
        help="Regenerar todos los compendios de NotebookLM aunque no haya cambios.",
    )
    args = parser.parse_args()

    github_token = os.environ.get("GITHUB_TOKEN")
    syncer = CopilotDocumentationSynchronizer(
        base_dir=args.output_dir, github_token=github_token
    )

    g_add, g_upd, g_skip = syncer.sync_github_repositories(
        force_recheck=args.force_recheck
    )
    w_add, w_upd, w_skip = syncer.sync_direct_web_sources(
        force_recheck=args.force_recheck
    )

    total_add = g_add + w_add
    total_upd = g_upd + w_upd
    total_skip = g_skip + w_skip

    syncer.build_notebooklm_bundles(rebuild_all=args.rebuild_all_bundles)
    syncer._save_manifest()
    syncer.write_audit_report(total_add, total_upd, total_skip)

    logger.info(
        "Resumen Final -> Nuevos: %d | Actualizados: %d | Sin Cambios (Hash Match): %d",
        total_add,
        total_upd,
        total_skip,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

```


### Automatización Continua mediante GitHub Actions (sync-copilot-rag.yml)


Para que el sistema opere de manera completamente autónoma sin intervención manual y notifique únicamente cuando el hash de un documento cambie, el script anterior se integra en un flujo de trabajo de GitHub Actions que ejecuta la verificación cada 12 horas, actualiza el manifiesto state_manifest.json en el repositorio propio y persiste únicamente los compendios modificados.
YAML

```code-container
name: Deterministic VS Code Copilot Docs RAG Sync

on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:
    inputs:
      force_recheck:
        description: "Recalcular hashes de todas las fuentes"
        required: false
        default: "false"

permissions:
  contents: write

jobs:
  sync-docs:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install requests beautifulsoup4

      - name: Run Deterministic Hash Synchronizer
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          if [ "${{ github.event.inputs.force_recheck }}" = "true" ]; then
            python scripts/copilot_docs_sync.py --output-dir ./copilot_rag_workspace --force-recheck
          else
            python scripts/copilot_docs_sync.py --output-dir ./copilot_rag_workspace
          fi

      - name: Commit and Push only if semantic hashes changed
        run: |
          git config user.name "copilot-rag-bot"
          git config user.email "copilot-rag-bot@users.noreply.github.com"
          git add copilot_rag_workspace/
          if git diff --staged --quiet; then
            echo "Ningún hash SHA-256 cambió. No se requiere commit."
          else
            git commit -m "chore(rag): update VS Code Copilot docs bundles and state manifest"
            git push
          fi

```


## Ingeniería de Empaquetado RAG para Google NotebookLM


### Límites Físicos y Comportamiento de Recuperación en NotebookLM


La arquitectura de Google NotebookLM opera como un entorno RAG estrictamente anclado en las fuentes suministradas (source-grounded), presentando restricciones físicas y de indexación que determinan cómo deben estructurarse los datos antes de su ingesta. Cada documento individual cargado en la plataforma soporta una cota máxima de 500.000 palabras o 200 MB de tamaño de archivo, mientras que las cuentas estándar admiten hasta 50 fuentes por cuaderno. No obstante, el análisis de precisión en sistemas de recuperación demuestra que cargar más de 15 a 20 archivos fragmentados sin una estructura organizativa clara incrementa el ruido de recuperación y degrada la capacidad del modelo para realizar síntesis multidocumento.


Adicionalmente, las fuentes importadas en NotebookLM —incluyendo los documentos vinculados desde Google Drive o las URLs web— constituyen instantáneas estáticas tomadas en el momento de la carga; las modificaciones posteriores en los archivos originales no se sincronizan de forma automática y exigen reemplazar manualmente la fuente afectada en el cuaderno. Aunque NotebookLM admite formatos diversos como PDF, .docx, hojas de cálculo y archivos de audio, el procesamiento de documentación de ingeniería de software y código alcanza su máxima fidelidad al utilizar scripts de empaquetado que concatenan los archivos relacionados en compendios estructurados en formato Markdown (.md) o texto plano (.txt), eliminando el bagaje binario y preservando una jerarquía clara de encabezados (#, ##, ###) que optimiza el particionamiento semántico (chunking) del motor RAG.


### Estructura de los 7 Compendios Maestros y Protocolo de Actualización


El script copilot_docs_sync.py resuelve simultáneamente el límite de 50 fuentes y el problema de la resincronización manual mediante la consolidación de más de 80 documentos técnicos en exactamente 7 Compendios Maestros (.md) alojados en el directorio notebooklm_bundles/.


| Compendio Maestro Generado | Dominios Documentales Consolidados | Uso Estratégico con Casillas de Selección en NotebookLM |
| --- | --- | --- |
| 01_Architecture_And_Agent_Harnesses.md | Conceptos de Agent Harnesses, comparación Local vs Copilot (Agent Host) vs Claude/Codex vs Cloud, mejores prácticas, setup y .github/skills/docs-product-alignment/SKILL.md. | Activar siempre como fuente base para consultas de diseño arquitectónico, elección de arnés y límites de proceso. |
| 02_Context_Memory_And_Compaction.md | Ensamblaje de contexto, menciones # y @, subagentes con aislamiento de contexto, compactación automática (80%/95%) y manual (/compact), Cache Explorer, memoria (/memories/) e indexación semántica. | Activar al diseñar estrategias de reducción de tokens, optimización de caché de prompts o persistencia de memoria entre sesiones. |
| 03_MCP_Servers_And_Tools_Execution.md | Guía de servidores MCP, esquema .vscode/mcp.json vs .mcp.json, reglas de sandbox (allowWrite, allowedDomains), variables ${input:...}, modo dev y gestión de herramientas en el Agent Host. | Seleccionar de forma aislada cuando se requiera generar o validar archivos mcp.json sin interferencia de otros temas. |
| 04_Customization_Skills_Hooks_And_Plugins.md | Instrucciones personalizadas, estándar abierto Agent Skills (SKILL.md), Custom Agents (*.agent.md), Hooks (hooks.json) y especificación Agent Plugins 1.0 (plugin.json). | Activar para generar plantillas declarativas de agentes, habilidades portables, interceptores de seguridad o manifiestos de plugins. |
| 05_Workflows_Planning_And_Remote_AHP.md | Flujo /plan, Autopilot, ventana dedicada code --agents, sesiones remotas por Agent Host Protocol (AHP), túneles, Cloud Agent (59 min timeout) y guías de TDD. | Activar para estructurar flujos de trabajo multi-repositorio, automatizaciones asíncronas y delegación hacia máquinas remotas. |
| 06_Extension_AI_APIs_And_Copilot_SDK.md | Guías de API para extensiones (registerTool, createChatParticipant, registerMcpServerDefinitionProvider, MCP Apps con @modelcontextprotocol/ext-apps) y características del Copilot SDK (Fleet Mode). | Activar exclusivamente cuando se desarrollen extensiones nativas en TypeScript o integraciones sobre el Copilot SDK. |
| 07_Release_Notes_And_Changelog_Radar.md | Últimas 3 notas de lanzamiento de VS Code (release-notes/v1_*.md) y los últimos 25 anuncios oficiales del feed RSS de GitHub Copilot Changelog. | Activar junto con cualquiera de los compendios anteriores para detectar configuraciones experimentales recién lanzadas o modelos próximos a retiro. |



Además de estos siete archivos de datos, resulta altamente efectivo incorporar en el cuaderno un octavo documento estático de gobernanza (00_System_Governance_And_Citation_Rules.md) que instruya a NotebookLM a verificar siempre las afirmaciones sintetizadas contra el bloque DOCUMENT_SOURCE, CANONICAL_URL y SHA256_FINGERPRINT inyectado por el script al inicio de cada sección. De esta manera, cuando el motor detecta que un único documento fuente cambió —por ejemplo, una actualización en docs/agents/reference/mcp-configuration.md—, el conjunto dirty_bundles garantiza que únicamente 03_MCP_Servers_And_Tools_Execution.md sea recompilado; el operador solo reemplaza ese archivo individual en el panel de fuentes de NotebookLM, manteniendo los seis compendios restantes intactos.


## Conclusiones y Recomendaciones Operativas para Arquitecturas de Agentes


El análisis integral de la documentación y del código fuente documental de Visual Studio Code Copilot demuestra que la plataforma ha evolucionado hacia una arquitectura de agentes estandarizada, modular y desacoplada del editor. Para capitalizar de inmediato estas capacidades en proyectos de desarrollo de software y mantener la ventaja competitiva mediante el sistema de monitoreo determinista expuesto, la ingeniería de proyectos debe articular cinco prácticas operativas fundamentales.


En primer lugar, la arquitectura de sesiones debe estandarizarse sobre el arnés Copilot (Agent Host) complementado con una estrategia de configuración MCP dual. Para tareas que requieran persistencia en segundo plano, uso intensivo de herramientas o continuidad con la terminal (GitHub Copilot CLI), el arnés Copilot supera las limitaciones del arnés Local al mantener vivo el proceso aunque se cierre la ventana del editor. En los repositorios del proyecto, las integraciones portables deben definirse en .mcp.json (bajo el objeto mcpServers) para que el Agent Host y los agentes de línea de comandos las consuman directamente, reservando .vscode/mcp.json (bajo el objeto servers) para herramientas que requieran inyección de secretos interactivos (${input:...}), depuración local (dev.watch) o políticas estrictas de aislamiento por sandbox (filesystem.allowWrite, filesystem.denyRead y network.allowedDomains).


En segundo lugar, la personalización del comportamiento de los agentes debe migrar desde archivos monolíticos de instrucciones hacia el estándar abierto de Agent Skills (SKILL.md) y Agent Plugins 1.0 (plugin.json). Concentrar todas las reglas de un proyecto en un único archivo de instrucciones personalizadas consume de manera permanente una fracción fija de la ventana de contexto en cada turno. Al modularizar el conocimiento especializado —como reglas de migración de bases de datos, flujos de desarrollo guiado por pruebas (TDD) o guías de componentes UI— en directorios bajo .github/skills/ o .agents/skills/ con su respectivo SKILL.md, el agente carga dichas instrucciones bajo demanda únicamente cuando la tarea lo requiere, preservando el caché de prompts y retrasando la activación del umbral del 80% de compactación.


En tercer lugar, el diseño de flujos de trabajo complejos debe combinar la planificación de solo lectura con la orquestación de subagentes y la higiene de la memoria persistente (/memories/). Toda modificación multi-archivo debe iniciarse mediante el comando /plan —asignando un modelo de alto razonamiento en chat.planAgent.defaultModel y herramientas adicionales de lectura en github.copilot.chat.planAgent.additionalTools— seguido de la ejecución delegada a subagentes que aíslen el contexto de subtareas paralelas sin contaminar el hilo principal. Asimismo, las invariantes arquitectónicas más críticas del desarrollador deben condensarse en las primeras 200 líneas del directorio /memories/ para garantizar su carga automática en cada nueva sesión.


En cuarto lugar, la delegación autónoma exige instrumentar controles deterministas de seguridad mediante hooks.json y reglas granulares de aprobación automática en terminal. Al habilitar modos como Autopilot o el ajuste chat.tools.terminal.enableAutoApprove, resulta imperativo acotar las rutas y subcomandos permitidos en chat.tools.terminal.autoApprove e implementar interceptores preToolUse, postToolUse, subagentStart y subagentStop en hooks.json. Esta combinación asegura que tanto el agente principal como sus subagentes ejecuten validaciones obligatorias de pruebas y prevengan vectores de inyección de prompts (prompt injection) derivados de peticiones externas mediante curl, wget o Invoke-WebRequest.


Finalmente, la explotación del cuaderno en Google NotebookLM debe aprovechar el filtrado selectivo de fuentes (source checkboxes) junto con los reportes diferenciales generados por copilot_docs_sync.py. Al marcar simultáneamente en la interfaz de NotebookLM el compendio de radar de novedades (07_Release_Notes_And_Changelog_Radar.md) y el compendio técnico específico (03_MCP_Servers_And_Tools_Execution.md o 04_Customization_Skills_Hooks_And_Plugins.md), el arquitecto de software puede solicitar al sistema RAG que contraste los diffs recién detectados por el motor SHA-256 contra la configuración vigente de sus repositorios, generando parches inmediatos y verificados para sus archivos .mcp.json, plugin.json, hooks.json y SKILL.md con trazabilidad absoluta hacia la documentación oficial.


## Documentación Complementaria y Ecosistema Avanzado

Para profundizar en el diseño e implementación de sistemas multi-agente modernos y la evolución futura de este pipeline, consulte los siguientes manuales técnicos de referencia:

1. **[Ecosistema de Agentes: Copilot SDK, Graph-Flows, AI Credits y Orquestación Híbrida](AGENT_ORCHESTRATION_AND_SDK.md)**:
   - Análisis comparativo de frameworks de grafos y flujos: **LangGraph**, **Microsoft AutoGen 0.4**, **LlamaIndex Workflows** y **CrewAI Flows**.
   - Arquitectura del **GitHub Copilot SDK** (`@github/copilot-sdk`), loops autónomos y configuración BYOK (`ProviderConfig`).
   - Estrategia híbrida de consumo de **GitHub Models** y optimización de **AI Credits**.
   - Patrón de ejecución encadenada con intercepción determinista vía lifecycle hooks (`onPreToolUse`, `onPostToolUse`, `onSubagentStart`, `onSubagentStop`).
   - Implementación de referencia funcional en Python.

2. **[Roadmap Técnico de Fases Futuras (Fases 4, 5 y 6)](ROADMAP_FUTURE_PHASES.md)**:
   - Especificación detallada de la **Fase 4 (Zero-Touch Sync en NotebookLM)** mediante `notebooklm-py` y secretos de sesión.
   - Especificación de las **Fases 5 y 6 (Expansión de Cobertura y CI/CD Avanzado)**: monitoreo de repositorios periféricos (`vscode-pull-request-github`, `vscode-dev-containers`) y empaquetado optimizado con Repomix.
