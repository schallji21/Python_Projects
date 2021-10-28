# create_land_mammal_reports_using_basic_class.py
# A program to print a report of land mammal records from a file in two different orders

from my_evolved_land_mammals import LandMammal


def main():
    land_mammal_animal_name = get_land_mammal_name()

    land_mammal_animal_name.sort(key=by_land_mammal_name)
    print_report(land_mammal_animal_name, 'BY LAND MAMMAL NAME')

    land_mammal_animal_name.sort(key=by_descending_variability_of_mass_in_pounds, reverse=True)
    print_report(land_mammal_animal_name, 'BY DESCENDING VARIABILITY OF MASS IN POUNDS')


def get_land_mammal_name():
    infile_name = input('Please enter input file name: ')
    infile = open(infile_name, 'r', encoding='utf-8')
    land_mammal = []
    for line in infile:
        animal_name, minimum_mass_in_pounds, maximum_mass_in_pounds = line.split(',')
        land_mammal.append(
            LandMammal(animal_name, float(minimum_mass_in_pounds), float(maximum_mass_in_pounds))
        )
    infile.close()
    return land_mammal


def print_report(these_land_mammals, report_title):
    print()
    print()
    print('{0:^60}'.format(report_title))
    print()
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('Land Mammal', 'Minimum Mass', 'Maximum Mass', 'Variability of Mass'))
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('Name', 'in Pounds', 'in Pounds', 'in Pounds'))
    for LandMammal in these_land_mammals:
        print('{0:<15}{1: >15,.0f}{2: >15,.0f}{3: >15,.0f}'.format(
            LandMammal.animal_name,
            LandMammal.minimum_mass_in_pounds,
            LandMammal.maximum_mass_in_pounds,
            LandMammal.calculate_variability_of_mass_in_pounds()
        ))


def by_land_mammal_name(land_mammal_instance):
    return land_mammal_instance.animal_name


def by_descending_variability_of_mass_in_pounds(land_mammal_instance):
    return land_mammal_instance.calculate_variability_of_mass_in_pounds()


main()
