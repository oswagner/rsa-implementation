import sys
from utils.primes import get_primes
from utils.encrypter import encrypt, decrypt
from utils.euclidean import generate_e, extended_euclidean


# generate public and private keys

def _generate_keys(e, d, n):
    return((e, n), (d, n))


def generate_key_pair(bits_size):
    # find primes
    p, q = get_primes(bits_size)

    # evaluate totiente
    phi_n = (p - 1) * (q - 1)

    # evaluate modulus
    n = p * q

    print("\n")

    # evaluate modular inverse of e
    founded_inverse = True
    e, gcd, a, b = 0, 0, 0, 0
    while founded_inverse:
        e = generate_e(phi_n)
        gcd, a, b = extended_euclidean(e, phi_n)
        if (gcd == 1 and (gcd == (a * e) + (phi_n * b))):
            if(a*e % phi_n == 1 and 0 <= a <= n):
                founded_inverse = False

    public_key, private_key = _generate_keys(e, a, n)

    print("\n")
    print("============================================ BEGIN PUBLIC KEY ============================================")
    print(public_key)
    print("============================================ END PUBLIC KEY ============================================")
    print("\n\n")
    print("============================================ BEGIN PRIVATE KEY ============================================")
    print(private_key)
    print("============================================ END PRIVATE KEY ============================================")
    return public_key, private_key


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    print("which option")
    print("1 - Generate keypair")
    print("2 - Encrypt a message")
    print("3 - Decrypt a message")
    option = int(input())
    while option not in [1, 2, 3]:
        print("Invalid option")
        option = int(input())

    if(option == 1):
        print("Generate keypair")
        bits_size = int(input("Enter key size in bits: "))
        print("Generating keys...")
        generate_key_pair(bits_size)

    if (option == 2):
        print("Encrypt a message")
        message = input("Enter the message: ")
        public_key = input("Enter the public key: ")

        encrypt(message, public_key)

    if(option == 3):
        print("Decrypt a message")
        message = input("Enter the cipher message: ")
        private_key = input("Enter the private key: ")

        decrypt(message, private_key)
