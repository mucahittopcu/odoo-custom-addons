from odoo import fields, models, api


class Building(models.Model):
    _name = 'fm.building'
    _description = 'Buildings'
    _rec_name = 'building_name'

    building_name = fields.Char(required=True, string='Building Name')
    building_no = fields.Char(required=True, string='Building No')
    building_dimension = fields.Char( string='Building Dimension')
    construction_year = fields.Integer( string='Construction Year')
    structural_system = fields.Char(string='Structural System')
    office_area_as_mt_square = fields.Float(string='Office Area As Mt Square')
    under_roof_area_as_mt = fields.Float(string='Under Roaf Area As Mt')
    under_roof_area_as_feet = fields.Float( compute='set_age_group', string='Under Roaf Area As Feet ')

    @api.depends('under_roof_area_as_mt')
    def set_age_group(self):
        for rec in self:
            rec.under_roof_area_as_feet = rec.under_roof_area_as_mt * 3.28