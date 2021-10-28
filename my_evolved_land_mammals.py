# my_evolved_land_mammals.py
# a module containing the LandMammal class and related code

PASSED = 'Passed'
FAILED = 'Failed'


class LandMammal:

    def __init__(self, animal_name, minimum_mass_in_pounds, maximum_mass_in_pounds):
        self.animal_name = str(animal_name)
        self.minimum_mass_in_pounds = float(minimum_mass_in_pounds)
        self.maximum_mass_in_pounds = float(maximum_mass_in_pounds)

    @property
    def animal_name(self):
        return self.__animal_name

    @animal_name.setter
    def animal_name(self, animal_name):
        if animal_name == '':
            raise AttributeError('The state_name attribute must be populated with a non-empty string value.')
        self.__animal_name = animal_name

    @property
    def minimum_mass_in_pounds(self):
        return self.__minimum_mass_in_pounds

    @minimum_mass_in_pounds.setter
    def minimum_mass_in_pounds(self, minimum_mass_in_pounds):
        if minimum_mass_in_pounds <= 0.00:
            raise AttributeError('The minimum_mass_in_pounds attribute must be populated with an integer value < 1')
        self.__minimum_mass_in_pounds = minimum_mass_in_pounds

    @property
    def maximum_mass_in_pounds(self):
        return self.__maximum_mass_in_pounds

    @maximum_mass_in_pounds.setter
    def maximum_mass_in_pounds(self, maximum_mass_in_pounds):
        if maximum_mass_in_pounds <= 0.00:
            raise AttributeError('The maximum_mass_in_pounds attribute must be populated with an integer value < 1')
        self.__maximum_mass_in_pounds = maximum_mass_in_pounds

    def __str__(self):
        strings_list = []
        strings_list.append("Name('")
        strings_list.append(self.animal_name)
        strings_list.append("', ")
        '{:.0f}'.format(self.minimum_mass_in_pounds)
        strings_list.append('{:.0f}'.format(self.minimum_mass_in_pounds))
        strings_list.append(", ")
        strings_list.append('{:.0f}'.format(self.maximum_mass_in_pounds))
        strings_list.append(")")
        return ''.join(strings_list)

    def __repr__(self):
        return self.__str__()

    def calculate_variability_of_mass_in_pounds(self):
        return self.maximum_mass_in_pounds - self.minimum_mass_in_pounds


def main():
    print('Unit testing output follows...')

    print('\nTest Case #1: Test constructor')
    expected_animal_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    result = PASSED
    if s1.animal_name != expected_animal_name:
        result = FAILED
    if s1.minimum_mass_in_pounds != expected_minimum_mass_in_pounds:
        result = FAILED
    if s1.maximum_mass_in_pounds != expected_maximum_mass_in_pounds:
        print(s1.maximum_mass_in_pounds)
        result = FAILED
    print(result)

    print('\nTest Case #2: Test str method')
    expected_animal_name = 'Alaska'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    expected_str_value = "Name('African elephant', 10000, 24000)"
    s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    actual_str_value = str(s1)
    if actual_str_value == expected_str_value:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #3: Test repr method')
    expected_animal_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    expected_repr_value = "Name('African elephant', 10000, 24000)"
    s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    actual_repr_value = repr(s1)
    if actual_repr_value == expected_repr_value:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #4: Test variability_of_mass_in_pounds method')
    expected_animal_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    expected_variability_of_mass_in_pounds = 14000
    s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    result = PASSED
    delta = s1.calculate_variability_of_mass_in_pounds() - expected_variability_of_mass_in_pounds
    if abs(delta) > 0.0001:
        print(s1.calculate_variability_of_mass_in_pounds(), delta)
        result = FAILED
    print(result)

    print('\nTest Case #5: Test passing empty string to animal_name setter')
    expected_animal_name = ''
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    test_result = FAILED
    try:
        s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    except AttributeError as ae:
        if str(ae) == 'The animal_name attribute must be populated with a non-empty string value.':
            test_result = PASSED
    finally:
        print(test_result)

    print('\nTest Case #6: Test passing zero to minimum_mass_in_pounds setter')
    expected_animal_name = 'African elephant'
    expected_minimum_mass_in_pounds = 1
    expected_maximum_mass_in_pounds = 24000
    test_result = FAILED
    try:
        s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    except AttributeError as ae:
        if str(ae) == 'The land_area_in_square_miles attribute must be populated with an integer value > 0.00':
            test_result = PASSED
    finally:
        print(test_result)

    print('\nTest Case #7: Test passing zero to maximum_mass_in_pounds setter')
    expected_animal_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 1
    test_result = FAILED
    try:
        s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    except AttributeError as ae:
        if str(ae) == 'The maximum_mass_in_pounds attribute must be populated with an integer value < 1':
            test_result = PASSED
    finally:
        print(test_result)

    print('\nTest Case #8: Test passing lesser maximum value than minimum value to mass in pounds setters')
    expected_animal_name = 'African elephant'
    expected_minimum_mass_in_pounds = 99000
    expected_maximum_mass_in_pounds = 24000
    test_result = FAILED
    try:
        s1 = LandMammal(expected_animal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    except AttributeError as ae:
        if str(ae) == 'The maximum_mass_in_pounds attribute must be populated with an integer value < 1':
            test_result = PASSED
    finally:
        print(test_result)


if __name__ == '__main__':
    main()
