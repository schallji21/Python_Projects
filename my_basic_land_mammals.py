# my_basic_land_mammals.py
# A program that defines a class and contains unit testing for said class.


PASSED = 'Passed'
FAILED = 'Failed'


class LandMammals:

    def __init__(self, name, minimum_mass_in_pounds, maximum_mass_in_pounds):
        self.name = str(name)
        self.minimum_mass_in_pounds = float(minimum_mass_in_pounds)
        self.maximum_mass_in_pounds = float(maximum_mass_in_pounds)

    def __str__(self):
        strings_list = []
        strings_list.append("Name('")
        strings_list.append(self.name)
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
    expected_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    s1 = LandMammals(expected_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    result = PASSED
    if s1.name != expected_name:
        result = FAILED
    if s1.minimum_mass_in_pounds != expected_minimum_mass_in_pounds:
        result = FAILED
    if s1.maximum_mass_in_pounds != expected_maximum_mass_in_pounds:
        print(s1.maximum_mass_in_pounds)
        result = FAILED
    print(result)

    print('\nTest Case #2: Test str method')
    expected_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    s1 = LandMammals(expected_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    expected_str_value = "Name('African elephant', 10000, 24000)"
    s1 = LandMammals(expected_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    actual_str_value = str(s1)
    if actual_str_value == expected_str_value:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #3: Test repr method')
    expected_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    s1 = LandMammals(expected_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    expected_repr_value = "Name('African elephant', 10000, 24000)"
    s1 = LandMammals(expected_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    actual_repr_value = repr(s1)
    if actual_repr_value == expected_repr_value:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #4: Test calculate_variability_of_mass_in_pounds')
    expected_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000
    expected_variability_of_mass_in_pounds = 14000
    s1 = LandMammals(expected_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    result = PASSED
    delta = s1.calculate_variability_of_mass_in_pounds() - expected_variability_of_mass_in_pounds
    if abs(delta) > 0.0001:
        print(s1.calculate_variability_of_mass_in_pounds(), delta)
        result = FAILED
    print(result)


if __name__ == '__main__':
    main()
