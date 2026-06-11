# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, models


# Editing existing model    
class CrmLead(models.Model):
    '''Overriding crm.lead from odoo/odoo to add default type_of_service_id computation for new quotations'''
    _inherit = 'crm.lead'
    
    
    # Editing existing fields
    
    
    # Creating new fields
    
    
    # Editing existing methods
    def _prepare_opportunity_quotation_context(self):
        res = super()._prepare_opportunity_quotation_context()
        res['default_type_of_service_id'] = self.type_of_service_id.id
        return res
    
    
    # Creating new methods
