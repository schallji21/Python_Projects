# sentinel_loop_using_break.py
# A program that demonstrates an interactive sentinel loop using break and counts even and odd integers.


def main():
    print('Process a series of integers entered at the console.\n')
    count_even = 0
    count_odd = 0

    while True:
        value_as_string = input('Please enter an integer or press <Enter> to stop: ')
        if value_as_string == '':
            break
        else:
            value = int(value_as_string)
            if value % 2 > 0:
                count_odd += 1
            else:
                count_even += 1

    if count_even + count_odd == 0:
        print('You did not provide any integers to process.')
    else:
        print('Number of evens is', str(count_even) + '.')
        print('Number of odds is', str(count_odd) + '.')


main()
