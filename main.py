from task1.const import ENC_TEXTS_DIR
from task1.simple_sub.simple_substitution import SimpleSubstitutionCipher

# # create keys for short and long texts
# create_key(ALPHABET, WORK_DIR / 'short_key.txt')
# create_key(ALPHABET, WORK_DIR / 'long_key.txt')
#
# # encrypt short text
# cipher_s = SimpleSubstitutionCipher(key_path=WORK_DIR / 'short_key.txt')
# cipher_s.encrypt(RAW_TEXTS_DIR / 'short.txt', ENC_TEXTS_DIR / 'short.txt')
#
# # encrypt long text
# cipher_l = SimpleSubstitutionCipher(key_path=WORK_DIR / 'long_key.txt')
# cipher_l.encrypt(RAW_TEXTS_DIR / 'long.txt', ENC_TEXTS_DIR / 'long.txt')

print(SimpleSubstitutionCipher.decrypt(ENC_TEXTS_DIR / 'long.txt'))
