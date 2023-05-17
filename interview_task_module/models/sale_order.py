from odoo import models,fields, api , _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit= 'sale.order'

    delivery_charge = fields.Float(string="Delivery Charge", compute = "compute_delivery_charge")


    @api.depends('amount_total')
    def compute_delivery_charge(self):
        for rec in self:
            if rec.amount_total:
                rec.delivery_charge = rec.amount_total * 0.1
            else:
                rec.delivery_charge = 0.00

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['delivery_charge'] = self.delivery_charge
        return invoice_vals


class SaleOrderLine(models.Model):
    _inherit= 'sale.order.line'

    brand_name = fields.Char(string="Brand Name")

    @api.onchange('product_id')
    def onchange_brand_name(self):
        for line in self:
            if line.product_id:
                line.brand_name = line.product_id.brand_name
            else:
                line.brand_name = ''


    @api.onchange('price_unit')
    def onchange_minimum_cost(self):
        for line in self:
            if line.price_unit and line.price_unit < line.product_id.minimum_cost:
                raise UserError(_('Unit Price is less than Minimum Cost (Please Change Unit price to more than Minimum Cost (' + str(line.product_id.minimum_cost) + '))'))