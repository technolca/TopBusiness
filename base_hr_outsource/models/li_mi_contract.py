from odoo import models, fields, api


class LifeInsuranceContract(models.Model):
    _name = 'tbg.contract'
    _description = 'Life Insurance and Medical Insurance Contract'

    branch_id = fields.Many2one('company.branch', string='Branch', required=True, ondelete='cascade')
    policy_number = fields.Char(string='Policy Number')
    life_insurance_company = fields.Many2one('res.partner', string='Life Insurance Company',
                                             domain="[('supplier', '=', True), ('life_insurance', '=', True)]")
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    medical_same_info = fields.Boolean(string='Medical Same Information')
    payment_terms = fields.Char(string='Payment Terms')
