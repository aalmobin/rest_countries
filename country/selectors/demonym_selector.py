from django.shortcuts import get_object_or_404

from country.helpers import BaseSelector
from country.models import Demonym


class DemonymSelector(BaseSelector):
    @staticmethod
    def retrieve(pk: int) -> Demonym:
        return get_object_or_404(Demonym, pk=pk)

    @staticmethod
    def list(search_params: dict) -> list:
        return DemonymSelector.dynamic_filter(
            Demonym.objects.filter(deleted=False), search_params
        )
