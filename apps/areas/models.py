# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports
from ..accounts.models import Account


# Create your models here.
class ProtectedNaturalArea(TimeStampedModel):
    account = models.OneToOneField(
        Account, related_name="protected_natural_area")
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Visits(TimeStampedModel):
    approved = models.BooleanField(default=False)
    date = models.DateField()
    exonerated = models.PositiveIntegerField()
    foreign = models.PositiveIntegerField()
    national = models.PositiveIntegerField()
    protected_natural_area = models.ForeignKey(
        "ProtectedNaturalArea", related_name="visits")

    def __str__(self):
        return self.protected_natural_area.name


class Money(TimeStampedModel):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    MONTH_CHOICES = (
        (JANUARY, "enero"),
        (FEBRUARY, "febrero"),
        (MARCH, "marzo"),
        (APRIL, "abril"),
        (MAY, "mayo"),
        (JUNE, "junio"),
        (JULY, "julio"),
        (AUGUST, "agosto"),
        (SEPTEMBER, "septiembre"),
        (OCTOBER, "octubre"),
        (NOVEMBER, "noviembre"),
        (DECEMBER, "diciembre"),
    )

    account = models.ForeignKey(
        Account, limit_choices_to={"level": Account.ADMIN},
        related_name="account")
    month = models.CharField(max_length=3, choices=MONTH_CHOICES)
    mount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.mount
