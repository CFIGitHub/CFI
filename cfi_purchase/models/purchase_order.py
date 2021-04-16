# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_ids = fields.Many2many(comodel_name='sale.order', compute='_compute_sale_order_ids', string='Sale Orders')

    @api.depends('sale_order_count')
    def _compute_sale_order_ids(self):
        for purchase in self:
            purchase.sale_order_ids = purchase._get_sale_orders()

# class PurchaseOrderLine(models.Model):
#     _inherit = 'purchase.order.line'
