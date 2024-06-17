# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'

    name = fields.Char()
