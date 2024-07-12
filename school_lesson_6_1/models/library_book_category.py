from odoo import models, fields


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'

    name = fields.Char()
