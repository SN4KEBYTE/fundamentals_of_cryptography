from task4.aes.aes import AES
from task4.const import IMAGE_DIR, ENC_DIR, DEC_DIR

password = input('Enter password: ')
aes = AES(password)

# part I
aes.encrypt(in_path=IMAGE_DIR / 'br4.png', out_path=ENC_DIR / 'br4_enc_part1')
aes.decrypt(in_path=ENC_DIR / 'br4_enc_part1', out_path=DEC_DIR / 'br4_dec_part1.png')

# part II, III, IV
aes.encrypt_png(in_path=IMAGE_DIR / 'br4.png', out_path=ENC_DIR / 'br4_enc_part2.png')
aes.decrypt_png(in_path=ENC_DIR / 'br4_enc_part2.png', out_path=DEC_DIR / 'br4_dec_part2.png')
