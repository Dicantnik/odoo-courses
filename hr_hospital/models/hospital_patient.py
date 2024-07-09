from datetime import date
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['hospital.person', ]

    personal_doctor_id = fields.Many2one(comodel_name='hospital.doctor',)
    birthday_date = fields.Date()
    age = fields.Integer(compute='_compute_age_patient')
    passport_data = fields.Char()
    contact_person = fields.Char()
    diagnosis_ids = fields.One2many(comodel_name='hospital.diagnosis',
                                    inverse_name='patient_id',
                                    string='Diagnosis history')

    @api.depends('birthday_date')
    def _compute_age_patient(self):
        today = date.today()
        for rec in self:
            year_difference = relativedelta(today, rec.birthday_date).years
            rec.age = year_difference

    def quick_set_visit(self):
        return {
            'name': 'Visit Patient',
            'model': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hospital.visit.patient',
            'context': {'default_patient_id': self.id},
            'type': 'ir.actions.act_window',
        }

    def action_history_visits(self):
        return {
            'name': 'Visit Patient',
            'model': 'ir.actions.act_window',
            'view_type': 'tree',
            'view_mode': 'tree,form',
            'res_model': 'hospital.visit.patient',
            'domain': f'[("patient_id", "=", {self.id})]',
            'type': 'ir.actions.act_window',
        }
