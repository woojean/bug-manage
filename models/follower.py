# -*- coding: utf-8 -*-
from odoo import models, fields


class follower(models.Model):
    _inherit = 'res.partner'  # 继承


    # 扩展字段遵循的逻辑就是我们没有修改的属性都会保留下来，就这个例子而言，相当于是我们在res.partner上面增加了bug_ids字段。
    bug_ids = fields.Many2many('bm.bug', string='bug')


