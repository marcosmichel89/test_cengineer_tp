from odoo import models, fields, api, _
from odoo.exceptions import UserError
import re
from validators import ValidationFailure
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    url_facebook = fields.Char(string='Facebook')
    url_linkedin = fields.Char(string='LinkedIn')
    url_twitter = fields.Char(string='Twitter')
    complete_profile = fields.Boolean(string='Complete Profile', readonly=True, compute='_compute_profile', store=True)
    website_size_x = fields.Integer('Size X', default=1)
    website_size_y = fields.Integer('Size Y', default=1)
    website_ribbon_id = fields.Many2one('partner.ribbon', string='Ribbon')

    @api.depends('url_facebook', 'url_linkedin', 'url_twitter')
    def _compute_profile(self):
        for partner in self:
            if not partner.url_facebook or not partner.url_twitter or not partner.url_linkedin:
                partner.complete_profile = False
            else:
                partner.complete_profile = True

    @api.model
    def _search_get_detail(self, website, order, options):
        search_details = super(ResPartner, self)._search_get_detail(website, order, options)
        search_details['search_fields'].append('your products')

    @api.onchange('url_facebook', 'url_linkedin', 'url_twitter')
    def validate_url(self):
        regex = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
        r = re.compile(regex)
        if not re.search(r, self.url_facebook) or not re.search(r, self.url_linkedin) or not re.search(r,
                                                                                                       self.url_twitter):
            raise UserError(_("The entered url is not valid"))
