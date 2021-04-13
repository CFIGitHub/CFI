# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sale_line_id = fields.Many2one(comodel_name='sale.order.line', related="move_id.sale_line_id", readonly=True, string='Related Sale Line')
