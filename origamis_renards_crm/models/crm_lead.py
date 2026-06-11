# Here import python (non-odoo) libraries, e.g. datetime
import json
from datetime import date

# Here import odoo libraries
from odoo import _, api, fields, models


# Editing existing model
class CrmLead(models.Model):
    '''Overriding crm.lead from odoo/odoo.'''
    _inherit = 'crm.lead'

    # Editing existing fields
    email_from = fields.Char(compute="_compute_email_from_from_contact_person")
    phone = fields.Char(compute="_compute_phone")

    # Creating new fields
    contact_person_id = fields.Many2one("res.partner", string="Contact person")
    contact_person_id_domain = fields.Char(compute="_compute_contact_person_id_domain", store=True)
    project_budget = fields.Monetary(string="Project Budget", currency_field='company_currency')

    type_of_intent_ids = fields.Many2many("type.of.intent", string="Types of Intent")
    
    def _get_default_source_of_intent(self):
        return self.env['res.partner'].search([('name', '=', 'RENARDS, a.s.')], limit=1, order='id').id
    source_of_intent = fields.Many2one("res.partner", string="Source of Intent", default=_get_default_source_of_intent)
    source_of_intent_domain = fields.Char(compute="_compute_source_of_intent_domain")
    
    partner_city = fields.Char(string="Partner City", related="partner_id.city", store=True)
    partner_region_id = fields.Many2one("res.region", string="Region", related="partner_id.region_id", store=True)
    
    type_of_service_id = fields.Many2one("type.of.service", string="Type Of Service")

    # Editing existing methods
    @api.depends('partner_id')
    def _compute_name(self):
        for lead in self:
            if not lead.name:
                lead.name = False
                
    def _inverse_email_from(self):
        return
    
    # Creating new methods
    @api.depends("partner_id")
    def _compute_contact_person_id_domain(self):
        for lead in self:
            if lead.partner_id and lead.partner_id.child_ids:
                valid_partners = self.env['res.partner'].sudo().search([("parent_id", "=", lead.partner_id.id),
                                                                        ('company_type', "=", "person")])
                lead.contact_person_id_domain = json.dumps([("id", "in", valid_partners.ids)])
            else:
                valid_partners = self.env['res.partner'].sudo().search([('company_type', "=", "person")])
                lead.contact_person_id_domain = json.dumps([("id", "in", valid_partners.ids)])
    
    @api.depends("source_of_intent")
    def _compute_source_of_intent_domain(self):
        for lead in self:
            category_parameter = self.env['ir.config_parameter'].sudo().get_param("origamis_renards_crm.recipient_tag")
            category_record = self.env['res.partner.category'].sudo().browse(int(category_parameter))
            
            valid_partners = []
            all_partners = self.env['res.partner'].sudo().search([])
            for partner in all_partners:
                for category in partner.category_id:
                    if category.name == category_record.name:
                        valid_partners.append(partner.id)
                        break
            
            lead.source_of_intent_domain = json.dumps([("id", "in", valid_partners)])

    @api.depends("contact_person_id")
    def _compute_phone(self):
        for lead in self:
            if lead.contact_person_id.mobile:
                lead.phone = lead.contact_person_id.mobile
            else:
                lead.phone = False
    
    @api.depends('contact_person_id', 'partner_id')
    def _compute_email_from_from_contact_person(self):
        for lead in self:
            if lead.contact_person_id.email:
                lead.email_from = lead.contact_person_id.email
            else:
                lead.email_from = False
    
    def _get_crm_lead_base_report_name(self):
        # Use following comand as the value for the "print_report_name" field of the chosen report.
        # (object._get_crm_lead_base_report_name())
        
        partner_name = f"_{self.partner_id.name}" if self.partner_id else ""
        
        type_of_intent_tags = ""
        if self.type_of_intent_ids:
            for tag in self.type_of_intent_ids:
                type_of_intent_tags += f"_{tag.name}"
            
        current_date = date.today().strftime("%y%m%d")
        current_date_string = f"_{current_date}"
        
        return f"CN{partner_name}{type_of_intent_tags}{current_date_string}"
