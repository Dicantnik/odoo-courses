from odoo import models, fields, api


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'

    visit_id = fields.Many2one(comodel_name='hospital.visit.patient')
    is_intern = fields.Boolean(related='visit_id.doctor_id.is_intern')
    illness_ids = fields.Many2many(comodel_name="hospital.illness",
                                   relation="diagnosis_illness",
                                   column1="diagnosis_id",
                                   column2="illness_id")
    description = fields.Text()
    is_confirmed = fields.Boolean(compute='_compute_is_confirmed',
                                  readonly=False)
    patient_id = fields.Many2one(comodel_name='hospital.patient',
                                 related='visit_id.patient_id')

    @api.depends('is_intern')
    def _compute_is_confirmed(self):
        for rec in self:
            rec.is_confirmed = not rec.is_intern

    @api.depends('visit_id', 'illness_ids')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = (
                f"{rec.visit_id.planned_date_time}"
                f" - {rec.visit_id.doctor_id.name}"
                f" - {rec.visit_id.patient_id.name}"
            )
