from odoo import models, fields
import re

FieldsDict = {
    "Monetary":
        [],
    "Date":
        [],
    "char2":
    [
        "nationality",
        "work_permit_status",
        "tax_treatment",
        "insurance_status",
        "comprehensive_health_insurance_status",
    ]
}

class EmployeeDetails(models.Model):
    _name = 'tbg.salary_info_taxs'
    _description = 'Employee Details For Taxs'
    _inherit = "tbg.base_validator"

    # ---------- Export Fields ----------
    employee_code = fields.Char(string='كود الموظف')
    employee_name = fields.Char(string='اسم الموظف')
    nationality = fields.Char(string='الجنسية')
    national_id = fields.Char(string='الرقم القومي')
    passport_number = fields.Char(string='رقم جواز السفر')
    phone_number = fields.Char(string='رقم التليفون')
    work_permit_status = fields.Char(string='حالة تصريح العمل لغير المصريين')
    work_permit_number = fields.Char(string='رقم تصريح العمل')
    job_position = fields.Char(string='الوظيفة')
    branch_name = fields.Char(string='اسم الجهة/الفرع')
    tax_treatment = fields.Char(string='المعاملة الضريبية')
    tax_registration_number = fields.Char(string='رقم التسجيل الضريبي لجهة العمل الأصلية')
    work_duration = fields.Char(string='مدة العمل')
    insurance_status = fields.Char(string='الحالة التأمينية')
    insurance_number = fields.Char(string='الرقم التأمينى')
    insurance_join_date = fields.Char(string='تاريخ الالتحاق بالتأمينات')
    previous_period_installment = fields.Float(string='قسط مدة سابقة')
    end_of_service_date = fields.Date(string='تاريخ نهاية الخدمة')
    social_insurance_end_date = fields.Date(string='تاريخ انتهاء الاشتراك من التأمينات الاجتماعية')
    total_salary = fields.Float(string='الأجر الشامل')
    non_insurance_allowances = fields.Float(string='بدلات غير خاضعة تأمينيأ')
    comprehensive_health_insurance_status = fields.Char(string='حالة التأمين الصحي الشامل')
    non_worker_wives_count = fields.Integer(string='عدد الزوجات الغير عاملات (التأمين الصحي الشامل)')
    dependents_number = fields.Integer(string='عدد المعالين (التأمين الصحي الشامل)')
    basic_salary = fields.Float(string='المرتب الأساسي')
    bonuses_and_incentives = fields.Float(string='مكافات وحوافز/أجر إضافي/منح')
    exempt_special_allowances = fields.Float(string='علاوات خاصة معفاة')
    taxable_special_allowances = fields.Float(string='علاوات خاصة خاضعة')
    commissions = fields.Float(string='عمولات')
    employee_share_in_profits = fields.Float(string='نصيب العامل في الأرباح')
    service_fee = fields.Float(string='مقابل الخدمة')
    tips = fields.Float(string='البقشيش')
    board_member_salaries = fields.Float(string='مرتبات ومكافات رؤساء اعضاء مجلس الادارة (مقابل العمل الإداري)')
    cash_compensation_for_leave_balance = fields.Float(string='المقابل النقدى لرصيد الاجازات أثناء الخدمة')
    end_of_service_bonus = fields.Float(string='مكافأة نهاية الخدمة الخاضعة')
    amounts_paid_under_special_laws_exempt_part = fields.Float(string='مبالغ منصرفة بقوانين خاصة (الجزء المعفي منها)')
    other_taxable_allowances = fields.Float(string='إضافات وبدلات اخرى خاضعة')
    company_borne_salary_tax = fields.Float(string='ما تحملته المنشاة من ضريبة مرتبات')
    company_borne_employee_social_insurance_share = fields.Float(string='ما تحملته المنشأة من حصة العامل في التأمينات الاجتماعية')
    quarterly_paid_taxable_amounts = fields.Float(string='مبالغ خاضعة منصرفة بصورة ربع سنوية')
    semi_annual_paid_taxable_amounts = fields.Float(string='مبالغ خاضعة منصرفة بصورة نصف سنوية')
    annual_paid_taxable_amounts = fields.Float(string='مبالغ خاضعة منصرفة بصورة سنوية')
    car_benefits = fields.Float(string='مزايا: السيارات')
    mobile_phone_benefits = fields.Float(string='مزايا: الهواتف المحمولة')
    loan_and_advance_benefits = fields.Float(string='مزايا: قروض وسلف')
    life_insurance_benefits_employer_share = fields.Float(string='مزايا: التأمين على الحياة (حصة صاحب العمل)')
    company_shares_inside_outside_egypt = fields.Float(string='مزايا: اسهم الشركة داخل مصر او خارج مصر')
    other_benefits = fields.Float(string='مزايا أخرى')
    employee_insurance_fund_contributions = fields.Float(string='اشتراكات العاملين فى صناديق التامين التى تنشاء طبقا لاحكام ق 54 لسنة 75')
    life_insurance_premiums_employee = fields.Float(string='أقساط التأمين على حياة الممول لمصلحتة ومصلحةزوجته وأولاده القصر')
    health_insurance_premiums = fields.Float(string='أقساط التأمين الصحي')
    pension_insurance_premiums = fields.Float(string='أقساط تأمين لإستحقاق معاش')
    additions_loan_value = fields.Float(string='اضافات: قيمة السلفة/قروض')
    additions_non_taxable_end_of_service_bonus = fields.Float(string='اضافات: قيمة مكافأة نهاية الخدمة الغير خاضعة')
    additions_non_taxable_leave_balance = fields.Float(string='اضافات: قيمة رصيد الأجازات الغير خاضعة')
    other_additions = fields.Float(string='اضافات أخرى')
    deductions_alimony = fields.Float(string='استقطاعات: نفقة')
    deductions_loan_installment = fields.Float(string='استقطاعات: قيمة قسط السلفة/القرض')
    deductions_union_club_subscriptions = fields.Float(string='استقطاعات: اشتراكات نقابات/أندية')
    deductions_penalties = fields.Float(string='استقطاعات: جزاءات')
    deductions_life_insurance_premium = fields.Float(string='استقطاعات: قيمة قسط بوليصة التأمين على الحياة')
    other_deductions = fields.Float(string='استقطاعات أخرى')
    actually_transferred_amounts = fields.Float(string='المبالغ المحولة فعلياً')

    # --------------------- Other Fields ---------------
    annual_gross_income = fields.Float(string='الوعاء السنوي')
    tax_due_for_original_employment = fields.Float(string='الضريبة المستحقة عن الفترة للعمالة الاصلية')
    tax_due_for_employment_model_3 = fields.Float(string='الضريبة المستحقة عن الفترة للعمالة المدرجه بنموذج 3 مرتبات')
    tax_due_for_employment_model_2 = fields.Float(string='الضريبة المستحقة عن الفترة للعمالة المدرجه بنموذج 2 مرتبات')
    total_tax_due_for_all_employment = fields.Float(string='اجمالى الضريبة المستحقة عن جميع انواع العمالة')
    tax_due_for_period = fields.Float(string='الضريبة المحتسبة عن الفترة')
    tax_due_for_previous_periods_1_4_5_6_7 = fields.Float(string='الضريبة المحتسبة عن الفترات السابقة للمعاملات الضريبية 1 و4 و5 و6 و7')
    tax_due_for_period_1_4_5_6_7 = fields.Float(string='الضريبة المحتسبة عن الفترة للمعاملات الضريبية 1 و4 و5 و6 و7')
    tax_due_for_previous_periods_2 = fields.Float(string='الضريبة المحتسبة عن الفترات السابقة للمعاملة ضريبية 2')
    tax_due_for_period_2 = fields.Float(string='الضريبة المحتسبة عن الفترة للمعاملة ضريبية 2')
    tax_due_for_previous_periods_3 = fields.Float(string='الضريبة المحتسبة عن الفترات السابقة للمعاملة ضريبية 3')
    tax_due_for_period_3 = fields.Float(string='الضريبة المحتسبة عن الفترة للمعاملة ضريبية 3')
    final_net_salary = fields.Float(string='صافي الأجر النهائي')
    social_contribution_for_martyrs_fund = fields.Float(string='مشاركه اجتماعيه استقطاع لصندوق الشهداء وما فى حكمها')
    support_for_people_with_disabilities = fields.Float(string='دعم ذوي الهمم (قانون 200 لسنة 2020)')
    additions_loan_value = fields.Float(string='اضافات: قيمة السلفة/قروض')
    additions_non_taxable_end_of_service_bonus = fields.Float(string='اضافات: قيمة مكافأة نهاية الخدمة الغير خاضعة')
    additions_non_taxable_leave_balance = fields.Float(string='اضافات: قيمة رصيد الأجازات الغير خاضعة')
    other_additions = fields.Float(string='اضافات أخرى')
    deductions_alimony = fields.Float(string='استقطاعات: نفقة')
    deductions_loan_installment = fields.Float(string='استقطاعات: قيمة قسط السلفة/القرض')
    deductions_union_club_subscriptions = fields.Float(string='استقطاعات: اشتراكات نقابات/أندية')
    deductions_penalties = fields.Float(string='استقطاعات: جزاءات')
    deductions_life_insurance_premium = fields.Float(string='استقطاعات: قيمة قسط بوليصة التأمين على الحياة')
    other_deductions = fields.Float(string='استقطاعات أخرى')
    actually_transferred_amounts = fields.Float(string='المبالغ المحولة فعلياً')

    total_entitlements = fields.Float(string='اجمالى الاستحقاقات')
    insurance_wage = fields.Char(string='الأجر التأميني')
    insurance_subscription_value = fields.Float(string='قيمة اشتراك التأمينات')
    personal_exemption = fields.Char(string='الاعفاء الشخصي')
    period_bowl = fields.Char(string='الوعاء للفترة')
    annual_tax = fields.Char(string='الضريبة السنوية')

    def create(self, vals):
        for val in vals:
            for field in FieldsDict.get('char2'):
                value = val.get(field)
                if value and len(value) < 2:
                    val[field] = '0' + value
        res = super(EmployeeDetails, self).create(vals)
        return res

    def action_validate(self):
        validate_and_fix = self.env.context.get('validate_and_fix', False)
        barcodes = []
        national_ids = []
        for rec in self:
            rec.fix_note = ''
            if rec.national_id:
                if not re.match(r"\b\d{14}\b", rec.national_id):
                    rec.fix_note += 'Employee National ID must be 14 number \n'
                else:
                    if rec.national_id in national_ids:
                        rec.fix_note += 'Employee National ID must be unique \n'
                    else:
                        national_ids.append(rec.national_id)
            elif rec.nationality == '01' and not rec.national_id:
                rec.fix_note += 'Employee National ID is required for foreigners \n'

            if rec.employee_code and not re.match(r"^[a-zA-Z0-9]+$", rec.employee_code):
                rec.fix_note += 'Employee Badge ID must be alphanumeric only \n'
            else:
                if rec.employee_code in barcodes:
                    rec.fix_note += 'Employee Badge ID must be unique \n'
                else:
                    barcodes.append(rec.employee_code)
            if rec.nationality and not re.match(r"^[0][1-2]$", rec.nationality):
                rec.fix_note += 'Nationality must be numeric with only 2 digits ex: 02, 01 \n'

            if rec.employee_name:
                if validate_and_fix:
                    rec.employee_name = rec.employee_name.strip().replace('  ', ' ')
                no = 4 if rec.nationality == '01' else 2
                if not re.match(r"^(?=\w+\s)(?=\w+(\s\w+){" + str(no - 1) + ",})(?=.{1,100}$)[^\s].*?[^\s]$", rec.employee_name):
                    rec.fix_note += f"Employee name must be {no} or more names without extra spaces and doesn't exceed 100 characters\n"
            else:
                rec.fix_note += 'Employee name is required \n'

            if not rec.work_permit_status:
                if rec.nationality == '02':
                    rec.fix_note += 'Work permit status is required for foreigners \n'
            else:
                if not re.match(r"^[0][1-3]$", rec.work_permit_status):
                    rec.fix_note += 'Work permit status must be numeric with only 2 digits ex: 02, 01, 03 \n'

            if not rec.passport_number:
                if rec.nationality == '02':
                    rec.fix_note += 'Passport number is required for foreigners \n'
            else:
                if not re.match(r"\b[\u0600-\u06FFa-zA-Z0-9]{1,14}\b", rec.passport_number):
                    rec.fix_note += 'Passport number must be 14 alphanumeric chars\n'

            if rec.phone_number and not re.match(r"^(010|011|012|015)\d{8}$", rec.phone_number):
                note = 'Phone number must be 11 number start with 010, 011, 012 or 015 \n'
                if validate_and_fix:
                    rec.phone_number = '0' + rec.phone_number if rec.phone_number[0] != '0' else rec.phone_number
                    if re.match(r"^(010|011|012|015)\d{8}$", rec.phone_number):
                        note = ''
                rec.fix_note += note

            if rec.fix_note:
                rec.need_confirm = True
            else:
                rec.need_confirm = False

