import pytest
from country.services import DemonymService
from rest_framework.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestDemonymService:
    def test_create(self):
        data = {"language": "eng", "female": "American", "male": "American"}
        instance = DemonymService.create(data)
        assert instance.language == data["language"]
        assert instance.female == data["female"]

    def test_update(self, demonym):
        data = {"language": "Updated Name"}
        instance = DemonymService(demonym_instance=demonym).update(data)
        assert instance.language == data["language"]

    def test_update_without_instance(self):
        data = {"language": "Updated Name"}
        instance = DemonymService()
        with pytest.raises(
            ValidationError, match="No Demonym instance set for updating."
        ):
            instance.update(data)

    def test_destroy(self, demonym):
        instance = DemonymService(demonym_instance=demonym)
        res = instance.destroy()
        assert res == True

    def test_destroy_without_instance(self):
        instance = DemonymService()
        with pytest.raises(ValidationError, match="No Demonym instance is provided"):
            instance.destroy()
