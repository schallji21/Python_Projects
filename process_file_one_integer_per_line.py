# process_file_one_integer_per_line.py
# A program that demonstrates an end-of-file loop and processes one integer per line.


def main():
    print('Process a series of integers from a text file.\n')
    end_of_input = False
    count_even = 0
    count_odd = 0
    input_filename = input('Please enter the name of the input file: ')
    infile = open(input_filename, 'r')

    while not end_of_input:
        line = infile.readline()
        if line == '':
            end_of_input = True
        else:
            value = int(line)
            if value % 2 > 0:
                count_odd += 1
            else:
                count_even += 1
    if count_odd + count_even == 0:
        print('You did not provide any integers to process.')
    else:
        print('Number of evens is', str(count_even) + '.')
        print('Number of odds is', str(count_odd) + '.')


main()
