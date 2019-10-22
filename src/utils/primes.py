import random


def generate_prime_random(bit_size):
    probably_prime = random.getrandbits(bit_size)

    while is_probably_prime(probably_prime) is False:
        probably_prime = random.getrandbits(bit_size)

    return probably_prime


def is_probably_prime(number):
    return pow(2, number-1, number) == 1
