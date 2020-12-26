from random import randint
from typing import List, Union, Tuple

from task2.utils import are_mutually_prime, fast_pow_mod, multiplicative_inverse, lcm, is_prime


class RSA:
    def __init__(self, p: int, q: int) -> None:
        if not is_prime(p):
            raise ValueError('p must be prime number')

        if not is_prime(q):
            raise ValueError('q must be prime number')

        self.__p: int = p
        self.__q: int = q
        self.__n: int = p * q
        self.__carmichael: int = lcm(p - 1, q - 1)
        self.__e: int = self.__generate_open_exp()
        self.__d: int = multiplicative_inverse(self.__e, self.__carmichael)

    def __generate_open_exp(self):
        e: int = randint(2, self.__carmichael - 1)

        while not are_mutually_prime(e, self.__carmichael):
            e = randint(2, self.__carmichael - 1)

        return e

    def encrypt(self, msg: Union[int, str]) -> Union[int, List[int]]:
        if isinstance(msg, int):
            return fast_pow_mod(msg, self.__e, self.__n)
        else:
            return [fast_pow_mod(b, self.__e, self.__n) for b in bytearray(msg, encoding='utf-8', errors='ignore')]

    def decrypt(self, msg: Union[int, List[int]]) -> Union[int, str]:
        if isinstance(msg, int):
            return fast_pow_mod(msg, self.__d, self.__n)
        else:
            return bytearray((fast_pow_mod(b, self.__d, self.__n) for b in msg)).decode('utf-8')

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        self.__n = value

    @property
    def e(self):
        return self.__e

    @e.setter
    def e(self, value):
        self.__e = value

    @property
    def d(self):
        return self.__n

    @d.setter
    def d(self, value):
        self.__d = value

    @property
    def public_key(self) -> Tuple[int, int]:
        return self.__n, self.__e

    @property
    def private_key(self) -> Tuple[int, int]:
        return self.__n, self.__d
