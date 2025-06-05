from rest_framework.exceptions import ValidationError
from country.models import Currency


class CurrencyService:

    def __init__(self, currency_instance=None):
        self.currency_instance = currency_instance

    @staticmethod
    def create(data: dict) -> Currency:
        currency = Currency.objects.create(**data)
        return currency

    def update(self, data: dict) -> Currency:
        if self.currency_instance is None:
            raise ValidationError("No Currency instance set for updating.")

        for key, value in data.items():
            if hasattr(self.currency_instance, key):
                setattr(self.currency_instance, key, value)

        self.currency_instance.save()
        return self.currency_instance

    def destroy(self) -> dict:
        if self.currency_instance is None:
            raise ValidationError("No Currency instance is provided")

        self.currency_instance.delete()
        return True
