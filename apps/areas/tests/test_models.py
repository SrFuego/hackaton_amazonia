# Python imports


# Django imports
from django.test import TestCase


# Third party apps imports
from model_mommy import mommy


# Local imports
from ..models import Money, ProtectedNaturalArea, Visits


# Create your model tests here.
class MoneyTestCase(TestCase):
    def setUp(self):
        self.money = mommy.make(Money)

    def test_method_str_return_month(self):
        self.assertEqual(self.money.__str__(), self.money.mount)

    def tearDown(self):
        self.money.delete()


class ProtectedNaturalAreaTestCase(TestCase):
    def setUp(self):
        self.protected_natural_area = mommy.make(ProtectedNaturalArea)

    def test_method_str_return_name(self):
        self.assertEqual(
            self.protected_natural_area.__str__(),
            self.protected_natural_area.name)

    def tearDown(self):
        self.protected_natural_area.delete()


class VisitsTestCase(TestCase):
    def setUp(self):
        self.visits = mommy.make(Visits)

    def test_method_str_return_name(self):
        self.assertEqual(
            self.visits.__str__(), self.visits.protected_natural_area.name)

    def tearDown(self):
        self.visits.delete()
