import requests
from prettytable import PrettyTable

def get_top_25_populated_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = response.json()

    # Sort countries by population in descending order
    sorted_countries = sorted(countries, key=lambda x: x.get('population', 0), reverse=True)

    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Country", "Population (in millions)"]

    # Add top 25 populated countries to the table
    for country in sorted_countries[:25]:
        country_name = country.get('name', {}).get('common', 'N/A')
        population = country.get('population', 'N/A')
        if population != 'N/A':
            population = round(population / 1_000_000, 2)  # Convert population to millions and round to 2 decimal places
        table.add_row([country_name, population])

    print(table)

if __name__ == "__main__":
    get_top_25_populated_countries()
