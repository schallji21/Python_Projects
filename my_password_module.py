# my_password_module.py
# A module for validating password candidate using re.search() function.

import re


def validate_password(candidate):
    error_messages = []

    if len(candidate) < 6:
        error_messages.append('Password must be at least 6 characters long.')

    if not re.search(r'[A-Z]', candidate):
        error_messages.append('Password must include at least one upper-case letter (A-Z).')

    if not re.search(r'[a-z]', candidate):
        error_messages.append('Password must include at least one lower-case letter (a-z).')

    if not re.search(r'[!@#$%^&*]', candidate):
        error_messages.append('Password must include at least one special character (!@#$%^&*).')

    if re.search(r'password', candidate):
        error_messages.append('Password contains word "password".')

    if re.search(r'secret', candidate):
        error_messages.append('Password contains word "secret".')

    return error_messages


def main():
    print('Unit testing output...')

    print('\nTest case 1: password too short')
    input_password = 'Ab#45'
    expected_result = ['Password must be at least 6 characters long.']
    actual_result = validate_password(input_password)
    if actual_result == expected_result:
        print('passed')
    else:
        print('failed')

    print('\nTest case 2: password meets all criteria')
    input_password = 'Bc&456'
    expected_result = []
    actual_result = validate_password(input_password)
    if actual_result == expected_result:
        print('passed')
    else:
        print('failed')

    print('\nTest case 3: password missing upper case letter')
    input_password = 'ac&456'
    expected_result = ['Password must include at least one upper-case letter (A-Z).']
    actual_result = validate_password(input_password)
    if actual_result == expected_result:
        print('passed')
    else:
        print('failed')

    print('\nTest case 4: password missing lower-case letter')
    input_password = 'A*3456'
    expected_result = ['Password must include at least one lower-case letter (a-z).']
    actual_result = validate_password(input_password)
    if actual_result == expected_result:
        print('passed')
    else:
        print('failed')

    print('\nTest case 5: password missing special character')
    input_password = 'Aa3456'
    expected_result = ['Password must include at least one special character (!@#$%^&*).']
    actual_result = validate_password(input_password)
    if actual_result == expected_result:
        print('passed')
    else:
        print('failed')

    print('\nTest case 6: password missing multiple of the criteria')
    input_password = '12345'
    msg_1 = 'Password must be at least 6 characters long.'
    msg_2 = 'Password must include at least one upper-case letter (A-Z).'
    msg_3 = 'Password must include at least one lower-case letter (a-z).'
    msg_4 = 'Password must include at least one special character (!@#$%^&*).'
    expected_result = [msg_1, msg_2, msg_3, msg_4]
    actual_result = validate_password(input_password)
    if actual_result == expected_result:
        print('passed')
    else:
        print('failed')

    print('\nTest case 7: password contains word "password".')
    input_password = '1password1'
    expected_result = ['Password may not contain the word "password" in any case.']
    actual_result = validate_password(input_password)
    if actual_result == expected_result:
        print('passed')
    else:
        print('failed')

    print('\nTest case 8: password contains word "secret".')
    input_password = '2secret2'
    expected_result = ['Password may not contain the word "secret" in any case.']
    actual_result = validate_password(input_password)
    if actual_result == expected_result:
        print('passed')
    else:
        print('failed')


if __name__ == '__main__':
    main()
