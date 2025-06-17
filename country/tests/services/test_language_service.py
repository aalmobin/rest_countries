import pytest
from country.services import LanguageService
from rest_framework.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestLanguageService:
    def test_create(self):
        data = {"code": "en", "name": "English"}
        instance = LanguageService.create(data)
        assert instance.code == data["code"]
        assert instance.name == data["name"]

    def test_update(self, language):
        data = {"name": "Updated Name"}
        instance = LanguageService(language_instance=language).update(data)
        assert instance.name == data["name"]

    def test_update_without_instance(self):
        data = {"name": "Updated Name"}
        instance = LanguageService()
        with pytest.raises(
            ValidationError, match="No Language instance set for updating."
        ):
            instance.update(data)

    def test_destroy(self, language):
        instance = LanguageService(language_instance=language)
        res = instance.destroy()
        assert res == True

    def test_destroy_without_instance(self):
        instance = LanguageService()
        with pytest.raises(ValidationError, match="No Language instance is provided"):
            instance.destroy()
