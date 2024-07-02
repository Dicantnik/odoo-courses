from odoo import models, fields


class HospitalListDiagnosis(models.Model):
    _name = 'hospital.list.diagnosis'

    doctor_ids = fields.Many2many(comodel_name="hospital.doctor")
    from_date = fields.Date(required=True)
    to_date = fields.Date(required=True)
    illness_ids = fields.Many2many(comodel_name="hospital.illness")

    def action_submit_list_diagnosis(self):
        domain = ["&",
                  ("create_date", ">", str(self.from_date)),
                  ("create_date", "<", str(self.to_date))]
        if self.doctor_ids:
            domain.append(("visit_id.doctor_id", "in", self.doctor_ids.ids))
            domain.insert(0, "&")
        if self.illness_ids:
            domain.append(("illness_ids", "in", self.illness_ids.ids))
            domain.insert(0, "&")
        return {
            'name': 'Diagnosis',
            'model': 'ir.actions.act_window',
            'view_type': 'tree',
            'view_mode': 'tree,form',
            'res_model': 'hospital.diagnosis',
            'context': {'group_by': ['illness_ids']},
            'domain': domain,
            'type': 'ir.actions.act_window',
        }
