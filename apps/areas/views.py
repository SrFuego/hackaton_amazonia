# Python imports


# Django imports
from django.utils import timezone

# Third party apps imports
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


# Local imports
from .models import Visits


# Create your views here.
class ChartView(APIView):
    authentication_classes = (
        authentication.TokenAuthentication, authentication.BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        if request.query_params.__len__() == 0:
            visits = Visits.objects.filter(date__month=timezone.now().month)
            foreign = sum(visits.values_list('foreign', flat=True))
            national = sum(visits.values_list('national', flat=True))
            exonerated = sum(visits.values_list('exonerated', flat=True))
            total = foreign + national + exonerated
        return Response({
            'total': total,
            'foreign': foreign,
            'national': national,
            'exonerated': exonerated,
            'foreign_percent': round(foreign * 100 / total),
            'national_percent': round(national * 100 / total),
            'exonerated_percent': round(exonerated * 100 / total),
        })
