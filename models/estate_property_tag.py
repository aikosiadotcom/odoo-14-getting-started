from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property.tag"
    _description = "tag of property"

    name = fields.Char()