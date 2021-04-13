# -*- coding: utf-8 -*-
{
    'name': "CFI Purchase Order Customizations",

    'summary': """Purchase Order connection with Sale Order""",

    'description': """
        [2446458]
        """,

    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': [
        'sale_mrp',
        'sale_purchase_stock',
        'stock_dropshipping'
        ],

    # always loaded
    'data': [
        'views/mrp_production_views.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}
