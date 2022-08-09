# -*- coding: utf-8 -*-

from odoo import models, fields


class Lead(models.Model):
    _inherit = "crm.lead"

    hedgedoc_pads = fields.One2many("hedgedoc.pad", "lead_id")

    def create_hedgedoc_pad(self):
        return {
            "name": "Create a Hedgedoc pad",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "create.hedgedoc.pad.wizard",
            "target": "new",
        }