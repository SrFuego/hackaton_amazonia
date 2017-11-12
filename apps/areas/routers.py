# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import MoneyViewSet, VisitsViewSet


# Create your routers here.
router_list = (
    (r'money', MoneyViewSet),
    (r'visits', VisitsViewSet),
)
