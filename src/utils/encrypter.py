import binascii

#
# String messages inspired by https://gist.github.com/JekaDeka/c9b0f5da16625e3c7bd1033356354579
#


def encrypt(message, public_key):
    n, e = public_key['modulus'], public_key['publicExponent']

    encoded_message = binascii.hexlify(message.encode())

    message_integer = int(encoded_message, 16)

    if message_integer > n:
        return "Unable to encrypt message"

    cipher_text = pow(message_integer, int(e), int(n))
    return cipher_text


def decrypt(message, private_key):
    d, n = private_key['privateExponent'], private_key['modulus']

    decoded_message = pow(message, int(d), int(n))

    hex_message = hex(decoded_message)[2:]

    plain_message = binascii.unhexlify(hex_message)

    return plain_message.decode()
