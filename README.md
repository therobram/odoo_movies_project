# Odoo Movies Project

Módulo personalizado para gestionar películas en Odoo.

## Características

- CRUD de películas con título y ranking.
- Cron para consumir películas desde un API externo.
- Endpoint REST público `/api/top_movies`.
- Docker Compose listo para levantar el entorno.

## Instalación

```bash
git clone https://github.com/therobram/odoo_movies_project.git
cd odoo_movies_project
docker-compose up
