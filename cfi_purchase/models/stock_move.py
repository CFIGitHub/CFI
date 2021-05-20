# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sale_order_id = fields.Many2one(comodel_name='sale.order', related='move_id.sale_order_id', string='Related Sale Order')
    sale_line_id = fields.Many2one(comodel_name='sale.order.line', related='move_id.sale_line_id', string='Related Sale Order Line')


class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_order_id = fields.Many2one(comodel_name='sale.order', related='sale_line_id.order_id')

    '''
    sale.order > sale.order.line(_action_launch_stock_rule) > procurement.group(run) > stock.rule(_run_pull) > stock.move(_action_confirm)

    stock.rule(_run_manufacture) > mrp.production
                called on create, write, action_confirm      procurement should have sale_line_id in values
                each procurment is related to a single sale order line
                _run_manufacture will create mrp production then stock moves within _run_manufacture > _get_moves_raw_values > _get_move_raw_values
                                                                                                    > _get_moves_finished_values >


        _action_launch_stock_rule
            - _prepare_procurement_vals ( sale_line_id passed in procurement.values['sale_line_id])
        _run_pull
        rule._get_stock_move_values(*procurements)
        
    '''

    def _prepare_procurement_values(self):
        values = super(StockMove, self)._prepare_procurement_values()
        values.update({'sale_line_id': self.sale_line_id.id})
        return values
