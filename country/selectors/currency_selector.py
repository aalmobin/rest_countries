from django.shortcuts import get_object_or_404

from country.helpers import BaseSelector
from country.models import Currency


class CurrencySelector(BaseSelector):
    @staticmethod
    def retrieve(pk: int) -> Currency:
        return get_object_or_404(Currency, pk=pk)

    @staticmethod
    def list(search_params: dict) -> list:
        return CurrencySelector.dynamic_filter(
            Currency.objects.filter(deleted=False), search_params
        )
