# numeric_character_analytics.py
# A simple program that counts the numeric characters that occur in the word and prints the total number of words.


def main():
    line = input('Please enter one line of text to be analyzed: ')
    lower_line = line.lower()

    words = lower_line.split()

    for word in words:
        numeric_characters = 0
        numeric_characters += word.count('0')
        numeric_characters += word.count('1')
        numeric_characters += word.count('2')
        numeric_characters += word.count('3')
        numeric_characters += word.count('4')
        numeric_characters += word.count('5')
        numeric_characters += word.count('6')
        numeric_characters += word.count('7')
        numeric_characters += word.count('8')
        numeric_characters += word.count('9')
        print(word, 'has', numeric_characters, 'numeric characters. ')

    print(len(words), 'words were analyzed. ')


main()
