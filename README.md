# 🔐 Random Password Generator

A simple Python script that generates random passwords for you.

## 🧰 Technologies Used

- Python 3

## 🚀 How to Run

1. Make sure you have Python / Pycharm installed.
2. Download or clone this repository.
3. Run the script using the command line:

```python
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


# Make a password and print it
print("Your Password is:",make_password())
