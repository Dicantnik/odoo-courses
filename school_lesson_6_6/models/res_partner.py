from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = "res.partner"

    @api.constrains('email')
    def _check_email(self):
        count_email = self.search_count([('email', '=', self.email)])
        if count_email > 1 and self.email is not False:
            raise ValidationError('The email already registered, please use another email!')