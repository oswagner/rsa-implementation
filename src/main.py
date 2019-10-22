import sys
from utils.primes import generate_prime_random


def main(bits_size):
    generate_prime_random(bits_size)
    generate_prime_random(bits_size)


if __name__ == "__main__":
    main(int(sys.argv[1]))
