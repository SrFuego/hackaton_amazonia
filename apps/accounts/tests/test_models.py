# Python imports


# Django imports
from django.test import TestCase


# Third party apps imports
from model_mommy import mommy


# Local imports
from ..models import Account


# Create your model tests here.
class AccountTestCase(TestCase):
    def setUp(self):
        self.account = mommy.make(Account)

    def test_method_str_return_user_full_name(self):
        self.assertEqual(
            self.account.__str__(),
            self.account.user.get_full_name())

    def tearDown(self):
        self.account.delete()
