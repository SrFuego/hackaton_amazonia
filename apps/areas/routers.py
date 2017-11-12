# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import MoneyViewSet, ProtectedNaturalAreaViewSet, VisitsViewSet


# Create your routers here.
areas = (
    (r"money", MoneyViewSet),
    (r"protected_natural_area", ProtectedNaturalAreaViewSet),
    (r"visits", VisitsViewSet),
)
