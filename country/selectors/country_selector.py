from django.shortcuts import get_object_or_404

from country.helpers import BaseSelector
from country.models import Country


class CountrySelector(BaseSelector):
    @staticmethod
    def retrieve(pk: int) -> Country:
        return get_object_or_404(Country, pk=pk)

    @staticmethod
    def list(search_params: dict) -> list:
        return CountrySelector.dynamic_filter(
            Country.objects.filter(deleted=False), search_params
        )
