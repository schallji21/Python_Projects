# find_zipcodes.py
# A program to read zip-codes embedded in surrounding text.

import re


def main():
    print('Extract matches to 2 different zip code patterns from input file.')
    infile_name = input("Please enter the input filename: ")
    infile = open(infile_name, 'r', encoding='utf-8')

    for line in infile:
        zip_codes = re.findall(r'\d{5}-\d{4}|\d{5}', line)
        for zip_codes in zip_codes:
            print(zip_codes)

    infile.close()


main()
