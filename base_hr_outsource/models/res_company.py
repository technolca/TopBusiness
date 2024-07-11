from odoo import models, fields, api


class ContractDetails(models.Model):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _inherit = 'res.company'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic

    contract_start_date = fields.Date(string='Contract Start Date')
    contract_end_date = fields.Date(string='Contract End Date')
    commission_type = fields.Selection([
        ('percentage', 'Percentage'),
        ('amount', 'Amount'),
        ('per_head', 'Per Head with Minimum Amount')
    ], string='Commission Type')
    commission_value = fields.Float(string='Commission Value')
    invoicing_method = fields.Selection([
        ('one_line', 'Invoice in 1 Line'),
        ('with_details', 'Invoice with Details'),
        ('by_cost_center', 'Invoice with Details by Cost Center'),
        ('gross_salary_details', 'Gross Salary Details')
    ], string='Invoicing Method')
    customer_hold = fields.Boolean(string='Customer Hold')

    # endregion

    # region  Special
    # endregion

    # region  Relational
    # life_insurance_contract_ids = fields.One2many('tbg.contract', 'branch_id',
    #                                               string='Life Insurance Contracts')
    # medical_insurance_contract = fields.Text(string='Medical Insurance Contract')

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
