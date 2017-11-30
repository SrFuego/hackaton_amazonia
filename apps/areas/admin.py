# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Money, ProtectedNaturalArea, Visits


# Register your models here.
admin.site.register(Money)
admin.site.register(ProtectedNaturalArea)
admin.site.register(Visits)
