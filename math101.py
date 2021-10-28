# math101.py
# A program that prints a simple sequence of numbers


def main():
    print('This program illustrates a chaotic function')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(10):
        x = x + 2
        print(x)


main()
