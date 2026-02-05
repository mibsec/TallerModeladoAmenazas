# ☁️ Workshop: Cloud Architecture & Threat Modeling

Este repositorio contiene los entornos de laboratorio para el taller práctico de **Auditoría de Infraestructura y Seguridad en Contenedores**.

El proyecto consta de dos escenarios distintos que simulan aplicaciones reales ("Legacy" y "Moderna") para realizar actividades de:

1.  **Arquitectura Forense:** Análisis de infraestructura desconocida.
2.  **Modelado de Amenazas:** Identificación de vectores de ataque.
3.  **Remediación:** Hardening y corrección de código.

⚠️ **DISCLAIMER:** Este código ha sido diseñado **exclusivamente con fines educativos**. Contiene configuraciones y patrones intencionalmente vulnerables. **NO** desplegar en entornos productivos ni exponer a Internet pública.

---

## 📋 Requisitos Previos

Para ejecutar los laboratorios necesitas tener instalado:

- **Docker Desktop** (o Docker Engine + Docker Compose).
- **Git**.
- Un editor de código (VS Code recomendado).
- Acceso a una IA Generativa (ChatGPT, Claude, Gemini) para las actividades del taller.

---

## 📂 Estructura del Proyecto

El repositorio está dividido en dos niveles de dificultad:

### 🟢 Nivel 1: Shadow Shop (`/level-1-shadow-shop`)

Una aplicación monolítica antigua heredada de un equipo previo.

- **Stack:** Python (Flask), PostgreSQL.
- **Objetivo:** Análisis de infraestructura básica y código legacy.

### 🔴 Nivel 2: PayFast Core (`/level-2-payfast-core`)

Una simulación de una Fintech moderna basada en microservicios.

- **Stack:** Python, Traefik (Proxy), Redis, PostgreSQL.
- **Arquitectura:** Malla de servicios, segmentación de redes y workers asíncronos.

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

## 🛠️ Solución de Problemas

- **Puertos ocupados:** Asegúrate de no tener otros servicios corriendo en el puerto `5000` (Nivel 1) u `80/8080` (Nivel 2).
- **Errores de Docker:** Si tienes problemas de permisos con el socket de Docker, asegúrate de que tu usuario tenga permisos para ejecutar comandos docker o ejecuta el terminal como administrador.
- **Limpieza:** Para detener y limpiar todo al finalizar el taller:
  ```bash
  docker-compose down -v
  ```

---

## 📝 Licencia

Este material es de libre uso para fines educativos y de capacitación en ciberseguridad.
