# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


# Editing existing model
class BaseDocumentLayout(models.TransientModel):
    '''Overriding base.document.layout from odoo/odoo to add new field for additional company logo.'''
    _inherit = 'base.document.layout'

    # Editing existing fields


    # Creating new fields
    logo_2 = fields.Binary(string="Company Logo 2", related='company_id.logo_2', readonly=False)

    # Editing existing methods


    # Creating new methods
