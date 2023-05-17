{
    'name': 'Interview Task Module',
    'version': '1.2',
    'summary': 'Interview Task module',
    'sequence': 1,
    'description': """
    """,
    'category': 'website',
    'website': 'https://www.odoo.com',
    'images': [],
    'depends': ['sale', 'product', 'account'],
    'data': [
        'views/account_move_view.xml',
        'views/sale_order_view.xml',
        'views/product_template.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
