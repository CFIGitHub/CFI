# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_ids = fields.Many2many(comodel_name='sale.order', groups="sales_team.group_sale_salesman", compute='_compute_sale_order_ids', string='Sale Orders')

    @api.depends('sale_order_count')
    def _compute_sale_order_ids(self):
        for purchase in self:
            purchase.sale_order_ids = purchase._get_sale_orders()

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.model
    def _prepare_purchase_order_line_from_procurement(self, product_id, product_qty, product_uom, company_id, values, po):
        ret_vals = super(PurchaseOrderLine, self)._prepare_purchase_order_line_from_procurement(product_id, product_qty, product_uom, company_id, values, po)
        if values.get('sale_line_id', False):
            ret_vals.update({'sale_line_id': values.get('sale_line_id')})
        return ret_vals
