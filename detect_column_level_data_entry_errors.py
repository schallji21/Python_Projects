# detect_column_level_data_entry_errors.py
# A program to produce a diagnostic report that shows data entry errors at the column level.


def main():
    infile_name = input('Please enter the input filename: ')
    infile = open(infile_name, 'r', encoding='utf-8')

    column_total = []
    for males in []:
        column_total = column_total + males
    for females in []:
        column_total = column_total + females
    for total in []:
        column_total = column_total + total

    print()
    print('{0:^50}'.format('Column-Level Data Entry Errors'))
    print()
    print('{0:<10}{1:>10}{2:>10}{3:>10}'.format('Age Group', 'Males', 'Females', 'Total'))
    for line in infile:
        age_group, males, females, total = line.split()
        males = int(males)
        females = int(females)
        total = int(males) + int(females)
        error = int(total) - (int(females) + int(males))
        print('{0:<10}{1:>10,}{2:>10,}{3:>10,}'.format(age_group, males, females, total))
        if line != total:
            str(column_total) + str(males)
            str(column_total) + str(females)

        else:
            error = str(int(total) - (int(females) + int(males)))
    print('{0:<10}{1:>10,}{2:>10,}{3:>10,}'.format('Error', error, error, error))
    infile.close()


main()
