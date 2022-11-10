from odoo import models, fields, tools
import logging

_logger = logging.getLogger(__name__)


class PartnerRibbon(models.Model):
    _name = "partner.ribbon"
    _description = 'Partner ribbon'

    def name_get(self):
        return [(ribbon.id, '%s (#%d)' % (tools.html2plaintext(ribbon.html), ribbon.id)) for ribbon in self]

    html = fields.Char(string='Ribbon html', required=True, translate=True)
    bg_color = fields.Char(string='Ribbon background color', required=False)
    text_color = fields.Char(string='Ribbon text color', required=False)
    html_class = fields.Char(string='Ribbon class', required=True, default='')