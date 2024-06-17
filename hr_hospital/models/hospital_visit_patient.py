# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalVisitPatient(models.Model):
    _name = 'hospital.visit.patient'

    name = fields.Char()
