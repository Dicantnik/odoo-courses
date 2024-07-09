from odoo import models, fields


class Person(models.AbstractModel):
    _name = 'hospital.person'

    name = fields.Char()
    surname = fields.Char()
    phone = fields.Char()
    photo = fields.Image()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['hospital.person', ]

    specialization = fields.Selection([('travmatolog', 'Travmatolog'),
                                       ('pediatr', 'Pediatr')])
    is_intern = fields.Boolean()
    doctor_mentor_id = fields.Many2one(comodel_name='hospital.doctor',
                                       domain="[('is_intern', '=', False)]", )
    intern_doctor_ids = fields.One2many(comodel_name='hospital.doctor',
                                        inverse_name='doctor_mentor_id', )
    mentor_name = fields.Char(related='doctor_mentor_id.name')
    mentor_surname = fields.Char(related='doctor_mentor_id.surname')
    mentor_phone = fields.Char(related='doctor_mentor_id.phone')
    mentor_specialization = fields.Selection(
        related='doctor_mentor_id.specialization'
    )
    color = fields.Integer()

    def quick_set_visit(self):
        return {
            'name': 'Visit Patient',
            'model': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hospital.visit.patient',
            'context': {'default_doctor_id': self.id},
            'type': 'ir.actions.act_window',
        }
