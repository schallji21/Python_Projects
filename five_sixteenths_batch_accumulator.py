# five_sixteenths_batch_accumulator.py
# A program to read an input file of text lines.
# Accumulate the sum of the float values.
# Calculate a final amount that is five-sixteenths of the accumulated sum.
# Print the contents of the text line.
# Print the final amount without rounding (formatting).
# Print the final amount rounded (formatted) to 3 decimal places.


def main():

    file_name = input('Please enter name of the input file:')
    infile = open(file_name, 'r')

    for line in infile:
        entries = line.split(', ')
        entries_total = 0.0
        for entry in entries:
            entries_total += float(entry)
        final_value = entries_total * 5.0 / 16.0
        print()
        print(line[:-1])
        print('Before rounding: ', final_value)
        print('After rounding: {0:0.3f}'.format(final_value))

    infile.close()


main()
