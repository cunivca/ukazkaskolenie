# Here import python (non-odoo) libraries, e.g. datetime

# Here import odoo libraries
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


# Editing existing model
class AccountMove(models.Model):
    '''Overriding account.move from odoo/odoo to add new field.'''
    _inherit = 'account.move'

    # Editing existing fields


    # Creating new fields
    additional_text = fields.Text(string="Additional Text on the Invoice")
    
    date_of_signature = fields.Date(string="Sale Order Date Of Signature", compute="_compute_renards_fields")
    origin = fields.Char(string="Sale Order Origin", compute="_compute_renards_fields")
    project_number = fields.Char(string="Sale Order Project Number", compute="_compute_renards_fields")
    tag_ids_string = fields.Char(compute="_compute_renards_fields")

    # Editing existing methods


    # Creating new methods
    @api.depends("line_ids")
    def _compute_renards_fields(self):
        for move in self:
            move.date_of_signature = False
            move.origin = False
            move.project_number = False
            move.tag_ids_string = False
            
            action_dict = self.action_view_source_sale_orders()
            if "res_id" in action_dict:
                origin_so_id = int(action_dict['res_id'])
                origin_so = self.env['sale.order'].sudo().browse(origin_so_id)
                move.date_of_signature = origin_so.date_of_signature
                move.origin = origin_so.origin
                move.project_number = origin_so.project_number
                
                tag_text = ""
                for tag in origin_so.tag_ids:
                    tag_text += tag.name + ", "
                tag_text = tag_text[:-2]
                
                move.tag_ids_string = tag_text
                 