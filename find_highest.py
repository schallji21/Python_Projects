# find_highest.py
# A program to find the highest in a sequence of values.


def main():
    input_list = [1, 5, 99, -1, 0, 23, 55, 96, -2048, 4096, -99]

    if len(input_list) == 0:
        print('The input list is empty.')
    else:
        highest_entry_so_far = input_list[0]

        for entry in input_list:
            if entry > highest_entry_so_far:
                highest_entry_so_far = entry

        print('There are', len(input_list), 'entries in the input list.')
        print('The highest value is', str(highest_entry_so_far)+'.')


main()
