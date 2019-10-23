import random


def get_primes(bits_size):
    return (
        _generate_prime_random(bits_size),
        _generate_prime_random(bits_size)
    )


def _generate_prime_random(bit_size):
    probably_prime = random.randrange(
        pow(2, (bit_size-1)),
        pow(2, bit_size)
    )

    while _is_probably_prime(probably_prime) is False:
        probably_prime = random.randrange(
            pow(2, (bit_size-1)),
            pow(2, bit_size)
        )

    return probably_prime


def _is_probably_prime(number):
    return pow(2, number-1, number) == 1
