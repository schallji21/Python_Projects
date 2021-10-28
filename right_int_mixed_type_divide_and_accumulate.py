# right_int_mixed_type_divide_and_accumulate.py
# A program to calculate the quotients on each of a series of five pairs of user-supplied values, sum and print them.


def main():

    accumulator = 0.0

    for i in range(1, 6):
        print('Now collecting mixed-type pair', i)

        dividend = float(input('Please enter a float for the dividend: '))
        divisor = int(input('Please enter an integer for a divisor: '))

        quotient = dividend / divisor
        print('This quotient is', quotient)
        accumulator += quotient

    print('The accumulated sum of the quotients is', accumulator)


main()
