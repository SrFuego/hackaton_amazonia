# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
# from .models import Money, ProtectedNaturalArea, Visits
from .models import ProtectedNaturalArea, Visits
from .serializers import ProtectedNaturalAreaSerializer, VisitsSerializer
#    MoneySerializer, ProtectedNaturalAreaSerializer, VisitsSerializer)


# Create your viewsets here.
class ProtectedNaturalAreaViewSet(ModelViewSet):
    queryset = ProtectedNaturalArea.objects.all()
    serializer_class = ProtectedNaturalAreaSerializer
    http_method_names = ["get"]


class VisitsViewSet(ModelViewSet):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
    filter_fields = ("approved",)
    http_method_names = ["get", "post", "put"]


# class MoneyViewSet(ModelViewSet):
#     queryset = Money.objects.all()
#     serializer_class = MoneySerializer
