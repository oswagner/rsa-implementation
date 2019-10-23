import sys
from utils.primes import get_primes
from utils.encrypter import encrypt, decrypt
from utils.euclidean import generate_e, evaluate_inverse, inverse_euclidean


def _generate_keys(e, d, n):
    return((e, n), (d, n))


def main(bits_size):
    p, q = get_primes(bits_size)

    print("primes")
    print(p)
    print("\n")
    print(q)

    print("\n")
    print("phi_n")
    phi_n = (p - 1) * (q - 1)
    print(phi_n)

    print("\n")
    print("mod n")
    n = p * q
    print(n)
    e = generate_e(phi_n, bits_size)

    print("\n")
    print("inverse of e in mod phi_n")
    d = inverse_euclidean(e, phi_n)
    print(d)

    public_key, private_key = _generate_keys(e, d, n)

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
    encrypt_message = encrypt(message, public_key)
    print("\n")
    print("Encrypt message")
    print(''.join(map(lambda x: str(x), encrypt_message)))

    print("\n")
    print("Decrypt message")
    decrypt_message = decrypt(encrypt_message, private_key)
    print(decrypt_message)


if __name__ == "__main__":
    main(int(sys.argv[1]))
