# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class InsurancePlan(models.Model):
    _name = 'tbg.insurance_plan'
    _description = 'Medical Insurance Plan'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    insurance_type = fields.Selection([
        ('medical_life', 'Media & Life'),
        ('medical', 'Medical'),
        ('life', 'Life'),
    ], string='Insurance Type', required=True)
    insurance_company = fields.Char(string='Insurance Company', required=True)
    insurance_number = fields.Char(string='Insurance Number', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    coverage_details = fields.Text(string='Coverage Details')
    deductible = fields.Float(string='Deductible')
    premium = fields.Float(string='Premium')

    # name = fields.Char(string='Plan Name', required=True)
    # coverage_details = fields.Text(string='Coverage Details')
    # premium = fields.Float(string='Premium')
    # deductible = fields.Float(string='Deductible')
    # co_pay = fields.Float(string='Co-Pay')
    # plan_type = fields.Selection([('medical', 'Medical'), ('life', 'Life')], string='Plan Type', required=True)
    # endregion

    # region  Special
    # endregion

    # region  Relational
    employee_id = fields.Many2one('hr.employee', string='Employees')
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
