# analyze_slot_machine_trys_ignoring_duplicates.py
# A program that analyzes slot machine trys and ignores the duplicates.


def main():
    infile_name = input('Please enter the name of the input file: ')
    infile = open(infile_name, 'r')
    color_count = {}

    for line in infile:
        slot_values = line.split()
        for slot_value in slot_values:
            color_count[slot_value] = color_count.get(slot_value, 0) + 1

    infile.close()

    these_keys = list(color_count.keys())
    these_keys.sort()

    for this_key in these_keys:
        print('{0:<10}{1:>7}'.format(
            this_key, color_count.get(this_key)))


def find_unique_values(value_list):
    unique_values = []

    for value in value_list:
        if value not in unique_values:
            unique_values.append(value)

    return unique_values


main()
