# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Money, ProtectedNaturalArea, Visits
from .serializers import (
    MoneySerializer, ProtectedNaturalAreaSerializer, VisitsSerializer)


# Create your viewsets here.
class ProtectedNaturalAreaViewSet(ModelViewSet):
    queryset = ProtectedNaturalArea.objects.all()
    serializer_class = ProtectedNaturalAreaSerializer


class VisitsViewSet(ModelViewSet):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer


class MoneyViewSet(ModelViewSet):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
