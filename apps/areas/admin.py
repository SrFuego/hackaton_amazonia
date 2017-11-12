# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import ProtectedNaturalArea, Visits, Money


# Register your models here.
admin.site.register(ProtectedNaturalArea)
admin.site.register(Visits)
admin.site.register(Money)
