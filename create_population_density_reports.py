# create_population_density_reports.py
# A program that reads and prints data files.

from my_countries import Country


def main():
    country = get_countries()

    country.sort(key=by_country_name)
    print_report(country, 'BY COUNTRY NAME')

    country.sort(key=by_population, reverse=True)
    print_report(country, 'BY DESCENDING POPULATION DENSITY PER SQUARE MILES')


def get_countries():
    infile_name = input('Please enter input file name: ')
    infile = open(infile_name, 'r', encoding='utf-8')
    my_countries = []
    for line in infile:
        country_name, population_as_string, area_in_square_miles_as_string = line.split(';')
        my_countries.append(
            Country(country_name, float(population_as_string), float(area_in_square_miles_as_string))
        )
    infile.close()
    return my_countries


def print_report(these_countries, report_title):
    print()
    print()
    print('{0:^60}'.format(report_title))
    print()
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('Country', 'Population', 'Area', 'Density'))
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('', '', '(SQMI)', '(/SQMI)'))
    for country in these_countries:
        print('{0:<15}{1: >15,.2f}{2: >15,.2f}{3: >15,.2f}'.format(
            country.country_name,
            country.population,
            country.area_in_square_miles,
            country.calculate_population_density_per_square_mile()
        ))


def by_country_name(country_instance):
    return country_instance.country_name


def by_population(country_instance):
    return country_instance.population


def by_calculate_population_density_per_square_mile(country_instance):
    return country_instance.calculate_population_density_per_sqaure_mile()


main()
