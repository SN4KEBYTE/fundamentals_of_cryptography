from task1.create_key import create_key
from task1.const import ALPHABET, RAW_TEXTS_DIR, ENC_TEXTS_DIR, WORK_DIR
from task1.simple_sub.simple_substitution import SimpleSubstitutionCipher


def main():
    # print('Creating keys for short and long text...', end=' ')
    short_key_path = WORK_DIR / 'short_key.txt'
    # long_key_path = WORK_DIR / 'long_key.txt'
    #
    # create_key(ALPHABET, short_key_path)
    # create_key(ALPHABET, long_key_path)
    # print('DONE')

    print('Encrypting short text...', end=' ')
    cipher = SimpleSubstitutionCipher(short_key_path)

    cipher.encrypt(RAW_TEXTS_DIR / 'short.txt', ENC_TEXTS_DIR / 'short.txt')
    print('DONE')

    # print('Encrypting long text...', end=' ')
    # cipher.key = long_key_path
    #
    # cipher.encrypt(RAW_TEXTS_DIR / 'long.txt', ENC_TEXTS_DIR / 'long.txt')
    # print('DONE')


if __name__ == '__main__':
    main()
