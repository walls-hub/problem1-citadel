from odoo import models, fields

class MasterSession(models.Model):

    _name = "master.session"
    name = fields.Char(string='Name', required=True)
    session = fields.Selection([('1', 'session1'), ('2', 'session2'), ('3', 'session3')], string='Session')
    level = fields.Selection([('1', 'easy'), ('2', 'difficult'), ('3', 'hard')], string='Level')