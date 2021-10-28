# batch_numeric_character_analytics.py
# A batch version of the program numeric_character_analytics.py
# Using numeric_character_data.txt, this program will print the contents of the line.
# Print each word and the number of numeric characters contained in the word.
# Print the total number of words analyzed for this line and the total number of text lines analyzed.


def main():
    input_file_name = 'numeric_character_data.txt'
    infile = open(input_file_name, 'r')
    line_count = 0

    for line in infile:
        print('\nAnalyzing:', line[:-1])
        line_count += 1
        lower_line = line.lower()

        words = lower_line.split()

        for word in words:
            numeric_character = 0
            numeric_character += word.count('0')
            numeric_character += word.count('1')
            numeric_character += word.count('2')
            numeric_character += word.count('3')
            numeric_character += word.count('4')
            numeric_character += word.count('5')
            numeric_character += word.count('6')
            numeric_character += word.count('7')
            numeric_character += word.count('8')
            numeric_character += word.count('9')
            print(word, 'has', numeric_character, 'numeric characters. ')

        print(len(words), 'words were analyzed. ')
    print()
    print(line_count, 'lines were analyzed from the file', input_file_name)

    infile.close()


main()
