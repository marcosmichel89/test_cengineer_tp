{
    'name': "cengineer_tp",

    'summary': """ 
        Module to extend funcionalities of crm module""",

    'author': "Marcos Michel Martinez Perez",
    'website': "https://odoo.cuban.engineer",

    # Categories can be used to filter modules in modules listing 
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': "CRM",
    'version': '14.0.0.0.1',

    'depends': ['base', 'website_sale', 'crm', 'website', 'portal'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/portal.xml',
    ],
    'license': 'LGPL-3',
}
