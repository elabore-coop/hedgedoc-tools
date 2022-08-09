# -*- coding: utf-8 -*-

from odoo import models, fields


class Task(models.Model):
    _inherit = "project.task"

    hedgedoc_pads = fields.One2many("hedgedoc.pad", "task_id")

    def create_hedgedoc_pad(self):
        return {
            "name": "Create a Hedgedoc pad",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "create.hedgedoc.pad.wizard",
            "target": "new",
        }