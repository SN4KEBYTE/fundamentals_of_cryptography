from random import randint

from task1.types import PathType
from task1.utils import swap


def create_key(alphabet: str, out_path: PathType) -> None:
    for i in range(len(alphabet) - 1, 0, -1):
        j: int = randint(0, i)
        alphabet: str = swap(alphabet, i, j)

    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(alphabet)
