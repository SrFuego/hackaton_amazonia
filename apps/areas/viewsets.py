# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet

# Local imports
from .models import Visits
from .serializers import VisitsSerializer


# Create your viewsets here.
class VisitsViewSet(ModelViewSet):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
