from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property.type"
    _description = "type of property"

    name = fields.Char()