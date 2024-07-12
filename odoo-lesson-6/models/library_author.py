from odoo import api, models, fields
import datetime

class LibraryAuthor(models.Model):
    _name = 'library.author'

    name = fields.Char()
    date_for_me = fields.Datetime(default=datetime.datetime.now())
    days_difference = fields.Integer(compute='_compute_difference_in_days')

    @api.depends('date_for_me')
    def _compute_difference_in_days(self):
        for rec in self:
            rec.days_difference = (datetime.date.today() - rec.date_for_me.date()).days
