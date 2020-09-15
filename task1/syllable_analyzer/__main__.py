from collections import Counter
from pathlib import Path

from task1.utils import preprocess

WORK_DIR = Path().absolute() / 'task1' / 'syllable_analyzer'
SYLLABLE_LEN = 2


def main():
    with open(WORK_DIR / 'data' / 'text.txt', 'r', encoding='utf-8') as inp:
        text: str = preprocess(inp.read())

    c = Counter([text[i:i + SYLLABLE_LEN] for i in range(0, len(text), SYLLABLE_LEN)])

    with open(WORK_DIR / 'data' / 'result.txt', 'w', encoding='utf-8') as out:
        for syllable, frequency in c.most_common():
            out.write(f'{syllable} {frequency}\n')


if __name__ == '__main__':
    main()
