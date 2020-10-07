from random import randint
from typing import Union

from task2.utils import are_mutually_simple, lcm


class RSA:
    def __init__(self, p: int, q: int) -> None:
        self.__p: int = p
        self.__q: int = q
        self.__n: int = p * q
        self.__carmichael: int = lcm(p - 1, q - 1)

    def __generate_open_exp(self):
        e: int = randint(2, self.__carmichael - 1)

        while not are_mutually_simple(e, self.__carmichael):
            e = randint(2, self.__carmichael - 1)

        self.__e = e

    def __generate_private_exp(self):
        # TODO: generate private exp using extended euclidean algorithm
        self.__d = 0

    def encrypt(self, msg: Union[int, str]):
        if isinstance(msg, int):
            return pow(msg, self.__e, self.__n)
        else:
            # TODO: string encryption
            pass

    def decrypt(self, msg: Union[int, str]):
        if isinstance(msg, int):
            return pow(msg, self.__e * self.__d, self.__n)
        else:
            # TODO: string decryption
            pass

    @property
    def public_key(self):
        return self.__n, self.__e

    @property
    def private_key(self):
        return self.__n, self.__d
