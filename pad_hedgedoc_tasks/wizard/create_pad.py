# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateHedgedocPadWizard(models.TransientModel):
    _inherit = "create.hedgedoc.pad.wizard"

    task_id = fields.Many2one('project.task', string='Task')
  
    def _compute_pad_values(self):
        values = super(CreateHedgedocPadWizard, self)._compute_pad_values()
        values["task_id"] = self.task_id.id
        return values

    def create_hedgedoc_pad(self):
        values = self._compute_pad_values()
        self.env["task.hedgedoc.pad"].create(values)
        return super(CreateHedgedocPadWizard, self).create_hedgedoc_pad()
