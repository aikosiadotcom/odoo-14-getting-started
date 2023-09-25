from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "offer of property"

    price = fields.Float()
    status = fields.Selection(copy=False,selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id = fields.Many2one("res.partner")
    property_id = fields.Many2one("estate.property")
    create_date = fields.Date()

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")

    @api.depends("create_date","validity")
    def _compute_date_deadline(self):
        for record in self:
            if(record.create_date is False):
                record.date_deadline = fields.Datetime.today() + relativedelta(days=+record.validity)
            else:
                record.date_deadline = record.create_date + relativedelta(days=+record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            if(record.create_date is False):
                record.validity = abs((fields.Datetime.today()-record.validity).days)
            else:
                record.validity = abs(((record.create_date-record.date_deadline).days))

    def action_accept(self):
        return True
    
    def action_reject(self):
        return True