from pathlib import Path

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MOST_FREQUENT = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'

WORK_DIR = Path(__file__).parent.absolute()

RAW_TEXTS_DIR = WORK_DIR / 'raw'
ENC_TEXTS_DIR = WORK_DIR / 'encrypted'
