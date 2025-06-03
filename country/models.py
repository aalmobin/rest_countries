from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Language(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Demonym(models.Model):
    language = models.CharField(max_length=3)  # e.g., 'eng', 'fra'
    female = models.CharField(max_length=50)
    male = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.language}: {self.male}/{self.female}"


class Country(models.Model):
    cca2 = models.CharField(max_length=10, null=True, blank=True)
    cca3 = models.CharField(max_length=10, null=True, blank=True)
    ccn3 = models.CharField(max_length=10, null=True, blank=True)
    cioc = models.CharField(max_length=10, null=True, blank=True)
    name_common = models.CharField(max_length=100)
    name_official = models.CharField(max_length=100)
    native_name_common = models.CharField(max_length=100)
    native_name_official = models.CharField(max_length=100)

    tld = models.JSONField(default=list)
    independent = models.BooleanField()
    status = models.CharField(max_length=50)
    un_member = models.BooleanField()
    currencies = models.ManyToManyField(Currency)
    idd_root = models.CharField(max_length=5)
    idd_suffixes = models.JSONField(default=list)
    capital = models.CharField(max_length=255, null=True, blank=True)
    alt_spellings = models.JSONField(default=list)
    region = models.CharField(max_length=255, null=True, blank=True)
    subregion = models.CharField(max_length=255, null=True, blank=True)
    languages = models.ManyToManyField(Language)
    latlng = models.JSONField(default=list)
    landlocked = models.BooleanField()
    borders = models.JSONField(default=list)
    area = models.FloatField(null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    gini = models.JSONField(null=True, blank=True)
    fifa = models.CharField(max_length=3, null=True, blank=True)
    car_signs = models.JSONField(default=list)
    car_side = models.CharField(max_length=10)
    timezones = models.JSONField(default=list)
    continents = models.JSONField(default=list)
    flag_emoji = models.CharField(max_length=10)
    flag_png = models.URLField()
    flag_svg = models.URLField()
    flag_alt = models.TextField()
    coat_of_arms_png = models.URLField()
    coat_of_arms_svg = models.URLField()
    start_of_week = models.CharField(max_length=10)
    capital_latlng = models.JSONField(default=list)
    postal_code_format = models.CharField(max_length=255, null=True, blank=True)
    postal_code_regex = models.CharField(max_length=255, null=True, blank=True)
    demonyms = models.ManyToManyField(Demonym)

    google_maps_url = models.URLField()
    openstreet_maps_url = models.URLField()

    def __str__(self):
        return self.name_common
