from pyasn1.type import univ, namedtype

#  RFC 8017 base para estruturas da chave publica e chave privada
#  https://tools.ietf.org/html/rfc8017#appendix-A.1.1
#
#  RSAPublicKey ::= SEQUENCE {
#          modulus           INTEGER,  -- n
#          publicExponent    INTEGER   -- e
#      }


class AsnSchemaPublicKey(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('modulus', univ.Integer()),
        namedtype.NamedType('publicExponent', univ.Integer()),
    )
