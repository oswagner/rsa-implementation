import sys
import base64
from utils.primes import get_primes
from utils.encrypter import encrypt, decrypt
from utils.euclidean import generate_e, extended_euclidean
from utils.key_generator import decode_private_key, decode_public_key
from utils.key_generator import generate_public_key, generate_private_key


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

    # d mod (p - 1).
    exp1 = a % (p - 1)
    # d mod (q - 1).
    exp2 = a % (q-1)
    # q^(-1) mod p.
    coef = (q ^ -1) % p

    public_key = generate_public_key(e, n)
    private_key = generate_private_key(e, n, a, p, q, exp1, exp2, coef)

    print("\n")
    print("-----BEGIN RSA PUBLIC KEY-----")
    encoded_public_key = base64.b64encode(public_key)
    print(encoded_public_key.decode())
    print("-----END RSA PUBLIC KEY-----")
    print("\n\n")

    print("-----BEGIN RSA PRIVATE KEY-----")
    encoded_private_key = base64.b64encode(private_key)
    print(encoded_private_key.decode())
    print("-----END RSA PRIVATE KEY-----")


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
        print("Encrypt a message...")
        message = input("Enter the message: ")
        public_key = input("Enter the public key: ")
        decode_key = decode_public_key(public_key)

        encrypt_message = encrypt(message, decode_key)
        print(encrypt_message)

    if(option == 3):
        print("Decrypt a message")
        message = input("Enter the cipher message: ")
        private_key = input("Enter the private key: ")

        decode_key = decode_private_key(private_key)

        decoded_message = decrypt(int(message), decode_key)
        print("Message: ", decoded_message)
