from collections import Counter, OrderedDict
from pathlib import Path

from task1.const import ALPHABET
from task1.types import PathType
from task1.utils import preprocess, split_into_syllables


class SimpleSubstitutionCipher:
    def __init__(self, key_path: PathType) -> None:
        k = self.__read_key(key_path)

        if not self.__validate_key(k):
            raise RuntimeError('Key must contain only cyrillic letters. Each one must occur no more than once.')

        self.__key: str = k
        self.__frequency = self.__get_frequency()

    def encrypt(self, text_path: PathType, out_path: PathType) -> None:
        mapping = {k: v for k, v in zip(ALPHABET, self.__key)}

        with open(text_path, 'r', encoding='utf-8') as inp:
            text = preprocess(inp.read())

        encrypted: str = ''.join(mapping[ch] for ch in text)

        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(encrypted)

    def decrypt(self, text_path: PathType, out_path: PathType) -> None:
        with open(text_path, 'r', encoding='utf-8') as inp:
            encrypted = split_into_syllables(inp.read())

        c = Counter(encrypted)
        mapping = {k[0]: v[0] for k, v in zip(c.most_common(), self.__frequency.items())}

        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(''.join(mapping[syl] for syl in encrypted))

    @staticmethod
    def __get_frequency():
        d = OrderedDict()

        with open(Path(__file__).parent.parent / 'syllable_analyzer' / 'data' / 'result.txt', 'r',
                  encoding='utf-8') as inp:
            for line in inp.readlines():
                syl, freq = line.split(' ')
                d[syl] = int(freq.rstrip('\n'))

        return d

    @staticmethod
    def __read_key(path: PathType) -> str:
        with open(path, 'r', encoding='utf-8') as inp:
            return inp.read()

    @staticmethod
    def __validate_key(key: str) -> bool:
        return sorted(key) == sorted(ALPHABET)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key_path):
        k = self.__read_key(key_path)

        if not self.__validate_key(k):
            raise RuntimeError('Key must contain only cyrillic letters. Each one must occur no more than once.')

        self.__key: str = k
