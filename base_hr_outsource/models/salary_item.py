# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class SalaryItem(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "tbg.salary_item"
    _description = "Employee Salary History"
    _rec_name = 'date'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    date = fields.Date(string='Date', default=fields.Date.context_today)
    transportation = fields.Monetary(string='Transportation', currency_field='currency_id')
    mobile = fields.Monetary(string='Mobile' , currency_field='currency_id')
    location = fields.Char(string='Location')
    meal = fields.Monetary(string='Meal' , currency_field='currency_id')
    plant = fields.Char(string='Plant')
    parking = fields.Monetary(string='Parking', currency_field='currency_id')
    fixed_ot = fields.Monetary(string='Fixed OT', currency_field='currency_id')
    commission = fields.Monetary(string='Commission', currency_field='currency_id')
    social_raise = fields.Monetary(string='Social Raise', currency_field='currency_id')
    guaranteed_bonus = fields.Monetary(string='Guaranteed Bonus', currency_field='currency_id')
    housing = fields.Monetary(string='Housing', currency_field='currency_id')
    acting = fields.Monetary(string='Acting', currency_field='currency_id')
    job_nature = fields.Char(string='Job Nature')
    occasional_bonus = fields.Monetary(string='Occasional Bonus', currency_field='currency_id')
    offshore = fields.Monetary(string='Offshore', currency_field='currency_id')

    # Salary Calculation section
    gross = fields.Monetary(string='Gross', currency_field='currency_id')
    full_basic = fields.Monetary(string='Full Basic', currency_field='currency_id')
    rate = fields.Float(string='Rate')
    all_insured = fields.Monetary(string='All Insured', currency_field='currency_id')
    all_not_insured = fields.Monetary(string='All Not Insured', currency_field='currency_id')
    full_basic_si = fields.Monetary(string='Full Basic SI', currency_field='currency_id')
    full_salary_si = fields.Monetary(string='Full Salary SI', currency_field='currency_id')

    # Social Insurance Calculation section
    fixed = fields.Monetary(string='Fixed')
    si_amount = fields.Monetary(string='SI Amount')
    si_salary = fields.Monetary(string='SI Salary')
    fees_on = fields.Selection([
        ('company', 'Company'),
        ('employee', 'Employee'),
        ('company_employee', 'Company & Employee'),
    ], string='Fees On')
    bank_fees = fields.Monetary(string='Bank Fees')
    deduction_fees = fields.Monetary(string='Deduction Fees')

    refund_salary = fields.Monetary(string='Refund Salary')

    basic = fields.Monetary(string='Basic', currency_field='currency_id')
    # endregion

    # region  Special
    # endregion

    # region  Relational
    bank_id = fields.Many2one('res.bank', string='Bank Name')
    bank_name = fields.Char(related='bank_id.name', string='Bank Name')
    currency_id = fields.Many2one('res.currency', string='Currency')
    pay_currency_id = fields.Many2one('res.currency', string='Pay Currency')
    salary_structure_id = fields.Many2one('hr.payroll.structure', string='Salary Structure')
    contract_id = fields.Many2one('hr.contract', string='Contract')
    # endregion

    # region  Computed
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------
    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion
