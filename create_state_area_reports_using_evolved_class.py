# create_state_area_reports_using_evolved_class.py
# A program to print a report of state/area records from a file in two different orders

from my_evolved_states import State


def main():
    states = get_states()

    states.sort(key=by_state_name)
    print_report(states, 'BY STATE NAME')

    states.sort(key=by_total_area, reverse=True)
    print_report(states, 'BY DESCENDING TOTAL AREA IN SQUARE MILES')


def get_states():
    infile_name = input('Please enter input file name: ')
    infile = open(infile_name, 'r', encoding='utf-8')
    my_states = []
    for line in infile:
        state_name, land_area_as_string, water_area_as_string = line.split(';')
        my_states.append(
            State(state_name, float(land_area_as_string), float(water_area_as_string))
        )
    infile.close()
    return my_states


def print_report(these_states, report_title):
    print()
    print()
    print('{0:^60}'.format(report_title))
    print()
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('State', 'Land Area', 'Water Area', 'Total Area'))
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('', '(SQMI)', '(SQMI)', '(SQMI)'))
    for state in these_states:
        print('{0:<15}{1: >15,.2f}{2: >15,.2f}{3: >15,.2f}'.format(
            state.state_name,
            state.land_area_in_square_miles,
            state.water_area_in_square_miles,
            state.calculate_total_area_in_square_miles()
        ))


def by_state_name(state_instance):
    return state_instance.state_name


def by_total_area(state_instance):
    return state_instance.calculate_total_area_in_square_miles()


main()
