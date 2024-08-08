from odoo import models, fields
import re
# import unicodedata

FieldsDict = {
    "Flout":
        [
            'bonuses_and_incentives',
            'exempt_special_allowances',
            'taxable_special_allowances',
            'commissions',
            'employee_share_in_profits_1',
            'employee_share_in_profits_2',
            'service_fee',
            'tips',
            'board_member_salaries',
            'cash_compensation_for_leave_balance',
            'end_of_service_bonus',
            'amounts_paid_under_special_laws_exempt_part',
            'other_taxable_allowances',
            'company_borne_salary_tax',
            'company_borne_employee_social_insurance_share',
            'quarterly_paid_taxable_amounts',
            'semi_annual_paid_taxable_amounts',
            'annual_paid_taxable_amounts',
            'car_benefits',
            'mobile_phone_benefits',
            'loan_and_advance_benefits',
            'life_insurance_benefits_employer_share',
            'company_shares_inside_outside_egypt',
            'other_benefits',
            'employee_insurance_fund_contributions',
            'life_insurance_premiums_employee',
            'health_insurance_premiums',
            'pension_insurance_premiums',
            'other_additions',
            'deductions_alimony',
            'deductions_penalties',
            'deductions_life_insurance_premium',
            'other_deductions',
            'actually_transferred_amounts',
            'annual_gross_income',
            'tax_due_for_original_employment',
            'tax_due_for_employment_model_3',
            'tax_due_for_employment_model_2',
            'total_tax_due_for_all_employment',
            'tax_due_for_period',
            'tax_due_for_previous_periods_1_4_5_6_7',
            'tax_due_for_period_1_4_5_6_7',
            'tax_due_for_previous_periods_2',
            'tax_due_for_period_2',
            'tax_due_for_previous_periods_3',
            'tax_due_for_period_3',
            'final_net_salary',
            'social_contribution_for_martyrs_fund',
            'support_for_people_with_disabilities',
            'additions_loan_value',
            'additions_non_taxable_end_of_service_bonus',
            'additions_non_taxable_leave_balance',
            'deductions_loan_installment',
            'deductions_union_club_subscriptions',
            'total_entitlements',
            'insurance_wage',
            'insurance_subscription_value',
            'personal_exemption',
            'period_bowl',
            'annual_tax',
            'previous_period_installment',
            'total_salary',
            'non_insurance_allowances',
            'basic_salary',
            'employee_share_in_social_insurance_and_pensions',
            'employee_share_deducted_in_comprehensive_health_insurance',
            'company_share_in_social_insurance',
            'company_share_in_comprehensive_health_insurance',
            'amounts_exempt_under_special_laws',
            'installments_previous_period_loan_secondment_consideration',
            'total_insurance_fund_contributions',
            'total_deductions',
            'net_income_period_bowl',
            'martyr_fund_contribution',
            'social_allowance'
        ],
    "Date":
        [
            'insurance_join_date',
            'end_of_service_date',
            'social_insurance_end_date'
        ],
    "char2":
    [
        "nationality",
        "work_permit_status",
        "tax_treatment",
        "insurance_status",
        "comprehensive_health_insurance_status",
        'phone_number'
    ],
    "required":
        [

        ]
}


