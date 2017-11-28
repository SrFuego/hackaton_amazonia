# Python imports


# Django imports
from django.utils import timezone


# Third party apps imports
from rest_framework.response import Response
from rest_framework.views import APIView


# Local imports
from .models import Visits


# Create your views here.
class VisitsChartView(APIView):
    def get(self, request, format=None):
        if len(request.query_params) == 0:
            month_filter = timezone.now().month
        else:
            month_filter = request.query_params['month']
        visits = Visits.objects.filter(date__month=month_filter)
        foreign = sum(visits.values_list('foreign', flat=True))
        national = sum(visits.values_list('national', flat=True))
        exonerated = sum(visits.values_list('exonerated', flat=True))
        total = foreign + national + exonerated
        foreign_percent = round(foreign * 100 / total) if total else 0
        national_percent = round(national * 100 / total) if total else 0
        exonerated_percent = round(exonerated * 100 / total) if total else 0
        return Response({
            'total': total,
            'foreign': foreign,
            'national': national,
            'exonerated': exonerated,
            'foreign_percent': foreign_percent,
            'national_percent': national_percent,
            'exonerated_percent': exonerated_percent})


class PayersChartView(APIView):
    def get(self, request, format=None):
        if request.query_params.__len__() == 0:
            month_filter = timezone.now().month
        else:
            month_filter = request.query_params['month']
        visits = Visits.objects.filter(date__month=month_filter)
        payers = sum(visits.values_list('payers', flat=True))
        non_paying = sum(visits.values_list('non_paying', flat=True))
        total = payers + non_paying
        payers_percent = round(payers * 100 / total) if total else 0
        non_paying_percent = round(non_paying * 100 / total) if total else 0
        return Response({
            'total': total,
            'payers': payers,
            'non_paying': non_paying,
            'payers_percent': payers_percent,
            'non_paying_percent': non_paying_percent})
