from pathlib import Path

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

SYLLABLE_LEN = 2

WORK_DIR = Path(__file__).parent.absolute() / 'simple_sub' / 'data'
RAW_TEXTS_DIR = WORK_DIR / 'raw'
ENC_TEXTS_DIR = WORK_DIR / 'encrypted'
