import pytest
from country.models import Currency

pytestmark = pytest.mark.django_db


class TestCurrencyModel:
    def test_create_currency(self):
        obj = Currency.objects.create(
            code="USD", name="United States Dollar", symbol="$"
        )

        assert obj.name == "United States Dollar"
        assert obj.code == "USD"

    def test_str_representation(self, currency):
        expected_str = f"{currency.name} ({currency.code})"
        assert str(currency) == expected_str
