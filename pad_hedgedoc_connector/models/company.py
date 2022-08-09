# -*- coding: utf-8 -*-

from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    hedgedoc_server_url = fields.Char(string="Hedgedoc Server URL")
