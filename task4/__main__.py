from Crypto.Cipher import AES as CryptoAES

from task4.aes import AES

aes = AES('mypass')
aes.encrypt_image('br4_2.jpg', 'br4_2_encrypted.jpg')

# aes.encrypt('br4_2.jpg', 'enc')
# aes.decrypt('enc', 'br4_2_enc.jpg')
