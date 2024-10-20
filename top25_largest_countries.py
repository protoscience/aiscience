import requests
from prettytable import PrettyTable

def get_top_25_largest_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = response.json()

    # Sort countries by area in descending order
    sorted_countries = sorted(countries, key=lambda x: x.get('area', 0), reverse=True)

    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Country", "Area (in sq. km)"]

    # Add top 25 largest countries to the table
    for country in sorted_countries[:25]:
        country_name = country.get('name', {}).get('common', 'N/A')
        area = country.get('area', 'N/A')
        table.add_row([country_name, area])

    print(table)

if __name__ == "__main__":
    get_top_25_largest_countries()
