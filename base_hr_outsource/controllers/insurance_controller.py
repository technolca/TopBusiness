# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MedicalInsuranceController(http.Controller):

     @http.route('/medical_insurance/plans', type='http', auth='user', website=True)
     def list_insurance_plans(self):
         plans = request.env['tbg.insurance_plan'].search([])
         return request.render('odoo_medical_insurance.insurance_plan_list', {'plans': plans})

     @http.route('/medical_insurance/claims', type='http', auth='user', website=True)
     def list_insurance_claims(self):
         claims = request.env['tbg.insurance_claim'].search([])
         return request.render('odoo_medical_insurance.insurance_claim_list', {'claims': claims})

