from odoo.tests import TransactionCase
from odoo.exceptions import UserError
import re
import logging

_logger = logging.getLogger(__name__)


class TestResPartner(TransactionCase):

    def setUp(self):
        super(TestResPartner, self).setUp()

    def test_create_partner(self):
        partner = {
            'name': 'TestPartner',
            'url_facebook': 'https://myfacebook.com/myprofile',
            'url_twitter': 'https://mytwitter.com/myprofile',
            'url_linkedin': 'https://mylinkedin.com/myprofile'
        }

        self.env['res.partner'].create(partner)
        self.assertTrue(partner)

    def test_create_partner_fault(self):
        partner = {
            'name': 'TestPartner',
            'url_facebook': 'ftp://myfacebook.com/myprofile',
            'url_twitter': 'https://mytwitter.com/myprofile',
            'url_linkedin': 'https://mylinkedin.com/myprofile'
        }

        self.env['res.partner'].create(partner)
        self.assertTrue(partner)

    def test_compute_profile(self):
        partner = {
            'name': 'TestPartner',
            'url_facebook': 'https://myfacebook.com/myprofile',
            'url_twitter': 'https://mytwitter.com/myprofile',
            'url_linkedin': 'https://mylinkedin.com/myprofile'
        }

        pnew = self.env['res.partner'].create(partner)
        self.assertTrue(pnew)
        self.assertTrue(self.validate_url(pnew.url_facebook))
        self.assertTrue(self.validate_url(pnew.url_twitter))
        self.assertTrue(self.validate_url(pnew.url_linkedin))

    def validate_url(self, url):
        regex = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
        r = re.compile(regex)
        if not re.search(r, url):
            return False
        return True

    def test_complete_profile(self):
        partner = {
            'name': 'TestPartner',
            'url_facebook': 'https://myfacebook.com/myprofile',
            'url_twitter': 'https://mytwitter.com/myprofile',
            'url_linkedin': 'https://mylinkedin.com/myprofile'
        }

        pnew = self.env['res.partner'].create(partner)
        self.assertTrue(partner)

        if pnew.url_facebook and pnew.url_twitter and pnew.url_linkedin:
            self.assertTrue(pnew.write({'complete_profile': True}))
