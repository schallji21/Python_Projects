# detect_row_level_data_entry_errors.py
# A program to produce a diagnostic report that shows data entry errors at the row level.


def main():
    infile_name = input('Please enter the input filename: ')
    infile = open(infile_name, 'r', encoding='utf-8')
    print()
    print('{0:^50}'.format('Row-Level Data Entry Errors'))
    print()
    print('{0:<10}{1:>10}{2:>10}{3:>10}{4:>10}'.format('Age Group', 'Males', 'Females', 'Total', 'Error'))
    for line in infile:
        age_group, males, females, total = line.split()
        males = int(males)
        females = int(females)
        total = int(total)
        error = int(total) - (int(females) + int(males))
        print('{0:<10}{1:>10,}{2:>10,}{3:>10,}{4:>10,}'.format(age_group, males, females, total, error))

    infile.close()


main()
