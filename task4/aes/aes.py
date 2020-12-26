import itertools
from typing import Optional

from Crypto.Cipher import AES as CryptoAES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL.PngImagePlugin import PngImageFile, PngInfo

from task4.const import HASH_ALGS
from task4.types import PathType


class AES:
    def __init__(self, password: str, hash_alg: str = 'sha256') -> None:
        if hash_alg not in HASH_ALGS:
            raise ValueError('unknown hash algorithm')

        self.__key: bytes = HASH_ALGS[hash_alg](password.encode('utf-8')).digest()
        self.__hmac: HMAC = HMAC.new(self.__key, digestmod=SHA256)

    def encrypt(self, data: Optional[bytes] = None, in_path: Optional[PathType] = None,
                out_path: Optional[PathType] = None) -> Optional[bytes]:
        if not data and not in_path:
            raise ValueError('you must pass data or path to data')

        if data and in_path:
            raise ValueError('you must pass only data or only path to data')

        if in_path:
            with open(in_path, 'rb') as f:
                content: bytes = f.read()
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
            raise ValueError('you must pass data or path to data')

        if data and in_path:
            raise ValueError('you must pass only data or only path to data')

        if in_path:
            with open(in_path, 'rb') as f:
                enc: bytes = f.read()
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

        # convert pixels to bytes in order to encrypt them
        im_bytes = bytearray(self.__get_pixels(image))

        # get random IV and calculate MAC
        iv = get_random_bytes(CryptoAES.block_size)
        h = HMAC.new(self.__key, digestmod=SHA256)
        h.update(im_bytes)

        # create metadata object in order to save IV and MAC to image
        metadata = PngInfo()
        metadata.add_text('iv', iv.hex())
        metadata.add_text('mac', h.hexdigest())

        print(f'writing IV = {iv.hex()} and MAC = {h.hexdigest()} to image metadata')

        # encrypt image
        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        enc_data = cipher.encrypt(im_bytes)

        # write image to file with metadata
        image.frombytes(enc_data)
        image.save(out_path, pnginfo=metadata)

    def decrypt_png(self, in_path: PathType, out_path: PathType) -> None:
        image = PngImageFile(in_path)
        iv: Optional[str] = None
        mac: Optional[str] = None

        # try to get IV from metadata
        try:
            iv = image.text['iv']

            print(f'found IV = {iv}')
        except KeyError:
            print('IV was not found in file')

        # try to get MAC from metadata
        try:
            mac = image.text['mac']

            print(f'found MAC = {mac}')
        except KeyError:
            print('MAC was not found in file')

        # convert pixels to bytes in order to decrypt them
        im_bytes = bytearray(self.__get_pixels(image))

        # decrypt image
        cipher = CryptoAES.new(self.__key, CryptoAES.MODE_ECB)
        dec: bytes = cipher.decrypt(im_bytes)

        # try to verify MAC
        try:
            self.__hmac.update(dec)
            self.__hmac.verify(bytes.fromhex(mac))

            print('MAC is valid')
        except ValueError:
            print('MAC is invalid')

        # don't forget about metadata
        metadata = PngInfo()
        metadata.add_text('iv', iv)
        metadata.add_text('mac', mac)

        # save decrypted image to file
        image.frombytes(dec)
        image.save(out_path, pnginfo=metadata)

    @staticmethod
    def __get_pixels(image):
        return list(itertools.chain(*list(image.getdata())))
