from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Getting Started Test"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Datetime.today() + relativedelta(months=+3),copy=False)
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Garden Orientation', selection=[('north','North'),('south','South'),('east','East'),('west','West')])

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    seller_id = fields.Many2one("res.users", string="Salesman")

    property_tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")

    active = fields.Boolean(default=True)
    state = fields.Selection(default="new", selection=[('new','New'),('offer_received','Offer Receive'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')])