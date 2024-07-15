from odoo import models, fields


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    # This model is needed to store book categories

    name = fields.Char()


    def actin_books_this_category(self):
        """Determine the options for opening view of model library.book
         with default filter active category

        :return: dictionary:
        """
        return {
            'name': 'Books',
            'model': 'ir.actions.act_window',
            'view_type': 'tree',
            'view_mode': 'tree,form',
            'res_model': 'library.book',
            # 'context': {'default_category_id': self.id},
            'domain': f'[("category_id", "=", {self.id})]',
            'type': 'ir.actions.act_window',
        }
