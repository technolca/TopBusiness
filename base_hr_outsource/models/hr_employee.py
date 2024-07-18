# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _inherit = 'hr.employee'
    _sql_constraints = [
        ('identification_id_uniq', 'unique(identification_id)', 'The national ID must be unique!'),
        ('barcode_uniq', 'unique(barcode)', 'The badge number must be unique!'),
    ]
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    arabic_name = fields.Char(string='Arabic Name')
    arabic_title = fields.Char(string='Arabic Title')
    wives = fields.Integer(string='Number of Wives')
    profile_type = fields.Selection([('type 1', 'Type 1'), ('type 2', 'Type 2')],string='Profile Type')
    employee_status = fields.Selection([
        ('active_now', 'Active Now'),
        ('active_joining_date', 'Active Joining Date'),
        ('cancel', 'Cancel'),
        ('resign_pending', 'Resign Pending'),
        ('resign_resigned', 'Resigned'),
        ('case', 'Case'),
    ], string='Employee Status')
    health_insurance = fields.Boolean(string='Health Insurance')
    health_insurance_date = fields.Date(string='Health Insurance Date')

    si_date = fields.Date(string='Insurance Date')
    si_form_date = fields.Date(string='Form Date')
    si_type = fields.Selection([
        ('normal', 'Normal'),
        ('injury', 'Injury'),
        ('insured_on_the_ot', 'Insured on the OT'),
        ('employer', 'Employer'),
        ('consultant', 'Consultant'),
        ('mona2da', 'Mona2da'),
        ('not_interested', 'Not interested'),
        ('n_a', 'N/A'),
    ], string='Insurance Type')
    purchasing_period = fields.Char(string='Purchasing Period')
    si_status_id = fields.Many2one('tbg.selection_fields', string='Status')
    si_status = fields.Selection([
        ('forign', 'أجنبي'),
        ('without_papers', 'بدون أوراق - غير مؤمن'),
        ('delivered', 'تم التسليم - غير مؤمن'),
        ('back_from_insurance', 'تم الرجوع من التأمينات - غير مؤمن'),
        ('in_process', 'جاري التأمين - غير مؤمن'),
        ('not_sure', 'غير مؤكد - غير مؤمن'),
        ('insured', 'مؤكد مؤمن'),
        ('not_needed', 'مؤمن لدى جهة أخرى'),
        ('conflict', 'مناقضة'),
        ('forign_conflict', 'مناقضة بالخارج'),
    ], string='Status')
    si_title = fields.Char(string='Insurance Title')

    electronic_type = fields.Selection([
        ('electronic', 'Electronic'),
        ('hard_copy', 'Hard Copy'),
    ], string='Electronic Type')

    # endregion

    # region  Insurance
    si_office = fields.Selection([
        ('office1', 'Office 1'),
        ('office2', 'Office 2'),
        # Add other offices here
    ], string='Office')
    si_sector = fields.Selection([
        ('sector1', 'Sector 1'),
        ('sector2', 'Sector 2'),
        # Add other sectors here
    ], string='Sector')
    si_group = fields.Char(string='Insurance Group')
    medical_from_to_si = fields.Char(string='Medical From To SI')
    medical_status = fields.Selection([
        ('no_photo', 'No Photo'),
        ('medical_form_in_progress', 'Medical Form in Progress'),
        ('medical_form_is_finished', 'Medical Form is Finished'),
        ('delivered_to_employee', 'Delivered to Employee'),
        ('medical_id_in_progress', 'Medical ID in Progress'),
        ('medical_id_is_finished', 'Medical ID is Finished'),
        ('medically_insured', 'Medically Insured'),
        ('delivered_to_manager', 'Delivered to Manager'),
    ], string='Medical Status')
    medical_form_to_emp = fields.Date(string='Medical Form to Employee')
    medical_form_from_emp = fields.Date(string='Medical Form from Employee')
    fit_status = fields.Selection([
        ('accepted', 'Accepted'),
        ('not_accepted', 'Not Accepted'),
    ], string='Fit Status')
    last_date = fields.Date(string='Last Date')
    registered_status = fields.Selection([
        ('tokin', 'Tokin'),
        ('print', 'Print'),
        ('medical_form', 'Medical Form'),
        ('transfer', 'Transfer'),
    ], string='Registered Status')
    si_reason_id = fields.Many2one('tbg.selection_fields', string='Reason', domain=[('type', '=', 'insured')])
    si_reason = fields.Selection([
        ('reason1', 'Reason 1'),
        ('reason2', 'Reason 2'),
        # Add other reasons here
    ], string='Reason')
    end_driving_license = fields.Date(string='End Driving License')

    military_status_id = fields.Many2one('tbg.selection_fields',string='Military Status',
                                      domain=[('type', '=', 'military_status'),()])

    # endregion

    # region  Hiring papers
    birth = fields.Selection([
        ('ok', 'OK'),
        ('copy', 'Copy'),
        ('no', 'No'),
    ], string='Birth', related='hiring_paper_id.birth', readonly=False, store=False)

    military = fields.Selection([
        ('ok', 'OK'),
        ('copy', 'Copy'),
        ('no', 'No'),
        ('n_a', 'N/A'),
    ], string='Military', related='hiring_paper_id.military', readonly=False, store=False)

    military_status = fields.Selection([
        ('exemption', 'Exemption / إعفاء'),
        ('completed_service', 'Complete the service/أتم الخدمة العسكرية'),
        ('postponed', 'Postponed / مؤجل'),
        ('currently_serving', 'Currently serving / حالياً فى الخدمة'),
    ], string='Military Status', related='hiring_paper_id.military_status', readonly=False, store=False)

    end_military = fields.Date(string='End Military', related='hiring_paper_id.end_military', readonly=False,
                               store=False)

    graduation = fields.Selection([
        ('ok', 'OK'),
        ('copy', 'Copy'),
        ('no', 'No'),
    ], string='Graduation', related='hiring_paper_id.graduation', readonly=False, store=False)

    qualification = fields.Char(string='Qualification', related='hiring_paper_id.qualification', readonly=False,
                                store=False)

    university_name = fields.Char(string='University Name', related='hiring_paper_id.university_name', readonly=False,
                                  store=False)

    graduation_year = fields.Char(string='Graduation Year', related='hiring_paper_id.graduation_year', readonly=False,
                                  store=False)

    national_id = fields.Selection([
        ('copy', 'Copy'),
        ('no', 'No'),
    ], string='National ID', related='hiring_paper_id.national_id', readonly=False, store=False)

    national_id_issue_date = fields.Date(string='National ID Issue Date',
                                         related='hiring_paper_id.national_id_issue_date', readonly=False, store=False)

    national_id_end_date = fields.Date(string='National ID End Date', related='hiring_paper_id.national_id_end_date',
                                       readonly=False, store=False)

    manpower_form = fields.Selection([
        ('ok', 'OK'),
        ('no', 'No'),
    ], string='Manpower Form', related='hiring_paper_id.manpower_form', readonly=False, store=False)

    manpower_date = fields.Date(string='Manpower Date', related='hiring_paper_id.manpower_date', readonly=False,
                                store=False)

    manpower_office = fields.Char(string='Manpower Office', related='hiring_paper_id.manpower_office', readonly=False,
                                  store=False)

    send_manpower_form = fields.Boolean(string='Send Manpower Form', related='hiring_paper_id.send_manpower_form',
                                        readonly=False, store=False)

    print_out_form = fields.Boolean(string='Print Out the Form', related='hiring_paper_id.print_out_form',
                                    readonly=False, store=False)

    si_not_insured_reason_id = fields.Many2one('tbg.selection_fields', string='Not Insured Reason',
                                               related='hiring_paper_id.si_not_insured_reason_id', readonly=False,
                                               store=False)

    si_not_insured_reasons = fields.Selection([
        ('under_age', 'تحت السن'), ('summer_training', 'تدريب صيفي'), ('contract', 'عقد اتفاق'),
        ('armed_forces', 'قوات مسلحة'), ('insured_by_others', 'مؤمن لدى جهة أخرى'),
        ('tour_guide', 'مرشد سياحي'), ('approved_by_admin', 'موافقة من الإدارة'),
    ], string='Not Insured Reasons', related='hiring_paper_id.si_not_insured_reasons', readonly=False, store=False)

    end_reason = fields.Char(string='End Reason', related='hiring_paper_id.end_reason', readonly=False, store=False)

    criminal_status = fields.Selection([
        ('ok', 'OK'),
        ('no', 'No'),
    ], string='Criminal Status', related='hiring_paper_id.criminal_status', readonly=False, store=False)

    photos = fields.Selection([
        ('ok', 'OK'),
        ('no', 'No'),
    ], string='Photos', related='hiring_paper_id.photos', readonly=False, store=False)

    contract = fields.Selection([
        ('ok', 'OK'),
        ('no', 'No'),
    ], string='Contract', related='hiring_paper_id.contract', readonly=False, store=False)

    sign_contract_date = fields.Date(string='Sign Contract Date', related='hiring_paper_id.sign_contract_date',
                                     readonly=False, store=False)

    certificate_type = fields.Selection([
        ('qualification_certificate', 'شهادة تأهيل'),
        ('skills_level_measurement', 'قياس مستوى المهارات'),
        ('professional_license', 'مزاولة المهنة'),
        ('union_membership_card', 'كارنية النقابة'),
        ('tax_id', 'Tax ID')
    ], string='Certificate', related='hiring_paper_id.certificate_type', readonly=False, store=False)

    # endregion

    # region  Relational
    children_dependant_ids = fields.One2many('tbg.employee_dependant', 'employee_id', string='Children', domain=[('type', '=', 'child')])
    parents_dependant_ids = fields.One2many('tbg.employee_dependant', 'employee_id', string='Parents', domain=[('type', '=', 'parent')])
    wives_dependant_ids = fields.One2many('tbg.employee_dependant', 'employee_id', string='Wives', domain=[('type', '=', 'spouse')])
    hiring_paper_id = fields.Many2one('tbg.hiring_papers', string='Hiring Papers')
    cost_center_id = fields.Many2one('account.analytic.account', string='Cost Center', help="Analytical Account")
    insurance_plan_ids = fields.One2many('tbg.insurance_plan', 'employee_id', string='Insurance Plans')
    insurance_claim_ids = fields.One2many('tbg.insurance_claim', 'patient_id', string='Insurance Claims')
    # endregion

    # region  Mapped
    # endregion

    # region  Computed
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------
    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    def create(self, vals):
        res = super(Employee, self).create(vals)
        self.env['tbg.hiring_papers'].create({'employee_id': res.id})
        return res
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion


