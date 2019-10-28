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
    print(encoded_public_key)
    print("-----END RSA PUBLIC KEY-----")
    print("\n\n")

    print("-----BEGIN RSA PRIVATE KEY-----")
    encoded_private_key = base64.b64encode(private_key)
    print(encoded_private_key)
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
        print("Encrypt a message")
        # message = input("Enter the message: ")
        message = 'heello wagner'
        # public_key = input("Enter the public key: ")
        public_key = 'MIICCQKCAQEAsaPaCCG28K7GrvGW4uSNB3iKBk3VrdGUX14JgRzBFCkGxFGvlGzTiw8aspsQcqXhjMova2qYU2pU3sBgsBSFoIZ5fkKbMrPT2w7DQgGJZcbosAPtlAKtAJ1ZN/V9snYhZCIC+pI+pNnAzxWgCVOGEvcYD0TpU+a/Q2C3EeS4eQwafXsksFwY7ZlyJHz+6PiE0hF9JUGeINYuvzzKv+4mFhwT4PkyZ1RREhJHJGSURqjicAIQ7brDbVettgRxmuPrrjo1rXBSAWL46NwBNnRmD72Jm9XXP/Y/xlzNstYl1BdDlkdiB8jJUlu0Cce2UDuMy6+O0jPpyQxaPHS8LVFZbwKCAQBqwN4H256s8dawHOuVEylPTPb8mHW9XFmFaI07PjMBjd9igynobopn9I6e61F6i/K4gxFE2cAl9OZr780yyPdYGUKa362hwADMSmGY7o/2gwQ/WJmDMq0bU+hOyE4ZgNRbaG4DQ3U0ulEZ6aaOWhqeyzGtHm93uTu+SJbIN7fH/z+wFm2AApkcB+oy23BPIBTM2fZ7FHUxL/T4VOQbk/mcyZNbuedCJ8/atnl88PPyjG8Ow65lQz5XlyxrTn6svjuVfasbwNjMWLhYoFEr3z+xWuwMzV+EhdBca6krCY/hPN/8RQbeEfZHCF4D8paIZ5oFoAG9fU5yoSfzOa44KQK/'
        decode_key = decode_public_key(public_key)

        encrypt_message = encrypt(message, decode_key)
        print(''.join(map(lambda x: str(x), encrypt_message)))

    if(option == 3):
        print("Decrypt a message")
        # message = input("Enter the cipher message: ")
        message = 'heello wagner'
        # private_key = input("Enter the private key: ")
        private_key = 'MIIFogIBAAKCAQEAsaPaCCG28K7GrvGW4uSNB3iKBk3VrdGUX14JgRzBFCkGxFGvlGzTiw8aspsQcqXhjMova2qYU2pU3sBgsBSFoIZ5fkKbMrPT2w7DQgGJZcbosAPtlAKtAJ1ZN/V9snYhZCIC+pI+pNnAzxWgCVOGEvcYD0TpU+a/Q2C3EeS4eQwafXsksFwY7ZlyJHz+6PiE0hF9JUGeINYuvzzKv+4mFhwT4PkyZ1RREhJHJGSURqjicAIQ7brDbVettgRxmuPrrjo1rXBSAWL46NwBNnRmD72Jm9XXP/Y/xlzNstYl1BdDlkdiB8jJUlu0Cce2UDuMy6+O0jPpyQxaPHS8LVFZbwKCAQBqwN4H256s8dawHOuVEylPTPb8mHW9XFmFaI07PjMBjd9igynobopn9I6e61F6i/K4gxFE2cAl9OZr780yyPdYGUKa362hwADMSmGY7o/2gwQ/WJmDMq0bU+hOyE4ZgNRbaG4DQ3U0ulEZ6aaOWhqeyzGtHm93uTu+SJbIN7fH/z+wFm2AApkcB+oy23BPIBTM2fZ7FHUxL/T4VOQbk/mcyZNbuedCJ8/atnl88PPyjG8Ow65lQz5XlyxrTn6svjuVfasbwNjMWLhYoFEr3z+xWuwMzV+EhdBca6krCY/hPN/8RQbeEfZHCF4D8paIZ5oFoAG9fU5yoSfzOa44KQK/AoIBABM6BIoMbGtUbryj/ZA8rHgQw89lTtnND4DPz7mUMQPIx5NT/1Lqnf85f/i68e+IdHQ03nJXD5Dy0+iCpDG7yviQNM3j7FsWT3yW7OKqPvMnE2L3rXKIx8qoTXsF/Bc0Huicd5ppuQZMt082+zYIjgeEnvX7ZYPkz7qsvoln/RCSIsc+ZFTmIf7HuWFevyS9JnJbCyWoLojk1OKno4ihIm+YML9xbHM6reJyK7WxzvTktC8g0hdoslG5pITwYy2Ain8RrKFZubEnlwqKFnvM+Ez29Nmod1Kd4jm8IqDWdOgmTJotfwsjQHa72nEH7F04Kl/rkc/xyWWfHUb94R0D4fcCgYEAvYCwYWRZdX6HWDsBQmwEbaP+881rDL6ACkWkH0zsULy0ztdqPM808RCUo2z2jMy/EUFhPR4HP9vkHnCih9FFlb3YOktLBAhK+9+0AIUp31jXf8MvnX52UkLN01Grg4VsOC33YEMSFVT7Jf0C7QB2C5K9J2BsCBN8UQ2xenDrKG0CgYEA7/mGAGPvNNF8d0nxNiUDWkzthDLKyThjjJC0mbqDgfDRPDqH8bBqkmgH4DPnKYpRCKwm0wiNSgs5ErNrJ1EM9p1MMlhkdA1STF5KgMi+olPZuguOV+6IH5xNcx9MgGX4NzWCJ4XcBvtUPJzS4vs1x7oP+yk7ALcT+cV9mOYAl8sCgYB6w2dJH1OPgr49fcatCZxL5d3t42knIjZp/+2Sy77oDce1cj9y450jSvkAVTf9JbyG4I84jy3mmgt2+cW5BqqzySoYbSmhMizI26vXDZbn+gL/3CicObs6qWQXMFGmMu/BMIIoO+Pf7xIp6Ez/rcj+ut3/l36CLLsjseRxcIXu9wKBgGZfkAE7MNyX60/QO7HXXFGRJaHmZFOGiIfcgQg1bVjPIZUdUO60i85kfxpIiaj3j8yXtSKi9dtKkiz9hPT1wgkuPXHzkhxq2A+JMSWGh8P3DHQUnrZD+Ya4LnwlUIEPrNpj3E+yaifExbDe9d/7YcqYQ+U3+zZnpHJnA7u2xY6nAoGBAIsH2sJkw7YrkjksEU6zBYD7EGNoC1BEnIf6k6TfVR+ImGF0TIft/0+5IWamBfAPLRnWm6czgTWsjyot2ehRfjTeZEI+MZQDQ6thHYBBlRxd1UV60OMOZITpTjOECoak4DkmbJkASCOuog9dMvcFtk9ralOXnQ9v5KhV5Vv71bkO'

        decode_key = decode_private_key(private_key)

        message = decrypt(message, decode_key)
