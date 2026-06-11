# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


# Editing existing model
class ResCompany(models.Model):
    '''Overriding res.company from odoo/odoo to add new field for additional company logo.'''
    _inherit = 'res.company'

    # Editing existing fields


    # Creating new fields
    logo_2 = fields.Binary()

    # Editing existing methods


    # Creating new methods
 