import random


def generate_e(phi_n):
    return random.randrange(1, phi_n)


def extended_euclidean(x, y):
    if (y == 0):
        return (x, 1, 0)
    (d1, a1, b1) = extended_euclidean(y, x % y)
    d = d1
    a = b1
    b = a1 - (x // y) * b1
    return (d, a, b)
