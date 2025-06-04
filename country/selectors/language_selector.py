from django.shortcuts import get_object_or_404

from country.helpers import BaseSelector
from country.models import Language


class LanguageSelector(BaseSelector):
    @staticmethod
    def retrieve(pk: int) -> Language:
        return get_object_or_404(Language, pk=pk)

    @staticmethod
    def list(search_params: dict) -> list:
        return LanguageSelector.dynamic_filter(
            Language.objects.filter(deleted=False), search_params
        )
