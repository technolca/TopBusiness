# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class InsuranceClaim(models.Model):
    _name = 'tbg.insurance_claim'
    _description = 'Medical Insurance Claim'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    claim_date = fields.Date(string='Claim Date', required=True)
    diagnosis = fields.Text(string='Diagnosis')
    treatment = fields.Text(string='Treatment')
    claim_amount = fields.Float(string='Claim Amount')
    status = fields.Selection([('pending', 'Pending'), ('approved', 'Approved'), ('denied',
                                                                                  'Denied')], string='Status',
                              default='pending')
    # endregion

    # region  Special
    # endregion

    # region  Relational
    patient_id = fields.Many2one('hr.employee', string='Patient', required=True)
    plan_id = fields.Many2one('tbg.insurance_plan', string='Insurance Plan',
                              required=True)
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
