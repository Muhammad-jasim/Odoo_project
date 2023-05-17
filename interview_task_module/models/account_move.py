from odoo import models,fields, api , _


class AccountMove(models.Model):
    _inherit= 'account.move'

    delivery_charge = fields.Float(string="Delivery Charge", compute = "compute_delivery_charge", store=True)


    @api.depends('amount_total')
    def compute_delivery_charge(self):
        for rec in self:
            if rec.amount_total:
                rec.delivery_charge = rec.amount_total * 0.1
            else:
                rec.delivery_charge = 0.00