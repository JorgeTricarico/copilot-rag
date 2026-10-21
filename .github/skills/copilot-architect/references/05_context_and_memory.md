# Módulo 05: Gestión de Contexto, Caché y Memoria Persistente

## 1. El Costo del Contexto y Preservación del Prompt Cache

Cada nuevo turno en una conversación con un agente envía el prefijo del sistema, el historial y los fragmentos de código inyectados.

- **Prompt Caching**: Modelos como Claude 3.5/3.7 y GPT-4o aplican descuentos de hasta el 90% en tokens de entrada si el prefijo inicial permanece exactamente idéntico byte por byte.
- **Riesgo de Inyección Dinámica**: Agregar marcas de tiempo cambiantes o estados mutables al inicio del prompt rompe el caché en cada turno.

---

## 2. Umbrales de Compactación Automática y Manual

1. **Umbral del 80%**: Copilot inicia una poda silenciosa de fragmentos intermedios de herramientas antiguas.
2. **Umbral del 95%**: Se activa la compactación forzada agresiva, resumiendo el diálogo anterior y descartando fragmentos de código fuente referenciados.
3. **Comando `/compact`**: Permite al desarrollador forzar la compactación semántica en momentos lógicos (por ejemplo, al concluir una fase de diseño antes de empezar la implementación).

---

## 3. Arquitectura de Memoria Persistente (`/memories/`)

- Directorio local donde el agente almacena directivas de largo plazo y preferencias de proyecto.
- **Regla de las 200 Líneas**: El runtime de Copilot lee de manera prioritaria las primeras 200 líneas de los archivos en `/memories/` para inyectarlas en el contexto de inicio de sesión.
- **Higiene**: Mantener reglas atómicas y eliminar notas transitorias que ya hayan sido resueltas en el código fuente.
