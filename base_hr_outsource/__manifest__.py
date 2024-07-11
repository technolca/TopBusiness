# -*- coding: utf-8 -*-
{
    'name': "tbg_base_hr_outsource",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
    Adds more personal data for employees
    """,

    'author': "TopBusiness Group",
    'website': "https://www.topbusiness-hr.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'analytic', 'hr_contract', 'om_hr_payroll'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/hiring_papers_views.xml',
        "views/res_company_views.xml",
        "views/salary_item_views.xml",
        "views/hr_contract_views.xml",
        "views/insurance_plan_views.xml",
        "views/insurance_claim_views.xml",
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'module_type': 'official',

    'installable': True,
    'auto_install': False,

}

