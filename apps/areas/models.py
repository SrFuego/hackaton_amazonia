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
        Account, related_name='protected_natural_area')
    name = models.CharField(max_length=100, unique=True)


class Visits(TimeStampedModel):
    approved = models.BooleanField(default=False)
    date = models.DateField()
    exonerated = models.PositiveIntegerField()
    foreign = models.PositiveIntegerField()
    national = models.PositiveIntegerField()
    non_paying = models.PositiveIntegerField()
    payers = models.PositiveIntegerField()
    protected_natural_area = models.ForeignKey(
        'ProtectedNaturalArea', related_name='visits')


class Money(TimeStampedModel):
    JANUARY = 'jan'
    FEBRUARY = 'feb'
    MARCH = 'mar'
    APRIL = 'apr'
    MAY = 'may'
    JUNE = 'jun'
    JULY = 'jul'
    AUGUST = 'aug'
    SEPTEMBER = 'sep'
    OCTOBER = 'oct'
    NOVEMBER = 'nov'
    DECEMBER = 'dic'

    MONTH_CHOICES = (
        (JANUARY, 'enero'),
        (FEBRUARY, 'febrero'),
        (MARCH, 'marzo'),
        (APRIL, 'abril'),
        (MAY, 'mayo'),
        (JUNE, 'junio'),
        (JULY, 'julio'),
        (AUGUST, 'agosto'),
        (SEPTEMBER, 'septiembre'),
        (OCTOBER, 'octubre'),
        (NOVEMBER, 'noviembre'),
        (DECEMBER, 'diciembre'),
    )

    account = models.ForeignKey(
        Account, limit_choices_to={'level': Account.ADMIN},
        related_name='account')
    month = models.CharField(max_length=3, choices=MONTH_CHOICES)
    mount = models.DecimalField(decimal_places=2, max_digits=10)
