import random


def code_generator():
    return str(random.randint(pow(10, 4), (pow(10, 5) - 1)))
