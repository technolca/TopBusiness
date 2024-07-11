from odoo import models, fields


class EmployeeContract(models.Model):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _inherit = 'hr.contract'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    hiring_month = fields.Date(string='Hiring Month')
    hiring_email = fields.Char(string='Hiring Email')
    probation_period = fields.Integer(string='Probation Period (Months)')
    renewal_date = fields.Date(string='Renewal Date')
    extra_renewal = fields.Boolean(string='Extra Renewal')
    salary_schema = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Salary Schema', default='no')
    renewal_type = fields.Selection([
        ('limited', 'Limited Contract'),
        ('unlimited', 'Unlimited Contract'),
        ('consultant', 'Consultant Contract'),
    ], string='Renewal Type', default='limited')

    # ----------------- Termination fields ---------------------------------
    termination_reason = fields.Selection([
        ('work_absence', 'انقطاع عن العمل'),
        ('incompetence', 'عدم صالحية'),
        ('contract_termination', 'انهاء عقد'),
    ], string='Reason', tracking=True)
    absent = fields.Boolean(string='Absent', tracking=True)
    letter = fields.Boolean(string='Letter', tracking=True)
    second_letter = fields.Boolean(string='Second Letter', tracking=True)
    received_letter = fields.Boolean(string='Received Letter', tracking=True)
    send_letter = fields.Boolean(string='Send Letter', tracking=True)
    send_second_letter = fields.Boolean(string='Send Second Letter', tracking=True)
    appear_letter = fields.Boolean(string='Appear Letter', tracking=True)

    # Custody Section
    declaration = fields.Boolean(string='Declaration', tracking=True)
    custody = fields.Boolean(string='Custody', tracking=True)
    custody_declaration = fields.Boolean(string='Custody Declaration', tracking=True)
    # endregion

    # region  Special
    # endregion

    # region  Relational
    salary_item_ids = fields.One2many('tbg.salary_item', 'contract_id', string='Salary Items')
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
