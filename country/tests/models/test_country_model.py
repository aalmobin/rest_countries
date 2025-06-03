import pytest
from country.models import Country

pytestmark = pytest.mark.django_db


class TestCountryModel:
    def test_create_country(self, currency, language, demonym):
        obj = Country.objects.create(
            cca2="US",
            cca3="USA",
            ccn3="840",
            cioc="USA",
            name_common="United States",
            name_official="United States of America",
            native_name_common="United States",
            native_name_official="United States of America",
            tld=[".us"],
            independent=True,
            status="officially-assigned",
            un_member=True,
            idd_root="+1",
            idd_suffixes=[""],
            capital="Washington D.C.",
            alt_spellings=["US", "USA", "United States of America"],
            region="Americas",
            subregion="Northern America",
            latlng=[38.0, -97.0],
            landlocked=False,
            borders=["CAN", "MEX"],
            area=9833520,
            population=331000000,
            gini={"2018": 41.4},
            fifa="USA",
            car_signs=["USA"],
            car_side="right",
            timezones=["UTC−04:00 to UTC−12:00", "UTC+10:00", "UTC+12:00"],
            continents=["North America"],
            flag_emoji="🇺🇸",
            flag_png="https://flagcdn.com/us.png",
            flag_svg="https://flagcdn.com/us.svg",
            flag_alt="Flag of the United States",
            coat_of_arms_png="https://example.com/coa.png",
            coat_of_arms_svg="https://example.com/coa.svg",
            start_of_week="monday",
            capital_latlng=[38.8977, -77.0365],
            postal_code_format="#####",
            postal_code_regex=r"^\d{5}(-\d{4})?$",
            google_maps_url="https://goo.gl/maps/usa",
            openstreet_maps_url="https://www.openstreetmap.org/relation/148838",
        )

        obj.currencies.add(currency)
        obj.languages.add(language)
        obj.demonyms.add(demonym)

        assert obj.id is not None
        assert obj.name_common == "United States"

    def test_str_representation(self, country):
        expected_str = country.name_common
        assert str(country) == expected_str
