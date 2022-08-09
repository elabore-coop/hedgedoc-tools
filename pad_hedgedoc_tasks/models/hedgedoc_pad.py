# -*- coding: utf-8 -*-

from odoo import models, fields, _


class HedgedocPad(models.Model):
    _inherit = "hedgedoc.pad"

    task_id = fields.Many2one("project.task", string=_("Associated task"), copy=True)
