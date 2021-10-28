# function_cannot_change_float_parameter.py
# A program illustrating an immutable value object passed to a called function as a-
# parameter can't be changed by the context of the calling code.


def main():
    value_in_main = 'I am an immutable object.'
    print('Starting value in main is:', value_in_main)
    attempt_to_change_parameter(value_in_main)
    print('Ending value in main is:', value_in_main)


def attempt_to_change_parameter(value_in_function):
    print()
    print('Starting value in function is:', value_in_function)
    value_in_function = 'The great and powerful function believes that it can change all parameters!!!!'
    print('Ending value in function is:', value_in_function)
    print()


main()
