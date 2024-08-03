# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class ObjectModel(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "tbg.base_validator"
    _description = "Base Validator"
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    need_confirm = fields.Boolean(default=False)
    fix_note = fields.Text()
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
    def action_confirm(self):
        pass

    def action_validate(self):
        pass
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion
