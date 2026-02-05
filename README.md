# 🤖 Workshop: Modelado de Amenazas con IA

Bienvenido al repositorio oficial del taller práctico **"Modelado de Amenazas con IA"**.

Este laboratorio contiene entornos vulnerables diseñados para enseñar cómo utilizar Inteligencia Artificial Generativa (LLMs) para acelerar procesos de ciberseguridad, desde el análisis de arquitectura desconocida hasta la remediación de código.

El taller se divide en dos escenarios que simulan infraestructuras reales ("Legacy" y "Moderna"), permitiendo practicar:

1.  **Arquitectura Forense:** Entender sistemas complejos sin documentación previa.
2.  **Red Teaming Asistido:** Identificar vectores de ataque lógicos y de configuración.
3.  **Remediación:** Generar parches y tests de validación automáticos.

⚠️ **DISCLAIMER:** Este código ha sido diseñado **exclusivamente con fines educativos**. Contiene vulnerabilidades críticas intencionales (OWASP Top 10, fallos de configuración). **NO** desplegar en entornos productivos ni exponer a Internet pública.

---

## 📋 Requisitos Previos

Para ejecutar los laboratorios necesitas tener instalado:

- **Docker Desktop** (o Docker Engine + Docker Compose).
- **Git**.
- Un editor de código (VS Code recomendado).
- Acceso a una IA Generativa (ChatGPT, Claude, Gemini) para interactuar durante el taller.

---

## 📂 Estructura del Proyecto

El repositorio está dividido en dos niveles de dificultad:

### 🟢 Nivel 1: Shadow Shop (`/level-1-shadow-shop`)

Una aplicación monolítica heredada ("Legacy") que simula una tienda online antigua.

- **Stack:** Python (Flask), PostgreSQL.
- **Foco:** Vulnerabilidades de infraestructura básica y código inseguro.

### 🔴 Nivel 2: PayFast Core (`/level-2-payfast-core`)

Una simulación de una Fintech moderna basada en microservicios.

- **Stack:** Python, Traefik (Proxy), Redis, PostgreSQL, Docker Networks.
- **Foco:** Vulnerabilidades de lógica de negocio, SSRF y configuraciones de red complejas.

---

## 🚀 Instrucciones de Despliegue

Sigue estos pasos para levantar cada entorno cuando el instructor lo indique.

### Para el Nivel 1 (Shadow Shop)

1.  Navega al directorio:
    ```bash
    cd level-1-shadow-shop
    ```
2.  Construye y levanta los contenedores:
    ```bash
    docker-compose up --build
    ```
3.  La aplicación estará disponible en: `http://localhost:5000`

### Para el Nivel 2 (PayFast Core)

1.  Navega al directorio:
    ```bash
    cd level-2-payfast-core
    ```
2.  Construye y levanta los contenedores:
    ```bash
    docker-compose up --build
    ```
3.  El API Gateway estará disponible en: `http://localhost:80`

---

## 🛠️ Solución de Problemas Comunes

- **Puertos ocupados:** Asegúrate de liberar el puerto `5000` (para el Nivel 1) y los puertos `80/8080` (para el Nivel 2) antes de iniciar.
- **Errores de Permisos:** Si usas Linux y tienes problemas con el socket de Docker, asegúrate de que tu usuario pertenezca al grupo `docker` o ejecuta con `sudo`.
- **Limpieza:** Para apagar y limpiar los contenedores al finalizar:
  ```bash
  docker-compose down -v
  ```

---

## 📝 Licencia

Material de libre uso para fines educativos y de capacitación en ciberseguridad.
