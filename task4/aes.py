import itertools
from typing import Optional
from pprint import pprint

import piexif
from Crypto.Cipher import AES as CryptoAES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import HMAC, SHA256
from PIL import Image, ExifTags
from PIL.PngImagePlugin import PngImageFile, PngInfo

from task4.const import HASH_ALGS
from task4.types import PathType


class AES:
    def __init__(self, password: str, hash_alg: str = 'sha256') -> None:
        if hash_alg not in HASH_ALGS:
            raise ValueError('Unknown hash algorithm')

        self.__key: bytes = HASH_ALGS[hash_alg](password.encode('utf-8')).digest()
        self.__hmac: HMAC = HMAC.new(self.__key, digestmod=SHA256)

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

    def encrypt_png(self, in_path: PathType, out_path: PathType) -> None:
        image = PngImageFile(in_path)

        iv = get_random_bytes(CryptoAES.block_size)
        self.__hmac.update(iv)

        metadata = PngInfo()
        metadata.add_text('iv', iv.hex())
        metadata.add_text('mac', self.__hmac.hexdigest())

        im_bytes = bytearray(self.__get_pixels(image))

        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        enc_data = cipher.encrypt(im_bytes)

        image.frombytes(enc_data)
        image.save(out_path, pnginfo=metadata)

    def decrypt_png(self, in_path: PathType, out_path: PathType) -> None:
        image = PngImageFile(in_path)

        try:
            h = HMAC.new(self.__key, digestmod=SHA256)
            h.update(bytes.fromhex(image.text["mac"]))

            self.__hmac.verify(h.digest())

            print('mac is valid')
        except KeyError:
            print('no mac in file')
        except ValueError:
            print('mac is invalid')

        im_bytes = bytearray(self.__get_pixels(image))

        # decrypt
        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        dec: bytes = cipher.decrypt(im_bytes)

        # save decrypted image to file
        image.frombytes(dec)
        image.save(out_path)

    def encrypt_image2(self, in_path: PathType, out_path: PathType) -> None:
        image = Image.open(in_path)
        image.load()  # needed only for .png EXIF data
        w, h = image.size

        exif = image.info['meta_to_read']

        pprint(dict(exif))

        im_bytes = bytearray(self.__get_pixels(image))

        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        enc_data = cipher.encrypt(im_bytes)

        enc_im = Image.frombytes('RGBA', (w, h), enc_data)
        enc_im.save(out_path)

    def decrypt_image2(self, in_path: PathType, out_path: PathType) -> None:
        image = Image.open(in_path)
        w, h = image.size

        im_bytes = bytearray(self.__get_pixels(image))

        # decrypt
        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        dec: bytes = cipher.decrypt(im_bytes)

        # save decrypted image to file
        dec_im = Image.frombytes('RGBA', (w, h), dec)
        dec_im.save(out_path)

    @staticmethod
    def __get_pixels(image):
        return list(itertools.chain(*list(image.getdata())))
