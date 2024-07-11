# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class HiringPapers(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = 'tbg.hiring_papers'
    _description = 'Hiring Papers'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    name = fields.Char(string='Description', default="Hiring Papers")
    # endregion
    # region  Personal
    # birth_date = fields.Date(string='Date of Birth')
    birth = fields.Selection([
        ('ok', 'OK'),
        ('copy', 'Copy'),
        ('no', 'No'),
    ], string='Birth')
    military = fields.Selection([
        ('ok', 'OK'),
        ('copy', 'Copy'),
        ('no', 'No'),
        ('n_a', 'N/A'),
    ], string='Military')
    military_status = fields.Selection([
        ('exemption', 'Exemption / إعفاء'),
        ('completed_service','Complete the service/أتم الخدمة العسكرية'),
        ('postponed', 'Postponed / مؤجل'),
        ('currently_serving', 'Currently serving / حالياً فى الخدمة'),
    ], string='Military Status')
    end_military = fields.Date(string='End Military')
    graduation = fields.Selection([
        ('ok', 'OK'),
        ('copy', 'Copy'),
        ('no', 'No'),
    ], string='Graduation')
    qualification = fields.Char(string='Qualification')
    university_name = fields.Char(string='University Name')
    graduation_year = fields.Char(string='Graduation Year')
    national_id = fields.Selection([
        ('copy', 'Copy'),
        ('no', 'No'),
    ], string='National ID')
    national_id_issue_date = fields.Date(string='National ID Issue Date')
    national_id_end_date = fields.Date(string='National ID End Date')
    manpower_form = fields.Selection([
        ('ok', 'OK'),
        ('no', 'No'),
    ], string='Manpower Form')
    manpower_date = fields.Date(string='Manpower Date')
    manpower_office = fields.Char(string='Manpower Office')
    send_manpower_form = fields.Boolean(string='Send Manpower Form')
    print_out_form = fields.Boolean(string='Print Out the Form')

    si_not_insured_reason_id = fields.Many2one('tbg.selection_fields', string='Not Insured Reason',
                                               domain=[('type', '=', 'not_insured')])
    si_not_insured_reasons = fields.Selection([
        ('under_age', 'تحت السن'), ('summer_training', 'تدريب صيفي'), ('contract', 'عقد اتفاق'),
        ('armed_forces', 'قوات مسلحة'), ('insured_by_others', 'مؤمن لدى جهة أخرى'),
        ('tour_guide', 'مرشد سياحي'), ('approved_by_admin', 'موافقة من الإدارة'),
    ], string='Not Insured Reasons')

    end_reason = fields.Char(string='End Reason')
    criminal_status = fields.Selection([
        ('ok', 'OK'),
        ('no', 'No'),
    ], string='Criminal Status')
    photos = fields.Selection([
        ('ok', 'OK'),
        ('no', 'No'),
    ], string='Photos')
    contract = fields.Selection([
        ('ok', 'OK'),
        ('no', 'No'),
    ], string='Contract')
    sign_contract_date = fields.Date(string='Sign Contract Date')
    # endregion
    certificate_type = fields.Selection([
        ('qualification_certificate', 'شهادة تأهيل'),
        ('skills_level_measurement', 'قياس مستوى المهارات'),
        ('professional_license', 'مزاولة المهنة'),
        ('union_membership_card', 'كارنية النقابة'),
        ('tax_id', 'Tax ID')
    ], string='Certificate')
    # region  Special
    # endregion

    # region  Relational
    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='cascade')
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

    # social_status = fields.Selection([
    #     ('single', 'Single'),
    #     ('married', 'Married'),
    #     ('cohabitant', 'Legal Cohabitant'),
    #     ('widower', 'Widower'),
    #     ('divorced', 'Divorced')
    # ], string='Social Status')
    # country_id = fields.Many2one(
    #     'res.country', string='Nationality', store=True,
    #     default=lambda self: self.employee_id.country_id)

    # national_id_no = fields.Char(string='National ID No', store=True)
    # passport_no = fields.Char(string='Passport No', store=True,)

    # birthdate = fields.Date(related='employee_id.birthday', string='Birth Date', store=True)
    # place_of_birth = fields.Char(related='employee_id.place_of_birth', string='Place of Birth', store=True)
    # gender = fields.Selection(related='employee_id.gender', string='Gender', store=True)