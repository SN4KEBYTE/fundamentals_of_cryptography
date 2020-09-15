from task1.const import ALPHABET


def swap(s: str, i: int, j: int) -> str:
    str_list = list(s)
    str_list[i], str_list[j] = str_list[j], str_list[i]

    return ''.join(str_list)


def preprocess(text: str) -> str:
    return ''.join(ch for ch in text.lower() if ch in ALPHABET)
