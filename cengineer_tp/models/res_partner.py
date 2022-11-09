from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    url_facebook = fields.Char(string='Facebook')
    url_linkedin = fields.Char(string='LinkedIn')
    url_twitter = fields.Char(string='Twitter')
    complete_profile = fields.Boolean(string='Complete Profile', readonly=True, compute='_compute_profile')

    def _compute_profile(self):
        for partner in self:
            if not partner.url_facebook or not partner.url_twitter or not partner.url_linkedin:
                partner.complete_profile = False
            else:
                partner.complete_profile = True
