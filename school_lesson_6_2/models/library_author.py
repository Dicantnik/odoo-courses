from odoo import fields, models, api
import datetime

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Datetime('Birthday', default=datetime.datetime.now())
    days_difference = fields.Integer(compute='_compute_difference_in_days')

    @api.depends('birth_date')
    def _compute_difference_in_days(self):
        for rec in self:
            rec.days_difference = (datetime.date.today() - rec.birth_date.date()).days

    def name_get(self):
        return [(rec.id, "%s %s" % (
            rec.first_name, rec.last_name)) for rec in self]

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)
