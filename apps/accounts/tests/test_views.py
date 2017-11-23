# Python imports


# Django imports
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


# Third party apps imports
from model_mommy import mommy


# Local imports
from ..models import Account


# Create your view tests here.
class TokenAuthTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.token_url = reverse("custom-token-view")
        self.user = User.objects.create_user("user_test", password="1234qwer")
        self.user_alone = User.objects.create_user(
            "user_alone", password="1234qwer")
        self.account = mommy.make(Account, user=self.user)

    def test_invalid_user(self):
        data = {
            "username": "root",
            "password": "rootroot"}
        response = self.client.post(self.token_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_user(self):
        data = {
            "username": "user_test",
            "password": "1234qwer"}
        response = self.client.post(self.token_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_user_without_person(self):
        data = {
            "username": "user_alone",
            "password": "1234qwer"}
        response = self.client.post(self.token_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        self.account.delete()
