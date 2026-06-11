# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, Command, fields, models
from odoo.exceptions import UserError


# Editing existing model
class Agreement(models.Model):
    '''Overriding agreement from agreement module to implement state functionality.'''
    _inherit = 'agreement'

    # Editing existing fields
    

    # Creating new fields
    state = fields.Selection(string="State", tracking=True,
                             selection=[("draft", "Draft"), ("sent", "Contract Sent"), 
                                        ("signed", "Signed Contract"), ("cancel", "Cancel")], default="draft")
    contract_amendment_to_framework_agreement_ids = fields.One2many("framework.contract.amendment", "agreement_id", 
                                                                    string="Contract Amendments to Framework Agreements"
                                                                    )

    # Editing existing methods


    # Creating new methods
    def action_agreement_send(self):
        self.ensure_one()
        
        self.state = "sent"

    def action_confirm(self):
        self.ensure_one()
        if not self.signature_date:
            raise UserError(_("An error occurred while confirming the contract proposal. "
                              "To confirm the Contract Proposal, please fill in the Date of Signature field."))
        
        self.state = "signed"
    
    def action_cancel(self):
        self.ensure_one()
        
        self.state = "cancel"
    
    def action_draft(self):
        self.ensure_one()
        
        self.state = "draft"