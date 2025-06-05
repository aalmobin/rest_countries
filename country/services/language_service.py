from rest_framework.exceptions import ValidationError
from country.models import Language


class LanguageService:

    def __init__(self, language_instance=None):
        self.language_instance = language_instance

    @staticmethod
    def create(data: dict) -> Language:
        language = Language.objects.create(**data)
        return language

    def update(self, data: dict) -> Language:
        if self.language_instance is None:
            raise ValidationError("No Language instance set for updating.")

        for key, value in data.items():
            if hasattr(self.language_instance, key):
                setattr(self.language_instance, key, value)

        self.language_instance.save()
        return self.language_instance

    def destroy(self) -> dict:
        if self.language_instance is None:
            raise ValidationError("No Language instance is provided")

        self.language_instance.delete()
        return True
