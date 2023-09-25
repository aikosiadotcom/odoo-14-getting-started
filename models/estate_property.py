from odoo import models, fields, api
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
    living_area = fields.Integer(default=0)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(default=0)
    garden_orientation = fields.Selection(string='Garden Orientation', selection=[('north','North'),('south','South'),('east','East'),('west','West')])

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    seller_id = fields.Many2one("res.users", string="Salesman")
    property_tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")
    property_offer_ids = fields.One2many("estate.property.offer","property_id")
    create_date = fields.Datetime("create_date")

    total_area = fields.Integer(compute="_compute_total_area")

    active = fields.Boolean(default=True)
    state = fields.Selection(default="new", selection=[('new','New'),('offer_received','Offer Receive'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')])

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area * record.garden_area

    @api.onchange("garden")
    def _onchange_garden(self):
        if(self.garden is None or self.garden is True):
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""