# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, fields, models


# Creating new model
class ContractNumber(models.Model):
    '''Creating model contract.number.'''
    _name = 'contract.number'
    _description = 'Contract Number'

    # Editing existing fields


    # Creating new fields
    contract_version = fields.Integer(string="Contract Version", default=0)
    framework_contract_no = fields.Integer(string="Contract Amendment No", default=0)
    contract_type = fields.Selection(string="Contract Type", selection=[
        ("framework_contract", "Framework contract"), 
        ("contract_version", "Contract Version"), 
        ("contract_addendum", "Contract Addendum"),
    ])
    sale_order_id = fields.Many2one("sale.order", string="Sale Order")
    
    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    upload_contract = fields.Binary(string="Upload Contract")

    customer_id = fields.Many2one("res.partner", related="sale_order_id.partner_id")
    agreement_id = fields.Many2one("agreement", string="Agreements")
    
    # Editing existing methods


    # Creating new methods
