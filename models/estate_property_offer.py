from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "offer of property"

    price = fields.Float()
    status = fields.Selection(copy=False,selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id = fields.Many2one("res.partner")
    property_id = fields.Many2one("estate.property")