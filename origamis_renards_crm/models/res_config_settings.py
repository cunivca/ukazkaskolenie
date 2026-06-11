# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, fields, models


# Editing existing model
class ResConfigSettings(models.TransientModel):
    '''Overriding res.config.settings from odoo/odoo.'''
    _inherit = 'res.config.settings'

    # Editing existing fields


    # Creating new fields
    recipient_tag_id = fields.Many2one("res.partner.category", string="Recipient Tag",
                                    config_parameter='origamis_renards_crm.recipient_tag')


    # Editing existing methods


    # Creating new methods
