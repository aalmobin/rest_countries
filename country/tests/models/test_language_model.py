import pytest
from country.models import Language

pytestmark = pytest.mark.django_db


class TestLanguageModel:
    def test_create_language(self):
        obj = Language.objects.create(code="en", name="English")
        assert obj.code == "en"
        assert obj.name == "English"

    def test_str_representation(self, language):
        expected_str = language.name
        assert str(language) == expected_str
