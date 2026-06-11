# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, Command, fields, models
from odoo.exceptions import UserError


# Editing existing model
class SaleOrder(models.Model):
    '''Overriding sale.order from odoo/odoo to add new fields and edit existing fields.'''
    _inherit = 'sale.order'

    # Editing existing fields
    partner_id = fields.Many2one("res.partner", 
                                 domain="[('company_id', 'in', (False, company_id)), ('is_company', '=', 'True')]")

    # Creating new fields
    form_of_legal_execution = fields.Text("Form Of Legal Execution", related="partner_id.form_of_legal_execution",
                                          readonly=False)
    contract_number_ids = fields.One2many("contract.number", "sale_order_id", string="Contracts")
    
    partner_child_ids = fields.Many2many("res.partner", compute="_compute_partner_child_ids")   
    individual_contact_ids = fields.Many2many("res.partner", string="Individual Contacts",
                                              domain="[('id', 'in', partner_child_ids)]")
    
    type_of_service_id = fields.Many2one("type.of.service", string="Type Of Service")
    
    date_of_signature = fields.Date(string="Date Of Signature")
    
    def _get_default_sale_order_name_readonly(self):
        return not self.env.user.has_group('sales_team.group_sale_manager')
    sale_order_name_readonly = fields.Boolean(compute="_compute_sale_order_name_readonly", 
                                              default=_get_default_sale_order_name_readonly)
    
    project_number = fields.Char(string="Project Number")
    

    # Editing existing methods
    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for index, order in enumerate(res):
            if order.agreement_id:
                agreement_count = res.agreement_id.sale_order_count
                order.name = f"{order.agreement_id.code}/{agreement_count:02}"
        return res


    # Creating new methods
    def _compute_sale_order_name_readonly(self):
        for order in self:
            order.sale_order_name_readonly = not order.env.user.has_group('sales_team.group_sale_manager')
    
    @api.depends("partner_id")
    def _compute_partner_child_ids(self):
        for order in self:
            order.partner_child_ids = [Command.set(order.partner_id.child_ids.ids)]
            
    def action_confirm(self):
        if not self.date_of_signature:
            raise UserError(_("An error occurred while confirming the contract proposal. "
                              "To confirm the Contract Proposal, please fill in the Date of Signature field. "))
        return super().action_confirm()
    
    @api.onchange("opportunity_id")
    def change_origin_on_opportunity_id_change(self):
        self.origin = self.opportunity_id.name
        
    def _get_sale_order_report_name(self):
        # Use following comand as the value for the "print_report_name" field of the sale order report.
        # (object._get_sale_order_report_name())
        
        sale_order_name = f"{self.name}" if self.name else ""
        sale_order_partner_name = f"_{self.partner_id.name}" if self.partner_id else ""
        
        sale_order_tags = ""
        if self.tag_ids:
            for tag in self.tag_ids:
                sale_order_tags += f"_{tag.name}"
        
        return f"{sale_order_name}{sale_order_partner_name}{sale_order_tags}"
