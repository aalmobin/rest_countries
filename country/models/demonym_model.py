from django.db import models


class Demonym(models.Model):
    language = models.CharField(max_length=3)  # e.g., 'eng', 'fra'
    female = models.CharField(max_length=50)
    male = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.language}: {self.male}/{self.female}"
