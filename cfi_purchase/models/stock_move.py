# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sale_line_id = fields.Many2one(comodel_name='sale.order.line', related='move_id.production_sale_line_id', string='Related Sale Line')

class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_order_id = fields.Many2one(comodel_name='sale.order', compute='_compute_sale_order_fields')
    production_sale_line_id = fields.Many2one(comodel_name='sale.order.line', compute='_compute_sale_order_fields')
    # @api.depends('raw_material_production_id', 'raw_material_production_id.sale_order_ids', 'production_id', 'production_id.sale_order_ids')
    @api.depends('raw_material_production_id', 'raw_material_production_id.sale_order_ids')
    def _compute_sale_order_fields(self):
        for move in self:
            if move.raw_material_production_id.sale_order_ids:
                for so_line in move.raw_material_production_id.sale_order_ids.mapped('order_line'):
                    if move.bom_line_id in so_line.bom_id.mapped('bom_line_ids'):
                        move.production_sale_line_id = so_line.id
                        move.sale_order_id = so_line.order_id.id
