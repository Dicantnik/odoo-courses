{
    'name': "Library",
    'summary': "Module for odoo-course",
    'license': 'LGPL-3',
    'author': "Dicantnik",
    'website': "https://example.com",
    'category': 'Uncategorized',
    'version': '17.0.1.0.0',
    'depends': [],
    'external_dependencies': {},
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/library_menus.xml',
        'views/library_book_category_views.xml',
        'views/library_book_views.xml',
        'data/library_book_category_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/library_book_demo.xml',
        'demo/library_book_change_demo.xml'
    ],
    'images': [],
    'live_test_url': 'https://demo.example.com',
    'price': 0.0,
    'currency': 'EUR',
    'support': 'support@example.com',
    'application': False,
    'installable': True,
    'auto_install': False,

}
