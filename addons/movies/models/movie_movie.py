import logging
import requests
from odoo import models, fields

_logger = logging.getLogger(__name__)

class Movie(models.Model):
    _name = 'movie.movie'
    _description = 'Movie'

    title = fields.Char(string="Título", required=True)
    ranking = fields.Float(string="Ranking")

    @models.api.model
    def fetch_movies_from_api(self):
        """Función programada para obtener una película del API externo y guardarla."""
        config = self.env['ir.config_parameter'].sudo()
        api_url = config.get_param('movies_api_url')
        api_key = config.get_param('movies_api_key')

        if not api_url or not api_key:
            _logger.error("Parámetros API no configurados (movies_api_url o movies_api_key están vacíos).")
            return

        try:
            response = requests.get(api_url, params={'api_key': api_key})
            response.raise_for_status()
        except Exception as e:
            _logger.error("Error de conexión al API de películas: %s", e)
            return

        try:
            data = response.json()
        except ValueError:
            _logger.error("Respuesta del API no es JSON válido: %s", response.text)
            return

        # Adaptado a los campos reales devueltos por el API
        title = data.get('movie_title')
        ranking = data.get('ranking_movie')

        if not title or ranking is None:
            _logger.error("Datos incompletos en respuesta API: %s", data)
            return

        existing = self.search([('title', '=', title)], limit=1)
        if existing:
            existing.write({'ranking': ranking})
            _logger.info("Película '%s' ya existente, ranking actualizado a %s", title, ranking)
        else:
            self.create({'title': title, 'ranking': ranking})
            _logger.info("Nueva película registrada: '%s' con ranking %s", title, ranking)
