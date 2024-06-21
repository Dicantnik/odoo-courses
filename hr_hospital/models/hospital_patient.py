from datetime import date
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class HospitalDoctor(models.Model):
    _name = 'hospital.patient'
    _inherit = ['hospital.person', ]

    personal_doctor_id = fields.Many2one(comodel_name='hospital.doctor',)
    birthday_date = fields.Date()
    age = fields.Integer(compute='_compute_age_patient')
    passport_data = fields.Char()
    contact_person = fields.Char()

    @api.depends('birthday_date')
    def _compute_age_patient(self):
        today = date.today()
        for rec in self:
            year_difference = relativedelta(today, rec.birthday_date).years
            rec.age = year_difference
