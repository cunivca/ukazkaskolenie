# -*- coding: utf-8 -*-
{
    'name': 'Origamis: Renards Invoice',
    'summary': 'This module makes changes to the default invoice template.',
    'version': '17.0.0.0.5',
    'website': 'https://origamis.cz',
    'author': 'Origamis',
    'depends': [
        #base odoo/odoo modules
        'account',
        'base',
        'l10n_cz',
        'web',
        #base odoo/enterprise modules
        'account_accountant',
        #modules from origamis
        'origamis_base_cz',
    ],
    'data': [
        'views/account_move_views.xml',
        'views/invoice_views.xml',
        'wizard/base_document_layout_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    
}
