# -*- coding: utf-8 -*-
{
    'name': "tbg_data_validator",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
        Validate salary Data imported from Excel sheets
    """,

    'author': "TopBusiness Group",
    'website': "https://www.topbusiness-hr.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_hr_outsource'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/salary_item_temp_views.xml",
        "views/hr_employee_temp_views.xml",
        "views/_menu.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'module_type': 'official',

    'installable': True,
    'auto_install': False,

}

