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

    cert = crypto.X509()
    cert.set_pubkey(pkey)

    buf = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)

    with open(path, 'wb') as f:
        f.write(buf)


def dump_private_key(pkey: crypto.PKey, path: PathType) -> None:
    if not str(path).endswith('.pem'):
        raise ValueError('You can dump private key only into .pem file.')

    pkcs = crypto.PKCS12()
    pkcs.set_privatekey(pkey)

    buf = pkcs.export()

    with open(path, 'wb') as f:
        f.write(buf)
