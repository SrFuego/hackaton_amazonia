# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import AccountViewSet


# Create your routers here.
accounts = (
    (r"accounts", AccountViewSet),
)
