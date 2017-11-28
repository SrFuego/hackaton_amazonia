"""hackaton_amazonia_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


from rest_framework.documentation import include_docs_urls


from apps.common.routers import router


from apps.accounts.views import ObtainAuthToken
from apps.areas.views import VisitsChartView, PayersChartView, VisitsAnualView


API_TITLE = "API app para la hackaton de la amazonia"
API_DESCRIPTION = "nombre de la app aun por definir :D"


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^api/v1/", include(router.urls, namespace="api")),
    url(
        r"^api-auth/",
        include("rest_framework.urls", namespace="rest_framework")),
    url(
        r"^api/v1/api-token-auth/", ObtainAuthToken.as_view(),
        name="custom-token-view"),
    url(r"^api/v1/visits-anual/", VisitsAnualView.as_view()),
    url(
        r"^api/v1/chart/visits/", VisitsChartView.as_view(),
        name="visits-chart"),
    url(
        r"^api/v1/chart/payers/", PayersChartView.as_view(),
        name="payers-chart"),
    url(
        r"^docs/",
        include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
