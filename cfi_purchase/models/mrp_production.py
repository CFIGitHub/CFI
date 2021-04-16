# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
import pudb

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_order_ids = fields.Many2many(comodel_name='sale.order', compute='_compute_sale_order_ids', string='Sale Orders')
    sale_line_id = fields.Many2many(comodel_name='sale.order.line', string='Sale Order Line')

    @api.depends('sale_order_count', 'move_raw_ids', 'move_finished_ids')
    def _compute_sale_order_ids(self):
        for production in self:
            production.sale_order_ids = production.procurement_group_id.mrp_production_ids.move_dest_ids.group_id.sale_id.ids
            lines = self.env['sale.order.line']
            lines |= production.move_raw_ids.mapped('sale_line_id')
            lines |= production.move_finished_ids.mapped('sale_line_id')
            production.sale_line_id = lines.ids

    # def _get_move_raw_values(self, product_id, product_uom_qty, product_uom, operation_id=False, bom_line=False):
