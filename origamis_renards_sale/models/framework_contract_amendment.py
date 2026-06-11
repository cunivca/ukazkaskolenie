# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, fields, models


# Creating new model
class FrameworkContractAmendment(models.Model):
    '''Creating model framework.contract.amendment.'''
    _name = 'framework.contract.amendment'
    _description = 'Amendment to Framework Contracts'

    # Editing existing fields


    # Creating new fields
    agreement_id = fields.Many2one("agreement", string="Agreement")
    name = fields.Char(string="Name", required=True)
    contract_amendment_no = fields.Integer(string="Contract Amendment No")
    description = fields.Char(string="Description")
    customer_id = fields.Many2one("res.partner", related="agreement_id.partner_id", string="Customer")
    upload_contract = fields.Binary(string="Upload Contract")
    
    
    # Editing existing methods


    # Creating new methods
