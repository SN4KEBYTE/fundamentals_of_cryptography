from collections import Counter

from task1.syllable_analyzer.const import TEXT_PATH, RES_PATH
from task1.utils import preprocess, split_into_syllables


def main():
    with open(TEXT_PATH, 'r', encoding='utf-8') as inp:
        text: str = preprocess(inp.read())

    c = Counter(split_into_syllables(text))

    with open(RES_PATH, 'w', encoding='utf-8') as out:
        for syllable, frequency in c.most_common():
            out.write(f'{syllable} {frequency}\n')


if __name__ == '__main__':
    main()
