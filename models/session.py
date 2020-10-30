from odoo import models, fields

class SessionAttendance(models.Model):

    _name = "session.attendance"
    name = fields.Many2one('class1.level', 'Student Name')
    master_name = fields.Many2one('master.session', 'Master name')
    attendance = fields.Selection([('Yes', 'Present'), ('No', 'Absent')], string='Attendance')



