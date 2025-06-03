import requests
from django.core.management.base import BaseCommand
from country.models import Country, Currency, Language, Demonym


class Command(BaseCommand):
    help = "Fetch country data from restcountries.com and store in database"

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code != 200:
            self.stderr.write("Failed to fetch data")
            return

        data = response.json()
        print(len(data))

        for item in data:
            try:
                # Create or get currencies
                currency_objs = []
                for code, cur in item.get("currencies", {}).items():
                    obj, _ = Currency.objects.get_or_create(
                        code=code,
                        defaults={
                            "name": cur.get("name", ""),
                            "symbol": cur.get("symbol", ""),
                        },
                    )
                    currency_objs.append(obj)

                # Create or get languages
                language_objs = []
                for code, name in item.get("languages", {}).items():
                    obj, _ = Language.objects.get_or_create(
                        code=code, defaults={"name": name}
                    )
                    language_objs.append(obj)

                # Create or get demonyms
                demonym_objs = []
                for lang, values in item.get("demonyms", {}).items():
                    obj, _ = Demonym.objects.get_or_create(
                        language=lang,
                        defaults={
                            "female": values.get("f", ""),
                            "male": values.get("m", ""),
                        },
                    )
                    demonym_objs.append(obj)

                # Create country
                country, _ = Country.objects.update_or_create(
                    cca2=item.get("cca2"),
                    defaults={
                        "cca3": item.get("cca3", ""),
                        "ccn3": item.get("ccn3", ""),
                        "cioc": item.get("cioc", ""),
                        "name_common": item["name"]["common"],
                        "name_official": item["name"]["official"],
                        "native_name_common": (
                            list(item["name"]["nativeName"].values())[0]["common"]
                            if item["name"].get("nativeName")
                            else ""
                        ),
                        "native_name_official": (
                            list(item["name"]["nativeName"].values())[0]["official"]
                            if item["name"].get("nativeName")
                            else ""
                        ),
                        "tld": item.get("tld", []),
                        "independent": item.get("independent", False),
                        "status": item.get("status", ""),
                        "un_member": item.get("unMember", False),
                        "idd_root": item.get("idd", {}).get("root", ""),
                        "idd_suffixes": item.get("idd", {}).get("suffixes", []),
                        "capital": item.get("capital", []),
                        "alt_spellings": item.get("altSpellings", []),
                        "region": item.get("region", ""),
                        "subregion": item.get("subregion", ""),
                        "latlng": item.get("latlng", []),
                        "landlocked": item.get("landlocked", False),
                        "borders": item.get("borders", []),
                        "area": item.get("area", 0),
                        "population": item.get("population", 0),
                        "gini": item.get("gini", {}),
                        "fifa": item.get("fifa", ""),
                        "car_signs": item.get("car", {}).get("signs", []),
                        "car_side": item.get("car", {}).get("side", ""),
                        "timezones": item.get("timezones", []),
                        "continents": item.get("continents", []),
                        "flag_emoji": item.get("flag", ""),
                        "flag_png": item.get("flags", {}).get("png", ""),
                        "flag_svg": item.get("flags", {}).get("svg", ""),
                        "flag_alt": item.get("flags", {}).get("alt", ""),
                        "coat_of_arms_png": item.get("coatOfArms", {}).get("png", ""),
                        "coat_of_arms_svg": item.get("coatOfArms", {}).get("svg", ""),
                        "start_of_week": item.get("startOfWeek", ""),
                        "capital_latlng": item.get("capitalInfo", {}).get("latlng", []),
                        "postal_code_format": item.get("postalCode", {}).get(
                            "format", ""
                        ),
                        "postal_code_regex": item.get("postalCode", {}).get(
                            "regex", ""
                        ),
                        "google_maps_url": item.get("maps", {}).get("googleMaps", ""),
                        "openstreet_maps_url": item.get("maps", {}).get(
                            "openStreetMaps", ""
                        ),
                    },
                )

                country.currencies.set(currency_objs)
                country.languages.set(language_objs)
                country.demonyms.set(demonym_objs)

                self.stdout.write(self.style.SUCCESS(f"Saved: {country.name_common}"))

            except Exception as e:
                self.stderr.write(
                    f"Error processing country: {item.get('name', {}).get('common', 'Unknown')}"
                )
                self.stderr.write(str(e))
