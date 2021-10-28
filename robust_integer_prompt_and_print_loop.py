# robust_integer_prompt_and_print_loop.py
# A program to prompt the user to input an integer and then print the determinant result.


def main():
    print('This program will prompt you to enter 10 integers')
    print('It prints proper integers...')
    print('And it complains about improper inputs.')
    try:
        for i in range(0, 10):
            some_integer = int(input('Please enter an integer: '))
            print('You have entered the integer:', some_integer)
    except ValueError:
        print('That was not an integer and you know it!')
    except KeyboardInterrupt:
        print('\nI detected a keyboard interrupt. Now that was just mean!!')
    print('Thanks for playing.')


main()
