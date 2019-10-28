
#
# String messages inspired by https://gist.github.com/JekaDeka/c9b0f5da16625e3c7bd1033356354579
#


def encrypt(message, public_key):
    e, n = public_key['modulus'], public_key['publicExponent']
    cipher_text = [((ord(char)**e) % n) for char in message]
    return cipher_text


def decrypt(message, private_key):
    d, n = private_key['modulus'], private_key['privateExponent']
    plain = [chr(((char**d) % n)) for char in message]
    return ''.join(plain)
