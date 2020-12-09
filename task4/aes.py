from Crypto.Cipher import AES as CryptoAES
from Crypto.Util.Padding import pad, unpad
from PIL import Image

from io import BytesIO
import struct
from typing import Optional
import itertools

from task4.const import HASH_ALGS
from task4.types import PathType


class AES:
    def __init__(self, password: str, hash_alg: str = 'sha256') -> None:
        if hash_alg not in HASH_ALGS:
            raise ValueError('Unknown hash algorithm')

        self.__key: bytes = HASH_ALGS[hash_alg](password.encode('utf-8')).digest()

    def encrypt(self, data: Optional[bytes] = None, in_path: Optional[PathType] = None,
                out_path: Optional[PathType] = None) -> Optional[bytes]:
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
        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_CBC, iv)
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

        # convert image pixels to bytes
        im_bytes = bytearray(self.__get_pixels(image))

        # encrypt
        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        enc_data = cipher.encrypt(im_bytes)

        # save encrypted image to file
        enc_im = Image.frombytes('RGB', (w, h), enc_data)
        enc_im.save(out_path)

    def decrypt_image(self, in_path: PathType, out_path: PathType) -> None:
        image = Image.open(in_path)
        w, h = image.size

        # convert image pixels to bytes
        im_bytes = bytearray(self.__get_pixels(image))

        # decrypt
        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        dec: bytes = cipher.decrypt(im_bytes)

        # save decrypted image to file
        dec_im = Image.frombytes('RGB', (w, h), dec)
        dec_im.save(out_path)

    @staticmethod
    def __get_pixels(image):
        return list(itertools.chain(*list(image.getdata())))