class EmployeeDependent(models.Model):
    _name = 'tbg.employee_dependant'
    _description = 'Employee Dependent For Insurance'

    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='cascade')
    type = fields.Selection([
        ('child', 'Child'),
        ('parent', 'Parent'),
        ('spouse', 'Spouse'),
    ], string='Type', required=True)
    status = fields.Selection([
        ('maried', 'Maried'),
        ('divorced', 'Divorced'),
    ])
    case_no = fields.Integer(string='Case No', required=True)
    for_year = fields.Integer(string='For Year', required=True)
    court = fields.Char(string='Court', required=True)
    alimony_type = fields.Selection([
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
        # Add more types as needed
    ], string='Alimony Type', required=True)
    start_from = fields.Date(string='Start From', required=True)
    amount = fields.Float(string='Amount', required=True)
    percent = fields.Float(string='Percent', required=True)
    stop = fields.Boolean(string='Stop')
    stop_reason = fields.Char(string='Stop Reason')
    comments = fields.Text(string='Comments')

class SelectionFields(models.Model):
    _name = 'tbg.selection_fields'
    _description = 'SI Reason'

    display_name = fields.Char(string='Display Name', required=True)
    ar_value = fields.Char(required=True)
    en_value = fields.Char(required=True)
    type = fields.Selection([
        ('si_reason_id', 'Social Insurance Reason'),
        ('si_not_insured_reasons', 'Not Insured Reasons'),
        ('military_status', 'Military Status'),
        ('si_status', 'Social Insurance Status'),
    ], string='Type')