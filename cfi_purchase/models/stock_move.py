# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sale_line_id = fields.Many2one(comodel_name='sale.order.line', compute='_compute_sale_line_id', string='Related Sale Line')

    @api.depends('move_id', 'move_id.sale_line_id', 'production_id', 'production_id.sale_order_ids')
    def _compute_sale_line_id(self):
        for line in self:
            if line.move_id.sale_line_id:
                line.sale_line_id = line.move_id.sale_line_id
            else:
                try:
                    bom_line_id = line.move_id.mapped('bom_line_id')
                    order_lines = production_id.mapped('sale_order_ids.order_line')
                    for so_line in order_lines:
                        if line.product_id in so_line.bom_id.bom_line_ids.mapped('product_id'):
                            line.sale_line_id = so_line.id
                except e:
                    line.sale_line_id = False
