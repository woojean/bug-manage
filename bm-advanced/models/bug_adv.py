# -*- coding: utf-8 -*-
from odoo import models, fields


class bugAdvanced(models.Model):
    _inherit = 'bm.bug'

    # 在进阶模型中新增一个所需的时间字段
    need_time = fields.Integer('所需时间(小时)')

    # 为bm.bug类的name字段增加help属性（不改变原来的字段）
    name = fields.Char(help='简要描述发现的bug')

    # 每个bug都有一个阶段，即一个阶段与bug是1对多的关系，即many bug对应one stage
    stage_id = fields.Many2one('bm.bug.stage', '阶段')
    tag_ids = fields.Many2many('bm.bug.tag', string='标示')
