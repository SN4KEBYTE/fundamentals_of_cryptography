from random import randint

from task1.utils import swap


def create_key(s: str, file) -> None:
    for i in range(len(s) - 1, 0, -1):
        j = randint(0, i)
        s = swap(s, i, j)

    with open(file, 'w', encoding='utf-8') as out:
        out.write(s)
