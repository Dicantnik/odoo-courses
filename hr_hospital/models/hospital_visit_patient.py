from datetime import datetime
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class HospitalVisitPatient(models.Model):
    _name = 'hospital.visit.patient'

    status = fields.Selection(
        [
            ('planned', 'Planned'),
            ('ended', 'Ended'),
            ('canceled', 'Canceled')
        ],
        default='planned',
    )
    planned_date_time = fields.Datetime(required=True)
    fact_date_time = fields.Datetime()
    doctor_id = fields.Many2one(comodel_name='hospital.doctor', )
    patient_id = fields.Many2one(comodel_name='hospital.patient', )
    diagnosis_ids = fields.One2many(comodel_name='hospital.diagnosis',
                                    inverse_name='visit_id', )

    @api.constrains('doctor_id', 'patient_id', 'planned_date_time')
    def _check_rules(self):
        records = (self.env['hospital.visit.patient'].
                   search(["&",
                           ('doctor_id', '=', self.doctor_id.id),
                           ('patient_id', '=', self.patient_id.id)]))
        matched_records = []
        if records:
            new_record_date = datetime.strptime(str(self.planned_date_time),
                                                '%Y-%m-%d %H:%M:%S').date()
            for record in records:
                if record.planned_date_time.date() == new_record_date:
                    matched_records.append(record)
        if len(matched_records) > 1:
            raise UserError(_("Cannot create record with the same"
                              " doctor patient and date"))

    def unlink(self):
        for record in self:
            if record.diagnosis_ids:
                raise UserError(_("Cannot delete record with Diagnosis"))
        return super(HospitalVisitPatient, self).unlink()

    @api.depends('planned_date_time', 'doctor_id', 'patient_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = (
                f"{rec.planned_date_time}"
                f" - {rec.doctor_id.name}"
                f" - {rec.patient_id.name}"
            )
