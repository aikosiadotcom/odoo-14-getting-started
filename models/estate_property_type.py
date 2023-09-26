from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "type of property"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(default=1)
    property_ids = fields.One2many("estate.property","property_type_id")

    offer_ids = fields.One2many("estate.property.offer","property_type_id")

    offer_count = fields.Integer(compute="_compute_count")

    @api.depends("offer_ids")
    def _compute_count(self):
        for record in self:
            record.offer_count = len(self.offer_ids)