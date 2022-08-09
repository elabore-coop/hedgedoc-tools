# -*- coding: utf-8 -*-

from odoo import models, fields


class Lead(models.Model):
    _inherit = "crm.lead"

    leads_hedgedoc_pads = fields.One2many("lead.hedgedoc.pad", "lead_id")

    def create_hedgedoc_pad(self):
        return {
            "name": "Create a Hedgedoc pad",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "create.hedgedoc.pad.wizard",
            "target": "new",
            "context": {'default_lead_id': self.id},
        }