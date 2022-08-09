# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    hedgedoc_server_url = fields.Char(
        related="company_id.hedgedoc_server_url",
        string="Hedgedoc Server URL",
        readonly=False,
    )
    