
# geography_toolkit

geography_toolkit is a python package that provides comprehensive geographical information about countries and continents. It allows you to obtain details such as the capital, population, area, official languages, currencies, timezones, flag, subregion, and neighboring countries of a given country. All data is stored locally, enabling offline use.

## Installation

To install the geography_toolkit package, make sure you have python 3.x installed. You can install the package directly from Pypi

### pip install geography_toolkit


## Usage

### Available Functions

#### Continent Functions

- **`get_continents()`**

  Returns the list of available continents.

  from geography_toolkit import get_continents
  
  continents = get_continents()

  print(continents)


  **Example Output:**


  ['Africa', 'Europe']


- **`get_countries(continent)`**

  Returns the list of countries in a given continent.


  from geography_toolkit import get_countries
  
  countries = get_countries('Africa')

  print(countries)


  **Example Output:**


  ['Nigeria', 'Egypt']


#### Country Information Functions

- **`get_capital(country_name)`**

  Returns the capital of a given country.


  from geography_toolkit import get_capital
  
  capital = get_capital('Nigeria')

  print(capital)


  **Example Output:**


  'Abuja'


- **`get_population(country_name)`**

  Returns the population of a given country.


  from geography_toolkit import get_population
  
  population = get_population('Egypt')

  print(population)


  **Example Output:**


  102334404


- **`get_area(country_name)`**

  Returns the area of a given country in km².


  from geography_toolkit import get_area
  
  area = get_area('Germany')

  print(area)


  **Example Output:**


  357114


- **`get_languages(country_name)`**

  Returns the list of official languages of a given country.


  from geography_toolkit import get_languages
  
  languages = get_languages('France')

  print(languages)


  **Example Output:**


  ['French']


- **`get_currencies(country_name)`**

  Returns the list of currencies of a given country.


  from geography_toolkit import get_currencies
  
  currencies = get_currencies('France')

  print(currencies)


  **Example Output:**


  ['EUR']


- **`get_timezones(country_name)`**

  Returns the list of timezones of a given country.


  from geography_toolkit import get_timezones
  
  timezones = get_timezones('Egypt')

  print(timezones)


  **Example Output:**


  ['UTC+02:00']


- **`get_flag(country_name)`**

  Returns the URL of the flag of a given country.


  from geography_toolkit import get_flag
  
  flag_url = get_flag('Germany')

  print(flag_url)


  **Example Output:**


  'https://flagcdn.com/w320/de.png'


- **`get_subregion(country_name)`**

  Returns the subregion of a given country.


  from geography_toolkit import get_subregion
  
  subregion = get_subregion('Nigeria')

  print(subregion)


  **Example Output:**


  'Western Africa'


- **`get_borders(country_name)`**

  Returns the list of neighboring countries of a given country.


  from geography_toolkit import get_borders
  
  borders = get_borders('Nigeria')

  print(borders)


  **Example Output:**


  ['NER', 'BEN', 'CMR', 'TCD']


- **`get_all_info(country_name)`**

  Returns all available information about a given country.


  from geography_toolkit import get_all_info
  
  all_info = get_all_info('Egypt')

  print(all_info)


  **Example Output:**


  {
      'country': 'Egypt',
      'capital': 'Cairo',
      'population': 102334404,
      'area_km2': 1002450,
      'languages': ['Arabic'],
      'currencies': ['EGP'],
      'timezones': ['UTC+02:00'],
      'flag': 'https://flagcdn.com/w320/eg.png',
      'subregion': 'Northern Africa',
      'borders': ['ISR', 'PSE', 'LBY', 'SDN']
  }


