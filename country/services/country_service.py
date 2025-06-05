from rest_framework.exceptions import ValidationError
from country.models import Country


class CountryService:

    def __init__(self, country_instance=None):
        self.country_instance = country_instance

    @staticmethod
    def create(data: dict) -> Country:
        country = Country.objects.create(**data)
        return country

    def update(self, data: dict) -> Country:
        if self.country_instance is None:
            raise ValidationError("No Country instance set for updating.")

        for key, value in data.items():
            if hasattr(self.country_instance, key):
                setattr(self.country_instance, key, value)

        self.country_instance.save()
        return self.country_instance

    def destroy(self) -> dict:
        if self.country_instance is None:
            raise ValidationError("No Country instance is provided")

        self.country_instance.delete()
        return True
