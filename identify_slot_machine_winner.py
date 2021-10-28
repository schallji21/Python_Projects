# identify_slot_machine_winner.py
# A program to read the slot machine results from lines of a text file and identifies the first winning line.


def main():
    infile_name = input('Please enter the name of the input file: ')
    infile = open(infile_name, 'r')
    end_of_file = False
    line_count = 0
    red_count = 0
    blue_count = 0

    while (red_count != 3 or blue_count != 2) and (not end_of_file):
        line = infile.readline()
        if line == '':
            end_of_file = True
        else:
            slot_values = line.split()
            line_count += 1
            red_count = slot_values.count('Red')
            blue_count = slot_values.count('Blue')

    infile.close()
    if end_of_file:
        print('No winning slot values found.')
        print(line_count, 'lines read from', str(line_count) + '.')
    else:
        print('Winner found on line', str(line_count)+'.')
        print(line[:-1])


main()
