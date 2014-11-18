# -*- coding: utf-8 -*-
from openerp.osv import fields as old_fields
from openerp.osv import osv
from openerp import api, models, fields
from openerp import SUPERUSER_ID
from openerp.tools.translate import _
from openerp.exceptions import AccessError

class hr_employee(models.Model):
    '''
    Employee
    '''

    _inherit = 'hr.employee'

    def _payslip_count(self, cr, uid, ids, field_name, arg, context=None):
        try:
            res = super(hr_employee, self)._payslip_count(cr, uid, ids, field_name, arg, context)
        except AccessError, e:
            res = {
                employee_id: 0
                for employee_id in ids
            }
        return res
    _columns = {
        'payslip_count': old_fields.function(_payslip_count, type='integer', string='Payslips'),
    }

    def _get_access_to_employee_information(self):
        self.access_to_employee_information = (self.user_id.id == self.env.uid) or (self.env.ref('access_custom.group_employee_information').id in self.env.user.groups_id.ids)

    access_to_employee_information = fields.Boolean('Access to employee information', compute=_get_access_to_employee_information, store=False)
