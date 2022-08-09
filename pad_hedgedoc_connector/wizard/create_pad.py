# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateHedgedocPadWizard(models.TransientModel):
    _name = "create.hedgedoc.pad.wizard"
    _description = "Create a Hedgedoc Pad"

    pad_name = fields.Char(string="Title", required=True)
  
    def _compute_pad_values(self):
        values = {
            "name": self.pad_name,
            "url": self.env.user.company_id.hedgedoc_server_url + "/" + self.pad_name
        }
        return values

    def create_hedgedoc_pad(self):
        return True
