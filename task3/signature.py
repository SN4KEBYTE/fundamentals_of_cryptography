from typing import Any

from OpenSSL import crypto

from task3.types import PathType


def sign_file(file_path: PathType, private_key_path: PathType, out_path: PathType) -> None:
    with open(private_key_path, 'rb') as f:
        buf: bytes = f.read()

    private_key: crypto.PKCS12 = crypto.load_pkcs12(buf).get_privatekey()

    with open(file_path, 'rb') as f:
        data: bytes = f.read()

    signed: Any = crypto.sign(private_key, data, 'sha256')

    with open(out_path, 'wb') as f:
        f.write(signed)


def verify_sign(cert_path: PathType, sign_path: PathType, data_path: PathType) -> bool:
    with open(cert_path, 'rb') as f:
        buf: bytes = f.read()

    cert: crypto.X509 = crypto.load_certificate(crypto.FILETYPE_ASN1, buf)

    with open(sign_path, 'rb') as f:
        sign: bytes = f.read()

    with open(data_path, 'rb') as f:
        data: bytes = f.read()

    try:
        crypto.verify(cert, sign, data, 'sha256')

        return True
    except:
        return False
