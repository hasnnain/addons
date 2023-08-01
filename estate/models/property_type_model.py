from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Model for Real-Estate Properties Types"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ('unique_property_type_name', 'unique(name)', 'Property Type name must be unique!')
    ]
