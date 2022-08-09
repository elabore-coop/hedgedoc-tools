# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateHedgedocPadWizard(models.TransientModel):
    _inherit = "create.hedgedoc.pad.wizard"

    lead_id = fields.Many2one('crm.lead', string='Lead')
  
    def _compute_pad_values(self):
        values = super(CreateHedgedocPadWizard, self)._compute_pad_values()
        values["lead_id"] = self.lead_id.id
        return values

    def create_hedgedoc_pad(self):
        values = self._compute_pad_values()
        self.env["lead.hedgedoc.pad"].create(values)
        return super(CreateHedgedocPadWizard, self).create_hedgedoc_pad()
