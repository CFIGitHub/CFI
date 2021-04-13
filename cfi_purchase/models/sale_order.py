# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    purchase_order_ids = fields.Many2many(comodel_name='purchase.order', compute='_compute_purchase_order_ids', string='Purchase Orders')
    mrp_production_ids = fields.Many2many(comodel_name='mrp.production', compute='_compute_production_order_ids', string='Production Orders')

    @api.depends('purchase_order_count')
    def _compute_purchase_order_ids(self):
        for order in self:
            order.purchase_order_ids = order._get_purchase_orders()

    @api.depends('mrp_production_count')
    def _compute_production_order_ids(self):
        for order in self:
            order.mrp_production_ids = order.procurement_group_id.stock_move_ids.created_production_id.procurement_group_id.mrp_production_ids.ids

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    production_line_ids = fields.One2many('stock.move.line', 'sale_line_id', string='Generated Production Lines', readonly=True)
