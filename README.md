# SentinelData AI 🛡️

SentinelData AI es una API de seguridad inteligente diseñada para analizar archivos y detectar automáticamente fugas de datos sensibles (PII) y secretos (como API Keys o tokens de acceso). Este proyecto ha sido construido aplicando **Clean Architecture** y altos estándares de seguridad y desarrollo.

## 🚀 Características Principales

- **Detección de PII y Secretos:** Identifica información como correos electrónicos, tarjetas de crédito, y llaves de acceso a plataformas Cloud (AWS, Google Cloud).
- **Validación Robusta de Archivos:** Verifica el contenido real de los archivos usando *Magic Numbers* (`python-magic`), previniendo bypass por extensión.
- **Seguridad Integrada:** Middlewares de protección (CORS restrictivo, validación de Trusted Hosts), y ejecución en contenedores sin permisos de usuario root.
- **Preparado para Integración con IA:** Módulos listos para incorporar modelos fundacionales (como Google Gemini) para análisis contextual de los documentos.

## 🏗️ Arquitectura del Proyecto

El proyecto sigue el patrón de **Clean Architecture**, asegurando escalabilidad, mantenibilidad y separación de responsabilidades:

```text
sentinel-data-ai/
├── app/
│   ├── main.py                 # Punto de entrada de la aplicación FastAPI
│   ├── api/
│   │   └── endpoints.py        # Controladores (Rutas REST) para recepción de archivos
│   ├── core/
│   │   ├── config.py           # Gestión centralizada de variables de entorno (Pydantic Settings)
│   │   └── security.py         # Configuración de middlewares y reglas de protección
│   ├── models/
│   │   └── schemas.py          # Definición estricta de esquemas Pydantic para Request/Response
│   ├── services/
│   │   └── analyzer.py         # Lógica de negocio (Expresiones regulares y futura conexión a IA)
├── Dockerfile                  # Receta de construcción segura del contenedor
├── requirements.txt            # Dependencias de Python
└── .env                        # Variables de entorno (No subido al repositorio)
```

## 🔒 Estándares de Seguridad Implementados

1. **Sin ejecución en el Shell:** Se evita cualquier tipo de ejecución de procesos mediante `shell=True` o funciones como `eval()`.
2. **Límite de Tamaño de Carga:** Prevención contra ataques de denegación de servicio (DoS) limitando la subida a un máximo de 5MB por archivo.
3. **Contenedores Seguros (Non-Root User):** El `Dockerfile` está diseñado para crear y utilizar un usuario `appuser` del sistema, evitando que la aplicación se ejecute con privilegios administrativos (`root`).
4. **Validación de Magic Numbers:** Uso de `libmagic` para la verificación segura de los tipos MIME en lugar de depender de la extensión que provee el cliente.

## ⚙️ Cómo Ejecutar el Proyecto

### Localmente (con entorno virtual)

1. Clona el repositorio.
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```
3. Instala las dependencias (se requiere `libmagic` instalado en el sistema operativo):
   ```bash
   pip install -r requirements.txt
   ```
4. Configura el archivo `.env` tomando como referencia los parámetros en `app/core/config.py`.
5. Ejecuta el servidor de desarrollo:
   ```bash
   uvicorn app.main:app --reload
   ```

### Usando Docker

Construye y levanta el contenedor con Docker, asegurando un ambiente limpio y replicable:

```bash
docker build -t sentinel-data-ai .
docker run -p 8000:8000 --env-file .env sentinel-data-ai
```

## 📚 Documentación de la API (Swagger UI)

Al levantar la aplicación, FastAPI genera automáticamente la documentación interactiva del proyecto.
Navega a `http://localhost:8000/docs` para ver e interactuar con todos los endpoints.

---
*Desarrollado para la detección inteligente y aseguramiento de información confidencial.*
