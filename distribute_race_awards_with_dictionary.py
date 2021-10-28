# distribute_race_awards_with_dictionary.py
# A simple lookup program using a python dictionary


def main():
    award_names = {
        1: 'Blue Ribbon',
        2: 'Red Ribbon',
        3: 'White Ribbon',
        4: 'Gold Ribbon',
        5: 'Green Ribbon',
        6: 'Purple Ribbon',
        7: 'Participant Ribbon'
    }

    award_code = int(input('Please enter the place in which the participant finished (1, 2, 3, ...): '))

    award_names = award_names.get(award_code, 'Input Error - Place must be greater than 0')
    print('Participant Place: ', award_code)
    print('Participant Award: ', award_names)


main()
