from django.urls import path, include
from rest_framework.routers import DefaultRouter

from country.viewsets import (
    CountryViewSet,
    CurrencyViewSet,
    DemonymViewSet,
    LanguageViewSet,
)


router = DefaultRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"currencies", CurrencyViewSet, basename="currency")
router.register(r"demonyms", DemonymViewSet, basename="demonym")
router.register(r"languages", LanguageViewSet, basename="language")


urlpatterns = [
    path("api/", include(router.urls)),
]
