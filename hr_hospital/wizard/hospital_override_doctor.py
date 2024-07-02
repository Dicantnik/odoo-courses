from odoo import models, fields


class HospitalOverrideDoctor(models.Model):
    _name = 'hospital.override.doctor'

    doctor_id = fields.Many2one(comodel_name="hospital.doctor")

    def action_submit_override(self):
        patient_ids = self.env.context.get('active_ids')
        for one_id in patient_ids:
            patient = self.env['hospital.patient'].browse(one_id)
            patient.personal_doctor_id = self.doctor_id
