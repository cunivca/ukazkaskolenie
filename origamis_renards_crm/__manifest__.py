# -*- coding: utf-8 -*-
{
    'name': 'Origamis: Renards CRM',
    'category': 'Contacts',
    'summary': 'THE MODULE INTRODUCES VARIOUS ADDITIONS AND CUSTOMISATIONS TO THE CRM APP',
    'version': '17.0.1.0.9',
    'website': 'https://origamis.cz',
    'author': 'Origamis',
    'depends': [
        #base odoo/odoo modules
        'account',
        'base',
        'crm',
        'sale_crm',
        #base odoo/enterprise modules
        'account_accountant',
        #modules from origamis
        'origamis_renards_contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/settings_crm_views.xml', 
        'views/type_of_intent_views.xml',
        'views/type_of_service_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    
}
