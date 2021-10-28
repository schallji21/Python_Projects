# distribute_race_awards.py
# A program that prompts the user to input an integer and the corresponding award description is returned.


def main():
    participant_place = int(input('Please enter the place in which the participant finished (1, 2, 3, ...): '))

    participant_award = lookup_participant_award(participant_place)

    print('Participant Place:', participant_place)
    print('Participant Place', participant_award)


def lookup_participant_award(participant_place):
    if participant_place == 1:
        participant_award = 'Blue Ribbon'
    elif participant_place == 2:
        participant_award = 'Red Ribbon'
    elif participant_place == 3:
        participant_award = 'White Ribbon'
    elif participant_place == 4:
        participant_award = 'Gold Ribbon'
    elif participant_place == 5:
        participant_award = 'Green Ribbon'
    elif participant_place == 6:
        participant_award = 'Purple Ribbon'
    elif participant_place == 6:
        participant_award = 'Participant Ribbon'
    else:
        participant_award = 'Input Error - Number must be greater than 0.'
    return participant_award


main()
