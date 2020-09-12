from task1.const import ALPHABET, MOST_FREQUENT
from task1.types import Path
from typing import Optional
from pprint import pprint
from collections import Counter, OrderedDict


class SimpleSubstitutionCipher:
    def __init__(self, key: Optional[str] = None, key_path: Optional[Path] = None) -> None:
        if key is not None and key_path is not None:
            raise RuntimeError('You can not use both key and path to key file.')

        self.__key: str = key if key is not None else self.__read_key(key_path)

    def encrypt(self, text_path: Path, out_path: Path = None) -> Optional[str]:
        mapping = {k: v for k, v in zip(ALPHABET, self.__key)}

        with open(text_path, 'r', encoding='utf-8') as inp:
            text = self.__preprocess(inp.read())

        encrypted: str = ''

        for ch in text:
            encrypted += mapping[ch]

        if out_path is None:
            return encrypted

        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(encrypted)

    @staticmethod
    def decrypt(text_path: Path, out_path: Path = None) -> Optional[str]:
        with open(text_path, 'r', encoding='utf-8') as inp:
            encrypted = inp.read()

        c = Counter(encrypted)
        pprint(c.most_common())

        mapping = {k[0]: v for k, v in zip(c.most_common(), MOST_FREQUENT)}
        pprint(mapping)

        decrypted: str = ''

        for ch in encrypted:
            decrypted += mapping[ch] if ch in ALPHABET else ch

        if out_path is None:
            return decrypted

        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(decrypted)

    @staticmethod
    def __read_key(path: Path) -> str:
        with open(path, 'r', encoding='utf-8') as inp:
            return inp.read()

    @staticmethod
    def __preprocess(text: str) -> str:
        return ''.join(ch for ch in text.lower() if ch in ALPHABET)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        if sorted(value) != sorted(ALPHABET):
            raise RuntimeError('Key must contain only cyrillic letters. Each one must occur no more than once.')

        self.__key = value
