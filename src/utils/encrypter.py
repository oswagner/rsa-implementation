
#
# String messages inspired by https://gist.github.com/JekaDeka/c9b0f5da16625e3c7bd1033356354579
#


def encrypt(message, public_key):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text


def decrypt(message, private_key):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in message]
    return ''.join(plain)
