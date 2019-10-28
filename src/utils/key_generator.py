from base64 import b64decode
from pyasn1.codec.der.encoder import encode
from pyasn1.codec.der.decoder import decode
from utils.private_key import AsnSchemaPrivateKey
from utils.public_key import AsnSchemaPublicKey

#
# Utilizado como apoio para criação formatação das chaves
# https://github.com/sybrenstuvel/python-rsa
#
#
# bibloteca de apoio para estrutura das chaves
# https://github.com/etingof/pyasn1
#
# #


def generate_public_key(e, modulus):

    asn_key = AsnSchemaPublicKey()
    asn_key.setComponentByName('modulus', modulus)
    asn_key.setComponentByName('publicExponent', e)

    return encode(asn_key)


def generate_private_key(e, n, d, p, q, exp1, exp2, coef):

    # Create the ASN object
    asn_key = AsnSchemaPrivateKey()
    asn_key.setComponentByName('version', 0)
    asn_key.setComponentByName('modulus', n)
    asn_key.setComponentByName('publicExponent', e)
    asn_key.setComponentByName('privateExponent', d)
    asn_key.setComponentByName('prime1', p)
    asn_key.setComponentByName('prime2', q)
    asn_key.setComponentByName('exponent1', exp1)
    asn_key.setComponentByName('exponent2', exp2)
    asn_key.setComponentByName('coefficient', coef)

    return encode(asn_key)


def decode_public_key(public_key_encoded):
    # Undo BASE64 serialisation
    der_serialisation = b64decode(public_key_encoded)

    # Undo DER serialisation, reconstruct SSH key structure
    public_key, rest_of_input = decode(
        der_serialisation, asn1Spec=AsnSchemaPublicKey())

    return public_key


def decode_private_key(private_key_encoded):
    # Undo BASE64 serialisation
    der_serialisation = b64decode(private_key_encoded)

    # Undo DER serialisation, reconstruct SSH key structure
    private_key, rest_of_input = decode(
        der_serialisation, asn1Spec=AsnSchemaPrivateKey())

    return private_key
