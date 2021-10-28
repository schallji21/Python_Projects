# find_whales.py
# A program that counts the string whale in a  text file.


import re


def main():
    print('Count lines that contain the string "whale" in the input file.|n')
    infile_name = input('Please enter the input filename: ')
    infile = open(infile_name, 'r', encoding='utf-8')
    line_count_contain = 0
    line_count_begin = 0
    line_count_end = 0
    line_count_begin_or_end = 0
    line_count_begin_and_end = 0

    for line in infile:
        line = line.lower()

        if re.search(r'whale', line):
            line_count_contain += 1
        if re.search(r'^whale', line):
            line_count_begin += 1
        if re.search(r'whale$', line):
            line_count_end += 1
        if re.search(r'^whale|whale$', line):
            line_count_begin_or_end += 1
        if re.search(r'^whale.*whale$', line):
            line_count_begin_and_end += 1
    infile.close()

    print(line_count_contain, "lines in file contain target string.")
    print(line_count_begin, "lines in file contain target string at the beginning.")
    print(line_count_end, "lines in file contain target string at the end.")
    print(line_count_begin_or_end, "lines in file contain target string at the beginning or at the end.")
    print(line_count_begin_and_end, "lines in file contain target string at the beginning and at the end.")


main()
