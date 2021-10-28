# determine_annual_registration_fee.py
# A program to determine registration fees of a vehicle based on weight and type.


def main():
    print(determine_registration('Car', 2000) == 125.00)
    print(determine_registration('Car', 2999) == 125.00)
    print(determine_registration('Car', 3000) == 200.00)
    print(determine_registration('Car', 3999) == 200.00)

    print(determine_registration('Truck', 3000) == 250.00)
    print(determine_registration('Truck', 3999) == 250.00)
    print(determine_registration('Truck', 4000) == 350.00)
    print(determine_registration('Truck', 4999) == 350.00)


def determine_registration(vehicle_type, weight):
    if vehicle_type == 'Car':
        if weight < 3000:
            premium = 125.00
        if vehicle_type == 'Car':
            if weight >= 3000:
                premium = 200.00
    if vehicle_type == 'Truck':
        if weight < 4000:
            premium = 250.00
        if vehicle_type == 'Truck':
            if weight >= 4000:
                premium = 350.00

    return premium


main()
