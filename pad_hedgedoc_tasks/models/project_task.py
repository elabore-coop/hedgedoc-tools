# -*- coding: utf-8 -*-

from odoo import models, fields


class Task(models.Model):
    _inherit = "project.task"

    task_hedgedoc_pads = fields.One2many("task.hedgedoc.pad", "task_id")

    def create_hedgedoc_pad(self):
        return {
            "name": "Create a Hedgedoc pad",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "create.hedgedoc.pad.wizard",
            "target": "new",
            "context": {'default_task_id': self.id},
        }