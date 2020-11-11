from OpenSSL import crypto

from task3.types import PathType


def sign_file(file_path: PathType, private_key_path: PathType, out_path: PathType) -> None:
    with open(private_key_path, 'rb') as f:
        buf = f.read()

    private_key = crypto.load_pkcs12(buf).get_privatekey()

    with open(file_path, 'rb') as f:
        data = f.read()

    signed = crypto.sign(private_key, data, 'sha256')

    with open(out_path, 'wb') as f:
        f.write(signed)


def verify_sign(cert_path: PathType, sign_path: PathType, data_path: PathType) -> bool:
    with open(cert_path, 'rb') as f:
        buf = f.read()

    cert = crypto.load_certificate(crypto.FILETYPE_ASN1, buf)

    with open(sign_path, 'rb') as f:
        sign = f.read()

    with open(data_path, 'rb') as f:
        data = f.read()

    try:
        crypto.verify(cert, sign, data, 'sha256')

        return True
    except:
        return False
