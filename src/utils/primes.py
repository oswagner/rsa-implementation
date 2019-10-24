import random


def get_primes(bits_size):
    return (
        _generate_big_prime(bits_size),
        _generate_big_prime(bits_size),
    )


def _is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = random.randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True


def _generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = random.randint(2**(n-1), 2**n)
        if _is_prime(p, 1000):
            return p