class EmployeeDetails(models.Model):
    _name = 'tbg.salary_info_taxs'
    _description = 'Employee Details For Taxs'
    _inherit = "tbg.base_validator"

    # ---------- Export Fields ----------
    sent = fields.Boolean(help='تم الارسال')
    done = fields.Boolean(help='تم التحقق منه مسبقا (بيانات قديمة)')
    sheet_date = fields.Date(help='تاريخ الورقة')

    sequence = fields.Char(string='EI005', help='مسلسل')
    employee_code = fields.Char(string='EI010', help='كود الموظف')
    employee_name = fields.Char(string='EI015', help='اسم الموظف')
    nationality = fields.Char(string='EI020', help='الجنسية')
    national_id = fields.Char(string='EI025', help='الرقم القومي')
    passport_number = fields.Char(string='EI026', help='رقم جواز السفر')
    phone_number = fields.Char(string='EI030', help='رقم التليفون')

    work_permit_status = fields.Char(string='EI035', help='حالة تصريح العمل لغير المصريين')
    work_permit_number = fields.Char(string='EI040', help='رقم تصريح العمل')
    job_position = fields.Char(string='EI045', help='الوظيفة')
    branch_name = fields.Char(string='EI055', help='اسم الجهة/الفرع')
    tax_treatment = fields.Char(string='EI060', help='المعاملة الضريبية')
    tax_registration_number = fields.Char(string='EI065', help='رقم التسجيل الضريبي لجهة العمل الأصلية')
    work_duration = fields.Char(string='EI130', help='مدة العمل')
    insurance_status = fields.Char(string='EI070', help='الحالة التأمينية')
    insurance_number = fields.Char(string='EI075', help='الرقم التأمينى')

    insurance_join_date = fields.Date(string='EI080', help='تاريخ الالتحاق بالتأمينات')
    previous_period_installment = fields.Float(string='EI085', help='قسط مدة سابقة')

    end_of_service_date = fields.Date(string='EI090', help='تاريخ نهاية الخدمة')
    social_insurance_end_date = fields.Date(string='EI095', help='تاريخ انتهاء الاشتراك من التأمينات الاجتماعية')
    total_salary = fields.Float(string='EI100', help='الأجر الشامل')
    non_insurance_allowances = fields.Float(string='EI105', help='بدلات غير خاضعة تأمينيأ')
    insurance_wage = fields.Float(string='EI110', help='الأجر التأميني')
    comprehensive_health_insurance_status = fields.Char(string='EI115', help='حالة التأمين الصحي الشامل')

    # region ============================================================
    non_worker_wives_count = fields.Integer(string='EI120', help='عدد الزوجات الغير عاملات (التأمين الصحي الشامل)')
    dependents_number = fields.Integer(string='EI125', help='عدد المعالين (التأمين الصحي الشامل)')

    basic_salary = fields.Float(string='DTE160', help='المرتب الأساسي')
    bonuses_and_incentives = fields.Float(string='DTE170', help='مكافات وحوافز/أجر إضافي/منح')
    exempt_special_allowances = fields.Float(string='DTE180', help='علاوات خاصة معفاة')
    taxable_special_allowances = fields.Float(string='DTE175', help='علاوات خاصة خاضعة')
    commissions = fields.Float(string='DTE190', help='عمولات')
    employee_share_in_profits_1 = fields.Float(string='DTE230', help='نصيب العامل في الأرباح1 ')
    employee_service_fee = fields.Float(string='DTE235', help='مقابل الخدمة')
    tips = fields.Float(string='DTE260', help='البقشيش')
    board_member_salaries = fields.Float(string='DTE240', help='مرتبات ومكافات رؤساء اعضاء مجلس الادارة (مقابل العمل الإداري)')
    cash_compensation_for_leave_balance = fields.Float(string='DTE245', help='المقابل النقدى لرصيد الاجازات أثناء الخدمة')
    end_of_service_bonus = fields.Float(string='DTE250', help='مكافأة نهاية الخدمة الخاضعة')
    amounts_paid_under_special_laws_exempt_part = fields.Float(string='DTE255', help='مبالغ منصرفة بقوانين خاصة (الجزء المعفي منها)')
    other_taxable_allowances = fields.Float(string='DTE265', help='إضافات وبدلات اخرى خاضعة')
    company_borne_salary_tax = fields.Float(string='DTE270', help='ما تحملته المنشاة من ضريبة مرتبات')
    company_borne_employee_social_insurance_share = fields.Float(string='DTE275', help='ما تحملته المنشأة من حصة العامل في التأمينات الاجتماعية')
    quarterly_paid_taxable_amounts = fields.Float(string='DTE280', help='مبالغ خاضعة منصرفة بصورة ربع سنوية')
    semi_annual_paid_taxable_amounts = fields.Float(string='DTE285', help='مبالغ خاضعة منصرفة بصورة نصف سنوية')
    annual_paid_taxable_amounts = fields.Float(string='DTE290', help='مبالغ خاضعة منصرفة بصورة سنوية')
    car_benefits = fields.Float(string='DTE200', help='مزايا: السيارات')

    mobile_phone_benefits = fields.Float(string='DTE205', help='مزايا: الهواتف المحمولة')
    loan_and_advance_benefits = fields.Float(string='DTE210', help='مزايا: قروض وسلف')
    life_insurance_benefits_employer_share = fields.Float(string='DTE215', help='مزايا: التأمين على الحياة (حصة صاحب العمل)')
    company_shares_inside_outside_egypt = fields.Float(string='DTE220', help='مزايا: اسهم الشركة داخل مصر او خارج مصر')
    other_benefits = fields.Float(string='DTE225', help='مزايا أخرى')
    total_entitlements = fields.Float(string='DTE295', help='اجمالى الاستحقاقات')

    employee_share_in_social_insurance_and_pensions = fields.Float(
        string='DAE405', help='حصة العامل فى التأمينات الإجتماعية والمعاشات')
    employee_share_deducted_in_comprehensive_health_insurance = fields.Float(
        string='DAE410', help='حصة العامل المستقطعة في التأمين الصحي الشامل')
    amounts_exempt_under_special_laws = fields.Float(
        string='DAE415', help='مبالغ معفاة بقوانين خاصة')
    exempt_special_allowances_2 = fields.Float(string='DAE420', help='علاوات خاصة معفاة')
    social_allowance = fields.Float(
        string='DAE425',
        help='العلاوة الاجتماعية/الإضافية لجهات حكومية و ق.ع. وغير خاضع للخدمة المدنية',)
    personal_exemption = fields.Float(string='DAE430', help='الاعفاء الشخصي')
    installments_previous_period_loan_secondment_consideration = fields.Float(
        string='DAE435', help='اقساط (مدة سابقة/اعارة/اعتبارية)')
    employee_share_in_profits_2 = fields.Float(string='DAE440', help='نصيب العامل في الأرباح2')
    employee_insurance_fund_contributions = fields.Float(string='DAE450', help='اشتراكات العاملين فى صناديق التامين التى تنشاء طبقا لاحكام ق 54 لسنة 75')
    life_insurance_premiums_employee = fields.Float(string='DAE455', help='أقساط التأمين على حياة الممول لمصلحتة ومصلحةزوجته وأولاده القصر')
    health_insurance_premiums = fields.Float(string='DAE460', help='أقساط التأمين الصحي')
    pension_insurance_premiums = fields.Float(string='DAE465', help='أقساط تأمين لإستحقاق معاش')
    total_insurance_fund_contributions = fields.Float(
        string='DAE470', help='إجمالي اشتراكات صناديق التأمين')
    total_deductions = fields.Float(string='DAE475', help='اجمالى الاستقطاعات')

    net_income_period_bowl = fields.Float(string='TC505', help='صافى الدخل (وعاء الفتره)')
    annual_gross_income = fields.Float(string='TC510', help='الوعاء السنوي')
    tax_due_for_original_employment = fields.Float(string='TC515', help='الضريبة المستحقة عن الفترة للعمالة الاصلية')
    tax_due_for_employment_model_3 = fields.Float(string='TC520',
                                                  help='الضريبة المستحقة عن الفترة للعمالة المدرجه بنموذج 3 مرتبات')
    tax_due_for_employment_model_2 = fields.Float(string='TC525',
                                                  help='الضريبة المستحقة عن الفترة للعمالة المدرجه بنموذج 2 مرتبات')
    total_tax_due_for_all_employment = fields.Float(string='TC530',
                                                    help='اجمالى الضريبة المستحقة عن جميع انواع العمالة')
    tax_due_for_period = fields.Float(string='END705', help='الضريبة المحتسبة عن الفترة')
    tax_due_for_previous_periods_1_4_5_6_7 = fields.Float(string='TC535',
                                                          help='الضريبة المحتسبة عن الفترات السابقة للمعاملات الضريبية 1 و4 و5 و6 و7')
    tax_due_for_period_1_4_5_6_7 = fields.Float(string='TC540',
                                                help='الضريبة المحتسبة عن الفترة للمعاملات الضريبية 1 و4 و5 و6 و7')
    tax_due_for_previous_periods_2 = fields.Float(string='TC545',
                                                  help='الضريبة المحتسبة عن الفترات السابقة للمعاملة ضريبية 2')
    tax_due_for_period_2 = fields.Float(string='TC550', help='الضريبة المحتسبة عن الفترة للمعاملة ضريبية 2')
    tax_due_for_previous_periods_3 = fields.Float(string='TC555',
                                                  help='الضريبة المحتسبة عن الفترات السابقة للمعاملة ضريبية 3')
    tax_due_for_period_3 = fields.Float(string='TC560', help='الضريبة المحتسبة عن الفترة للمعاملة ضريبية 3')
    final_net_salary = fields.Float(string='TC565', help='صافي الأجر النهائي')

    social_contribution_for_martyrs_fund = fields.Float(string='NAD610',
                                                        help='مشاركه اجتماعيه استقطاع لصندوق الشهداء وما فى حكمها')
    support_for_people_with_disabilities = fields.Float(string='CLD825', help='دعم ذوي الهمم (قانون 200 لسنة 2020)')

    additions_loan_value = fields.Float(string='NAD615', help='اضافات: قيمة السلفة/قروض')
    additions_non_taxable_end_of_service_bonus = fields.Float(string='NAD620', help='اضافات: قيمة مكافأة نهاية الخدمة الغير خاضعة')
    additions_non_taxable_leave_balance = fields.Float(string='NAD625', help='اضافات: قيمة رصيد الأجازات الغير خاضعة')
    other_additions = fields.Float(string='NAD630', help='اضافات أخرى')

    deductions_alimony = fields.Float(string='NAD635', help='استقطاعات: نفقة')
    deductions_loan_installment = fields.Float(string='NAD640', help='استقطاعات: قيمة قسط السلفة/القرض')
    deductions_union_club_subscriptions = fields.Float(string='NAD645', help='استقطاعات: اشتراكات نقابات/أندية')
    deductions_penalties = fields.Float(string='NAD650', help='استقطاعات: جزاءات')
    deductions_life_insurance_premium = fields.Float(string='NAD655', help='استقطاعات: قيمة قسط بوليصة التأمين على الحياة')
    other_deductions = fields.Float(string='NAD660', help='استقطاعات أخرى')
    company_share_in_social_insurance = fields.Float(
        string='NAD665',help='حصة الشركة في التأمينات الاجتماعية')
    company_share_in_comprehensive_health_insurance = fields.Float(
        string='CLD805',help='حصة الشركة في التأمين الصحي الشامل')
    martyr_fund_contribution = fields.Float(
        string='CLD810', help='المساهمة فى صندوق الشهداء')
    company_share_in_comprehensive_medical_insurance = fields.Float(
        string='CLD815',help='حصة الشركة في التأمين الطبي الشامل')

    actually_transferred_amounts = fields.Float(string='CLD820', help='المبالغ المحولة فعلياً')

    # --------------------- Other Fields ---------------

    insurance_subscription_value = fields.Float(string='قيمة اشتراك التأمينات', help='قيمة اشتراك التأمينات')
    insurance_subscription_percentage = fields.Float(string='نسبة اشتراك التأمينات', help='نسبة اشتراك التأمينات')
    period_bowl = fields.Float(string='الوعاء للفترة', help='الوعاء للفترة')
    annual_tax = fields.Float(string='الضريبة السنوية', help='الضريبة السنوية')
    # endregion ---------------------------------------------

    def create(self, vals):
        for val in vals:
            for field in FieldsDict.get('char2'):
                value = val.get(field, '')
                if value and (len(value) == 1 or len(value) > 2) and value[0] != '0':
                    val[field] = '0' + value
            val['sequence'] = False
            # for field in FieldsDict.get('Date'):
            #     val[field] = float(str(round(val.get(field, 0.0), 2)).replace(',', '') ) #
            # if 'الله' in val.get('employee_name', ''):
            #     val['employee_name'] = val.get('employee_name', '').replace('اللّه', 'الله')
        res = super(EmployeeDetails, self).create(vals)
        return res

    def action_validate(self):
        validate_and_fix = self.env.context.get('validate_and_fix', False)
        barcodes = []
        national_ids = []
        for rec in self:
            rec.fix_note = ''
            if not rec.nationality:
                rec.fix_note += 'Nationality is required \n'
            elif rec.nationality and not re.match(r"^[0][1-2]$", rec.nationality):
                rec.fix_note += 'Nationality must be numeric with only 2 digits ex: 02, 01 \n'

            if not rec.employee_code:
                rec.fix_note += 'Employee code is required \n'
            elif rec.employee_code and not re.match(r"^[a-zA-Z0-9]+$", rec.employee_code):
                rec.fix_note += 'Employee code must be alphanumeric only \n'
            else:
                if rec.employee_code in barcodes:
                    rec.fix_note += 'Employee code must be unique \n'
                else:
                    barcodes.append(rec.employee_code)

            if rec.employee_name:
                if validate_and_fix:
                    rec.employee_name = rec.employee_name.strip().replace('  ', ' ')
                no = 4 if rec.nationality == '01' else 2
                if not re.match(r"^(?=\w+\s)(?=\w+(\s\w+){" + str(no - 1) + ",})(?=.{1,100}$)[^\s].*?[^\s]$", rec.employee_name):
                    rec.fix_note += f"Employee name must be {no} or more names without extra spaces and doesn't exceed 100 characters\n"
            else:
                rec.fix_note += 'Employee name is required \n'

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

            if rec.nationality == '02':
                if not rec.work_permit_number:
                    rec.fix_note += 'EI040 is required for foreigners \n'
                if not rec.work_permit_status:
                    rec.fix_note += 'EI035 is required for foreigners \n'
                if not rec.passport_number:
                    rec.fix_note += 'Passport number (EI026) is required for foreigners \n'

            if rec.work_permit_status and not re.match(r"^[0][1-3]$", rec.work_permit_status):
                rec.fix_note += 'Work permit status must be numeric with only 2 digits ex: 02, 01, 03 \n'

            if rec.passport_number and not re.match(r"\b[\u0600-\u06FFa-zA-Z0-9]{1,14}\b", rec.passport_number):
                rec.fix_note += 'Passport number must be 14 alphanumeric chars or less \n'

            if not rec.phone_number:
                rec.fix_note += 'Phone number is required \n'
            elif rec.phone_number and not re.match(r"^(010|011|012|015)\d{8}$", rec.phone_number):
                rec.fix_note += 'Phone number must be 11 number start with 010, 011, 012 or 015 \n'

            if not rec.job_position:
                rec.fix_note += 'Job position (EI045) is required \n'

            if not rec.branch_name:
                rec.fix_note += 'Branch name (EI055) is required \n'

            if not rec.tax_treatment:
                rec.fix_note += 'EI060 is required \n'
            else:
                if not re.match(r"^[0][1-7]$", rec.tax_treatment):
                    rec.fix_note += 'EI060 must be numeric with only 2 digits ex: 02, 01, 03, .., 07 \n'

            if rec.tax_treatment == '02' and not rec.tax_registration_number:
                rec.fix_note += 'EI065 is required for EI060 = 02 \n'
            elif rec.tax_registration_number and not re.match(r"\b\d{9}\b", rec.tax_registration_number):
                rec.fix_note += 'EI065 must be 9 number \n'

            # ---------------- الحالة التأمينية -------------------
            if not rec.insurance_status:
                rec.fix_note += 'EI070 is required \n'
            elif rec.insurance_status and not re.match(r"^(0[1-9]|1[0-9]|2[0-8])$", rec.insurance_status):
                rec.fix_note += 'EI070 must be numeric with only 2 digits ex: 02, 01, 03, .., 28 \n'

            if rec.insurance_status == '21':
                if validate_and_fix:
                    rec.insurance_number = False
                    rec.insurance_join_date = False
                    rec.non_insurance_allowances = False
                    rec.total_salary = False

                if rec.insurance_number:
                    rec.fix_note += 'EI075 should be empty for EI070 = 21 \n'
                if rec.total_salary:
                    rec.fix_note += 'EI100 should be empty for EI070 = 21 \n'
                if rec.insurance_join_date:
                    rec.fix_note += 'EI080 should be empty for EI070 = 21 \n'
                if rec.non_insurance_allowances:
                    rec.fix_note += 'EI105 should be empty for EI070 = 21 \n'
            else:
                if not rec.insurance_number:
                    rec.fix_note += 'EI075 is required \n'
                if not rec.total_salary:
                    rec.fix_note += 'EI100 is required \n'
                if not rec.insurance_join_date:
                    rec.fix_note += 'EI080 is required \n'
                # if not rec.non_insurance_allowances:
                #     rec.fix_note += 'EI105 is required \n'
                # if rec.insurance_number and not re.match(r"\b\d{1,8}\b", rec.insurance_number):
                #     rec.fix_note += 'EI075 must be 8 number or less \n'
                # if
            # -----------------------------------------------------------
            if rec.tax_treatment in ['02', '08']:
                if not rec.insurance_status == '21':
                    rec.fix_note += 'EI070 must be 21 for EI060 = 08 or 02 \n'

            if rec.tax_treatment == '08':
                if validate_and_fix and rec.work_duration:
                    rec.work_duration = False
                if rec.work_duration:
                    rec.fix_note += 'EI130 should be empty for EI060 = 08 \n'

                if not rec.annual_gross_income:
                    rec.fix_note += 'TC510 is required for EI060 = 08 \n'
                if not rec.tax_due_for_employment_model_2:
                    rec.fix_note += 'TC525 is required for EI060 = 08 \n'

            # ------------- Dates ---------------------------------------------------
            if rec.insurance_join_date and rec.sheet_date: #  yyyymmdd
                # if re.match(r"^\d{4}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$", rec.insurance_join_date):
                #     day = rec.insurance_join_date[6:7]
                #     if int(day) > 1:
                #         if rec.tax_treatment in ['01', '04']:
                #             if validate_and_fix:
                #                 rec.non_insurance_allowances = False
                #                 rec.total_salary = False
                #             if rec.non_insurance_allowances or rec.total_salary:
                #                 rec.fix_note += 'EI105 and EI100 should be empty for EI070 = 01 or 04 \n'
                # else:
                #     rec.fix_note += 'EI080 must be in yyyymmdd format \n'
                if (rec.insurance_join_date.day > 1 and rec.sheet_date.month == rec.insurance_join_date.month
                        and rec.tax_treatment in ['01', '04']):
                    if validate_and_fix:
                        rec.non_insurance_allowances = False
                        rec.total_salary = False
                    if rec.non_insurance_allowances or rec.total_salary:
                        rec.fix_note += 'EI105 and EI100 should be empty for EI060 = 01 or 04 \n'

            # if rec.end_of_service_date and re.match(r"^\d{4}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$", rec.end_of_service_date):
            #     rec.fix_note += 'EI090 must be in yyyymmdd format  \n'
            # if rec.social_insurance_end_date and re.match(r"^\d{4}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$", rec.social_insurance_end_date):
            #     rec.fix_note += 'EI095 must be in yyyymmdd format  \n'

            if rec.fix_note:
                rec.need_confirm = True
            else:
                rec.need_confirm = False

    def action_fix_decimal_fields(self):
        for rec in self:
            monetary_fields = FieldsDict.get('Flout')
            for field in monetary_fields:
                setattr(rec, field, float(str(round(getattr(rec, field), 2)).replace(',', '')))
            # if rec.need_confirm:
            #     rec.need_confirm = False
            # if rec.fix_note:
            #     rec.fix_note = ''

    def action_done(self):
        for rec in self:
            if not rec.need_confirm:
                rec.done = True

    def action_add_sheet_date(self):
        return {
            'name': 'Add Sheet Date',
            'view_mode': 'form',
            'res_model': 'tbg.add_date_wizard',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def action_open_form_view(self):
        return {
            'name': 'Form View',
            'view_mode': 'form',
            'res_model': 'tbg.salary_info_taxs',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': self.id
        }