from odoo import fields, models


class Employee(models.Model):
    _name = 'employee.building.assignment'
    _description = 'employee'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    building_id = fields.Many2one('fm.building', string='Building')
    assignment_start_date = fields.Date(string='Start Date')
    assignment_end_date = fields.Date(string='End Date')
