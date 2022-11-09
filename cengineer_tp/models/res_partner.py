from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    url_facebook = fields.Char(string='Facebook')
    url_linkedin = fields.Char(string='LinkedIn')
    url_twitter = fields.Char(string='Twitter')

