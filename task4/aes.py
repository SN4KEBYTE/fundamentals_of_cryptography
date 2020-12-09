from Crypto.Cipher import AES as CryptoAES
from Crypto.Util.Padding import pad, unpad
from PIL import Image

from io import BytesIO
import struct
from typing import Optional

from task4.const import HASH_ALGS
from task4.types import PathType


class AES:
    def __init__(self, password: str, hash_alg: str = 'sha256') -> None:
        if hash_alg not in HASH_ALGS:
            raise ValueError('Unknown hash algorithm')

        self.__key: bytes = HASH_ALGS[hash_alg](password.encode('utf-8')).digest()

    def encrypt(self, data: Optional[bytes] = None, in_path: Optional[PathType] = None,
                out_path: Optional[PathType] = None, mode: int = CryptoAES.MODE_CBC) -> Optional[bytes]:
        if not data and not in_path:
            raise ValueError('You must pass data or path to data')

        if data and in_path:
            raise ValueError('You must pass only data or only path to data')

        if in_path:
            with open(in_path, 'rb') as f:
                content = f.read()
        else:
            content = data

        iv: bytes = self.__key[:CryptoAES.block_size]
        cipher = CryptoAES.new(self.__key, mode, iv)
        enc: bytes = iv + cipher.encrypt(pad(content, CryptoAES.block_size))

        if out_path:
            with open(out_path, 'wb') as f:
                f.write(enc)
        else:
            return enc

    def decrypt(self, data: Optional[bytes] = None, in_path: Optional[PathType] = None,
                out_path: Optional[PathType] = None, mode: int = CryptoAES.MODE_CBC) -> Optional[bytes]:
        if not data and not in_path:
            raise ValueError('You must pass data or path to data')

        if data and in_path:
            raise ValueError('You must pass only data or only path to data')

        if in_path:
            with open(in_path, 'rb') as f:
                enc = f.read()
        else:
            enc = data

        iv: bytes = enc[:CryptoAES.block_size]
        cipher = CryptoAES.new(self.__key, mode, iv)
        dec: bytes = unpad(cipher.decrypt(enc[CryptoAES.block_size:]), CryptoAES.block_size)

        if out_path:
            with open(out_path, 'wb') as f:
                f.write(dec)
        else:
            return dec

    def encrypt_image(self, in_path: PathType, out_path: PathType) -> None:
        image = Image.open(in_path)
        w, h = image.size

        data_bytes = [struct.pack('ccc', pixel[0], pixel[1], pixel[2]) for pixel in image.getdata()]
        print(data_bytes)

        # extract content of the image and encrypt it
        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        enc_content = cipher.encrypt(pad(image.getdata(), CryptoAES.block_size))

        # now we need to reconstruct image
        # extract metadata
        exif_data = image.getexif()

        # construct new image and save to file
        # TODO: set correct size
        enc_image = Image.frombytes('RGB', (w, h), exif_data + enc_content)
        enc_image.save(out_path)

    # @staticmethod
    # def __image_to_bytes(image: Image):
    #     b = BytesIO()
    #     image.save(b, 'jpg')
    #
    #     return b.getvalue()
