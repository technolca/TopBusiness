# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
import re

DATA_TYPES = {

    'no_spaces': [],
        'Monetary': [
        'mobile',
        'meal',
        'parking',
        'fixed_ot',
        'commission',
        'social_raise',
        'guaranteed_bonus',
        'housing',
        'occasional_bonus',
        'offshore',
        'gross',
        'full_basic',
        'all_insured',
        'all_not_insured',
        'full_basic_si',
        'full_salary_si',
        'fixed',
        'si_amount',
        'si_salary',
        'bank_fees',
        'deduction_fees',
        'refund_salary',
        'basic',
        'location',
        'plant',
        'job_nature',
        'rate'
    ],
    'relational': [
        {'bank_name': ['res.bank', 'name']},
        {'employee_badge_id': ['tbg.employees', 'badge_id']}
    ],
    'Selection': [
        'fees_on'
    ],

}


class SalaryItem(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "tbg.salary_item_temp"
    _description = "Employee temporary Salary item"
    _inherit = []
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    date = fields.Char(help="Date")
    transportation = fields.Char(string='Transportation', currency_field='currency_id', help="Monetary")
    need_confirm = fields.Boolean(default=False)
    fix_note = fields.Text()
    mobile = fields.Char(string='Mobile', help='Original data type: Monetary')
    location = fields.Char(string='Location')
    meal = fields.Char(string='Meal', help='Original data type: Monetary')
    plant = fields.Char(string='Plant')
    parking = fields.Char(string='Parking', help='Original data type: Monetary')
    fixed_ot = fields.Char(string='Fixed OT', help='Original data type: Monetary')
    commission = fields.Char(string='Commission', help='Original data type: Monetary')
    social_raise = fields.Char(string='Social Raise', help='Original data type: Monetary')
    guaranteed_bonus = fields.Char(string='Guaranteed Bonus', help='Original data type: Monetary')
    housing = fields.Char(string='Housing', help='Original data type: Monetary')
    acting = fields.Char(string='Acting', help='Original data type: Monetary')
    job_nature = fields.Char(string='Job Nature')
    occasional_bonus = fields.Char(string='Occasional Bonus', help='Original data type: Monetary')
    offshore = fields.Char(string='Offshore', help='Original data type: Monetary')

    # Salary Calculation section
    gross = fields.Char(string='Gross', help='Original data type: Monetary')
    full_basic = fields.Char(string='Full Basic', help='Original data type: Monetary')
    rate = fields.Float(string='Rate')
    all_insured = fields.Char(string='All Insured', help='Original data type: Monetary')
    all_not_insured = fields.Char(string='All Not Insured', help='Original data type: Monetary')
    full_basic_si = fields.Char(string='Full Basic SI', help='Original data type: Monetary')
    full_salary_si = fields.Char(string='Full Salary SI', help='Original data type: Monetary')

    # Social Insurance Calculation section
    fixed = fields.Char(string='Fixed', help='Original data type: Monetary')
    si_amount = fields.Char(string='SI Amount', help='Original data type: Monetary')
    si_salary = fields.Char(string='SI Salary', help='Original data type: Monetary')
    bank_name = fields.Char(string='Bank Name')
    fees_on = fields.Selection([
        ('company', 'Company'),
        ('employee', 'Employee'),
        ('company_employee', 'Company & Employee'),
    ], string='Fees On')
    bank_fees = fields.Char(string='Bank Fees', help='Original data type: Monetary')
    deduction_fees = fields.Char(string='Deduction Fees', help='Original data type: Monetary')

    refund_salary = fields.Char(string='Refund Salary', help='Original data type: Monetary')

    basic = fields.Char(string='Basic', help='Original data type: Monetary')

    employee_national_id = fields.Char()
    employee_badge_id = fields.Char()
    # endregion

    # region  Special
    # endregion

    # region  Relational
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
    def action_validate(self):
        monetary_fields = DATA_TYPES.get('Monetary', [])
            # dict(filter(lambda field: field[1].get('name') in DATA_TYPES.get('Monetary', [])
            #                           , list(all_fields.items())))
        for rec in self:
            rec.fix_note = ''
            if monetary_fields:
                result = rec.search_read(
                    [('id', 'in', rec.ids)],
                    list(monetary_fields),
                )[0]
                monetary_fields_with_char = dict(
                    filter(lambda field: not re.match(r'^[1-9]\d*(\.\d+)?$', str(field[1])) and field[1], list(result.items())))
                if monetary_fields_with_char:
                    rec.fix_note = ', '.join(list(monetary_fields_with_char.keys())) + ' contains non-numeric value \n'

            if rec.employee_national_id and not re.match(r"\b\d{14}\b", rec.employee_national_id):
                rec.fix_note += 'Employee National ID must be 14 number \n'
            if rec.employee_badge_id and not re.match(r"^[a-zA-Z0-9]+$", rec.employee_badge_id):
                rec.fix_note += 'Employee Badge ID must be alphanumeric only \n'
            if rec.date and not re.match(r"\b(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\b", rec.date):
                rec.fix_note += 'Date must be in yyyy-mm-dd format \n'

            if rec.fix_note:
                rec.need_confirm = True
            else:
                rec.need_confirm = False

    def action_confirm(self):
        vals_list = []
        bank_ids = self.env['res.bank'].sudo().search([])
        employee_ids = self.env['hr.employee'].sudo().search(['|', ('barcode', 'in', self.mapped('employee_badge_id')),
                                                              ('identification_id', 'in', self.mapped('employee_national_id'))])
        for rec in self:
            if not rec.need_confirm:
                vals = rec.prepare_values(employee_ids, bank_ids)
                if vals:
                    vals_list.append(vals)
        if vals_list:
            self.env['tbg.salary_item'].sudo().create(vals_list)
            confirmed_records = self.filtered(lambda x: x.need_confirm == False)
            if confirmed_records:
                confirmed_records.unlink()

    def action_open_form_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Salary Item',
            'res_model': 'tbg.salary_item_temp',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.id
        }
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    def prepare_values(self, employee_ids, bank_ids):
        rec = self
        rec.fix_note = ''
        employee_id = employee_ids.filtered(
            lambda x: x.identification_id == rec.employee_national_id or x.barcode == rec.employee_badge_id)

        bank_id = bank_ids.filtered(
                    lambda x: x.display_name == rec.bank_name)

        if employee_id and employee_id.contract_id and bank_id:
            values = {
                'date': rec.date,
                'transportation': rec.transportation,
                'mobile': rec.mobile,
                'location': rec.location,
                'meal': rec.meal,
                'plant': rec.plant,
                'parking': rec.parking,
                'fixed_ot': rec.fixed_ot,
                'commission': rec.commission,
                'social_raise': rec.social_raise,
                'guaranteed_bonus': rec.guaranteed_bonus,
                'housing': rec.housing,
                'acting': rec.acting,
                'job_nature': rec.job_nature,
                'occasional_bonus': rec.occasional_bonus,
                'offshore': rec.offshore,
                'gross': rec.gross,
                'full_basic': rec.full_basic,
                'rate': rec.rate,
                'all_insured': rec.all_insured,
                'all_not_insured': rec.all_not_insured,
                'full_basic_si': rec.full_basic_si,
                'full_salary_si': rec.full_salary_si,
                'fixed': rec.fixed,
                'si_amount': rec.si_amount,
                'si_salary': rec.si_salary,
                'fees_on': rec.fees_on,
                'bank_fees': rec.bank_fees,
                'deduction_fees': rec.deduction_fees,
                'refund_salary': rec.refund_salary,
                'basic': rec.basic,
                'currency_id': rec.currency_id,
                'pay_currency_id': rec.pay_currency_id,
                'salary_structure_id': rec.salary_structure_id,
                'contract_id': employee_id.contract_id.id,
                'bank_id': bank_id.id
            }
            return values
        else:
            rec.need_confirm = True
            if not employee_id:
                rec.fix_note += 'Employee badge or national id not found \n'
            if not employee_id.contract_id:
                rec.fix_note += 'Contract not found \n'
            if not bank_id:
                rec.fix_note += 'Bank not found \n'
            return False
    # endregion
