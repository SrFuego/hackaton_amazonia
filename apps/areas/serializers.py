# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer

# Local imports
from ..accounts.serializers import AccountSerializer
from .models import Money, ProtectedNaturalArea, Visits


# Create your serializers here.
class ProtectedNaturalAreaSerializer(ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = ProtectedNaturalArea
        fields = ('account', 'id', 'name')


class VisitsSerializer(ModelSerializer):
    class Meta:
        model = Visits
        fields = (
            'approved', 'date', 'exonerated', 'foreign', 'id', 'national',
            'non_paying', 'payers', 'protected_natural_area',)


class MoneySerializer(ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Money
        fields = ('account', 'id', 'mount', 'month',)
