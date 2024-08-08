# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class AddDateWizard(models.TransientModel):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "tbg.add_date_wizard"
    _description = "Add Sheet Date"
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    date = fields.Date()
    # endregion

    # region  Special
    # endregion

    # region  Relational
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
    def action_add_date(self):
        salary_info = self.env['tbg.salary_info_taxs'].search([])
        if salary_info:
            salary_info.sudo().write({'sheet_date': self.date})

    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion
