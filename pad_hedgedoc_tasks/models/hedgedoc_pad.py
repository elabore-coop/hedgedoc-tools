# -*- coding: utf-8 -*-

from odoo import models, fields, _


class TaskHedgedocPad(models.Model):
    _name = "task.hedgedoc.pad"
    _inherit = "hedgedoc.pad"

    task_id = fields.Many2one("project.task", string=_("Associated task"), copy=True)
