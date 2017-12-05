# Python imports


# Django imports
# from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils import timezone

# Third party apps imports
from drf_pdf.renderer import PDFRenderer
from pdfkit import from_string
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import Money, ProtectedNaturalArea, Visits


# Create your views here.
class VisitsChartView(APIView):
    def get(self, request, format=None):
        visits = Visits.objects.filter(date__year=timezone.now().year)
        if len(request.query_params) == 0:
            month_filter = timezone.now().month
        else:
            month_filter = request.query_params["month"]
        visits = visits.filter(date__month=month_filter)
        foreign = sum(visits.values_list("foreign", flat=True))
        national = sum(visits.values_list("national", flat=True))
        exonerated = sum(visits.values_list("exonerated", flat=True))
        total = foreign + national + exonerated
        foreign_percent = round(foreign * 100 / total) if total else 0
        national_percent = round(national * 100 / total) if total else 0
        exonerated_percent = round(exonerated * 100 / total) if total else 0
        return Response({
            "total": total,
            "foreign": foreign,
            "national": national,
            "exonerated": exonerated,
            "foreign_percent": foreign_percent,
            "national_percent": national_percent,
            "exonerated_percent": exonerated_percent})


# class PayersChartView(APIView):
#     def get(self, request, format=None):
#         visits = Visits.objects.filter(date__year=timezone.now().year)
#         if len(request.query_params) == 0:
#             month_filter = timezone.now().month
#         else:
#             month_filter = request.query_params["month"]
#         visits = visits.filter(date__month=month_filter)
#         payers = sum(visits.values_list("payers", flat=True))
#         non_paying = sum(visits.values_list("non_paying", flat=True))
#         total = payers + non_paying
#         payers_percent = round(payers * 100 / total) if total else 0
#         non_paying_percent = round(non_paying * 100 / total) if total else 0
#         return Response({
#             "total": total,
#             "payers": payers,
#             "non_paying": non_paying,
#             "payers_percent": payers_percent,
#             "non_paying_percent": non_paying_percent})


