from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HospitalDoctor(models.Model):
    _name = 'hospital.illness'
    _parent_name = "parent_id"

    name = fields.Char()
    parent_id = fields.Many2one(comodel_name="hospital.illness",
                                string='Parent',
                                index=True)
    parent_path = fields.Char(index=True)

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise UserError(_('You cannot create recursive illness'))
