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
