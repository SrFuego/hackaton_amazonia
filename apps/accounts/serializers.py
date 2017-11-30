# Python imports


# Django imports
from django.contrib.auth import get_user_model


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Account


# Create your serializers here.
class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name", "email",)


class AccountSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ("id", "level", "user",)
