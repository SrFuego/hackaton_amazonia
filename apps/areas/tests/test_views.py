# Python imports
import random


# Django imports
from django.urls import reverse


# Third party apps imports
from rest_framework import status
from rest_framework.test import APITestCase


# Local imports


# Create your view tests here.
class VisitsChartTests(APITestCase):
    def setUp(self):
        self.visits_url = reverse("visits-chart")

    def test_get_without_month(self):
        response = self.client.get(self.visits_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_with_month(self):
        data = {"month": random.randrange(1, 13)}
        response = self.client.get(self.visits_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def tearDown(self):


class PayersChartTests(APITestCase):
    def setUp(self):
        self.payers_url = reverse("payers-chart")

    def test_get_without_month(self):
        response = self.client.get(self.payers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_with_month(self):
        data = {"month": random.randrange(1, 13)}
        response = self.client.get(self.payers_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