class VisitsCompareLastYearView(APIView):
    def get(self, request, format=None):
        aux = {}
        aux_list = []
        this_year = timezone.now().year
        last_year = this_year - 1
        for anp in ProtectedNaturalArea.objects.all():
            visits = Visits.objects.filter(
                date__year=this_year, protected_natural_area=anp)
            visits_last_year = Visits.objects.filter(
                date__year=last_year, protected_natural_area=anp)
            if len(request.query_params) == 0:
                month_filter = timezone.now().month
            else:
                month_filter = request.query_params["month"]
            visits = visits.filter(date__month=month_filter)
            visits_last_year = visits_last_year.filter(
                date__month=month_filter)
            aux["anp"] = anp.name
            aux["this_year_exonerated"] = sum(
                visits.values_list("exonerated", flat=True))
            aux["this_year_foreign"] = sum(
                visits.values_list("foreign", flat=True))
            aux["this_year_national"] = sum(
                visits.values_list("national", flat=True))
            aux["last_year_exonerated"] = sum(
                visits_last_year.values_list("exonerated", flat=True))
            aux["last_year_foreign"] = sum(
                visits_last_year.values_list("foreign", flat=True))
            aux["last_year_national"] = sum(
                visits_last_year.values_list("national", flat=True))

            aux_percent = aux["this_year_exonerated"] * 100
            if aux["last_year_exonerated"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_exonerated"]
            if aux["last_year_exonerated"]:
                aux["exonerated_percent"] = aux_percent - 100
            else:
                aux["exonerated_percent"] = 0
            if aux["exonerated_percent"] < 0:
                aux["exonerated_negative"] = True
            else:
                aux["exonerated_negative"] = False

            aux_percent = aux["this_year_foreign"] * 100
            if aux["last_year_foreign"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_foreign"]
            if aux["last_year_foreign"]:
                aux["foreign_percent"] = aux_percent - 100
            else:
                aux["foreign_percent"] = 0
            if aux["foreign_percent"] < 0:
                aux["foreign_negative"] = True
            else:
                aux["foreign_negative"] = False

            aux_percent = aux["this_year_national"] * 100
            if aux["last_year_national"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_national"]
            if aux["last_year_national"]:
                aux["national_percent"] = aux_percent - 100
            else:
                aux["national_percent"] = 0
            if aux["national_percent"] < 0:
                aux["national_negative"] = True
            else:
                aux["national_negative"] = False

            aux_list.append(aux)
            aux = {}
        return Response({"list_anp": aux_list})


class VisitsPeriodCompareLastYearView(APIView):
    def get(self, request, format=None):
        aux = {}
        aux_list = []
        this_year = timezone.now().year
        last_year = this_year - 1
        for anp in ProtectedNaturalArea.objects.all():
            visits = Visits.objects.filter(
                date__year=this_year, protected_natural_area=anp)
            visits_last_year = Visits.objects.filter(
                date__year=last_year, protected_natural_area=anp)
            if len(request.query_params) == 0:
                month_filter = timezone.now().month
            else:
                month_filter = request.query_params["month"]
            visits = visits.filter(date__month__lte=month_filter)
            visits_last_year = visits_last_year.filter(
                date__month__lte=month_filter)
            aux["anp"] = anp.name
            aux["this_year_exonerated"] = sum(
                visits.values_list("exonerated", flat=True))
            aux["this_year_foreign"] = sum(
                visits.values_list("foreign", flat=True))
            aux["this_year_national"] = sum(
                visits.values_list("national", flat=True))
            aux["last_year_exonerated"] = sum(
                visits_last_year.values_list("exonerated", flat=True))
            aux["last_year_foreign"] = sum(
                visits_last_year.values_list("foreign", flat=True))
            aux["last_year_national"] = sum(
                visits_last_year.values_list("national", flat=True))

            aux_percent = aux["this_year_exonerated"] * 100
            if aux["last_year_exonerated"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_exonerated"]
            if aux["last_year_exonerated"]:
                aux["exonerated_percent"] = aux_percent - 100
            else:
                aux["exonerated_percent"] = 0
            if aux["exonerated_percent"] < 0:
                aux["exonerated_negative"] = True
            else:
                aux["exonerated_negative"] = False

            aux_percent = aux["this_year_foreign"] * 100
            if aux["last_year_foreign"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_foreign"]
            if aux["last_year_foreign"]:
                aux["foreign_percent"] = aux_percent - 100
            else:
                aux["foreign_percent"] = 0
            if aux["foreign_percent"] < 0:
                aux["foreign_negative"] = True
            else:
                aux["foreign_negative"] = False

            aux_percent = aux["this_year_national"] * 100
            if aux["last_year_national"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_national"]
            if aux["last_year_national"]:
                aux["national_percent"] = aux_percent - 100
            else:
                aux["national_percent"] = 0
            if aux["national_percent"] < 0:
                aux["national_negative"] = True
            else:
                aux["national_negative"] = False

            aux_list.append(aux)
            aux = {}
        return Response({"list_anp": aux_list})


class ReportPDF(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (PDFRenderer,)

    def get(self, request, *args, **kwargs):
        aux = {}
        aux_list_per_month = []
        this_year = timezone.now().year
        last_year = this_year - 1
        if len(request.query_params) == 0:
            month_filter = timezone.now().month
        else:
            month_filter = request.query_params["month"]

        for anp in ProtectedNaturalArea.objects.all():
            visits = Visits.objects.filter(
                approved=True, date__year=this_year,
                protected_natural_area=anp)
            visits_last_year = Visits.objects.filter(
                approved=True, date__year=last_year,
                protected_natural_area=anp)
            visits = visits.filter(date__month=month_filter)
            visits_last_year = visits_last_year.filter(
                date__month=month_filter)

            aux["name"] = anp.name
            aux["this_year_exonerated"] = sum(
                visits.values_list("exonerated", flat=True))
            aux["this_year_foreign"] = sum(
                visits.values_list("foreign", flat=True))
            aux["this_year_national"] = sum(
                visits.values_list("national", flat=True))
            aux["last_year_exonerated"] = sum(
                visits_last_year.values_list("exonerated", flat=True))
            aux["last_year_foreign"] = sum(
                visits_last_year.values_list("foreign", flat=True))
            aux["last_year_national"] = sum(
                visits_last_year.values_list("national", flat=True))

            aux_percent = aux["this_year_exonerated"] * 100
            if aux["last_year_exonerated"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_exonerated"]

            if aux["last_year_exonerated"]:
                aux["exonerated_percent"] = round(aux_percent - 100, 1)
            else:
                aux["exonerated_percent"] = 0
            if aux["exonerated_percent"] < 0:
                aux["exonerated_negative"] = True
            else:
                aux["exonerated_negative"] = False

            aux_percent = aux["this_year_foreign"] * 100
            if aux["last_year_foreign"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_foreign"]
            if aux["last_year_foreign"]:
                aux["foreign_percent"] = round(aux_percent - 100, 1)
            else:
                aux["foreign_percent"] = 0
            if aux["foreign_percent"] < 0:
                aux["foreign_negative"] = True
            else:
                aux["foreign_negative"] = False

            aux_percent = aux["this_year_national"] * 100
            if aux["last_year_national"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_national"]
            if aux["last_year_national"]:
                aux["national_percent"] = round(aux_percent - 100, 1)
            else:
                aux["national_percent"] = 0
            if aux["national_percent"] < 0:
                aux["national_negative"] = True
            else:
                aux["national_negative"] = False

            aux_list_per_month.append(aux)
            aux = {}

        aux = {}
        aux_list_per_period = []
        for anp in ProtectedNaturalArea.objects.all():
            visits = Visits.objects.filter(
                date__year=this_year, protected_natural_area=anp)
            visits_last_year = Visits.objects.filter(
                date__year=last_year, protected_natural_area=anp)
            visits = visits.filter(date__month__lte=month_filter)
            visits_last_year = visits_last_year.filter(
                date__month__lte=month_filter)
            aux["name"] = anp.name
            aux["this_year_exonerated"] = sum(
                visits.values_list("exonerated", flat=True))
            aux["this_year_foreign"] = sum(
                visits.values_list("foreign", flat=True))
            aux["this_year_national"] = sum(
                visits.values_list("national", flat=True))
            aux["last_year_exonerated"] = sum(
                visits_last_year.values_list("exonerated", flat=True))
            aux["last_year_foreign"] = sum(
                visits_last_year.values_list("foreign", flat=True))
            aux["last_year_national"] = sum(
                visits_last_year.values_list("national", flat=True))

            aux_percent = aux["this_year_exonerated"] * 100
            if aux["last_year_exonerated"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_exonerated"]
            if aux["last_year_exonerated"]:
                aux["exonerated_percent"] = round(aux_percent - 100, 1)
            else:
                aux["exonerated_percent"] = 0
            if aux["exonerated_percent"] < 0:
                aux["exonerated_negative"] = True
            else:
                aux["exonerated_negative"] = False

            aux_percent = aux["this_year_foreign"] * 100
            if aux["last_year_foreign"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_foreign"]
            if aux["last_year_foreign"]:
                aux["foreign_percent"] = round(aux_percent - 100, 1)
            else:
                aux["foreign_percent"] = 0
            if aux["foreign_percent"] < 0:
                aux["foreign_negative"] = True
            else:
                aux["foreign_negative"] = False

            aux_percent = aux["this_year_national"] * 100
            if aux["last_year_national"] == 0:
                aux_percent = 0
            else:
                aux_percent /= aux["last_year_national"]
            if aux["last_year_national"]:
                aux["national_percent"] = round(aux_percent - 100, 1)
            else:
                aux["national_percent"] = 0
            if aux["national_percent"] < 0:
                aux["national_negative"] = True
            else:
                aux["national_negative"] = False

            aux_list_per_period.append(aux)
            aux = {}

        template = loader.get_template("areas/reporte_pdf.html")
        html = template.render({
            "anp_per_month": aux_list_per_month,
            "anp_per_period": aux_list_per_period,
            "month": Money.MONTH_CHOICES[
                int(month_filter) - 1][1].upper()[:3]})
        pdf_options = {
            "quiet": "",
            "page-size": "A4",
            "margin-top": "0.5in",
            "margin-right": "0.75in",
            "margin-bottom": "0.75in",
            "margin-left": "0.75in",
            "encoding": "UTF-8",
            "custom-header": [
                ("Accept-Encoding", "gzip")
            ],
            "no-outline": None
        }
        pdf = from_string(html, False, options=pdf_options)
        headers = {
            "Content-Disposition": "filename='foo.pdf'",
            "Content-Length": len(pdf)}
        return Response(pdf, headers=headers, status=status.HTTP_200_OK)
