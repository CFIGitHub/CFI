# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
import pudb

class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

class StockRule(models.Model):
    _inherit = 'stock.rule'

    # handles run manufacture
    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom):
        ret_vals = super(StockRule, self)._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom)
        return {
            'sale_line_id': values.get('sale_line_id', False),
            **ret_vals
        }

    # handles run pull
    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        ret_vals = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        return {
            'sale_line_id': values.get('sale_line_id', False),
            **ret_vals
        }

    # handles run buy
    def _prepare_purchase_order_line(self, product_id, product_qty, product_uom, company_id, values, po):
        ret_vals = super(StockRule, self)._prepare_purchase_order_line(product_id, product_qty, product_uom, company_id, values, po)
        return {
            'sale_line_id': values.get('sale_line_id', False),
            **ret_vals
        }
