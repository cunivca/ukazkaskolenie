# -*- coding: utf-8 -*-
{
    'name': 'Origamis: Renards Sale',
    'category': 'Contacts',
    'summary': 'THE MODULE INTRODUCES VARIOUS ADDITIONS AND CUSTOMISATIONS TO THE SALE APP',
    'version': '17.0.0.0.12',
    'website': 'https://origamis.cz',
    'author': 'Origamis',
    'depends': [
        #base odoo/odoo modules
        'account',
        'base',
        'sale',
        'sale_management',
        #base odoo/enterprise modules
        'account_accountant',
        #external 3rd party modules
        'agreement_sale',
        #modules from origamis
        'origamis_renards_ares_extension',
        'origamis_renards_crm',

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/agreement_views.xml',
        'views/contract_number_views.xml',
        'views/framework_contract_amendment_views.xml',
        'views/sale_order_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    
}
