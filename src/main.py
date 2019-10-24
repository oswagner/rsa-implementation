import sys
from utils.primes import get_primes
from utils.encrypter import encrypt, decrypt
from utils.euclidean import generate_e, extended_euclidean


def _generate_keys(e, d, n):
    return((e, n), (d, n))


def main(bits_size):
    p, q = get_primes(bits_size)

    phi_n = (p - 1) * (q - 1)

    n = p * q
    print("Generating keys...")
    print("\n")

    founded_inverse = True
    e = generate_e(phi_n)
    gcd, a, b = extended_euclidean(e, phi_n)
    while founded_inverse:
        e = generate_e(phi_n)
        gcd, a, b = extended_euclidean(e, phi_n)
        if (gcd == 1 and (gcd == (a * e) + (phi_n * b))):
            if(a*e % phi_n == 1 and 0 <= a <= n):
                founded_inverse = False

    public_key, private_key = _generate_keys(
        e, a, n)  # a is modular inverse of e

    print("\n")
    print("============================================ BEGIN PUBLIC KEY ============================================")
    print(public_key)
    print("============================================ END PUBLIC KEY ============================================")
    print("\n\n")
    print("============================================ BEGIN PRIVATE KEY ============================================")
    print(private_key)
    print("============================================ END PRIVATE KEY ============================================")

    print("\n\n\n\n")

    message = input("Mensagem: ")
    message = int(message)
    encrypt_message = encrypt(message, public_key)
    print("\n")
    print("Encrypt message")
    print(encrypt_message)

    print("\n")
    print("Decrypt message")
    decrypt_message = decrypt(encrypt_message, private_key)
    print(decrypt_message)
    print("\n")


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main(int(sys.argv[1]))
