# create_data_analysis_reports.py
# A program to analyze the supplied data file and produce analysis reports.

from my_population_groups import PopulationGroup


def main():
    population_group = build_population_group_list()

    population_group.sort(key=by_category)
    print_report(population_group, "Counts by Age Group")

    population_group.sort(key=by_category)
    print_report(population_group, "Percentages by Age Group")

    population_group.sort(key=by_total_count, reverse=True)
    print_report(population_group, "Counts by Descending Total Count")

    population_group.sort(key=by_total_count, reverse=True)
    print_report(population_group, "Percentages by Descending Total Count")

    population_group.sort(key=by_female_count, reverse=True)
    print_report(population_group, "Counts by Descending Female Count")

    population_group.sort(key=by_female_count, reverse=True)
    print_report(population_group, "Percentages by Descending Female Count")

    population_group.sort(key=by_male_count, reverse=True)
    print_report(population_group, "Counts by Descending Male Count")

    population_group.sort(key=by_male_count, reverse=True)
    print_report(population_group, "Percentages by Descending Male Count")


def print_report(these_population_groups, report_title):
    print()
    print()
    print('{0:^60}'.format(report_title))
    print()
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('Age Group', 'Males', 'Females', 'Total'))
    for population_group in these_population_groups:
        print('{0:<15}{1: >15,.2f}{2: >15,.2f}{3: >15,.2f}'.format(
            population_group.category,
            population_group.male_count,
            population_group.female_count,
            population_group.total_count
        ))


def build_population_group_list():
    infile_name = input('Please enter input file name: ')
    infile = open(infile_name, 'r', encoding='utf-8')
    my_population_groups = []
    for line in infile:
        category, male_count, female_count, total_count = line.split()
        category = str(category)
        male_count = int(male_count)
        female_count = int(female_count)

        my_population_groups.append(PopulationGroup(category, male_count, female_count,))
    infile.close()
    return my_population_groups


def calculate_column_totals(my_population_groups):
    male_total = []
    female_total = []
    overall_total = []
    for line in my_population_groups:
        category, male_total, female_total, overall_total = line.split()
        male_total = int(male_total)
        female_total = int(female_total)
        overall_total = int(male_total) + int(female_total)
    return male_total, female_total, overall_total


def create_count_based_report(my_population_groups, male_total, female_total, overall_total, title):
    print()
    print()
    print('{0:^60}'.format(title))
    print()
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('Age Group', 'Males', 'Females', 'Total'))
    for population_group in my_population_groups:
        print('{0:<15}{1: >15,.2f}{2: >15,.2f}{3: >15,.2f}'.format(
            population_group.category,
            population_group.male_count,
            population_group.female_count,
            population_group.total_count
        ))
    print('{0:<15}{1: >15,.2f}{2: >15,.2f}'.format(male_total, female_total, overall_total))


def create_percentage_based_report(my_population_groups, male_total, female_total, overall_total, title):
    print()
    print()
    print('{0:^60}'.format(title))
    print()
    print('{0:<15}{1:>15}{2:>15}{3:>15}'.format('Age Group', 'Males', 'Females', 'Total'))
    for population_group in my_population_groups:
        print('{0:<15}{1: >15,.2f}{2: >15,.2f}{3: >15,.2f}'.format(
            population_group.category,
            population_group.male_count,
            population_group.female_count,
            population_group.total_count
        ))
    print('{0:<15}{1: >15,.2f}{2: >15,.2f}'.format(male_total, female_total, overall_total))


def by_category(my_population_groups):
    return my_population_groups.category


def by_total_count(my_population_groups):
    return my_population_groups.overall_total


def by_female_count(my_population_groups):
    return my_population_groups.female_total


def by_male_count(my_population_groups):
    return my_population_groups.male_total


main()
