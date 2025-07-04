#Not really needed, but you can remove

import random


def make_password():
    # Get a list of all possible characters
    all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

    # Choose a random length for the password
    length = random.randint(8, 16)

    # Make a password by picking random characters
    password = ''
    for i in range(length):
        password += random.choice(all_chars)

    return password


# Make a password and print Your password is: ""

print("Your Password is:",make_password())

#And Your password is now generated! you can change the length for the password where it says: "length = random.randint(8, 16)"
