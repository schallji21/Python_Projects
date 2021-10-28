# miles_to_kilometers.py
# A simple program designed to convert miles to kilometers rounded to one decimal place.


def main():

    miles = float(input('Please enter the measurement in miles: '))
    kilometers = miles_to_kilometers(miles)
    print('The measurement in kilometers is {0:0.1f}'.format(kilometers))


def miles_to_kilometers(my_miles):
    result = my_miles * 1.60934
    return result


main()
