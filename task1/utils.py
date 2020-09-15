from typing import List

from task1.const import ALPHABET, SYLLABLE_LEN


def swap(s: str, i: int, j: int) -> str:
    str_list = list(s)
    str_list[i], str_list[j] = str_list[j], str_list[i]

    return ''.join(str_list)


def preprocess(text: str) -> str:
    return ''.join(ch for ch in text.lower() if ch in ALPHABET)


def split_into_syllables(text: str) -> List[str]:
    return [text[i:i + SYLLABLE_LEN] for i in range(0, len(text), SYLLABLE_LEN)]
