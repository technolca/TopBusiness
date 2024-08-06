# -*- coding: utf-8 -*-
import re
from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class EmployeeTemp(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "tbg.hr_employee_temp"
    _description = "Employee Temporary"
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    @api.model
    def _lang_get(self):
        return self.env['res.lang'].get_installed()

    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    need_confirm = fields.Boolean(default=False)
    fix_note = fields.Text()
    # endregion
    # ------------- my fields --------------
    # region ---------------- Basic Info ----------------
    arabic_name = fields.Char(string='Arabic Name')
    arabic_title = fields.Char(string='Arabic Title')
    wives = fields.Integer(string='Number of Wives')
    profile_type = fields.Selection([('type 1', 'Type 1'), ('type 2', 'Type 2')], string='Profile Type')
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

    military_status_id = fields.Many2one('tbg.selection_fields', string='Military Status',
                                         domain=[('type', '=', 'military_status'), ()])

    # endregion

    # region --------- odoo fields -----------------
    name = fields.Char()
    active = fields.Boolean("Active", default=True)
    color = fields.Integer('Color Index', default=0)
    department_id = fields.Many2one('hr.department', 'Department', check_company=True)
    job_id = fields.Many2one('hr.job', 'Job Position', check_company=True)
    job_title = fields.Char(related='job_id.name', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)

    work_contact_id = fields.Many2one('res.partner', 'Work Contact', copy=False)
    work_location_id = fields.Many2one('hr.work.location', 'Work Location', domain="[('address_id', '=', address_id)]")
    user_id = fields.Many2one('res.users')
    resource_id = fields.Many2one('resource.resource')
    resource_calendar_id = fields.Many2one('resource.calendar', check_company=True)

    tz = fields.Selection(
        string='Timezone', related='resource_id.tz', readonly=False,
        help="This field is used in order to define in which timezone the resources will work.")

    company_country_id = fields.Many2one('res.country', 'Company Country', related='company_id.country_id',
                                         readonly=True)
    company_country_code = fields.Char(related='company_country_id.code', depends=['company_country_id'], readonly=True)
    private_street = fields.Char(string="Private Street", groups="hr.group_hr_user")
    private_street2 = fields.Char(string="Private Street2", groups="hr.group_hr_user")
    private_city = fields.Char(string="Private City", groups="hr.group_hr_user")
    private_state_id = fields.Many2one(
        "res.country.state", string="Private State",
        domain="[('country_id', '=?', private_country_id)]",
        groups="hr.group_hr_user")
    private_zip = fields.Char(string="Private Zip", groups="hr.group_hr_user")
    private_country_id = fields.Many2one("res.country", string="Private Country", groups="hr.group_hr_user")
    private_phone = fields.Char(string="Private Phone", groups="hr.group_hr_user")
    private_email = fields.Char(string="Private Email", groups="hr.group_hr_user")
    lang = fields.Selection(selection='_lang_get', string="Lang", groups="hr.group_hr_user")
    country_id = fields.Many2one(
        'res.country', 'Nationality (Country)', groups="hr.group_hr_user", tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", tracking=True)
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status', groups="hr.group_hr_user", default='single', tracking=True)
    spouse_complete_name = fields.Char(string="Spouse Complete Name", groups="hr.group_hr_user", tracking=True)
    spouse_birthdate = fields.Date(string="Spouse Birthdate", groups="hr.group_hr_user", tracking=True)
    children = fields.Integer(string='Number of Dependent Children', groups="hr.group_hr_user", tracking=True)
    place_of_birth = fields.Char('Place of Birth', groups="hr.group_hr_user", tracking=True)
    country_of_birth = fields.Many2one('res.country', string="Country of Birth", groups="hr.group_hr_user",
                                       tracking=True)
    birthday = fields.Char('Date of Birth', groups="hr.group_hr_user", tracking=True)
    ssnid = fields.Char('SSN No', help='Social Security Number', groups="hr.group_hr_user", tracking=True)
    sinid = fields.Char('SIN No', help='Social Insurance Number', groups="hr.group_hr_user", tracking=True)
    identification_id = fields.Char(string='Identification No', groups="hr.group_hr_user", tracking=True)
    passport_id = fields.Char('Passport No', groups="hr.group_hr_user", tracking=True)
    bank_account_id = fields.Many2one(
        'res.partner.bank', 'Bank Account Number',
        domain="[('partner_id', '=', work_contact_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        groups="hr.group_hr_user",
        tracking=True,
        help='Employee bank account to pay salaries')
    permit_no = fields.Char('Work Permit No', groups="hr.group_hr_user", tracking=True)
    visa_no = fields.Char('Visa No', groups="hr.group_hr_user", tracking=True)
    visa_expire = fields.Date('Visa Expiration Date', groups="hr.group_hr_user", tracking=True)
    work_permit_expiration_date = fields.Date('Work Permit Expiration Date', groups="hr.group_hr_user", tracking=True)
    has_work_permit = fields.Binary(string="Work Permit", groups="hr.group_hr_user")
    work_permit_scheduled_activity = fields.Boolean(default=False, groups="hr.group_hr_user")
    additional_note = fields.Text(string='Additional Note', groups="hr.group_hr_user", tracking=True)
    certificate = fields.Selection([
        ('graduate', 'Graduate'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctor', 'Doctor'),
        ('other', 'Other'),
    ], 'Certificate Level', default='other', groups="hr.group_hr_user", tracking=True)
    study_field = fields.Char("Field of Study", groups="hr.group_hr_user", tracking=True)
    study_school = fields.Char("School", groups="hr.group_hr_user", tracking=True)
    emergency_contact = fields.Char("Contact Name", groups="hr.group_hr_user", tracking=True)
    emergency_phone = fields.Char("Contact Phone", groups="hr.group_hr_user", tracking=True)
    km_home_work = fields.Integer(string="Home-Work Distance", groups="hr.group_hr_user", tracking=True)
    employee_type = fields.Selection([
        ('employee', 'Employee'),
        ('student', 'Student'),
        ('trainee', 'Trainee'),
        ('contractor', 'Contractor'),
        ('freelance', 'Freelancer'),
    ], string='Employee Type', default='employee', required=True, groups="hr.group_hr_user",
        help="The employee type. Although the primary purpose may seem to categorize employees, this field has also an impact in the Contract History. Only Employee type is supposed to be under contract and will have a Contract History.")
    notes = fields.Text('Notes', groups="hr.group_hr_user")

    barcode = fields.Char(string="Badge ID", help="ID used for employee identification.", groups="hr.group_hr_user",
                          copy=False)
    pin = fields.Char(string="PIN", groups="hr.group_hr_user", copy=False,
                      help="PIN used to Check In/Out in the Kiosk Mode of the Attendance application (if enabled in Configuration) and to change the cashier in the Point of Sale application.")
    departure_description = fields.Html(string="Additional Information", groups="hr.group_hr_user", copy=False)
    departure_date = fields.Date(string="Departure Date", groups="hr.group_hr_user", copy=False, tracking=True)
    id_card = fields.Binary(string="ID Card Copy", groups="hr.group_hr_user")
    driving_license = fields.Binary(string="Driving License", groups="hr.group_hr_user")
    private_car_plate = fields.Char(groups="hr.group_hr_user",
                                    help="If you have more than one car, just separate the plates by a space.")
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', readonly=True)

    # endregion
    # region  Special
    # endregion

    # region  Relational
    hiring_paper_id = fields.Many2one('tbg.hiring_papers', string='Hiring Papers')
    cost_center_id = fields.Many2one('account.analytic.account', string='Cost Center', help="Analytical Account")
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
        barcodes = []
        national_ids = []
        for rec in self:
            rec.fix_note = ''

            if not rec.identification_id and not rec.barcode:
                rec.fix_note += 'Employee National ID or Badge ID should be filled \n'
            else:
                if rec.identification_id and not re.match(r"\b\d{14}\b", rec.identification_id):
                    rec.fix_note += 'Employee National ID must be 14 number \n'
                else:
                    if rec.identification_id in national_ids:
                        rec.fix_note += 'Employee National ID must be unique \n'
                    else:
                        national_ids.append(rec.identification_id)

                    if rec.barcode and not re.match(r"^[a-zA-Z0-9]+$", rec.barcode):
                        rec.fix_note += 'Employee Badge ID must be alphanumeric only \n'
                    else:
                        if rec.barcode in barcodes:
                            rec.fix_note += 'Employee Badge ID must be unique \n'
                        else:
                            barcodes.append(rec.barcode)

            if rec.birthday:
                # \b(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\b    yyyy-mm-dd
                if not re.match(r"^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{4}$", rec.birthday):
                    rec.fix_note += 'Date of birth must be in mm/dd/yyyy format \n'
                elif datetime.strptime(rec.birthday, '%m/%d/%Y').date() >= fields.Date.today():
                    rec.fix_note += 'Date of birth must be before today\n'

            if rec.private_phone and not re.match(r"^(010|011|012|015)\d{8}$", rec.private_phone):
                rec.fix_note += 'Mobile number must be 11 number start with 010, 011, 012 or 015 \n'

            if rec.private_email and not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", rec.private_email):
                rec.fix_note += 'Email not valid \n'

            if rec.fix_note:
                rec.need_confirm = True
            else:
                rec.need_confirm = False

    def action_confirm(self):
        for rec in self:
            if not rec.need_confirm:
                try:
                    employee_vals = {
                        field.name: getattr(rec, field.name)
                        for field in rec._fields.values()
                        if field.name not in ['id', 'need_confirm', 'fix_note', 'create_date', 'write_date', 'company_id']
                    }
                    employee_vals['company_id'] = rec.company_id.id if rec.company_id else False
                    employee_vals['birthday'] = datetime.strptime(rec.birthday, '%m/%d/%Y').date()
                    self.env['hr.employee'].sudo().create(employee_vals)
                except Exception as e:
                    rec.need_confirm = True
                    rec.fix_note = f'Failed to create record : {e}\n'

        to_delete = self.filtered(lambda x: not x.need_confirm)
        if to_delete:
            to_delete.unlink()
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------

    # endregion
