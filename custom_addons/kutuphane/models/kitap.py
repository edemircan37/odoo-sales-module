from odoo import models, fields

class KutuphaneKitap(models.Model):
    _name = 'kutuphane.kitap'
    _description = 'Kütüphane Kitap'

    name = fields.Char(string='Kitap Adı', required=True)
    yazar = fields.Char(string='Yazar')
    yayin_tarihi = fields.Date(string='Yayın Tarihi')
