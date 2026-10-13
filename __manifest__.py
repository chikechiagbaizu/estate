{
    'name': 'Real Estate Ads',
    'summary': 'Real Estate Ads',
    'description': """
    Odoo technical course project developed while following
    Miracle Ayodele's Odoo 16/17 technical course, adapted
    for Odoo 19.0.
    """,
    'author': 'Chike Chiagbaizu',
    'maintainer': 'Chike Chiagbaizu',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'sequence': 20,
    'category': 'Sales',
    'application': True,
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_action.xml',
        'views/menu_items.xml',
    ]
}