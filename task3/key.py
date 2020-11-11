from typing import Any

from OpenSSL import crypto

from task3.const import KEY_TYPE, KEY_BITS
from task3.types import PathType


def generate_key_pair() -> crypto.PKey:
    pkey: crypto.PKey = crypto.PKey()
    pkey.generate_key(KEY_TYPE, KEY_BITS)

    return pkey


def dump_public_key(pkey: crypto.PKey, path: PathType) -> None:
    if not str(path).endswith('.cer'):
        raise ValueError('You can dump public key only into .cer file.')

    cert: crypto.X509 = crypto.X509()
    subject: crypto.X509Name = cert.get_subject()
    subject.commonName = 'PM-83 Kasimov'

    cert.set_pubkey(pkey)
    cert.set_issuer(subject)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    cert.sign(pkey, 'SHA256')

    buf: Any = crypto.dump_certificate(crypto.FILETYPE_ASN1, cert)

    with open(path, 'wb') as f:
        f.write(buf)


def dump_private_key(pkey: crypto.PKey, path: PathType) -> None:
    if not str(path).endswith('.pem'):
        raise ValueError('You can dump private key only into .pem file.')

    pkcs: crypto.PKCS12 = crypto.PKCS12()
    pkcs.set_privatekey(pkey)

    buf: Any = pkcs.export()

    with open(path, 'wb') as f:
        f.write(buf)
