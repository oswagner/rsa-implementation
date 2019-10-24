

def encrypt(message, public_key):
    e, n = public_key
    cipher_text = pow(message, e, n)
    return cipher_text


def decrypt(message, private_key):
    d, n = private_key
    plain = pow(message, d, n)
    return plain
