# -*- coding: utf-8 -*-

from odoo import models


class CreateHedgedocPadWizard(models.TransientModel):
    _inherit = "create.hedgedoc.pad.wizard"
  
    def _compute_pad_values(self):
        values = super(CreateHedgedocPadWizard, self)._compute_pad_values()
        values["task_id"] = self.env["project.task"].browse(self._context.get("active_ids")).id
        return values
