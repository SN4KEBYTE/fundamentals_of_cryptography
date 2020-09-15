from collections import Counter
from pprint import pprint
from typing import Optional

from task1.const import ALPHABET, MOST_FREQUENT
from task1.types import Path
from task1.utils import preprocess


class SimpleSubstitutionCipher:
    def __init__(self, key_path: Path) -> None:
        k = self.__read_key(key_path)

        if not self.__validate_key(k):
            raise RuntimeError('Key must contain only cyrillic letters. Each one must occur no more than once.')

        self.__key: str = k

    def encrypt(self, text_path: Path, out_path: Path) -> None:
        mapping = {k: v for k, v in zip(ALPHABET, self.__key)}

        with open(text_path, 'r', encoding='utf-8') as inp:
            text = preprocess(inp.read())

        encrypted: str = ''

        for ch in text:
            encrypted += mapping[ch]

        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(encrypted)

    @staticmethod
    def decrypt(text_path: Path, out_path: Path) -> None:
        with open(text_path, 'r', encoding='utf-8') as inp:
            encrypted = inp.read()

        c = Counter(encrypted)
        pprint(c.most_common())

        # mapping = {k[0]: v for k, v in zip(c.most_common(), MOST_FREQUENT)}
        # pprint(mapping)
        #
        # decrypted: str = ''
        #
        # for ch in encrypted:
        #     decrypted += mapping[ch] if ch in ALPHABET else ch
        #
        # if out_path is None:
        #     return decrypted
        #
        # with open(out_path, 'w', encoding='utf-8') as out:
        #     out.write(decrypted)

    @staticmethod
    def __read_key(path: Path) -> str:
        with open(path, 'r', encoding='utf-8') as inp:
            return inp.read()

    @staticmethod
    def __validate_key(key: str) -> bool:
        return sorted(key) == sorted(ALPHABET)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        if not self.__validate_key(value):
            raise RuntimeError('Key must contain only cyrillic letters. Each one must occur no more than once.')

        self.__key = value
