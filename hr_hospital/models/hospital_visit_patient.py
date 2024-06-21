from datetime import datetime
from odoo import models, fields, _
from odoo.exceptions import UserError


class HospitalVisitPatient(models.Model):
    _name = 'hospital.visit.patient'

    status = fields.Selection([('planned', 'Planned'),
                               ('ended', 'Ended'),
                               ('canceled', 'Canceled')])
    planned_date_time = fields.Datetime()
    fact_date_time = fields.Datetime()
    doctor_id = fields.Many2one(comodel_name='hospital.doctor', )
    patient_id = fields.Many2one(comodel_name='hospital.patient', )
    diagnosis_ids = fields.One2many(comodel_name='hospital.diagnosis',
                                    inverse_name='visit_id', )

    def create(self, vals_list):
        records = (self.env['hospital.visit.patient'].
                   search(["&",
                           ('doctor_id', '=', vals_list['doctor_id']),
                           ('patient_id', '=', vals_list['patient_id'])]))
        new_record_date = datetime.strptime(vals_list['planned_date_time'],
                                            '%Y-%m-%d %H:%M:%S').date()
        if records:
            for record in records:
                if record.planned_date_time.date() == new_record_date:
                    raise UserError(_("Cannot create record with the same"
                                      " doctor patient and date"))
        return super().create(vals_list)

    def unlink(self):
        for record in self:
            if record.diagnosis_ids:
                raise UserError(_("Cannot delete record with Diagnosis"))
        return super(HospitalVisitPatient, self).unlink()
