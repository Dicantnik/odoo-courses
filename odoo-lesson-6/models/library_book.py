from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char()
    user_id = fields.Many2one(comodel_name='res.users')
    author_id = fields.Many2one(comodel_name='library.author')
    book_category_id = fields.Many2one(comodel_name='library.book.category')
