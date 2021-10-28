# remainder_accumulator.py
# A program to calculate the remainders on each of a series of five pairs of user-supplied integers, sum and print them.


def main():

    accumulator = 0

    for i in range(1, 6):
        print('Now collecting integer pair', i)

        dividend = int(input('Please input an integer for the dividend: '))
        divisor = int(input('Please input an integer for the divisor: '))

        remainder = dividend % divisor
        print('The remainder is', remainder)
        accumulator += remainder

    print('The accumulated sum of the remainders is', accumulator)


main()
