from django.contrib import admin
from country.models import Country, Currency, Language, Demonym


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [
        "name_common",
        "flag_emoji",
        "independent",
        "status",
        "capital",
    ]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["code", "name"]


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "symbol"]


@admin.register(Demonym)
class DemonymAdmin(admin.ModelAdmin):
    list_display = ["language", "female", "male"]
