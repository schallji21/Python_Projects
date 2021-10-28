# function_can_change_list_parameter.py
# A simple program using integers to demonstrate that a mutable value object passed to a called function as a parameter
# can be changed within the context of the calling code.


def main():
    list_in_main = [9, 7, 5, 3, 1]
    print('Starting value of list in main is', list_in_main)
    replace_integer_in_list_with_its_square(list_in_main)
    print('Ending value of list in main is', list_in_main)


def replace_integer_in_list_with_its_square(list_in_function):
    print()
    print('Starting value of list in function is', list_in_function)

    for i in range(len(list_in_function)):
        square_of_x = list_in_function[i]**2
        list_in_function[i] = square_of_x

    print('Ending value of list in function is', list_in_function)
    print()


main()
