from rest_framework.exceptions import ValidationError
from country.models import Demonym


class DemonymService:

    def __init__(self, demonym_instance=None):
        self.demonym_instance = demonym_instance

    @staticmethod
    def create(data: dict) -> Demonym:
        demonym = Demonym.objects.create(**data)
        return demonym

    def update(self, data: dict) -> Demonym:
        if self.demonym_instance is None:
            raise ValidationError("No Demonym instance set for updating.")

        for key, value in data.items():
            if hasattr(self.demonym_instance, key):
                setattr(self.demonym_instance, key, value)

        self.demonym_instance.save()
        return self.demonym_instance

    def destroy(self) -> dict:
        if self.demonym_instance is None:
            raise ValidationError("No Demonym instance is provided")

        self.demonym_instance.delete()
        return True
