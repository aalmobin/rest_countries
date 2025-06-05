import pytest
from country.services import CurrencyService
from rest_framework.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestCurrencyService:
    def test_create(self):
        data = {"code": "USD", "name": "United States Dollar", "symbol": "$"}
        instance = CurrencyService.create(data)
        assert instance.code == data["code"]
        assert instance.name == data["name"]
        assert instance.symbol == data["symbol"]

    def test_update(self, currency):
        data = {"name": "Updated Name", "symbol": "updated symbol"}
        instance = CurrencyService(currency_instance=currency).update(data)

        assert instance.name == data["name"]
        assert instance.symbol == data["symbol"]

    def test_destroy(self, currency):
        instance = CurrencyService(currency_instance=currency)
        res = instance.destroy()
        assert res == True

    def test_destroy_without_instance(self):
        instance = CurrencyService()
        with pytest.raises(ValidationError, match="No Currency instance is provided"):
            instance.destroy()
