from odoo import http
from odoo.http import request
import json

class MovieAPIController(http.Controller):

    @http.route('/api/top_movies', auth='public', methods=['GET'], type='http')
    def top_movies(self, **kwargs):
        # Obtener top 10 películas por ranking descendente
        movies = request.env['movie.movie'].sudo().search([], order='ranking desc', limit=10)

        # Preparar datos en formato JSON
        data = [{
            'id': movie.id,
            'title': movie.title,
            'ranking': movie.ranking,
        } for movie in movies]

        # Devolver respuesta JSON
        return http.Response(
            json.dumps(data),
            content_type='application/json',
            status=200
        )
