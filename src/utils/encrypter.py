

def encrypt(message, public_key):
    e, n = public_key

    # print("unicode", ord(message[0]))
    # value = pow(ord(message[0]), e, n)
    # print(value)

    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text


def decrypt(message, private_key):
    d, n = private_key

    # print("unicode", chr(pow(ord(message[0]), d, n)))
    # print("value", pow(ord(message[0]), d, n))

    plain = [chr(pow(ord(char), d, n)) for char in message]
    return ''.join(plain)
