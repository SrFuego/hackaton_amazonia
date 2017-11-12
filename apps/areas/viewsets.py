# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet

# Local imports
from .models import Money, Visits
from .serializers import MoneySerializer, VisitsSerializer


# Create your viewsets here.
class VisitsViewSet(ModelViewSet):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer


class MoneyViewSet(ModelViewSet):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
