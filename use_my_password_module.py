# use_my_password_module.py
# A program utilizing my_password_module.py to validate a password candidate.

from my_password_module import validate_password


def main():
    password_candidate = input('Please enter a candidate password: ')
    error_messages = validate_password(password_candidate)
    if len(error_messages) == 0:
        print('This password is valid.')
    else:
        for message in error_messages:
            print(message)


main()
