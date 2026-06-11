# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


# Editing existing model
class ResPartner(models.Model):
    '''Overriding res.partner from odoo/odoo to adjust partner address format.'''
    _inherit = 'res.partner'

    # Editing existing fields


    # Creating new fields
    

    # Editing existing methods
    def _get_address_format(self):
        res = super()._get_address_format()
        return "%(street)s\n%(street2)s\n%(zip)s %(state_code)s %(city)s\n"


    # Creating new methods
  