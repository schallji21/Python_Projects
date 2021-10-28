# sentinel_loop_without_break.py
# A program to demonstrate an interactive sentinel loop without a break and counts even and odd integers.


def main():
    print('Process a series of integers entered at the console.\n')
    count_odd = 0
    count_even = 0
    end_of_input = False

    while not end_of_input:
        value_as_string = input('Please enter an integer or press <Enter> to stop: ')
        if value_as_string == '':
            end_of_input = True
        else:
            value = int(value_as_string)
            if value % 2 > 0:
                count_odd += 1
            else:
                count_even += 1
    if count_odd + count_even == 0:
        print('You did not provide any integers to process.')
    else:
        print('Number of evens is', str(count_even) + '.')
        print('Number of odds is', str(count_odd) + '.')


main()
