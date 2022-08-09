# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HedgedocPad(models.Model):
    _name = "hedgedoc.pad"
    _description = "Hedgedoc Pad"

    name = fields.Char(string=_("Title"), required=True,)
    url = fields.Char(string=_("URL"))