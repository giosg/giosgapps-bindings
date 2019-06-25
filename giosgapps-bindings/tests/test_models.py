from django.test import TestCase
from common.models import GiosgAppInstallation


class GiosgAppInstallationTest(TestCase):

    def test_creation(self):
        m = GiosgAppInstallation(
            installed_org_uuid='f50ec0b7-f960-400d-91f0-c42a6d44e3d0',
            persistent_bot_token='8ajjx980937h8fshxnba1700dshjfncm',  # from public documentation
            persistent_token_prefix='Token'
        )
        m.save()
        self.assertTrue(isinstance(m, GiosgAppInstallation))
