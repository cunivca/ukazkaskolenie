# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, fields, models


# Creating new model
class TypeOfIntent(models.Model):
    '''Creating type.of.intent to do represent a type of intent'''
    _name = 'type.of.intent'
    _description = 'Type Of Intent'

    # Editing existing fields


    # Creating new fields
    name = fields.Char(string="Name")
    colour = fields.Integer(string="Colour")

    # Editing existing methods


    # Creating new methods
