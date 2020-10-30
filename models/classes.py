from odoo import models, fields

class Classlevel(models.Model):

    _name = "class1.level"
    name = fields.Char(string='Student Name', required=True)
    dob = fields.Date(string='Date of Birth', required=True)

