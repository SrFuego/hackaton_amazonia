# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import VisitsViewSet


# Create your routers here.
router_list = (
    (r'visits', VisitsViewSet),
)
