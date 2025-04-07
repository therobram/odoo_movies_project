{
    'name': "Gestión de Películas",
    'summary': "Módulo personalizado para gestionar películas y rankings",
    'author': "Tu Nombre",
    'version': '1.0.0',
    'category': 'Tools',
    'depends': ['base'],  # depende al menos del módulo base de Odoo
    'data': [
        'security/ir.model.access.csv',
        'data/movies_data.xml',     # parámetros de sistema (si lo usamos)
        'data/cron_data.xml',       # definición del cron
        'views/movie_views.xml',    # vistas y menú
    ],
    'installable': True,
    'application': True,
}
