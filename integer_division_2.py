# integer_division.py
# A program designed to calculate both the quotient and remainder for two integers provided by the user and print them.


def main():

    dividend = int(input('Please enter an integer for the dividend: '))
    divisor = int(input('Please enter an integer for the divisor: '))

    quotient = dividend // divisor
    remainder = (dividend % divisor)

    print('The quotient is', quotient)
    print('The remainder is', remainder)


main()
