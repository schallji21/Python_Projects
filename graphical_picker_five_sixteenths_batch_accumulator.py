# graphical_picker_five_sixteenths_batch_accumulator.py
# A modified program version of five_sixteenths_batch_accumulator.py that uses a graphical_file_picker.

from tkinter.filedialog import askopenfilename


def main():

    filename = askopenfilename()
    infile = open(filename, 'r')

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


main()
