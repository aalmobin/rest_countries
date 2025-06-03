import pytest
from country.models import Demonym

pytestmark = pytest.mark.django_db


class TestDemonymModel:
    def test_create_demonym(self):
        obj = Demonym.objects.create(language="eng", female="American", male="American")

        assert obj.id is not None
        assert obj.language == "eng"

    def test_str_representation(self, demonym):
        expected_str = f"{demonym.language}: {demonym.male}/{demonym.female}"
        assert str(demonym) == expected_str
