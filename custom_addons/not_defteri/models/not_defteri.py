from odoo import fields, models

class NotDefteri(models.Model):
    _name = 'not.defteri'
    _description = 'Not Defteri'

    name = fields.Char(string='Başlık', required=True)
    note = fields.Text(string='Not')