# my_population_groups.py
# A program that defines the PopulationGroup Class.
PASSED = 'Passed'
FAILED = 'Failed'


class PopulationGroup:

    def __init__(self, category, male_count, female_count):
        self.category = str(category)
        self.male_count = int(male_count)
        self.female_count = int(female_count)

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        if category == '':
            raise AttributeError('The Age Group must be populated with a non-empty string value.')
        self.__category = category

    @property
    def male_count(self):
        return self.__male_count

    @male_count.setter
    def male_count(self, male_count):
        if male_count < 0:
            raise AttributeError('The total amount of males cannot be less than zero.')
        self.__male_count = male_count

    @property
    def female_count(self):
        return self.__female_count

    @female_count.setter
    def female_count(self, female_count):
        if female_count < 0:
            raise AttributeError('The total amount of females cannot be less than zero.')
        self.__female_count = female_count

    def __str__(self):
        strings_list = []
        strings_list.append("Category('")
        strings_list.append(self.category)
        strings_list.append("', ")
        strings_list.append(str(self.male_count))
        strings_list.append("' ")
        strings_list.append(str(self.male_count))
        strings_list.append("' ")
        return "".join(strings_list)

    def __repr__(self):
        return self.__str__()

    def calculate_total_count(self):
        return self.male_count + self.female_count


def main():
    print('Unit testing output follows...')

    print('\nTest Case #1: Test constructor')
    expected_category = '0-14'
    expected_male_count = 97680
    expected_female_count = 93991
    c1 = PopulationGroup(expected_category, expected_male_count, expected_female_count)
    result = PASSED
    if c1.category != expected_category:
        result = FAILED
    if c1.male_count != expected_male_count:
        result = FAILED
    if c1.female_count != expected_female_count:
        result = FAILED
    print(result)

    print('\nTest Case #2: Attempt to set category attribute to empty string')
    expected_category = ''
    expected_male_count = 97680
    expected_female_count = 93991
    test_result = PASSED
    try:
        c1 = PopulationGroup(expected_category, expected_male_count, expected_female_count)
    except AttributeError as ae:
        if str(ae) == 'The category attribute must be populated with a non-empty string value.':
            test_result = FAILED
    finally:
        print(test_result)

    print('\nTest Case #3: Attempt to set male_count attribute to negative value')
    expected_category = '0-14'
    expected_male_count = -10
    expected_female_count = 93991
    test_result = PASSED
    try:
        c1 = PopulationGroup(expected_category, expected_male_count, expected_female_count)
    except AttributeError as ae:
        if str(ae) == 'The male_count attribute must be populated with an integer value > 0.':
            test_result = FAILED
    finally:
        print(test_result)

    print('\nTest Case #4: Attempt to set female_count attribute to negative value')
    expected_category = '0-14'
    expected_male_count = 97680
    expected_female_count = -10
    test_result = PASSED
    try:
        c1 = PopulationGroup(expected_category, expected_male_count, expected_female_count)
    except AttributeError as ae:
        if str(ae) == 'The female_count attribute must be populated with an integer value > 0.':
            test_result = FAILED
    finally:
        print(test_result)

    print('\nTest Case #5: Test calculate_total_count() method')
    expected_category = '0-14'
    expected_male_count = 97680
    expected_female_count = 93992
    expected_total_count = 191671
    c1 = PopulationGroup(expected_category, expected_male_count, expected_female_count)
    if c1.calculate_total_count() == expected_total_count:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #6: Test str method')
    expected_category = '0-14'
    expected_male_count = 97680
    expected_female_count = 93991
    expected_str_value = '0-14', 97680, 93991
    c1 = expected_category, expected_male_count, expected_female_count
    actual_str_value = c1
    if actual_str_value == expected_str_value:
        print(PASSED)
    else:
        print(FAILED)

    print('\nTest Case #7: Test repr method')
    expected_category = '0-14'
    expected_male_count = 97680
    expected_female_count = 93991
    c1 = PopulationGroup(expected_category, expected_male_count, expected_female_count)
    if repr(c1) == str(c1):
        print(PASSED)
    else:
        print(FAILED)


if __name__ == '__main__':
    main()

