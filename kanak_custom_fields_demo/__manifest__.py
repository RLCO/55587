# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    "name": "Kanak Custom Fields Demo Module",
    'summary': 'A custom module for demo of various fields in Odoo.',
    "description": '''
        A custom module for demo of various fields in Odoo.
    ''',
    "version": "15.0.1.0",
    "category": "Hidden/Tools",
    "license": 'OPL-1',
    "website": "https://www.kanakinfosystems.com",
    "author": "Kanak Infosystems LLP.",
    "images": ['static/description/banner.jpg'],
    "depends": ['base', 'hr'],
    "data": [
        "security/ir.model.access.csv",
        "views/knk_view.xml",
    ],
    'sequence': 1,
    "installable": True,
}
