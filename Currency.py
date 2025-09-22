import pycountry

def get_currency_by_country(country_name):
    country = pycountry.countries.get(name=country_name)
    if country:
        currency = pycountry.currencies.get(numeric=country.numeric)
        return currency.alpha_3 if currency else "Currency not found"
    return "Country not found"