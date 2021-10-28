# Please DO NOT DISTRIBUTE exercise solutions
#
# my_countries.py
# a module containing the Country class and related code

PASSED = 'Passed'
FAILED = 'Failed'


class Country:

    def __init__(self, country_name, population, area_in_square_miles):
        self.country_name = str(country_name)
        self.population = int(population)
        self.area_in_square_miles = int(area_in_square_miles)

    @property
    def country_name(self):
        return self.__country_name

    @country_name.setter
    def country_name(self, country_name):
        if country_name == '':
            raise AttributeError('The country_name attribute must be populated with a non-empty string value.')
        self.__country_name = country_name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        if population <= 0:
            raise AttributeError('The population attribute must be populated with an integer value > 0.')
        self.__population = population

    @property
    def area_in_square_miles(self):
        return self.__area_in_square_miles

    @area_in_square_miles.setter
    def area_in_square_miles(self, area_in_square_miles):
        if area_in_square_miles <= 0:
            raise AttributeError('The area_in_square_miles attribute must be populated with an integer value > 0.')
        self.__area_in_square_miles = area_in_square_miles

    def __str__(self):
        strings_list = []
        strings_list.append("Country('")
        strings_list.append(self.country_name)
        strings_list.append("', ")
        strings_list.append(str(self.population))
        strings_list.append(", ")
        strings_list.append(str(self.area_in_square_miles))
        strings_list.append(")")
        return "".join(strings_list)

    def __repr__(self):
        return self.__str__()

    def calculate_population_density_per_square_mile(self):
        return round(float(self.population) / float(self.area_in_square_miles))


def main():
    print('Unit testing output follows...')

    print('\nTest Case #1: Test constructor')
    expected_country_name = 'Australia'
    expected_population = 25273752
    expected_area_in_square_miles = 2969907
    c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    result = PASSED
    if c1.country_name != expected_country_name:
        result = FAILED
    if c1.population != expected_population:
        result = FAILED
    if c1.area_in_square_miles != expected_area_in_square_miles:
        result = FAILED
    print(result)

    print('\nTest Case #2: Test str method')
    expected_country_name = 'Australia'
    expected_population = 25273752
    expected_area_in_square_miles = 2969907
    expected_str_value = "Country('Australia', 25273752, 2969907)"
    c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    actual_str_value = str(c1)
    if actual_str_value == expected_str_value:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #3: Test repr method')
    expected_country_name = 'Australia'
    expected_population = 25273752
    expected_area_in_square_miles = 2969907
    c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    if repr(c1) == str(c1):
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #4: Test calculate_population_density_per_square_mile method')
    expected_country_name = 'Australia'
    expected_population = 25273752
    expected_area_in_square_miles = 2969907
    expected_population_density_per_square_mile = 9
    c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    if c1.calculate_population_density_per_square_mile() == expected_population_density_per_square_mile:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #5: Test passing empty string to country_name setter')
    expected_country_name = ''
    expected_population = 25273752
    expected_area_in_square_miles = 2969907
    test_result = FAILED
    try:
        c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    except AttributeError as ae:
        if str(ae) == 'The country_name attribute must be populated with a non-empty string value.':
            test_result = PASSED
    finally:
        print(test_result)

    print('\nTest Case #6: Test passing zero to population setter')
    expected_country_name = 'Australia'
    expected_population = 0
    expected_area_in_square_miles = 2969907
    expected_population_density_per_square_mile = 9
    test_result = FAILED
    try:
        c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    except AttributeError as ae:
        if str(ae) == 'The population attribute must be populated with an integer value > 0.':
            test_result = PASSED
    finally:
        print(test_result)

    print('\nTest Case #7: Test passing zero to area_in_square_miles setter')
    expected_country_name = 'Australia'
    expected_population = 25273752
    expected_area_in_square_miles = 0
    expected_population_density_per_square_mile = 9
    test_result = FAILED
    try:
        c1 = Country(expected_country_name, expected_population, expected_area_in_square_miles)
    except AttributeError as ae:
        if str(ae) == 'The area_in_square_miles attribute must be populated with an integer value > 0.':
            test_result = PASSED
    finally:
        print(test_result)


if __name__ == '__main__':
    main()
