# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_order_ids = fields.Many2many(comodel_name='sale.order', compute='_compute_sale_order_ids', string='Sale Orders')
    sale_line_id = fields.Many2many(comodel_name='sale.order.line', string='Sale Order Line')

    @api.depends('sale_order_count')
    def _compute_sale_order_ids(self):
        for production in self:
            production.sale_order_ids = production.procurement_group_id.mrp_production_ids.move_dest_ids.group_id.sale_id.ids

    def _get_move_raw_values(self, product_id, product_uom_qty, product_uom, operation_id=False, bom_line=False):
        data = super(MrpProduction, self)._get_move_raw_values(product_id, product_uom_qty, product_uom, operation_id, bom_line)
        data.update({'sale_line_id': self.sale_line_id[0].id if len(self.sale_line_id) else False})
        return data

    def _get_move_finished_values(self, product_id, product_uom_qty, product_uom, operation_id=False, byproduct_id=False):
        data = super(MrpProduction, self)._get_move_finished_values(product_id, product_uom_qty, product_uom, operation_id, byproduct_id)
        data.update({'sale_line_id': self.sale_line_id[0].id if len(self.sale_line_id) else False})
        return data
