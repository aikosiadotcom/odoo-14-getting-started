from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "tag of property"
    _order = "name"

    name = fields.Char()
    color = fields.Integer()