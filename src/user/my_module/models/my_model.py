from odoo import models, fields

class MyModel(models.Model):
    _name = 'my_model.my_model'
    _description = 'My Model Description'

    name = fields.Char(string="Name")
