# 🎬 Odoo Movies Project

Módulo personalizado para Odoo que permite la **gestión automatizada de películas** mediante integración con una API externa, y expone un **endpoint REST** para obtener el top 10.

---

## 📌 Características principales

- Consulta periódica (cron job) a un API REST externo de películas.
- Almacenamiento de películas con `Título` y `Ranking`.
- Exposición de un endpoint público REST (`/api/top_movies`).
- Configuración flexible de URL y API Key mediante parámetros del sistema.
- Levantamiento completo del entorno con Docker Compose.
- Cumplimiento de la metodología GitFlow.

---

## 🛠️ Instalación y uso con Docker

### Clonar el proyecto
```bash
git clone https://github.com/therobram/odoo_movies_project.git
cd odoo_movies_project
```

### Construir y levantar contenedores
```bash
docker-compose up --build
```

> Esto levantará Odoo y PostgreSQL. Accede a Odoo desde: `http://localhost:8069`

---

## 🔧 Configuración del Sistema

Los parámetros del sistema necesarios (`movies_api_url` y `movies_api_key`) se crean automáticamente mediante un archivo XML incluido en el módulo al momento de ejecutar `docker-compose`. No es necesario configurarlos manualmente.

---

## ⏱️ Cron Automático

El módulo incluye una tarea programada (`ir.cron`) que consulta periódicamente la API externa cada minuto para obtener una película y guardarla en la base de datos.

---

## 🌐 Endpoint REST

Puedes acceder al top 10 de películas registradas mediante:

```
GET http://localhost:8069/api/top_movies
```

Este endpoint responde con un JSON público sin autenticación.

---

## 🚀 GitFlow aplicado

El proyecto utiliza la metodología GitFlow para la gestión de ramas:

- `main`: versión estable en producción.
- `develop`: rama de desarrollo principal.
- `feature/*`: nuevas funcionalidades.
- `release/*`: preparación para releases.
- `hotfix/*`: correcciones rápidas en producción.

---

## 🧪 Pruebas y validación

- Revisión visual desde el panel de Odoo (menú de películas).
- Validación de logs en consola Docker.
- Pruebas del endpoint REST con herramientas como Postman o Curl.

---

## 📂 Estructura del módulo

```
addons/movies/
├── controllers/
│   └── controllers.py
├── data/
│   ├── cron_data.xml
│   └── movies_data.xml
├── models/
│   └── movie_movie.py
├── views/
│   └── movie_views.xml
├── __manifest__.py
├── __init__.py
```

---

## 📃 Licencia

MIT License.

---

**Desarrollado por @therobram como prueba técnica de desarrollo en Odoo.**