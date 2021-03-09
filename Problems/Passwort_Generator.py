import random
import string


def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

print(password_generator(7))