# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bm-advanced(models.Model):
#     _name = 'bm-advanced.bm-advanced'
#     _description = 'bm-advanced.bm-advanced'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
