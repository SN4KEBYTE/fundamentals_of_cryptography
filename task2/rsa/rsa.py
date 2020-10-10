from random import randint
from typing import List, Union

from task2.utils import are_mutually_simple, multiplicative_inverse, lcm


class RSA:
    def __init__(self, p: int, q: int) -> None:
        self.__p: int = p
        self.__q: int = q
        self.__n: int = p * q
        self.__carmichael: int = lcm(p - 1, q - 1)
        self.__e = self.__generate_open_exp()
        self.__d = multiplicative_inverse(self.__e, self.__carmichael)

    def __generate_open_exp(self):
        e: int = randint(2, self.__carmichael - 1)

        while not are_mutually_simple(e, self.__carmichael):
            e = randint(2, self.__carmichael - 1)

        return e

    def encrypt(self, msg: Union[int, str]):
        if isinstance(msg, int):
            return pow(msg, self.__e, self.__n)
        else:
            return [pow(b, self.__e, self.__n) for b in bytearray(msg, encoding='utf-8', errors='ignore')]

    def decrypt(self, msg: Union[int, List[int]]):
        if isinstance(msg, int):
            return pow(msg, self.__d, self.__n)
        else:
            return bytearray((pow(b, self.__d, self.__n) for b in msg)).decode('utf-8')

    @property
    def public_key(self):
        return self.__n, self.__e

    @property
    def private_key(self):
        return self.__n, self.__d
