from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

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
    state = fields.Selection(default="new", selection=[('new','New'),('offer_received','Offer Receive'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],readonly=True)

    _sql_constraints = [
            ('positive_expected_price', 'CHECK (expected_price >= 0)', 'Expected Price must be positive!'),
            ('positive_selling_price', 'CHECK (selling_price >= 0)', 'Selling Price must be positive!'),
            # The line `('unique_property_tag_ids', 'unique (property_tag_ids)', 'Tag must unique')`
            # is defining a SQL constraint on the `estate.property` model.
            ('unique_property_tag_ids', 'unique (property_tag_ids)', 'Tag must unique'),
    ]

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

    def btn_cancel(self):
        for record in self:
            if(record.state == "sold"):
                raise ValidationError("its already sold. so you can't cancel it")
            else:
                record.state = "canceled"
        return True
    
    def btn_sold(self):
        for record in self:
            if(record.state == "canceled"):
                raise ValidationError("its already cancel. so you can't sell it")
            else:
                record.state = "sold"
        return True
    
    @api.constrains("garden_area")
    def _check_garden_area(self):
        for record in self:
            if(record.garden_area > 2000):
                raise ValidationError("garden area cannot more than 2000")