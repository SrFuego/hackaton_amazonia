# Python imports


# Django imports
from django.conf import settings
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Account(TimeStampedModel):
    BOSS = "boss"
    ADMIN = "admin"
    OPERATOR = "operator"

    LEVEL_CHOICE = (
        (BOSS, "jefe"),
        (ADMIN, "administrador"),
        (OPERATOR, "operador"),)

    level = models.CharField(
        max_length=8, choices=LEVEL_CHOICE, verbose_name="Nivel")
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="account",
        verbose_name="Usuario")

    def __str__(self):
        return self.user.get_full_name()
