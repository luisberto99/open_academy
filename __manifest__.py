# -*- coding: utf-8 -*-
{
    'name': "Open Academy - 20142000922",

    'summary': """
        Modulo de Open Academy Elaborado por Luis Alberto Medina - 20142000922
        """,

    'description': """
        Modulo de Open Academy Elaborado por Luis Alberto Medina - 20142000922
    """,

    'author': "Luis Alberto Medina",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'test',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/open_academy.xml',
        'views/partner.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
