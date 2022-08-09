# -*- coding: utf-8 -*-

from odoo import models, fields, _


class HedgedocPad(models.Model):
    _inherit = "hedgedoc.pad"

    lead_id = fields.Many2one("crm.lead", string=_("Associated opportunity"), copy=True)
