from odoo import models, fields

class MyModel(models.Model):
    _name = 'my_module.my_model'
    _description = 'A simple model'
    name = fields.Char("Name")
