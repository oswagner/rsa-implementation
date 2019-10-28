from pyasn1.type import univ, namedtype


#  RFC 8017 base para estruturas da chave publica e chave privada
#  https://tools.ietf.org/html/rfc8017#appendix-A.1.1
# RSAPrivateKey ::= SEQUENCE {
#          version           Version,
#          modulus           INTEGER,  -- n
#          publicExponent    INTEGER,  -- e
#          privateExponent   INTEGER,  -- d
#          prime1            INTEGER,  -- p
#          prime2            INTEGER,  -- q
#          exponent1         INTEGER,  -- d mod (p-1)
#          exponent2         INTEGER,  -- d mod (q-1)
#          coefficient       INTEGER,  -- (inverse of q) mod p
#          otherPrimeInfos   OtherPrimeInfos OPTIONAL
#      }


class AsnSchemaPrivateKey(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('version', univ.Integer()),
        namedtype.NamedType('modulus', univ.Integer()),
        namedtype.NamedType('publicExponent', univ.Integer()),
        namedtype.NamedType('privateExponent', univ.Integer()),
        namedtype.NamedType('prime1', univ.Integer()),
        namedtype.NamedType('prime2', univ.Integer()),
        namedtype.NamedType('exponent1', univ.Integer()),
        namedtype.NamedType('exponent2', univ.Integer()),
        namedtype.NamedType('coefficient', univ.Integer()),
    )
