# -*- coding: utf-8 -*-

from odoo import models, fields, _


class LeadHedgedocPad(models.Model):
    _name = "lead.hedgedoc.pad"
    _inherit = "hedgedoc.pad"

    lead_id = fields.Many2one("crm.lead", string=_("Associated opportunity"), copy=True)
