# Please DO NOT DISTRIBUTE exercise solutions
#
# my_basic_states.py
# a module containing a basic version of the State class and related code

PASSED = 'Passed'
FAILED = 'Failed'


class State:

    def __init__(self, state_name, land_area_in_square_miles, water_area_in_square_miles):
        self.state_name = str(state_name)
        self.land_area_in_square_miles = float(land_area_in_square_miles)
        self.water_area_in_square_miles = float(water_area_in_square_miles)

    def __str__(self):
        strings_list = []
        strings_list.append("State('")
        strings_list.append(self.state_name)
        strings_list.append("', ")
        '{0:0.2f}'.format(self.land_area_in_square_miles)
        strings_list.append('{0:0.2f}'.format(self.land_area_in_square_miles))
        strings_list.append(", ")
        strings_list.append('{0:0.2f}'.format(self.water_area_in_square_miles))
        strings_list.append(")")
        return ''.join(strings_list)

    def __repr__(self):
        return self.__str__()

    def calculate_total_area_in_square_miles(self):
        return self.land_area_in_square_miles + self.water_area_in_square_miles


def main():
    print('Unit testing output follows...')

    print('\nTest Case #1: Test constructor')
    expected_state_name = 'Alaska'
    expected_land_area_in_square_miles = 570640.95
    expected_water_area_in_square_miles = 94743.10
    s1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    result = PASSED
    if s1.state_name != expected_state_name:
        result = FAILED
    if s1.land_area_in_square_miles != expected_land_area_in_square_miles:
        result = FAILED
    if s1.water_area_in_square_miles != expected_water_area_in_square_miles:
        print(s1.water_area_in_square_miles)
        result = FAILED
    print(result)

    print('\nTest Case #2: Test str method')
    expected_state_name = 'Alaska'
    expected_land_area_in_square_miles = 570640.95
    expected_water_area_in_square_miles = 94743.10
    s1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    expected_str_value = "State('Alaska', 570640.95, 94743.10)"
    s1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    actual_str_value = str(s1)
    if actual_str_value == expected_str_value:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #3: Test repr method')
    expected_state_name = 'Alaska'
    expected_land_area_in_square_miles = 570640.95
    expected_water_area_in_square_miles = 94743.10
    s1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    expected_repr_value = "State('Alaska', 570640.95, 94743.10)"
    s1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    actual_repr_value = repr(s1)
    if actual_repr_value == expected_repr_value:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #4: Test calculate_total_area_in_square_miles method')
    expected_state_name = 'Alaska'
    expected_land_area_in_square_miles = 570640.95
    expected_water_area_in_square_miles = 94743.10
    expected_total_area_in_square_miles = 665384.05
    s1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    result = PASSED
    delta = s1.calculate_total_area_in_square_miles() - expected_total_area_in_square_miles
    if abs(delta) > 0.0001:
        print(s1.calculate_total_area_in_square_miles(), delta)
        result = FAILED
    print(result)


if __name__ == '__main__':
    main()
