{
    'name': 'MBA UX Branding',
    'version': '19.0.1.0.0',
    'category': 'Hidden',
    'summary': 'Iconos de apps con el estandar visual nativo de Odoo (MBA Consultings)',
    'description': """
Iconos y marca visual comun para las implementaciones de MBA Consultings.

Estandar de iconos: SVG 50x50, 3 formas planas en 3 tonos de la paleta de Odoo,
sin fondo, sin degradados, sin sombras.
    """,
    'author': 'MBA Consultings',
    'website': 'https://mbaconsultings.com',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'views/menus.xml',
    ],
    'icon': '/mba_ux_branding/static/description/icon.png',
    'installable': True,
    'application': False,
}
