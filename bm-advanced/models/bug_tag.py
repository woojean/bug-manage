# -*- coding: utf-8 -*-
from odoo import models, fields


class bugTag(models.Model):
    _name = 'bm.bug.tag'
    _description = 'bug标示'
    name = fields.Char('名称')

    # 对应bug中tag_ids=fields.Many2many('bm.bug.tag',string='标示')
    bug_ids = fields.Many2many('bm.bug', string='bug')
