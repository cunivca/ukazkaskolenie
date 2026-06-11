# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, fields, models


# Creating new model
class TypeOfService(models.Model):
    '''Creating type.of.service to represent a type of service.'''
    _name = 'type.of.service'
    _description = 'Type Of Service'

    # Editing existing fields


    # Creating new fields
    name = fields.Char(string="Name Of Service")

    # Editing existing methods


    # Creating new methods
