# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_order_ids = fields.Many2many(comodel_name='sale.order', compute='_compute_sale_order_ids', string='Sale Orders')

    @api.depends('sale_order_count')
    def _compute_sale_order_ids(self):
        for production in self:
            production.sale_order_ids = production.procurement_group_id.mrp_production_ids.move_dest_ids.group_id.sale_id.ids
