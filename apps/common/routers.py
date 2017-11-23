# Python imports


# Django imports


# Third party apps imports
from rest_framework.routers import DefaultRouter

# Local imports
from ..accounts.routers import accounts
from ..areas.routers import areas

# Create your routers here.
routers_tuples = (accounts, areas,)
routers_lists = sum([list(router_list) for router_list in routers_tuples], [])

router = DefaultRouter()

for router_list in sorted(routers_lists):
    router.register(router_list[0], router_list[1])
